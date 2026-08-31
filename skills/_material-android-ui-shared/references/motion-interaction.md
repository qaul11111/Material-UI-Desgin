# Motion and interaction baseline

Snapshot: 2026-08-26. Current Material motion is physics-oriented. Legacy easing and duration tokens remain useful as an explicit compatibility fallback, but do not present them as the current preferred system.

## Motion decision

Choose and record one scheme:

- `standard`: functional, controlled, lower personality.
- `expressive`: more energetic spatial response; use only when it fits the selected brand style and the framework supports or intentionally emulates it.
- `reduced`: suppress nonessential spatial travel, parallax, looping, and scale; retain immediate state feedback and continuity cues.

For each transition record: trigger, source state, destination state, properties, scheme, speed, interruption behavior, reduced-motion behavior, and framework implementation. Motion may clarify continuity, hierarchy, cause/effect, or status; decoration alone is not sufficient justification.

## Physics categories

Use spatial motion for position, scale, size, rotation, and corner shape. Use effects motion for opacity and color, which should not overshoot. Select speed by travel and prominence:

- fast: small controls or a short local response;
- default: a component or partial-screen transition;
- slow: a large or full-screen transition.

## Verified AndroidX spring anchor

The following damping/stiffness values were verified from current AndroidX `StandardMotionTokens.kt` and `ExpressiveMotionTokens.kt` on 2026-08-26. Treat them as the normative physics anchor and still bind implementation to the repository's pin.

| Scheme | Channel | Speed | Damping | Stiffness |
|---|---|---|---:|---:|
| expressive | spatial | fast | 0.6 | 800 |
| expressive | spatial | default | 0.8 | 380 |
| expressive | spatial | slow | 0.8 | 200 |
| expressive | effects | fast / default / slow | 1.0 | 3800 / 1600 / 800 |
| standard | spatial | fast / default / slow | 0.9 | 1400 / 700 / 300 |
| standard | effects | fast / default / slow | 1.0 | 3800 / 1600 / 800 |

Jetpack Compose can use `MotionScheme.standard()` or `MotionScheme.expressive()` only when exposed by the target library. Dated context: the API was absent from stable Material 3 1.4.0 and graduated from experimental on the 1.5.0 alpha line. Flutter exposes Material `Durations` and `Easing`, not this native spring system. For Flutter or embedded web, use a framework-supported baseline transition or deliberately approximate the values below and label/test the result as an adaptation.

## Web/Flutter approximation values

These cubic-bezier/duration pairs are human-checked transcriptions from Material web guidance that was not machine-readable on the snapshot date. They remain pending re-verification. They approximate the spring; they are not identical physics or a native Flutter motion scheme.

| Scheme/token | Cubic bezier | Duration |
|---|---|---:|
| expressive fast spatial | `(0.42, 1.67, 0.21, 0.90)` | 350 ms |
| expressive default spatial | `(0.38, 1.21, 0.22, 1.00)` | 500 ms |
| expressive slow spatial | `(0.39, 1.29, 0.35, 0.98)` | 650 ms |
| standard fast spatial | `(0.27, 1.06, 0.18, 1.00)` | 350 ms |
| standard default spatial | `(0.27, 1.06, 0.18, 1.00)` | 500 ms |
| standard slow spatial | `(0.27, 1.06, 0.18, 1.00)` | 750 ms |
| either fast effects | `(0.31, 0.94, 0.34, 1.00)` | 150 ms |
| either default effects | `(0.34, 0.80, 0.34, 1.00)` | 200 ms |
| either slow effects | `(0.34, 0.88, 0.34, 1.00)` | 300 ms |

## Legacy compatibility tokens

Use only where current physics APIs are unavailable or the existing codebase already standardizes on these transitions.

| Token | Curve | Typical duration |
|---|---|---:|
| emphasized decelerate | cubic `(0.05, 0.7, 0.1, 1)` | 400 ms enter |
| emphasized accelerate | cubic `(0.3, 0, 0.8, 0.15)` | 200 ms exit |
| emphasized | platform emphasized curve | 500 ms on-screen transform |
| standard | cubic `(0.2, 0, 0, 1)` | 300 ms |
| standard decelerate | cubic `(0, 0, 0, 1)` | 250 ms enter |
| standard accelerate | cubic `(0.3, 0, 1, 1)` | 200 ms exit |

Legacy duration ladder: short 50/100/150/200 ms; medium 250/300/350/400 ms; long 450/500/550/600 ms; extra-long 700/800/900/1000 ms. These values carry the same pending-re-verification caveat as the approximation table. Choose a named token; do not scatter arbitrary durations.

## State layers

State-layer color is normally the component content or `on*` color. Default opacities:

| State | Opacity |
|---|---:|
| hover | 8% |
| focus | 10% |
| pressed | 10% |
| dragged | 16% |

Only one transient state layer is visually active at a time, though selection can coexist with hover/focus/press. Disabled controls cannot hover, focus, press, or drag. Pressed feedback normally uses ripple on Android; hover is a lower-emphasis fade. Use the framework's interaction/ripple system so clipping, boundedness, accessibility, and cancellation remain correct.

## Interaction specification checklist

For every interactive component specify:

1. semantic role, accessible name, value/state, and target size;
2. tap/click, keyboard activation, focus, hover, press, drag, long-press, and back/Escape behavior where applicable;
3. enabled/disabled, selected/unselected, loading/success/error, empty/offline/permission state where applicable;
4. visual state layer plus any elevation, shape, icon, text, or container change;
5. transition token and interruption/reversal behavior;
6. haptic/audio feedback only when useful and platform-appropriate;
7. reduced-motion behavior;
8. test assertions for state and semantics, not just a screenshot.

Avoid long blocking animations, layout jumps, simultaneous unrelated motion, automatic infinite motion, gesture-only actions, and hover-only information. User input must be interruptible and must not wait for decorative animation to finish.
