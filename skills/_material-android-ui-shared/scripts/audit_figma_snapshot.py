#!/usr/bin/env python3
"""Audit a read-only Figma snapshot. Unsupported/ambiguous cases need review."""
import argparse
import math
import sys
from qa_common import emit, finding, read_json, report

CONTAINERS = {"FRAME", "COMPONENT", "COMPONENT_SET", "INSTANCE", "SECTION"}


def audit(snapshot, config=None, contract=None):
    config = {} if config is None else config
    if contract is not None and (not isinstance(contract, dict)
                                or not isinstance(contract.get("meta"), dict)):
        raise ValueError("Contract must contain a meta object; validate it first")
    if not isinstance(config, dict):
        raise ValueError("Audit config must be an object")
    for key in ("iconSlots", "exceptions", "sectionGroups"):
        if key in config and (not isinstance(config[key], list)
                              or not all(isinstance(x, dict) for x in config[key])):
            raise ValueError(key + " must be an array of objects")
    if (not isinstance(snapshot, dict) or snapshot.get("schemaVersion") != "1.0"
            or not isinstance(snapshot.get("revision"), str) or not snapshot["revision"]
            or not isinstance(snapshot.get("nodes"), list) or not snapshot["nodes"]
            or not isinstance(snapshot.get("roots"), list) or not snapshot["roots"]):
        raise ValueError("A nonempty versioned snapshot with roots/revision/nodes is required")
    findings, nodes = [], {}
    def add(rule, node, message, status="fail"):
        findings.append(finding(rule, node, message, status))
    def number(value):
        return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value)
    tolerance = config.get("tolerance", 0.5)
    if not number(tolerance) or not 0 <= tolerance <= 1:
        raise ValueError("tolerance must be between 0 and 1 logical pixel")
    for node in snapshot["nodes"]:
        if (not isinstance(node, dict) or not isinstance(node.get("id"), str)
                or not node["id"] or node["id"] in nodes
                or not isinstance(node.get("type"), str)
                or not all(number(node.get(k)) and node[k] >= 0 for k in ("width", "height"))
                or "parentId" not in node):
            raise ValueError("Invalid/duplicate node or geometry")
        if node["parentId"] is not None and not isinstance(node["parentId"], str):
            raise ValueError("parentId must be a string or null")
        for key in ("clipsContent", "hasMask", "hasMissingFont"):
            if not isinstance(node.get(key), bool):
                raise ValueError("Missing/invalid collector field: " + key)
        if not isinstance(node.get("rawSolidFills"), int) or node["rawSolidFills"] < 0:
            raise ValueError("Missing/invalid rawSolidFills")
        if node.get("textStyleStatus") not in ("none", "styled", "raw-or-mixed"):
            raise ValueError("Missing/invalid textStyleStatus")
        if node["type"] == "TEXT" and node.get("textAutoResize") not in ("NONE", "HEIGHT", "WIDTH_AND_HEIGHT", "TRUNCATE"):
            raise ValueError("Missing/invalid textAutoResize")
        nodes[node["id"]] = node
    roots = snapshot["roots"]
    if not all(isinstance(value, str) for value in roots):
        raise ValueError("Root IDs must be strings")
    if len(roots) != len(set(roots)) or set(roots) != {n["id"] for n in nodes.values() if n["parentId"] is None}:
        raise ValueError("Root list and parent graph differ")
    for node in nodes.values():
        current, visited = node, set()
        while current["parentId"] is not None:
            if current["id"] in visited or current["parentId"] not in nodes:
                raise ValueError("Cyclic graph or missing parent")
            visited.add(current["id"])
            current = nodes[current["parentId"]]
        if current["id"] not in roots:
            raise ValueError("Orphan node")
    if not isinstance(snapshot.get("errors"), list):
        raise ValueError("Collector errors array is required")
    for error in snapshot["errors"]:
        add("figma.collection", "snapshot", str(error), "review")
    if contract is not None and snapshot["revision"] != contract.get("meta", {}).get("revision"):
        add("figma.revision", "snapshot", "Snapshot and contract revisions differ")
    for node in nodes.values():
        nid, pid = node["id"], node["parentId"]
        if pid is not None:
            b = node.get("boundsInParent")
            if (not isinstance(b, dict) or not all(number(b.get(k)) for k in ("x", "y", "width", "height"))
                    or b["width"] < 0 or b["height"] < 0):
                raise ValueError("Missing or invalid transformed child bounds")
            parent = nodes[pid]
            if parent["type"] in CONTAINERS:
                outside = {"left": max(0, -b["x"]), "top": max(0, -b["y"]),
                           "right": max(0, b["x"] + b["width"] - parent["width"]),
                           "bottom": max(0, b["y"] + b["height"] - parent["height"])}
                if any(value > tolerance for value in outside.values()):
                    add("figma.bounds", nid, "Outside parent " + pid + ": " + str(outside))
        if node.get("hasMask"):
            add("figma.mask", nid, "Mask silhouette requires visual review", "review")
        if node.get("rawSolidFills", 0):
            add("figma.raw-fill", nid, "Unbound solid fill(s); verify token or intentional artwork", "review")
        if node["type"] == "TEXT":
            if node.get("hasMissingFont"):
                add("figma.missing-font", nid, "Missing font; rendering is not the approved type")
            if node.get("textStyleStatus") == "raw-or-mixed":
                add("figma.text-style", nid, "Text has unstyled ranges; verify typography tokens", "review")
            if node.get("textAutoResize") in ("NONE", "TRUNCATE"):
                add("figma.text-fit", nid, "Fixed/truncated text: visually verify glyphs, wrapping and intended truncation", "review")
    children = {n["parentId"] for n in nodes.values() if n["parentId"]}
    for rid in roots:
        if rid not in children and nodes[rid]["type"] in CONTAINERS:
            add("figma.empty-root", rid, "No visible child content", "review")
    assets = {a["id"]: a for a in (contract or {}).get("assets", [])}
    for group in config.get("sectionGroups", []):
        pid, ids = group["parentId"], group["nodeIds"]
        axis = group.get("axis", "vertical")
        if pid not in nodes or axis not in ("vertical", "horizontal") or len(ids) < 2:
            raise ValueError("Section group needs a parent, axis and at least two nodeIds")
        if len(ids) != len(set(ids)):
            raise ValueError("Section group contains duplicate node IDs")
        gap = (contract or {}).get("theme", {}).get("spacing", {}).get("tokens", {}).get(group["gapToken"])
        if not number(gap) or gap < 0:
            raise ValueError("Section gapToken must resolve to a numeric spacing token")
        position, size = ("y", "height") if axis == "vertical" else ("x", "width")
        previous = None
        for nid in ids:
            if nid not in nodes or nodes[nid]["parentId"] != pid:
                add("figma.section-node", nid, "Section is absent or not a direct child")
                continue
            b = nodes[nid]["boundsInParent"]
            if previous:
                actual = b[position] - previous[position] - previous[size]
                if abs(actual - gap) > tolerance:
                    add("figma.section-gap", nid, "Expected token " + group["gapToken"] +
                        "=" + str(gap) + "; measured " + str(actual))
            previous = b
    for slot in config.get("iconSlots", []):
        nid, purpose = slot["nodeId"], slot["purpose"]
        if nid not in nodes:
            add("figma.icon-slot", nid, "Configured icon node is missing")
            continue
        if purpose in ("status", "decoration"):
            if not slot.get("reason"):
                add("figma.icon-role", nid, "Status/decorative classification needs a reason", "review")
            continue
        if purpose not in ("action", "navigation"):
            raise ValueError("Unknown icon purpose")
        asset = assets.get(slot.get("assetId"))
        if not asset or asset["kind"] != "icon" or not asset.get("source") or not asset.get("license"):
            add("figma.icon-asset", nid, "Functional icon has no traceable licensed icon asset")
        if not slot.get("label"):
            add("figma.icon-label", nid, "Functional icon has no semantic label")
        if nodes[nid]["type"] in ("ELLIPSE", "RECTANGLE", "TEXT"):
            add("figma.icon-shape", nid, "Possible placeholder; verify shape/font is the intended symbol", "review")
    # Exact, scoped exceptions stay visible; no global ignore rules.
    used = set()
    exceptions = config.get("exceptions", [])
    for i, exception in enumerate(exceptions):
        for key in ("ruleId", "nodeId", "reason", "approvedBy", "reReviewTrigger"):
            if not isinstance(exception.get(key), str) or not exception[key].strip():
                raise ValueError("Every exception needs rule/node/reason/approver/re-review trigger")
        for item in findings:
            if item["ruleId"] == exception["ruleId"] and item["location"] == exception["nodeId"]:
                if item["ruleId"] in ("figma.revision", "figma.collection", "figma.missing-font"):
                    raise ValueError("Cannot waive stale, incomplete or missing-font evidence")
                item["status"] = "approved-deviation"
                item["exception"] = exception
                used.add(i)
    for i, exception in enumerate(exceptions):
        if i not in used:
            add("figma.stale-exception", exception["nodeId"], "Exception matches no finding; re-review it", "review")
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot")
    parser.add_argument("--config")
    parser.add_argument("--contract")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()
    try:
        findings = audit(read_json(args.snapshot),
                         read_json(args.config) if args.config else None,
                         read_json(args.contract) if args.contract else None)
    except (ValueError, OSError, TypeError, KeyError) as error:
        findings = [finding("tool.input", "input", str(error), "review")]
    result = report(findings, "Visible snapshot bounds, fills/text and explicitly mapped icon slots")
    result["manualChecks"] = [
        "Actual glyph clipping, strokes/shadows, rounded corners and masks",
        "All action/navigation slots mapped; semantics, targets and contrast",
        "Section spacing/overlap, state/adaptive coverage, interaction and visual direction",
        "Final section/root screenshots and correspondence to the captured revision"
    ]
    return emit(result, args.format)


if __name__ == "__main__":
    sys.exit(main())
