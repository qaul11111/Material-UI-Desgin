---
name: material-android-ui-design
description: "Design distinctive Material 3 Android UI from product prototypes, requirements, wireframes, or flows, from visual exploration through editable design and code-ready handoff. Also use for an explicitly authorized new product-wide visual identity. Use the refinement skill for improving existing screens within their product identity; do not implement code."
---

# Material Android UI Design

Develop a product-specific visual direction in real screens, then carry the chosen decisions into an editable Material design and structured handoff. Deliver the stage and scope the owner requested.

## Route and load only what is needed

Infer the request in ordinary language; do not ask the owner to choose mode names.

- New product/visual direction: read `references/design-workflow.md` and `../_material-android-ui-shared/references/visual-direction.md` first. Connect visual references to concrete decisions in a rendered representative screen before expanding the system.
- Existing approved direction/new flow: inherit its tokens, assets and composition rules; read only the relevant workflow sections. Do not reopen brand intake unnecessarily.
- Theme-only or component-only: limit output to the requested scope and affected instances. Do not require a full product handoff for a small task.
- Existing design defect or request for visual elevation within its identity: use the refinement workflow. An authorized product-wide replacement identity belongs here; preserve the old source as a baseline.

Infer whether the owner needs exploration, a confirmed design, or development handoff. A full-design request proceeds through these stages; a concept-only request ends with reviewable concepts. Do not ask the owner to name stages or repeat an already delegated choice.

Read `../_material-android-ui-shared/references/material-foundations.md` when defining tokens; `component-specs.md` in that same directory for used components; `motion-interaction.md` for motion; `adaptive-accessibility.md` for target configurations; and `handoff-contract.md` for structured delivery. Verify unstable rules through `source-registry.md`.
For Figma writes, first read `../_material-android-ui-shared/references/figma-structural-qa.md`; use its executable checks after the final mutation.

## Input and output contract

Accept the owner's prototype in its existing form: runnable HTML/CSS, a Figma wireframe, static screenshots, sketches, annotated flows, PRD content, or a mixture. Do not require the owner to redraw or normalize it first. Inspect runnable prototypes at representative Android window sizes and inventory their routes, interactions, copy, states, and original assets. Treat prototype visuals as product intent to interpret through Material 3, not as automatically compliant styling.

When editable Figma access is available, the default final design deliverable is an editable Figma file. Its contents grow with the requested stage; a concept does not require a component catalog. HTML may be an input or temporary comparison artifact, but is not the default final UI deliverable unless requested. If Figma is unavailable, use the most editable available format and disclose the limitation; preserve the stage's required evidence.

## Intake and authority

Extract the relevant brief from supplied materials and prior decisions. Ask only missing choices that materially affect this task. For a new identity, offer an understandable color/style choice before finalizing it; use actual visual examples when adjectives are ambiguous. Previously supplied colors, approved designs and “other choices as recommended” remain valid authority within their stated scope. Record recommendations as delegated, never as a human approval that did not occur.

1. Theme color, when newly defined: obtain a primary seed/brand color or permission to propose accessible choices; precheck displayed semantic pairs. Establish static/dynamic/hybrid strategy and supported themes before theme delivery, including an API <31 static fallback when dynamic color is in scope.
2. Visual direction: understand the intended feeling and admired/avoided references. Propose a coherent Material baseline/Expressive treatment, density, shape, type, icon, imagery and motion approach; explain these through screens rather than making the owner answer a technical questionnaire.
3. Product context: users, top tasks, information hierarchy, screen/flow scope, window classes/devices, locales/RTL, accessibility needs, and known content extremes. Read framework/API versions from the repository; do not require a product owner to supply discoverable engineering facts.
4. Brand constraints: fonts, logo clear space, fixed colors, legal content, asset licensing, and any existing components that must remain.

An unresolved choice blocks only the work that depends on it. Continue authorized inspection and reversible exploration with labeled assumptions; do not invent business rules, replace frozen assets or finalize an undecided identity. Do not require a complete intake for a component-only task.

When direction is uncertain, normally compare two materially different compositions of the same real-content screen; add another only when it tests a distinct useful hypothesis. Keep tasks and information available in both. Render and inspect the candidates, explain concrete tradeoffs, and recommend one. With an established direction, develop one screen. Stop unproductive variation and revisit the brief after repeated rejection. Obtain selection before batch production unless that choice is delegated; an inherited approved system can satisfy this by reference.

Keep a concise visual study with reference observations, proposed treatments, actual exports and critique/revision evidence. At handoff, carry the chosen thesis, attention hierarchy, containment, imagery, icon and font profiles into `meta.visualDirection`; link the study through handoff evidence. Do not populate an entire contract with invented values just to explore.

