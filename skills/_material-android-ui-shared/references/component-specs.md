# Material component specification snapshot

Snapshot: 2026-08-26. Use official Material components whenever possible. The target library's current default wins over this snapshot; remeasure and record version-dependent differences. All dimensions are dp/logical pixels unless stated otherwise.

## Universal component rules

- Interactive touch target: at least 48 × 48, even when the visible glyph or control is smaller. A modality-specific precision-pointer target may be smaller only when touch is not active and the exception is tested. Keep neighboring targets from overlapping.
- Icons: normally 24; use each component's own token when it specifies 18, 20, 28, 32, or 40.
- State-layer visual container: commonly 40; interaction target remains 48.
- Text and icon colors use semantic `on*` roles. Never select color by visual similarity alone.
- Implement enabled, disabled, pressed, focused, hovered where relevant, selected/unselected where relevant, drag where relevant, loading if an action can wait, and error when validation can fail.
- Native Material defaults are the starting point. Custom drawing must reproduce semantics, focus, ripple/state layer, minimum target, and all states.

## Controls and actions

| Component | Current baseline metrics | Required notes |
|---|---|---|
| Baseline Compose `Button()` | 40 high, min width 58, icon 20, gap 8; horizontal padding 24 without an icon and 16 with a leading icon | This is the baseline framework default. A precision-pointer context may use a 36-high visual control; preserve an accessible interaction target appropriate to the active input mode. |
| Expressive Button XS | 32 high, icon 20, icon gap 8, horizontal padding 16, outline 1 | Visible control may be 32; touch target still 48 for touch. Round corner `full`; square 12; pressed square 8. |
| Expressive Button S | 40 high, icon 20, gap 8, horizontal padding 16, outline 1 | This is the Expressive small-size path, not baseline `Button()` content padding. Round `full`; square 12; pressed square 8. |
| Expressive Button M | 56 high, icon 24, gap 8, horizontal padding 24, outline 1 | Round `full`; square 16; pressed square 12. |
| Expressive Button L | 96 high, icon 32, gap 12, horizontal padding 48, outline 2 | Round `full`; square 28; pressed square 16. |
| Expressive Button XL | 136 high, icon 40, gap 16, horizontal padding 64, outline 3 | Round `full`; square 28; pressed square 16. |
| Icon button | Component-defined visual size, icon generally 24 | Preserve 48 target and state layer; include selected and toggle semantics where applicable. |
| FAB | small 40/icon 24; standard 56/icon 24; medium 80/icon 28; large 96/icon 32 | Small visible FAB still needs 48 target. Do not leave an unavailable FAB disabled; hide or replace it. |
| Chip | 32 high, icon 18, avatar 24, outline 1 | Preserve 48 target; selection and removal are separate semantic actions when both exist. |
| Checkbox | visual 18, outline 2, state layer 40 | Support checked, unchecked, indeterminate, disabled; target 48. |
| Radio | visual 20, state layer 40 | Group semantics and one selected value; target 48. |
| Switch | 52 × 32; selected handle 24; unselected 16; pressed 28; optional icon 16; state layer 40 | Entire labeled row should toggle where appropriate; target 48. |
| Slider | current expressive track 16; handle 44 × 4, pressed width 2; stop 4 | Use native component and semantics; target at least 48; format value accessibly. |

The five-size button set is a current Material/AndroidX Expressive token snapshot and its entry points may require `@ExperimentalMaterial3ExpressiveApi` in the pinned version. Do not confuse it with baseline `Button()`, and do not recreate unavailable variants unless the product explicitly selected Expressive, the version/opt-in is approved, and behavior can be tested.

## Text, selection, and feedback

| Component | Metrics | Required notes |
|---|---|---|
| Filled/outlined text field | container 56; vertical padding 8; horizontal 16 without icons or 12 with icons; icon gap 12; icon 24; supporting text top gap 4; outline 1 rest/2 focus | Label, input, placeholder, prefix/suffix, supporting/error text, counter, disabled/read-only, focus, autofill, keyboard type. Let multiline fields grow. |
| Snackbar | 48 single-line; 68 two-line; icon 24 | One concise action; announce semantics; do not obscure navigation or IME. |
| Divider | 1 | Use `outlineVariant` or component token; do not use as a substitute for spacing. |
| Tooltip | Native component metrics | Provide for unfamiliar icon actions and keyboard/mouse users; do not require hover to reveal essential information. |
| Progress/loading | Native linear/circular/loading indicator | Respect reduced-motion preference; announce meaningful long-running states without excessive repetition. |

## Containers and navigation

| Component | Metrics | Required notes |
|---|---|---|
| Top app bar | small 64; medium 112; large 152 | Account for status-bar inset separately. Define scroll/collapse behavior and elevation change. |
| Bottom app bar | 80 | Account for navigation inset; actions must retain 48 targets. |
| Navigation bar | baseline 80; newer compact/expressive token may be 64 | Use 3–5 top-level destinations; preserve destination state; avoid lateral hierarchy. |
| Navigation rail | narrow 80; regular collapsed 96; expanded min 220/max 360; top space 44 | Use at wider windows; destination labels and expansion behavior must be explicit. |
| List item | one/two/three line 56/72/88; horizontal padding 16; vertical padding 10; content gap 12; avatar 40; image 56; icon usually 24 | Let height grow for font scaling/localization; trailing action must be separately labeled. |
| Primary tabs | 48 text-only or 64 icon+label; icon 24; active indicator 3 | Keep tab count manageable, preserve selection and scroll behavior. |
| Secondary tabs | 48; divider 1 | Use for peer sections inside a surface. |
| Search bar | 56; full-screen search header 72 | Define query, clear, suggestions, history, loading, empty, error, and back behavior. |
| Modal date picker | common baseline 360 × 568; day target 40; header 120 | Use native picker where available; localization and calendar semantics override pixel mimicry. |
| Dialog | Use current native component constraints | Verify compact and large windows, IME, scrolling, focus trap, dismissal, and destructive-action wording. |
| Sheet/drawer/menu | Use current native component constraints | Define modal/modeless behavior, scrim, drag/dismiss, focus order, back/Escape, and safe areas. |
| Card/carousel | Use component variant tokens | Card clickability must be obvious and semantic; carousel items need predictable focus and scroll position. |

## Component selection checklist

1. Choose the Material component whose semantics match the job, not merely its appearance.
2. Choose its supported variant and size from the target framework version.
3. Apply semantic theme roles and spacing tokens.
4. Specify every state and transition.
5. Verify 48 target, contrast, focus order, label, screen reader output, RTL, large text, and keyboard/IME.
6. If custom behavior remains, document why a native component cannot satisfy it and add dedicated tests.

## Catalog to inspect for each product

Audit all used members of the current Material catalog: app bars, badges, bottom/side sheets, buttons and button groups, cards, carousel, checkbox, chips, date/time pickers, dialogs, dividers, extended/FABs, icon buttons, lists, loading/progress indicators, menus, navigation bar/drawer/rail, radio buttons, search, segmented/split buttons, sliders, snackbar, switch, tabs, text fields, toolbars, and tooltips. Do not declare a design complete while a used component is represented by only its resting screenshot.
