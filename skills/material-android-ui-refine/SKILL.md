---
name: material-android-ui-refine
description: "Audit, fix or visually elevate existing Material 3 Android UI in Figma, screenshots or design prototypes. Use for measured defects and requests such as 'generic', 'component stacking' or 'improve hierarchy', preserving product identity and frozen boundaries unless changes are authorized. Do not use for greenfield design, a new product-wide identity or code implementation."
---

# Material Android UI Refine

Improve the existing design within the owner's requested scope. Use minimal coherent changes for defects; for authorized visual elevation, reshape the affected composition enough to resolve the observed weakness while preserving product meaning and frozen boundaries.

## Route and load proportionally

Infer audit-only, targeted fix, visual elevation, or regression from the request. Audit-only does not authorize edits. Read `references/refinement-workflow.md` and any existing handoff; do not reopen approved brand decisions for a local correction.

“Improve this layout; it looks like stacked components” authorizes visual elevation of that layout. “Only fix these clipped labels” authorizes a targeted fix. “Why does it feel generic?” is an audit. Requests to replace the whole product identity route to the design skill. Do not ask the owner to select internal mode names.

Load only affected references under `../_material-android-ui-shared/references/`: `material-foundations.md` for tokens/type, `component-specs.md` for affected components, `motion-interaction.md` for interactions, `adaptive-accessibility.md` for relevant configurations, and `handoff-contract.md` for delivery changes. Use `source-registry.md` for unstable rules.
For Figma, read `figma-structural-qa.md` in that directory before editing. For visual elevation, also read `visual-direction.md` and use its rendered critique loop. Distinguish a product-directed improvement from a Material defect; aesthetic judgments need an observed reason, not a fabricated official rule.

## Intake and preservation boundary

Inspect relevant editable source, exports, prototype, existing `material-ui-contract.json`, component library, target framework/version, and feedback. Verify that design, existing contract and export revisions match; stale or mixed evidence cannot be treated as an acceptance baseline. Infer the changed screens/states/window classes and frozen brand, content, layout or component regions from the request. If no contract exists, record the measurements and assumptions needed for this edit; reconstruct a contract only when a structured handoff is requested or needed for downstream work.

Classify each finding as a conformance defect or a visual/product improvement. Inherit approved or delegated choices. Ask only when the needed change exceeds the authorized scope or crosses an unresolved frozen boundary; continue independent in-scope work. If a requested detail conflicts with Material or accessibility, identify the exact conflict and offer viable compliant alternatives with visual/engineering tradeoffs. Record an exception only after explicit approval and include its re-review trigger.

## Audit and correction order

1. Structure and adaptive composition: task hierarchy, panes/navigation, insets, IME, scroll, overflow.
2. Foundation tokens: color roles/contrast, typography, spacing, shape, elevation, iconography, motion scheme.
3. Component correctness: semantic component, variant, size, alignment, target, state layers, every reachable state.
4. Interaction: focus/keyboard, ripple/hover/press, navigation/back, interruption, reduced motion.
5. Accessibility/localization: semantics, order, text scale, Chinese/long locale/RTL, color-independent cues.
6. Visual fidelity and consistency: repeated measurements, token drift, duplicate near-identical components, export cleanliness.

For defects, record a stable deduplicated ID, severity (`blocker`, `major`, `minor`), location, measured observation/confidence, target rule/token and source, root cause, coherent fix, affected variants and verification. For visual improvements, record the actual screenshot observation, intended product effect, proposed treatment, affected scope and before/after result; mark qualitative judgment honestly. Do not fabricate measurements, conformance violations or beauty scores.

## Visual elevation

Preserve a genuine before export. Inspect the primary task, content grouping, scale, whitespace, type/icon balance and any imagery at a readable device size. Select the consequential weakness supported by the request and image. Recompose the affected representative screen, render it, compare the same state/content/configuration, and revise if the weakness remains. Expand to affected sibling screens only after the treatment works in the representative view. An approved local composition change need not trigger a new brand interview.

Use references when they help decide a treatment; explain the transferable choice and where it appears in the result. Preserve information and actions, and keep image quality/content comparable so a decorative mockup does not masquerade as better UI. Finish with concrete visual changes and remaining concerns, not just a checklist of answered questions. Full procedure: `references/refinement-workflow.md`.

## Editing rules

- Keep stable screen/component IDs and reuse keys unless a semantic split is required.
- Bind corrected values to semantic tokens; remove accidental raw-value drift.
- Preserve selected style direction unless the request authorizes changing it. Do not flatten expressive choices that remain compliant.
- Correct all instances and states of a shared component, then inspect downstream layout changes.
- Reflow rather than shrink text when localization or font scaling exposes a fixed-height defect.
- Replace placeholder dots, generic shapes, emoji, letters, or text glyphs used as action/navigation icons with named vector assets or components. Preserve genuine status/presence/pagination indicators when their circle or dot is the intended symbol.
- For Figma, repair the innermost incorrect container first, restore its intended sizing mode, let ancestor Auto Layout frames reflow, and re-run bounds and section-gap audits.
- Update interaction definitions and design components, not only static screenshots.
- Update any existing handoff contract, revision, decisions/deviations, exports and affected verification records in the same change. For screenshot-only advice, do not invent an editable-source update.
- Preserve the approved icon family/axes and font roles. Do not make all projects use the same Rounded icons or replace brand typography with default Roboto just to claim Material compliance.
- Run the scoped snapshot audit for Figma changes and the contract validator when a contract is changed. Recollect after fixes; do not reuse pre-edit evidence. A clear automated report still requires the visual/semantic checks it explicitly cannot perform.

## Completion contract

For audit-only, deliver findings and evidence without edits. For fixes, deliver the corrected source, comparable before/after exports, scoped issue resolution and affected checks. For visual elevation, also include screenshot-grounded rationale and the observed result of revision. Update existing contracts/manifests and identify downstream effects; a full delivery package is required only when requested. For Figma edits, include changed-section/root screenshots and applicable bounds/gap/clipping checks. A pixel score does not override a failed Material semantic, adaptive, interaction, accessibility or structural-layout gate.