Material compliance and art direction are separate acceptance questions. Expressive does not mean every control is large, colorful or decorative. Marketing collages and device mockups are optional presentation artifacts, never the source used for implementation.

## Design workflow

Apply these activities at the requested stage; full state/configuration inventories belong to system expansion and development handoff, not as prerequisites to exploration.

1. Normalize the prototype into routes, tasks, content hierarchy, data states, and interaction events. Flag ambiguous or missing behavior; do not invent business rules silently.
2. Record the working brief, supplied constraints, delegated choices and open decisions. Start a contract when useful; it is required for development handoff, not a prerequisite for drawing a concept.
3. Translate relevant visual references into composition/type/asset decisions, establish a small semantic token set, and render the representative screen. Inspect the actual image, correct consequential weaknesses and re-render changed work before selection. Expand the system after selection or delegated choice.
4. Map interactive controls to suitable Material components and target-framework variants. Compose page layouts, content graphics and brand moments to suit the task; they need not correspond to catalog components. Document custom interactive behavior and its semantics, accessibility and implementation implications.
5. Resolve hierarchy and task flows with low-fidelity studies where useful; do not mechanically wrap each prototype block in a Card. Include loading, content, empty, error, offline, permission, disabled, focus, hover, pressed, selected, and drag states that can occur.
6. Define adaptive composition at the named window classes and canonical viewports. Preserve state as panes/navigation change.
7. Apply the approved visual direction and build reusable design components/variants bound to semantic tokens.
8. Replace every prototype icon placeholder with an intentional vector asset or component. Prefer supplied product assets, then suitable Material Symbols, then an approved licensed icon set. Never use undifferentiated dots, generic circles/squares, emoji, or text glyphs as stand-ins for actions or navigation; intentional status indicators are the exception and must be named as such.
9. Specify interactions and reduced-motion behavior. Prototype critical transitions and ambiguous gestures.
10. Verify contrast, target size, text scaling, localization/RTL, focus order, screen-reader semantics, system insets, IME, and all unique adaptive branches.
11. For Figma delivery, run section-level and full-page structural QA from `../_material-android-ui-shared/references/figma-structural-qa.md`; fix every unintended crop, overlap, overflow, placeholder icon, and broken Auto Layout relationship before export.
12. Deliver the requested stage with evidence of what was actually checked. For development handoff, complete the shared contract and full in-scope conformance package. No silent deviations.

If Figma is available, use variables/styles, component properties, variants, Auto Layout, and named screens; recover original assets instead of approximating them. Fixed-height content containers require evidence that all children fit. Clipping is allowed only when it expresses intentional scrolling, masking, or media cropping and is documented.

## Completion by stage

- **Exploration:** reviewable real-content representative screen(s), concise reference-to-decision rationale, working color/type/icon choices, observed visual critique, recommendation and open decisions. Inspect rendered legibility, task hierarchy, actual icons/assets and unintended clipping. Clearly label provisional styles, media and untested configurations. A concept can be complete as a concept; it is not full Material or development acceptance.
- **Confirmed design:** selected or delegated direction, editable in-scope screens, necessary working tokens/components, relevant alternate configurations and recorded visual revision evidence. Test the direction on content extremes and in-scope dark/enlarged-text views before expanding it. Record remaining delivery work without manufacturing approval.
- **Development handoff:** all applicable items below, bounded by the agreed screens and target configurations. If this is what the owner requested, do not stop after concepts or silently omit its remaining work.

For a local theme/component change, deliver that source delta, affected-instance verification and updates to existing handoff records. Do not create unrelated screens, catalogs or a full new contract. Detailed stage evidence is in `references/design-workflow.md`.

Development handoff includes:

- editable design source plus deterministic exports for every verification configuration;
- token tables for supported themes and all selected Material subsystems;
- component inventory with variants, sizes, states, semantics, and reuse keys;
- icon and brand-asset manifest with source, semantic name, size, optical treatment, license, and component/reuse key;
- screen-state matrix, adaptive screen matrix, and critical interaction prototype/specification;
- `material-ui-contract.json`, checked with the shared `validate_contract.py` tool; distinguish draft validation from delivery validation and report missing tooling/evidence instead of silently passing;
- categorized asset manifest with source/license/variants/alt text;
- Figma structural-QA evidence when Figma is used: section and root screenshots, zero unintended child-bound overflow, verified tokenized section gaps, and documented intentional clipping;
- Material/accessibility conformance report, assumptions, unresolved questions, and approved deviations.

Do not claim full Material compliance or development readiness while required states, adaptive branches, text scaling or evidence are missing. State which stage is complete.

Retain actual selection/delegation and screenshot-based critique with the specific changes made and their observed result. Use the shared `references/regression-cases.md` when revising this Skill or validating a changed workflow; do not run the entire regression set on every small product edit.
