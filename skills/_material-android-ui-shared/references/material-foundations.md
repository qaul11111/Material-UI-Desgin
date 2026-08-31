# Material 3 foundation baseline

Snapshot: 2026-08-26. Treat this file as a design baseline, not a substitute for the target framework's current component implementation. When a dimension conflicts with the Material component shipped by the target library version, use the shipped component default and record the difference in the handoff contract.

## Version policy

1. Identify the target Material library, framework version, Android API range, and whether experimental APIs are allowed.
2. Use the common Material 3 baseline for cross-platform parity.
3. Add Material 3 Expressive only when the product selects it and the target framework supports the needed tokens/components. Newer Jetpack Compose Material 3 versions expose motion schemes, but the API is absent from some stable pins; Flutter exposes duration/easing primitives, not Material's spring-physics scheme. Record and check the pinned version before selecting either path.
4. Never silently mix legacy Material 2 metrics, baseline Material 3, and Expressive variants. Put intentional exceptions in `deviations`.
5. Preserve semantic token names in design and code. Do not replace roles with raw hex, dp, or sp values inside screens.

## Color system

Use semantic roles and generate both light and dark schemes. Pair every `on*` role only with its named parent.

| Group | Required roles |
|---|---|
| Primary | `primary`, `onPrimary`, `primaryContainer`, `onPrimaryContainer` |
| Secondary | `secondary`, `onSecondary`, `secondaryContainer`, `onSecondaryContainer` |
| Tertiary | `tertiary`, `onTertiary`, `tertiaryContainer`, `onTertiaryContainer` |
| Error | `error`, `onError`, `errorContainer`, `onErrorContainer` |
| Surface | `surface`, `onSurface`, `onSurfaceVariant`, `surfaceContainerLowest`, `surfaceContainerLow`, `surfaceContainer`, `surfaceContainerHigh`, `surfaceContainerHighest` |
| Inverse | `inverseSurface`, `inverseOnSurface`, `inversePrimary` |
| Outline | `outline`, `outlineVariant` |
| Overlay/tint | `scrim`, `surfaceTint` |

Optional fixed accents use `primaryFixed`, `primaryFixedDim`, `onPrimaryFixed`, and `onPrimaryFixedVariant`, with corresponding secondary and tertiary roles. Fixed roles intentionally do not change across light and dark themes; avoid them where adaptive contrast is required. `surfaceBright` and `surfaceDim` may be added when the platform implementation provides them.

Give `scrim` one owner for modal overlays and use `surfaceTint` only through the framework's tonal-elevation behavior. `background`/`onBackground` may exist for compatibility in framework color schemes, but new surfaces should use the `surface*` model.

Choose one color strategy during intake:

- Static brand scheme: controlled, repeatable company colors.
- Dynamic scheme: colors derived from a source color or Android wallpaper; design against role mappings and test multiple seeds. Android dynamic color requires API 31 or newer, so provide a static fallback.
- Hybrid: static brand-critical surfaces plus dynamic noncritical surfaces. Document the boundary.

Contrast is a release criterion, not a palette-generation assumption: text smaller than 18 sp, or bold text smaller than 14 sp, is at least 4.5:1; all larger text is at least 3:1; meaningful non-text boundaries/icons are at least 3:1. Check every interactive state and both themes.

## Typography

Use `sp` on Android and logical pixels with text scaling in Flutter. Never encode a font size as fixed physical pixels. Material uses the platform default sans (`FontFamily.SansSerif`, normally Roboto on Android); a brand family must cover all required scripts and weights and must be licensed and bundled correctly.

