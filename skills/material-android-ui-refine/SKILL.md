---
name: material-android-ui-refine
description: "Audit and precisely refine an existing Android UI design, screenshot set, prototype, or Figma screen against Material 3. Use for measured corrections to tokens, typography, spacing, component geometry/states, motion, adaptive behavior, accessibility, localization, and design-to-code handoff while preserving approved product identity. Do not use for greenfield design or code implementation."
---

# Material Android UI Refine

Make the smallest coherent corrections that satisfy Material, accessibility, and the approved product direction. Preserve intent; expose conflicts instead of silently redesigning.

## Load the suite baseline

Read:

1. `../_material-android-ui-shared/references/material-foundations.md`
2. `../_material-android-ui-shared/references/component-specs.md`
3. `../_material-android-ui-shared/references/motion-interaction.md`
4. `../_material-android-ui-shared/references/adaptive-accessibility.md`
5. `../_material-android-ui-shared/references/handoff-contract.md`
6. `references/refinement-workflow.md`

Use the official source registry for unstable/version-specific questions.
When the editable source is Figma, also read `../_material-android-ui-shared/references/figma-structural-qa.md` before editing.

## Intake and preservation boundary

Inspect editable source, exports, prototype, existing `material-ui-contract.json`, component library, target framework/version, and feedback. Verify that the contract revision and design/export revisions match; stale or mixed evidence cannot be treated as an acceptance baseline. Confirm the screens/states/window classes to change and any frozen brand, content, layout, or component regions. If no contract exists, reconstruct the minimum contract from measured evidence and label every inference.

Classify each request as a conformance defect or an intentional product change. If it changes product identity or a frozen boundary, pause that edit until its owner confirms the new direction or route it back through the design skill. Ask only decisions that materially change the result. If a requested detail conflicts with Material or accessibility, identify the exact conflict and offer two compliant alternatives with visual/engineering tradeoffs. Record an exception only after explicit approval and include its re-review trigger.

## Audit and correction order

1. Structure and adaptive composition: task hierarchy, panes/navigation, insets, IME, scroll, overflow.
2. Foundation tokens: color roles/contrast, typography, spacing, shape, elevation, iconography, motion scheme.
3. Component correctness: semantic component, variant, size, alignment, target, state layers, every reachable state.
4. Interaction: focus/keyboard, ripple/hover/press, navigation/back, interruption, reduced motion.
5. Accessibility/localization: semantics, order, text scale, Chinese/long locale/RTL, color-independent cues.
6. Visual fidelity and consistency: repeated measurements, token drift, duplicate near-identical components, export cleanliness.

For each issue record a stable deduplicated ID, severity (`blocker`, `major`, `minor`), design node/screen, observed measurement, measurement confidence (`exact`, `derived`, or `estimated`), target rule/token, official source or suite baseline, proposed smallest fix, affected variants, and verification status. Fix shared tokens/components before applying per-screen patches.

## Editing rules

- Keep stable screen/component IDs and reuse keys unless a semantic split is required.
- Bind corrected values to semantic tokens; remove accidental raw-value drift.
- Preserve selected style direction. Do not flatten expressive choices that remain compliant.
- Correct all instances and states of a shared component, then inspect downstream layout changes.
- Reflow rather than shrink text when localization or font scaling exposes a fixed-height defect.
- Replace placeholder dots, generic shapes, emoji, letters, or text glyphs used as action/navigation icons with named vector assets or components. Preserve genuine status/presence/pagination indicators when their circle or dot is the intended symbol.
- For Figma, repair the innermost incorrect container first, restore its intended sizing mode, let ancestor Auto Layout frames reflow, and re-run bounds and section-gap audits.
- Update interaction definitions and design components, not only static screenshots.
- Update the handoff contract, revision, decisions/deviations, exports, and verification matrix in the same change.

## Completion contract

Deliver corrected editable source; before/after exports at exact configurations; resolved issue ledger; updated contract and asset manifest; regression matrix; remaining risks; and conformance report. For Figma, include section/root screenshots, child-bound overflow results, section-gap checks, and documented intentional clipping. A pixel score does not override a failed Material semantic, adaptive, interaction, accessibility, or structural-layout gate.
