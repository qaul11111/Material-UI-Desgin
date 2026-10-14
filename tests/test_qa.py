import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "skills/_material-android-ui-shared"
sys.path.insert(0, str(SHARED / "scripts"))
from audit_figma_snapshot import audit
from validate_contract import validate
from qa_common import report, sha256


def node(nid, parent=None, x=0, y=0, width=100, height=100, kind="FRAME", **changes):
    item = dict(id=nid, name=nid, parentId=parent, type=kind, width=width, height=height,
                boundsInParent=None if parent is None else dict(x=x, y=y, width=width, height=height),
                clipsContent=False, hasMask=False, rawSolidFills=0, textStyleStatus="styled",
                hasMissingFont=False, textAutoResize="HEIGHT")
    item.update(changes)
    return item


def snapshot(*nodes):
    return dict(schemaVersion="1.0", revision="design-r1", roots=[n["id"] for n in nodes if n["parentId"] is None],
                nodes=list(nodes), errors=[])


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads((SHARED / "examples/material-ui-contract.example.json").read_text())

    def rules(self, **options):
        return {i["ruleId"] for i in validate(self.contract, **options)}

    def test_draft_example_has_no_broken_references(self):
        self.assertEqual(self.rules(), set())

    def test_legacy_contract_still_supported(self):
        del self.contract["meta"]["visualDirection"]
        self.assertEqual(self.rules(), set())

    def test_draft_is_not_delivery(self):
        self.assertTrue({"contract.approval", "contract.coverage", "contract.evidence"} <= self.rules(delivery=True))

    def test_duplicate_ids(self):
        self.contract["components"].append(copy.deepcopy(self.contract["components"][0]))
        self.assertIn("contract.duplicate", self.rules())

    def test_missing_component(self):
        self.contract["components"].pop(0)
        self.assertIn("contract.component-ref", self.rules())

    def test_wrong_variant_reference(self):
        self.contract["verification"]["configurations"][0]["variantId"] = "missing"
        self.assertIn("contract.variant-ref", self.rules())

    def test_unknown_viewport(self):
        self.contract["screens"][0]["variants"][0]["viewportId"] = "missing"
        self.assertIn("contract.viewport-ref", self.rules(delivery=True))

    def test_event_binding(self):
        self.contract["interactions"][0]["event"] = "Unknown"
        self.assertIn("contract.event", self.rules())

    def test_data_binding(self):
        self.contract["components"][0]["dataBindings"] = ["unknown"]
        self.assertIn("contract.binding", self.rules())

    def test_font_reference(self):
        self.contract["meta"]["visualDirection"]["fontProfile"]["assetIds"] = ["missing-font"]
        self.assertIn("contract.font-ref", self.rules())

    def test_stale_snapshot_and_direction(self):
        self.contract["meta"]["visualDirection"]["sourceRevision"] = "old"
        self.assertIn("contract.revision", self.rules(snapshot={"revision": "old"}))

    def test_file_and_hash_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            export = Path(directory) / "exports/sign-in-compact-light-content-zh.png"
            export.parent.mkdir()
            export.write_bytes(b"test-only-artifact")
            index = dict(revision="design-r1", files=[dict(path=export.relative_to(directory).as_posix(), sha256=sha256(export))])
            self.assertEqual(self.rules(root=directory, artifact_index=index), set())
            export.write_bytes(b"changed")
            self.assertIn("contract.hash", self.rules(root=directory, artifact_index=index))
            index["revision"] = "old"
            self.assertIn("contract.revision", self.rules(root=directory, artifact_index=index))

    def test_path_traversal(self):
        self.contract["screens"][0]["variants"][0]["reference"] = "../outside.png"
        with tempfile.TemporaryDirectory() as directory:
            self.assertIn("contract.file", self.rules(root=directory))

    def test_invalid_schema_is_reported(self):
        self.contract["screens"] = "wrong"
        self.assertEqual(self.rules(), {"contract.schema"})

    def test_delivery_can_pass_only_with_recorded_scope_and_artifacts(self):
        c = self.contract
        c["targets"].update(locales=["zh-CN"], fontScales=[1], themeModes=["light"], windowClasses=["compact"])
        c["targets"]["canonicalViewports"] = c["targets"]["canonicalViewports"][:1]
        c["verification"]["configurations"][0]["status"] = "passed"
        c["meta"]["visualDirection"].update(status="approved", approvedBy="Test fixture owner",
                                            approvalEvidence="Test fixture only; not a real product approval")
        with tempfile.TemporaryDirectory() as directory:
            export = Path(directory) / c["screens"][0]["variants"][0]["reference"]
            export.parent.mkdir()
            export.write_bytes(b"test-only-not-an-actual-screenshot")
            index = dict(revision="design-r1", files=[dict(path=export.relative_to(directory).as_posix(), sha256=sha256(export))])
            self.assertEqual(self.rules(root=directory, artifact_index=index, delivery=True), set())