| Role | Size / line height (sp) | Typical use |
|---|---:|---|
| `displayLarge` | 57 / 64 | Rare hero statement |
| `displayMedium` | 45 / 52 | Large hero statement |
| `displaySmall` | 36 / 44 | Compact hero statement |
| `headlineLarge` | 32 / 40 | Screen or major section |
| `headlineMedium` | 28 / 36 | Major section |
| `headlineSmall` | 24 / 32 | Section |
| `titleLarge` | 22 / 28 | Prominent component title |
| `titleMedium` | 16 / 24 | Medium-emphasis title |
| `titleSmall` | 14 / 20 | Compact title |
| `bodyLarge` | 16 / 24 | Primary body copy |
| `bodyMedium` | 14 / 20 | Default body copy |
| `bodySmall` | 12 / 16 | Supporting copy; do not go smaller for body text |
| `labelLarge` | 14 / 20 | Button and prominent label |
| `labelMedium` | 12 / 16 | Secondary label |
| `labelSmall` | 11 / 16 | Small control label |

Current Material adds emphasized counterparts for all 15 roles. Use an emphasized role only for intentional hierarchy, selection, action emphasis, or editorial expression; Material components do not adopt emphasized roles by default. Swap to the same role's emphasized token rather than inventing a one-off weight.

Line height must survive localization. Validate at least the product's longest supported script and font scale. Material's script guidance groups Latin-like scripts as small, Arabic/CJK/Thai/Vietnamese-like scripts around medium, and some scripts substantially taller. Prefer flexible vertical padding; any fixed-height text container must prove it does not clip.

## Project spacing and layout tokens

Use the 8 dp grid for primary rhythm and 4 dp for compact details, icons, and type alignment. The `space0`–`space900` ladder below is this suite's project-owned convention, not an AndroidX Material token scale. Use parent padding and layout gaps before child margins. Use logical start/end rather than left/right.

| Token | dp | Token | dp |
|---|---:|---|---:|
| `space0` | 0 | `space250` | 20 |
| `space25` | 2 | `space300` | 24 |
| `space50` | 4 | `space400` | 32 |
| `space75` | 6 | `space450` | 36 |
| `space100` | 8 | `space500` | 40 |
| `space125` | 10 | `space600` | 48 |
| `space150` | 12 | `space700` | 56 |
| `space175` | 14 | `space800` | 64 |
| `space200` | 16 | `space900` | 72 |

Compact window edge padding starts at 16 dp. Increase usable gutters and cap content width on larger windows; do not merely stretch a phone column. Every screen must define safe-area/system-bar behavior and keyboard/IME behavior.

## Shape

| Token | Radius |
|---|---:|
| `none` | 0 dp |
| `extraSmall` | 4 dp |
| `small` | 8 dp |
| `medium` | 12 dp |
| `large` | 16 dp |
| `largeIncreased` | 20 dp |
| `extraLarge` | 28 dp |
| `extraLargeIncreased` | 32 dp |
| `extraExtraLarge` | 48 dp |
| `full` | pill/circle |

For visibly nested rounded surfaces, begin with `inner radius = outer radius - padding`, then optically inspect. Use unconventional shapes sparingly and avoid them around dense or long text.

## Elevation

| Level | dp |
|---|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |
| 4 | 8 |
| 5 | 12 |

Prefer tonal surface separation; add shadows only when hierarchy or overlap requires them. Do not override a Material component's default elevation without a measured reason. Current AndroidX tokens place a resting FAB at level 3 (hover level 4). Typical resting levels that must be rechecked against the pinned component version include modal dialogs/search/date and time pickers at level 3; scrolled app bars, menus, navigation bars, rich tooltips, and toolbars at level 2; modal bottom sheets, elevated controls/cards, modal drawers, and side sheets at level 1; ordinary inline controls and unscrolled app bars at level 0.

## Token ownership

Maintain one source for each semantic token:

- Design: named variables/styles, component variants, and interaction definitions.
- Compose: `MaterialTheme` plus project token objects only for gaps not represented by the framework.
- Flutter: `ThemeData`, `ColorScheme`, `TextTheme`, component themes, and narrowly scoped theme extensions for true project tokens.
- Embedded web: CSS custom properties generated from the same contract; never hand-copy a second palette.

Raw values are permitted only inside the token definition or a documented one-off exception.
