# Design-to-code handoff contract

The suite uses `material-ui-contract.json` as the continuity artifact. The design skill creates it, the refinement skill updates it, and either implementation skill consumes it. Validate it against `../schemas/material-ui-contract.schema.json` when a JSON Schema validator is available.

## Ownership and lifecycle

1. Product/design owns intent, approved visual direction, content, flows, and deviations.
2. Design records exact semantic tokens, component variants, adaptive behavior, states, interactions, assets, and data placeholders.
3. Refinement preserves stable IDs and updates only changed values, issue resolution, verification, and revision metadata.
4. Engineering maps each stable screen/component/asset ID to code and reports implementation-only deviations.
5. Visual QA compares the exact design export and runtime screenshot at the same viewport, pixel ratio, theme, locale, font scale, state, and system-bar policy.

Never use a screenshot as the sole handoff when source variables/components or this contract can be supplied. Never invent backend behavior from visual appearance; represent unknown data and events as typed seams.

## Required contract content

- `meta`: product/feature, revision, source prototype/design, Material snapshot, baseline or expressive flavor, repository framework/library pins, owners, decisions, assumptions.
- `targets`: Compose/Flutter/WebView scope, Android API range, locales, RTL, window classes, canonical viewports, font scales, theme modes.
- `theme`: semantic color roles for light/dark, typography, spacing, shape, elevation, motion, icon strategy.
- `screens`: stable IDs, routes, layout behavior per window class, system insets, state variants, focus order, scroll behavior.
- `components`: stable IDs, Material component/variant/size, reuse key, token overrides, content rules, states, semantics, data bindings.
- `interactions`: trigger, source/destination state, event, navigation, motion, reduced-motion path, interruption.
- `assets`: kind, source, license, dimensions/density variants, localization/theme variants, alt text, destination hint.
- `dataContract`: immutable UI state fields, events, loading/content/empty/error/offline/permission states, validation, sample/fake data.
- `deviations`: stable ID, rule, reason, alternatives considered, approver, impact, tests, and the condition that triggers re-review. An empty array is valid and preferred.
- `verification`: exact configurations, geometry tolerances, screenshot match rule, masks, accessibility gates, and evidence locations.

## Operational definition of 99% visual fidelity

A claim of “99%” is valid only when all of the following hold:

1. Reference export and runtime screenshot have identical pixel dimensions. Do not resize either image for comparison.
2. Capture uses the same logical viewport, device-pixel ratio, theme, locale, font scale, content/state fixture, and system-bar treatment.
3. At least 99% of evaluated pixels have a maximum per-channel difference no greater than 8 on a 0–255 scale. Use `../scripts/visual_match.py` or an equivalent documented comparator.
4. Masks cover only declared nondeterministic regions such as system time or approved dynamic media. Excluded area and reason are recorded; masks may not hide layout or component defects.
5. Key geometry anchors are within 1 logical dp/pixel unless the component/platform rasterization requires a recorded tolerance. Typography family, role, weight, size, line height, letter spacing, wrapping, and baseline must match tokens.
6. There is no clipping, overflow, missing state, wrong navigation behavior, accessibility failure, or unapproved Material deviation. These fail acceptance even if the pixel score passes.
7. Every unique adaptive branch and critical state has evidence. One phone screenshot cannot establish product-wide fidelity.

Anti-aliasing differences may be tolerated by the channel threshold; structural changes may not. A pixel score is diagnostic evidence, not permission to compromise semantics or platform behavior.

## Required evidence matrix

At minimum include:

- all in-scope compact/medium/expanded branches, plus large/extra-large when targeted;
- light and dark themes;
- content, loading, empty, recoverable error, and offline/permission states that can occur;
- base and enlarged font scale;
- `zh-CN` plus the longest supported locale, and one RTL locale if supported;
- focused/hovered navigation for keyboard/mouse scope;
- WebView loading, navigation rejection, main-frame error, back, and themed content when WebView is used.

## Handoff completion checklist

- Stable IDs match between design, contract, assets, fixtures, tests, and code.
- No ambiguous “looks like” component remains; each has a Material component or documented custom rationale.
- Copy is final or clearly marked; localization keys and wrapping constraints exist.
- Assets are export-ready, licensed, named, categorized, and include density/theme/locale variants.
- Interaction and reduced-motion behavior are explicit.
- Data/API/storage unknowns are typed interfaces with fakes, not guessed production implementations.
- Approved deviations are visible in the final conformance report.
- Every nonempty deviation has a re-review trigger such as a framework upgrade, accessibility audit, changed input modality, expanded locale/device scope, or product requirement change.