class FigmaAuditTests(unittest.TestCase):
    def test_good_geometry(self):
        self.assertEqual(audit(snapshot(node("r"), node("c", "r", width=80, height=80))), [])

    def test_foundations_crop_reproductions(self):
        for name, height in (("Colors", 60), ("Elevation", 50)):
            with self.subTest(section=name):
                s = snapshot(node(name, height=height), node("specimen", name, y=35, height=60))
                self.assertIn("figma.bounds", {x["ruleId"] for x in audit(s)})
                s["nodes"][0]["height"] = 100
                self.assertEqual(audit(s), [])

    def test_negative_left_top_detected(self):
        rows = audit(snapshot(node("r"), node("c", "r", x=-4, y=-3, width=20, height=20)))
        self.assertEqual(rows[0]["ruleId"], "figma.bounds")

    def test_clipping_disabled_does_not_hide_overflow(self):
        self.assertEqual(report(audit(snapshot(node("r"), node("c", "r", y=90))), "")["status"], "failed")

    def test_rotated_child_uses_transformed_bounds(self):
        child = node("c", "r", width=20, height=20)
        child["boundsInParent"] = dict(x=-10, y=5, width=28, height=28)
        self.assertTrue(audit(snapshot(node("r"), child)))

    def test_intentional_scroll_exception_retains_evidence(self):
        s = snapshot(node("r", clipsContent=True), node("scroll-content", "r", height=200))
        config = {"exceptions": [dict(ruleId="figma.bounds", nodeId="scroll-content", reason="Intentional vertical scrolling",
                                     approvedBy="Test owner", reReviewTrigger="Change scroll ownership")]}
        rows = audit(s, config)
        self.assertEqual(rows[0]["status"], "approved-deviation")
        self.assertIn("Outside parent", rows[0]["evidence"])

    def test_unreasoned_exception_rejected(self):
        with self.assertRaises(ValueError):
            audit(snapshot(node("r")), {"exceptions": [{"ruleId": "figma.bounds", "nodeId": "r"}]})

    def test_functional_dot_without_asset_fails(self):
        s = snapshot(node("r"), node("dot", "r", kind="ELLIPSE", width=24, height=24))
        rows = audit(s, {"iconSlots": [dict(nodeId="dot", purpose="navigation", label="客户")]})
        self.assertIn("figma.icon-asset", {x["ruleId"] for x in rows})

    def test_status_dot_is_not_a_placeholder(self):
        s = snapshot(node("r"), node("dot", "r", kind="ELLIPSE", width=8, height=8))
        self.assertEqual(audit(s, {"iconSlots": [dict(nodeId="dot", purpose="status", reason="Online status")]}), [])

    def test_real_icon_mapping(self):
        s = snapshot(node("r"), node("icon", "r", kind="VECTOR", width=24, height=24))
        contract = dict(meta=dict(revision="design-r1"), assets=[dict(id="people", kind="icon", source="licensed fixture", license="test")])
        self.assertEqual(audit(s, {"iconSlots": [dict(nodeId="icon", purpose="navigation", assetId="people", label="客户")]}, contract), [])

    def test_fixed_text_and_raw_styles_need_review(self):
        s = snapshot(node("r"), node("t", "r", kind="TEXT", textAutoResize="NONE", textStyleStatus="raw-or-mixed", rawSolidFills=1))
        self.assertEqual(report(audit(s), "")["status"], "needs-review")

    def test_missing_font_fails(self):
        rows = audit(snapshot(node("r"), node("t", "r", kind="TEXT", hasMissingFont=True)))
        self.assertIn("figma.missing-font", {x["ruleId"] for x in rows})

    def test_empty_snapshot_rejected(self):
        with self.assertRaises(ValueError):
            audit(snapshot())

    def test_missing_collector_field_rejected(self):
        s = snapshot(node("r"), node("child", "r"))
        del s["nodes"][1]["hasMissingFont"]
        with self.assertRaises(ValueError):
            audit(s)

    def test_invalid_config_rejected(self):
        for config in ({"iconSlots": "wrong"}, {"exceptions": ["wrong"]}, {"tolerance": 50}):
            with self.subTest(config=config):
                with self.assertRaises(ValueError):
                    audit(snapshot(node("r")), config)

    def test_snapshot_revision_mismatch(self):
        rows = audit(snapshot(node("r"), node("c", "r")), contract={"meta": {"revision": "old"}})
        self.assertIn("figma.revision", {x["ruleId"] for x in rows})

    def test_missing_fonts_cannot_be_waived(self):
        s = snapshot(node("r"), node("t", "r", kind="TEXT", hasMissingFont=True))
        exception = dict(ruleId="figma.missing-font", nodeId="t", reason="Ignore", approvedBy="Test",
                         reReviewTrigger="Later")
        with self.assertRaises(ValueError):
            audit(s, {"exceptions": [exception]})

    def test_partial_snapshot_is_review_not_pass(self):
        s = snapshot(node("r"), node("c", "r"))
        s["errors"] = [dict(nodeId="c", message="unreadable text")]
        self.assertEqual(report(audit(s), "")["status"], "needs-review")

    def test_duplicate_or_missing_parent_rejected(self):
        for s in (snapshot(node("r"), node("r")), snapshot(node("r"), node("c", "missing"))):
            with self.subTest(snapshot=s):
                with self.assertRaises(ValueError):
                    audit(s)

    def test_section_token_gap(self):
        s = snapshot(node("r", height=300), node("a", "r", height=80), node("b", "r", y=100, height=80))
        config = dict(sectionGroups=[dict(parentId="r", nodeIds=["a", "b"], gapToken="section")])
        contract = dict(meta=dict(revision="design-r1"), theme=dict(spacing=dict(tokens=dict(section=24))))
        self.assertIn("figma.section-gap", {x["ruleId"] for x in audit(s, config, contract)})
        s["nodes"][2]["boundsInParent"]["y"] = 104
        self.assertEqual(audit(s, config, contract), [])

    def test_invalid_input_cli_nonzero_and_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bad.json"
            source.write_text("{}")
            result = subprocess.run([sys.executable, str(SHARED / "scripts/audit_figma_snapshot.py"), str(source)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)["status"], "needs-review")


if __name__ == "__main__":
    unittest.main()
