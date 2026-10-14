#!/usr/bin/env python3
"""Validate schema, references and optional revision/file evidence. Never writes."""
import argparse
from pathlib import Path
import sys
from qa_common import emit, finding, local_file, read_json, report, sha256

SCHEMA = Path(__file__).resolve().parents[1] / "schemas/material-ui-contract.schema.json"


def validate(contract, root=None, artifact_index=None, snapshot=None, delivery=False):
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        return [finding("tool.dependency", "jsonschema",
                        "Install the shared scripts/requirements.txt in a virtual environment.",
                        "review")]
    schema = read_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(contract))
    findings = [finding("contract.schema", "/" + "/".join(map(str, e.absolute_path)), e.message)
                for e in errors]
    if findings:
        return findings

    def add(rule, location, message, status="fail"):
        findings.append(finding(rule, location, message, status))

    def index(items, location, key="id"):
        result = {}
        for item in items:
            value = item[key]
            if value in result:
                add("contract.duplicate", location + "/" + value, "Duplicate " + key)
            result[value] = item
        return result

    revision = contract["meta"]["revision"]
    targets = contract["targets"]
    viewports = index(targets["canonicalViewports"], "targets/canonicalViewports")
    components = index(contract["components"], "components")
    screens = index(contract["screens"], "screens")
    assets = index(contract["assets"], "assets")
    index(contract["interactions"], "interactions")
    index(contract["deviations"], "deviations")
    index(contract["meta"]["decisions"], "meta/decisions")
    for name in ("uiState", "events"):
        index(contract["dataContract"][name], "dataContract/" + name, "name")
    index(contract["dataContract"]["fixtures"], "dataContract/fixtures")
    events = {e["name"] for e in contract["dataContract"]["events"]}
    state_fields = {e["name"] for e in contract["dataContract"]["uiState"]}
    for component in components.values():
        for ref in component.get("dataBindings", []):
            if ref not in state_fields:
                add("contract.binding", component["id"], "Unknown UI state field: " + ref)
    for action in contract["interactions"]:
        if action["event"] not in events:
            add("contract.event", action["id"], "Unknown event: " + action["event"])
    variants, required_files = {}, set()
    for screen in screens.values():
        sid = screen["id"]
        for ref in screen.get("componentIds", []):
            if ref not in components:
                add("contract.component-ref", sid, "Unknown component: " + ref)
        for variant in index(screen["variants"], sid + "/variants").values():
            variants[(sid, variant["id"])] = variant
            required_files.add(variant["reference"])
            viewport = viewports.get(variant["viewportId"])
            if not viewport:
                add("contract.viewport-ref", sid, "Unknown viewport: " + variant["viewportId"])
            elif viewport["windowClass"] not in targets["windowClasses"]:
                add("contract.window-class", sid, "Viewport window class is outside targets")
            for field, options in (("locale", "locales"), ("fontScale", "fontScales"),
                                   ("themeMode", "themeModes")):
                if variant[field] not in targets[options]:
                    add("contract.target", sid + "/" + variant["id"], "Undeclared " + field)
    configurations = index(contract["verification"]["configurations"], "verification/configurations")
    covered = set()
    for item in configurations.values():
        key = (item["screenId"], item["variantId"])
        if key not in variants:
            add("contract.variant-ref", item["id"], "Unknown screen/variant pair")
            continue
        covered.add(key)
        if item.get("reference") and item["reference"] != variants[key]["reference"]:
            add("contract.export-ref", item["id"], "Configuration and variant references differ")
        if delivery and item["status"] != "passed":
            add("contract.unverified", item["id"], "Required configuration has not passed")
        if item.get("actual"):
            required_files.add(item["actual"])
    if delivery:
        for key in sorted(set(variants) - covered):
            add("contract.coverage", "/".join(key), "Variant has no verification configuration")
        # Check each promised dimension, not an unnecessary full Cartesian product.
        for sid, screen in screens.items():
            rows = screen["variants"]
            for field, options in (("locale", "locales"), ("fontScale", "fontScales"),
                                   ("themeMode", "themeModes")):
                promised = set(targets[options]) - ({"system"} if field == "themeMode" else set())
                if not promised <= {row[field] for row in rows}:
                    add("contract.coverage", sid, "Missing promised " + field + " evidence")
            classes = {viewports[v["viewportId"]]["windowClass"] for v in rows
                       if v["viewportId"] in viewports}
            if not set(targets["windowClasses"]) <= classes:
                add("contract.coverage", sid, "Missing promised window-class evidence")
    direction = contract["meta"].get("visualDirection")
    if delivery and not direction:
        add("contract.direction", "meta/visualDirection", "Visual direction evidence is missing")
    if direction:
        if direction["sourceRevision"] != revision:
            add("contract.revision", "meta/visualDirection", "Direction is linked to a stale revision")
        required_files.update(direction["representativeExports"])
        for asset_id in direction["fontProfile"]["assetIds"]:
            if asset_id not in assets or assets[asset_id]["kind"] != "font":
                add("contract.font-ref", "meta/visualDirection", "Unknown font asset: " + asset_id)
        if delivery and (direction["status"] == "proposed" or not direction.get("approvedBy")
                         or not direction.get("approvalEvidence")):
            add("contract.approval", "meta/visualDirection", "Approval/delegation/inheritance is undocumented")
    for asset in assets.values():
        if asset["destinationHint"]:
            required_files.add(asset["destinationHint"])
        if delivery and (not asset["license"].strip() or not asset["source"].strip()):
            add("contract.asset", asset["id"], "Asset source/license is missing")
    for deviation in contract["deviations"]:
        if delivery and not deviation.get("approvedBy"):
            add("contract.deviation", deviation["id"], "Deviation is not approved")
    required_files.update(contract["verification"].get("evidence", []))
    for mask in contract["verification"].get("masks", []):
        required_files.add(mask["path"])
    if snapshot is not None:
        if not isinstance(snapshot, dict) or snapshot.get("revision") != revision:
            add("contract.revision", "snapshot", "Snapshot revision differs from the contract")
    elif delivery and "figma.com" in (contract["meta"].get("sourceDesign") or ""):
        add("contract.snapshot", "snapshot", "Figma handoff requires a current snapshot")
    if delivery and (root is None or artifact_index is None):
        add("contract.evidence", "handoff", "Delivery requires --root and --artifact-index")
    if root is not None:
        for value in sorted(required_files):
            try:
                local_file(root, value)
            except ValueError as error:
                add("contract.file", value, str(error))
    if artifact_index is not None:
        if not isinstance(artifact_index, dict) or not isinstance(artifact_index.get("files"), list):
            add("contract.index", "artifact-index", "Expected object with files array")
        else:
            if artifact_index.get("revision") != revision:
                add("contract.revision", "artifact-index", "Artifact index revision differs")
            listed = set()
            for item in artifact_index["files"]:
                if not isinstance(item, dict) or not isinstance(item.get("path"), str):
                    add("contract.index", "artifact-index", "Invalid file entry")
                    continue
                value = item["path"]
                if value in listed:
                    add("contract.index", value, "Duplicate artifact path")
                listed.add(value)
                if root is None:
                    add("contract.index", value, "--root is required to verify hashes")
                    continue
                try:
                    if sha256(local_file(root, value)) != item.get("sha256"):
                        add("contract.hash", value, "File hash differs or is missing")
                except ValueError as error:
                    add("contract.file", value, str(error))
            for value in sorted(required_files - listed):
                add("contract.index", value, "Referenced artifact is absent from the index")
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract")
    parser.add_argument("--root", help="Read-only handoff root; checks referenced files")
    parser.add_argument("--artifact-index")
    parser.add_argument("--snapshot")
    parser.add_argument("--delivery", action="store_true")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()
    try:
        findings = validate(read_json(args.contract), args.root,
                            read_json(args.artifact_index) if args.artifact_index else None,
                            read_json(args.snapshot) if args.snapshot else None, args.delivery)
    except (ValueError, OSError, TypeError) as error:
        findings = [finding("tool.input", "input", str(error), "review")]
    return emit(report(findings, "Contract schema/references/files; not visual acceptance"), args.format)


if __name__ == "__main__":
    sys.exit(main())
