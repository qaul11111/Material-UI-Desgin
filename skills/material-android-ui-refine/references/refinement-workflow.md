# Evidence-based refinement and visual elevation

## Choose the scope from the request

- Audit-only: explain observed problems without writes.
- Targeted fix: make the smallest coherent correction to the reported defect and shared root cause.
- Visual elevation: improve composition, hierarchy, type/icon balance or imagery within the authorized existing identity. Use the rendered critique loop in `../../_material-android-ui-shared/references/visual-direction.md`.
- Regression: verify the affected states and instances after a change.

An explicit request to improve a generic-looking page permits relevant recomposition; it does not automatically permit a new logo, brand identity, business flow or unrelated screens. Preserve user-declared frozen boundaries. A full replacement identity routes to the design workflow; do not ask again for authority already granted.

## 1. Establish evidence

Collect editable source, exact exports, component/variable library, prototype transitions, content/localization samples, target framework/version, and any previous conformance report. Compare source, contract, export, and runtime revisions; resolve staleness or explicitly block affected comparisons. Freeze a baseline revision before editing. List incomplete evidence instead of assuming it exists.

If comparing runtime UI, capture viewport, pixel ratio, theme, locale, font scale, state fixture, system-bar/IME treatment, and build revision. A screenshot without configuration metadata is visual context, not pass/fail evidence.

## 2. Issue ledger

Use one row per independently verifiable defect:

| Field | Meaning |
|---|---|
| ID | Stable issue ID; reuse it for the same root cause and deduplicate repeated instances |
| Request class | Conformance defect or visual/product improvement |
| Severity | `blocker`, `major`, or `minor` |
| Location | Screen/component/node/state/viewport |
| Observed | Measured value/behavior for a defect; visible region and concrete qualitative observation for visual improvement |
| Confidence | `exact`, `derived`, or `estimated` for measurements; label qualitative judgment without fake precision |
| Expected | Applicable Material requirement, or the intended effect from the authorized product brief |
| Source | Exact rule/version for conformance; supplied brief/reference and image evidence for aesthetic decisions |
| Root cause | Token, shared component, local override, layout, content, or interaction |
| Fix | Minimal defect correction, or a justified visual treatment within the authorized scope |
| Blast radius | Instances/states/breakpoints/themes/locales affected |
| Verification | Before/after evidence and status |

Severity guidance:

Use severity for defects. Prioritize aesthetic changes by their impact on the primary task and approved identity; do not label personal preference a Material blocker.

- blocker: prevents task completion, creates severe accessibility/security/data-loss risk, or makes handoff unusable;
- major: Material component/state/adaptive/accessibility failure or repeated visual-system inconsistency;
- minor: localized polish defect without task/accessibility impact.

## 3. Measure before changing

Measure token use, bounding boxes, visible bounds of SVG/icon artwork, padding/gaps, baselines, line height, wrapping, color/opacity, contrast, corner radius, elevation, state-layer geometry, target bounds, and transition timing/curve. Distinguish a visible icon's artwork bounds from its layout box.

For Figma containers, also measure maximum child right/bottom bounds, clipping mode, Auto Layout sizing mode, sibling section boundaries, and the token represented by each inter-section gap. Treat action/navigation dots and generic shapes as unresolved placeholders unless their shape is the documented product meaning.

Compare repeated instances to detect systemic drift. If five cards share the same 13 dp radius, correct the component/token once rather than patching five screens.

### Visual elevation loop

1. Preserve the current source/export and its configuration. Identify what is frozen, delegated and open to change.
2. Inspect the actual composition: first noticeable element, primary task, supporting information, containment, rhythm, type/icon balance and relevant imagery. Connect the significant weakness to the user's complaint.
3. Choose a representative affected screen. Use references only if they help decide the treatment; record the visible observation and product-specific transfer. Preserve content and actions.
4. Make the coherent composition/type/asset changes needed to test the hypothesis. Fix a shared token first when it is the real cause, but do not require a full token-system rebuild before exploring a local composition.
5. Render and compare the same viewport, theme, locale, font scale, content and state. Record what visibly improved, what remains and any regression. Revise consequential weaknesses and re-render; do not stop at a written critique.
6. Carry a successful treatment into authorized affected siblings and challenging states. Verify relevant enlarged text, long copy and target layouts. Stop at the requested scope, or ask only if a necessary change would cross a frozen boundary.

The loop can finish when the observed weakness is resolved and affected checks pass. Do not invent product-owner acceptance, always demand two variants, or keep restyling a screen with no specific unresolved concern.

## 4. Correct in dependency order

1. Wrong semantics/information architecture and adaptive pattern.
2. Foundation variable/style definitions.
3. Shared component definitions and variants.
4. Screen composition and instance configuration.
5. Interaction/prototype transitions and semantics.
6. Export naming/configuration and handoff contract.

After each shared correction inspect affected variants in supported themes, reachable states and affected breakpoints. Preserve intentional optical adjustments only when named and documented.

## 5. Conflict handling

When product direction conflicts with a rule:

1. quote/paraphrase the exact requirement and show the measured conflict;
2. explain user impact, not merely “Material says so”;
3. provide two compliant alternatives that retain the desired brand effect;
4. mock the smallest representative comparison if useful;
5. if the owner rejects both, record an approved deviation with impact, compensating tests, and a concrete re-review trigger.

If a needed change crosses an unapproved product identity, frozen content or core information-architecture boundary, preserve the baseline and request the missing decision for that change. If the user already authorized it, follow that authorization; a full new identity uses the design workflow. Visual elevation within an existing identity does not automatically reopen brand approval.

Accessibility and platform security are release gates, not aesthetic preferences. Do not accept an exception that creates an unsafe WebView, inaccessible task, or destructive ambiguity without explicit risk ownership.

## 6. Regression matrix

Retest every unique layout/state branch touched by the root cause. Within the supported scope, include both themes when color or elevation changes, enlarged text and long copy when type/size changes, RTL when direction/alignment changes, hover/focus/press when control geometry changes, and all affected instances when a shared component changes. Do not introduce new product modes merely to populate a test matrix.

Use the shared comparator for exact exports/runtime captures, but manually inspect text baselines, anti-aliasing, semantics, target bounds, focus, scrolling, and motion. Record masks and exclusions.

For Figma changes, retain a readable screenshot of every changed section plus the full root frame. Acceptance requires zero unintended child-bound overflow and no section overlap; intentional scrolling, masking, or media cropping must be documented.

## 7. Completion report

Report the requested scope: findings only for an audit; corrected root causes and affected checks for fixes; observed composition changes and genuine before/after evidence for visual elevation. Update existing contract/manifests and report downstream impact when affected. No new full contract is required for isolated fixes without a prior handoff. Distinguish draft design improvements from a full development-ready package. Do not hide unresolved major/blocker issues in a generic “known limitations” note.
