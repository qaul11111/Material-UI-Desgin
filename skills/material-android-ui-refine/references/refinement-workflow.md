# Measured refinement workflow

## 1. Establish evidence

Collect editable source, exact exports, component/variable library, prototype transitions, content/localization samples, target framework/version, and any previous conformance report. Compare source, contract, export, and runtime revisions; resolve staleness or explicitly block affected comparisons. Freeze a baseline revision before editing. List incomplete evidence instead of assuming it exists.

If comparing runtime UI, capture viewport, pixel ratio, theme, locale, font scale, state fixture, system-bar/IME treatment, and build revision. A screenshot without configuration metadata is visual context, not pass/fail evidence.

## 2. Issue ledger

Use one row per independently verifiable defect:

| Field | Meaning |
|---|---|
| ID | Stable issue ID; reuse it for the same root cause and deduplicate repeated instances |
| Request class | Conformance defect or intentional product change |
| Severity | `blocker`, `major`, or `minor` |
| Location | Screen/component/node/state/viewport |
| Observed | Measured current value or behavior |
| Confidence | `exact`, `derived`, or `estimated`, with method/evidence |
| Expected | Material token/component/accessibility requirement |
| Source | Shared baseline or exact official/version source |
| Root cause | Token, shared component, local override, layout, content, or interaction |
| Fix | Smallest coherent correction |
| Blast radius | Instances/states/breakpoints/themes/locales affected |
| Verification | Before/after evidence and status |

Severity guidance:

- blocker: prevents task completion, creates severe accessibility/security/data-loss risk, or makes handoff unusable;
- major: Material component/state/adaptive/accessibility failure or repeated visual-system inconsistency;
- minor: localized polish defect without task/accessibility impact.

## 3. Measure before changing

Measure token use, bounding boxes, visible bounds of SVG/icon artwork, padding/gaps, baselines, line height, wrapping, color/opacity, contrast, corner radius, elevation, state-layer geometry, target bounds, and transition timing/curve. Distinguish a visible icon's artwork bounds from its layout box.

For Figma containers, also measure maximum child right/bottom bounds, clipping mode, Auto Layout sizing mode, sibling section boundaries, and the token represented by each inter-section gap. Treat action/navigation dots and generic shapes as unresolved placeholders unless their shape is the documented product meaning.

Compare repeated instances to detect systemic drift. If five cards share the same 13 dp radius, correct the component/token once rather than patching five screens.

## 4. Correct in dependency order

1. Wrong semantics/information architecture and adaptive pattern.
2. Foundation variable/style definitions.
3. Shared component definitions and variants.
4. Screen composition and instance configuration.
5. Interaction/prototype transitions and semantics.
6. Export naming/configuration and handoff contract.

After each shared correction inspect all variants in both themes, reachable states, and affected breakpoints. Preserve intentional optical adjustments only when named and documented.

## 5. Conflict handling

When product direction conflicts with a rule:

1. quote/paraphrase the exact requirement and show the measured conflict;
2. explain user impact, not merely “Material says so”;
3. provide two compliant alternatives that retain the desired brand effect;
4. mock the smallest representative comparison if useful;
5. if the owner rejects both, record an approved deviation with impact, compensating tests, and a concrete re-review trigger.

If a request changes the approved product identity, frozen content, or core information architecture, do not disguise it as defect correction. Route it back through the design decision process and preserve the last approved baseline until a new direction is owned.

Accessibility and platform security are release gates, not aesthetic preferences. Do not accept an exception that creates an unsafe WebView, inaccessible task, or destructive ambiguity without explicit risk ownership.

## 6. Regression matrix

Retest every unique layout/state branch touched by the root cause. Always include both themes when color or elevation changes, enlarged text and long copy when type/size changes, RTL when direction/alignment changes, hover/focus/press when control geometry changes, and all screen instances when a shared component changes.

Use the shared comparator for exact exports/runtime captures, but manually inspect text baselines, anti-aliasing, semantics, target bounds, focus, scrolling, and motion. Record masks and exclusions.

For Figma changes, retain a readable screenshot of every changed section plus the full root frame. Acceptance requires zero unintended child-bound overflow and no section overlap; intentional scrolling, masking, or media cropping must be documented.

## 7. Completion report

Summarize resolved counts by severity, root causes corrected, before/after evidence, contract revision, changed shared tokens/components, remaining approved deviations, blocked items, and downstream implementation impact. Do not hide unresolved major/blocker issues in a generic “known limitations” note.
