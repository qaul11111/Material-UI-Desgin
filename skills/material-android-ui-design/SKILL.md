---
name: material-android-ui-design
description: "Create a complete, high-fidelity Material 3 Android UI design from a product prototype, requirement, wireframe, or flow. Use for greenfield UI design that needs theme/style discovery, semantic tokens, adaptive screen variants, component states, motion, accessibility, and a code-ready handoff for Compose or Flutter/WebView. Do not use for auditing an already designed UI or implementing code."
---

# Material Android UI Design

Create the design and the structured handoff as one artifact. The next refinement and implementation skills must be able to continue without reinterpreting intent.

## Load the suite baseline

Read these sibling resources before designing:

1. `../_material-android-ui-shared/references/material-foundations.md`
2. `../_material-android-ui-shared/references/component-specs.md`
3. `../_material-android-ui-shared/references/motion-interaction.md`
4. `../_material-android-ui-shared/references/adaptive-accessibility.md`
5. `../_material-android-ui-shared/references/handoff-contract.md`
6. `references/design-workflow.md`

Use `../_material-android-ui-shared/references/source-registry.md` when a current or version-specific rule must be verified.
When the editable destination is Figma, also read `../_material-android-ui-shared/references/figma-structural-qa.md` before the first Figma write.

## Input and output contract

Accept the owner's prototype in its existing form: runnable HTML/CSS, a Figma wireframe, static screenshots, sketches, annotated flows, PRD content, or a mixture. Do not require the owner to redraw or normalize it first. Inspect runnable prototypes at representative Android window sizes and inventory their routes, interactions, copy, states, and original assets. Treat prototype visuals as product intent to interpret through Material 3, not as automatically compliant styling.

When editable Figma access is available, the default final design deliverable is an editable Figma file containing decisions, foundations, reusable components, screens, states, adaptive variants, motion specifications, and handoff evidence. HTML may be used as an input or temporary visual reference; it is not the default final UI artifact unless the owner explicitly requests HTML. If Figma is unavailable, use the most editable native design format available and preserve the same structure and handoff contract.

## Intake gate

Inspect every supplied prototype, requirement, flow, content sample, brand asset, target device, and existing design-system artifact before asking questions. Then ask the product owner for the decisions below. Final UI is blocked until each is answered or the owner explicitly authorizes recorded defaults.

1. Theme color: require a primary seed/brand color or permission to propose 2–3 accessible seeds; precheck proposed seeds in semantic light/dark roles; choose static, dynamic, or hybrid color; confirm the API <31 static fallback for dynamic color plus light, dark, and system-theme scope.
2. Visual direction: choose Material baseline or Expressive; collect 3–5 style adjectives; choose density, shape character, icon family, imagery treatment, and motion intensity; collect admired references and “must avoid” examples.
3. Product context: users, top tasks, information hierarchy, screen/flow scope, target Android API/frameworks, window classes/devices, locales/RTL, accessibility needs, and known content extremes.
4. Brand constraints: fonts, logo clear space, fixed colors, legal content, asset licensing, and any existing components that must remain.

When visual direction is uncertain, create two or three small style directions using the same representative screen and content. Show meaningful differences in semantic palette, typography emphasis, shape, density, imagery, and motion. Ask the owner to select or combine them before producing the full set. Limit comparison to two rounds; if none fits, reopen the style brief instead of generating unbounded variants. Do not call arbitrary aesthetic choices “Material requirements.”

## Design workflow

1. Normalize the prototype into routes, tasks, content hierarchy, data states, and interaction events. Flag ambiguous or missing behavior; do not invent business rules silently.
2. Create the `material-ui-contract.json` from the shared schema and record all intake decisions and assumptions.
3. Build semantic light/dark color, typography, spacing, shape, elevation, icon, and motion tokens before polishing screens.
4. Map each UI element to an official Material component and supported target-framework variant. Document custom-component rationale.
5. Design task flows in grayscale/low fidelity first, including loading, content, empty, error, offline, permission, disabled, focus, hover, pressed, selected, and drag states that can occur.
6. Define adaptive composition at the named window classes and canonical viewports. Preserve state as panes/navigation change.
7. Apply the approved visual direction and build reusable design components/variants bound to semantic tokens.
8. Replace every prototype icon placeholder with an intentional vector asset or component. Prefer supplied product assets, then suitable Material Symbols, then an approved licensed icon set. Never use undifferentiated dots, generic circles/squares, emoji, or text glyphs as stand-ins for actions or navigation; intentional status indicators are the exception and must be named as such.
9. Specify interactions and reduced-motion behavior. Prototype critical transitions and ambiguous gestures.
10. Verify contrast, target size, text scaling, localization/RTL, focus order, screen-reader semantics, system insets, IME, and all unique adaptive branches.
11. For Figma delivery, run section-level and full-page structural QA from `../_material-android-ui-shared/references/figma-structural-qa.md`; fix every unintended crop, overlap, overflow, placeholder icon, and broken Auto Layout relationship before export.
12. Export the complete handoff package and a conformance report. No silent deviations.

If Figma is available, use variables/styles, component properties, variants, Auto Layout, and named screens; recover original assets instead of approximating them. Fixed-height content containers require evidence that all children fit. Clipping is allowed only when it expresses intentional scrolling, masking, or media cropping and is documented.

## Completion contract

Deliver all of the following:

- editable design source plus deterministic exports for every verification configuration;
- token tables for light/dark and all selected Material subsystems;
- component inventory with variants, sizes, states, semantics, and reuse keys;
- icon and brand-asset manifest with source, semantic name, size, optical treatment, license, and component/reuse key;
- screen-state matrix, adaptive screen matrix, and critical interaction prototype/specification;
- `material-ui-contract.json`, validated when possible against the shared schema;
- categorized asset manifest with source/license/variants/alt text;
- Figma structural-QA evidence when Figma is used: section and root screenshots, zero unintended child-bound overflow, verified tokenized section gaps, and documented intentional clipping;
- Material/accessibility conformance report, assumptions, unresolved questions, and approved deviations.

Do not claim “complete,” “Material compliant,” or “99% handoff ready” while required states, adaptive branches, text scaling, or evidence are missing.
