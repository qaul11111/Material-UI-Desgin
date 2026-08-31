# Adaptive layout, localization, and accessibility

## Window size classes

Classify the current app window, not the device model. Recompute when the window changes because rotation, split screen, desktop windowing, and fold posture can change available space while the app runs.

### Width

| Class | Window width |
|---|---:|
| compact | `< 600 dp` |
| medium | `600–839 dp` |
| expanded | `840–1199 dp` |
| large | `1200–1599 dp` |
| extra-large | `>= 1600 dp` |

### Height

| Class | Window height |
|---|---:|
| compact | `< 480 dp` |
| medium | `480–899 dp` |
| expanded | `>= 900 dp` |

Most decisions use width; height changes vertical density, sheets/dialogs, media, and scroll behavior. If the target API exposes only compact/medium/expanded by default, explicitly opt into large/extra-large support when the product targets desktop-sized or very large Android windows.

## Adaptive composition

Specify each screen at the relevant classes, not just at arbitrary phone/tablet labels.

- Compact: usually one pane, 16 dp edge padding, bottom navigation where top-level navigation is needed.
- Medium: consider navigation rail and two-pane layouts; supporting-pane layouts often begin around 50/50.
- Expanded: use rail/drawer, list-detail or supporting pane, and capped readable columns; supporting content often begins near 70/30.
- Large/extra-large: add whitespace, panes, or persistent tools; do not inflate every component.

Prefer the canonical feed, list-detail, and supporting-pane patterns when they fit the information architecture. Preserve user context and selection when changing panes. Hoist window/adaptive state to the lowest common owner that coordinates the screen; do not encode device-name branches inside leaves.

Always design and test:

- system bars, display cutouts, rounded corners, gesture navigation, IME, and edge-to-edge layout;
- fold/hinge or occlusion information when the product targets foldables;
- portrait, landscape, multi-window resizing, and process/activity recreation as relevant;
- keyboard, mouse, trackpad, focus traversal, and hover at larger windows;
- scrolling rather than clipping when vertical space shrinks.

Compose should use current Android adaptive window APIs where available. Flutter should use `MediaQuery.sizeOf(context)` for whole-window decisions and `LayoutBuilder` for local constraints. Never lock portrait orientation merely to avoid adaptive work.

## Accessibility release gates

- Touch targets are at least 48 × 48 dp/logical pixels and do not overlap.
- Text smaller than 18 sp, or bold text smaller than 14 sp, has contrast of at least 4.5:1; all larger text and meaningful non-text graphics are at least 3:1.
- Body copy is not smaller than 12 sp at the base scale.
- Text respects system font scaling without clipping, overlap, or loss of actions.
- Every meaningful control/image has a concise accessible label; decorative imagery is excluded from semantics.
- Reading order and focus order match the visual/task order.
- Selection, error, loading, expanded/collapsed, checked, and value states are exposed semantically.
- Information is not conveyed by color, shape, position, sound, gesture, or motion alone.
- Keyboard and switch/voice access can reach and activate every action.
- Screen-reader announcements are useful and not duplicated by merging child semantics incorrectly.
- Reduced-motion and high-contrast/platform contrast preferences are honored where exposed.
- TalkBack/manual exploration is performed on critical flows; automated lint/guidelines supplement rather than replace it.

Compose may enlarge touch bounds automatically for Material components only when they are interactive, but explicit spacing is still required to prevent overlap. Precision pointer input can justify a smaller visible/interactive target only when touch is not the active modality and the exception is tested. In Flutter, include automated checks for `androidTapTargetGuideline`, `textContrastGuideline`, and `labeledTapTargetGuideline` where applicable.

## Localization and content resilience

- Use resource/localization keys; no user-facing strings in screen code.
- Support plural, gender, date, time, number, currency, and relative-time formatting through platform APIs.
- Use logical start/end alignment and mirrored directional icons for RTL; do not mirror universal media/navigation symbols blindly.
- Test Chinese and the longest supported locale; test RTL when supported.
- Allow labels to wrap or components to grow according to their specification. Do not shrink text to preserve a screenshot.
- Use stable semantics IDs/test tags sparingly for tests; never expose implementation jargon to users.

## Required adaptive design matrix

The contract must list exact canonical viewports. At minimum, cover compact, medium, and expanded widths when those classes are in product scope; add large and extra-large for desktop/large-screen scope. Cross each critical flow with light/dark, content/loading/empty/error, base and enlarged font scale, Chinese and the longest supported locale, and RTL where supported. Risk-based sampling is allowed only after all unique layout branches have at least one direct test.
