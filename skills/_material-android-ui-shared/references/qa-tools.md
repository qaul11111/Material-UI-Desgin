# Read-only QA tools

These tools do not generate UI, fix Figma, fetch URLs or certify Material compliance.

## Setup

Commands run from the handoff folder. Set SHARED to the installed sibling _material-android-ui-shared directory. Contract validation needs Python 3.9+ and jsonschema 4.18–4.x; snapshot audit uses the standard library. Node 18+ is only for collector mock tests.

    python3 -m venv .venv
    .venv/bin/python -m pip install -r "$SHARED/scripts/requirements.txt"
    .venv/bin/python "$SHARED/scripts/validate_contract.py" material-ui-contract.json

Do not install into system Python automatically. Missing dependencies produce needs-review and exit 2, not success.

## Contract validation

Draft mode checks Schema and cross-references without pretending files or promised variants are delivered.

    .venv/bin/python "$SHARED/scripts/validate_contract.py" material-ui-contract.json \
      --root . --artifact-index artifact-index.json --snapshot figma-snapshot.json --delivery

Delivery mode also checks recorded approval/delegation, targeted configuration coverage, passed verification records, revisions and files/hashes. It does not independently prove a claimed human approval or recorded test result; retain actual evidence.

Artifact index:

    {
      "revision": "design-r2",
      "files": [
        {"path": "exports/home-light.png", "sha256": "<actual SHA-256>"},
        {"path": "figma-snapshot.json", "sha256": "<actual SHA-256>"}
      ]
    }

Include every referenced export, representative export, bundled asset destinationHint, verification evidence and mask. List the snapshot in verification.evidence so it is hashed too. Compute hashes after the final mutation/export, for example with shasum -a 256 on exact named files. Never invent hashes.

An index stamped with a new revision is not proof that Figma itself is current. Only handoff-relative local paths are accepted for file checks; traversal and symlink escapes are rejected. sourcePrototype/sourceDesign/source asset URLs are provenance, not automatically fetched evidence. System fonts need no bundled file but do require verified rendering and fallback.

The shipped example is deliberately a DRAFT: limited tokens, planned exports and incomplete configuration coverage must not pass delivery mode.

## Figma collection and audit

The collector runs inside a supported Figma Plugin API tool, not a shell or browser page. Read its source and follow the installed tool instructions, then call:

    const snapshot = await collectMaterialSnapshot({
      rootIds: ["<observed Figma frame ID>"],
      revision: "<current contract revision>"
    });
    return snapshot;

Save the returned JSON using the host's allowed file workflow; no remote upload is required.

    python3 "$SHARED/scripts/audit_figma_snapshot.py" figma-snapshot.json \
      --contract material-ui-contract.json --config audit-config.json

JSON is default; use --format markdown for a readable report. Both tools print to stdout without writing files.

Configuration example (replace IDs with observed IDs):

    {
      "tolerance": 0.5,
      "iconSlots": [
        {"nodeId": "1:4", "purpose": "navigation", "assetId": "people-icon", "label": "客户"},
        {"nodeId": "1:5", "purpose": "status", "reason": "Online presence indicator"}
      ],
      "sectionGroups": [
        {"parentId": "1:2", "nodeIds": ["1:10", "1:20"], "axis": "vertical", "gapToken": "section"}
      ],
      "exceptions": []
    }

Map all in-scope functional icon slots. Asset IDs resolve to licensed icon assets in the contract; human review still confirms their meaning. section resolves to a numeric theme.spacing.tokens entry. Section groups list direct children in visual order.

Intentional scroll/media crops or reviewed raw artwork fills can use an exact exception with ruleId, nodeId, reason, approvedBy and reReviewTrigger. No blanket page exemptions. Exceptions do not waive stale snapshots, collection errors or missing fonts and must be reviewed when stale.

## Results

- Exit 0 / checks-clear: implemented checks found no unresolved issue; not complete acceptance.
- Exit 1 / failed: a deterministic check failed.
- Exit 2 / needs-review: input/tooling is incomplete or human review is needed.
- approved-deviation: exact documented exception retained in findings.

Checks cover transformed bounds, section-token gaps, missing fonts, raw fill/text-style candidates, mapped icon assets and revision/reference/file consistency.

Manual checks still cover actual glyph clipping/coverage, masks/rounded outlines, shadows, imagery, optical alignment, icon meaning, contrast, touch targets, interaction, accessibility and aesthetics. No node-tree audit can prove all of these.

## Regression

From the repository root:

    python3 -m unittest discover -s tests -p 'test_*.py' -v
    node --test tests/collector.test.js

See [regression-cases.md](regression-cases.md). Mock/API tests are not live Figma end-to-end validation.
