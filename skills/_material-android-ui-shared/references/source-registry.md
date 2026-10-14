# Official source registry

Research snapshot: 2026-08-26. Recheck unstable framework APIs, component tokens, package constraints, and accessibility guidance before changing dependencies or claiming conformance. Prefer the target repository's pinned documentation/version over a newer incompatible example.

## Material Design 3

- Material Design 3 home: https://m3.material.io/
- Color roles: https://m3.material.io/styles/color/roles
- Typography overview and type scale: https://m3.material.io/styles/typography/overview and https://m3.material.io/styles/typography/type-scale-tokens
- Shape scale: https://m3.material.io/styles/shape/shape-scale-tokens
- Elevation: https://m3.material.io/styles/elevation/overview
- Motion overview and physics: https://m3.material.io/styles/motion/overview and https://m3.material.io/styles/motion/physics
- State layers: https://m3.material.io/foundations/interaction/states/state-layers
- Spacing: https://m3.material.io/foundations/layout/understanding-layout/spacing
- Window size classes: https://m3.material.io/foundations/layout/applying-layout/window-size-classes
- Component catalog: https://m3.material.io/components
- Accessibility: https://m3.material.io/foundations/accessible-design/overview

## Android and Jetpack Compose

- Android UI/design hub: https://developer.android.com/design/ui
- Material 3 in Compose: https://developer.android.com/develop/ui/compose/designsystems/material3
- Adaptive layouts and window size classes: https://developer.android.com/develop/ui/compose/layouts/adaptive and https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes
- Material 3 adaptive releases/API status: https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive
- Edge-to-edge enforcement and insets: https://developer.android.com/develop/ui/views/layout/edge-to-edge
- Navigation 3 releases: https://developer.android.com/jetpack/androidx/releases/navigation3
- State and state hoisting: https://developer.android.com/develop/ui/compose/state and https://developer.android.com/develop/ui/compose/state-hoisting
- UI architecture: https://developer.android.com/develop/ui/compose/architecture
- Compose accessibility: https://developer.android.com/develop/ui/compose/accessibility
- Compose testing: https://developer.android.com/develop/ui/compose/testing
- Preview screenshot testing: https://developer.android.com/studio/preview/compose-screenshot-testing
- Views in Compose / `AndroidView`: https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose
- WebView apps: https://developer.android.com/develop/ui/views/layout/webapps
- Unsafe WebView native bridges: https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges
- Resource types: https://developer.android.com/guide/topics/resources/providing-resources
- AndroidX Material 3 token sources: https://github.com/androidx/androidx/tree/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens
- Compose Material 3 releases and MotionScheme status: https://developer.android.com/jetpack/androidx/releases/compose-material3

## Flutter

- Material design for Flutter: https://docs.flutter.dev/ui/design/material
- Adaptive and responsive design: https://docs.flutter.dev/ui/adaptive-responsive and https://docs.flutter.dev/ui/adaptive-responsive/general
- Safe areas/MediaQuery: https://docs.flutter.dev/ui/adaptive-responsive/safearea-mediaquery
- Android large-screen orientation restrictions: https://docs.flutter.dev/release/breaking-changes/android-large-screens-restrictions-ignored
- Flutter architecture guide: https://docs.flutter.dev/app-architecture/guide
- State management fundamentals: https://docs.flutter.dev/data-and-backend/state-mgmt
- Accessibility: https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility
- Testing overview: https://docs.flutter.dev/testing/overview
- Golden matching/font behavior: https://api.flutter.dev/flutter/flutter_test/matchesGoldenFile.html
- Predictive-back-compatible scope: https://api.flutter.dev/flutter/widgets/PopScope-class.html
- Text scaling: https://api.flutter.dev/flutter/painting/TextScaler-class.html
- Assets and images: https://docs.flutter.dev/ui/assets/assets-and-images
- `webview_flutter`: https://pub.dev/packages/webview_flutter
- `webview_flutter_android`: https://pub.dev/packages/webview_flutter_android

## Visual expression and QA supplement — verified 2026-09-04

- Expressive/attention research: https://design.google/library/expressive-material-design-google-research
- Quiet and energetic expression: https://design.google/library/design-notes-material-3-expressive-liam-spradlin
- Brand typography: https://developer.android.com/codelabs/m3-design-theming
- Fonts and script fallback: https://m3.material.io/styles/typography/fonts
- Editorial treatments: https://m3.material.io/styles/typography/editorial-treatments
- Icon styles: https://m3.material.io/styles/icons/overview
- Custom icon consistency: https://m3.material.io/styles/icons/designing-icons
- Symbol axes/assets: https://developers.google.com/fonts/docs/material_symbols
- Figma collector API: https://developers.figma.com/docs/plugins/api/FrameNode/ and https://developers.figma.com/docs/plugins/api/TextNode/

The Material font/editorial/icon pages were read in a JavaScript-capable browser because plain extraction returned a JavaScript-required shell. This supplement does not refresh every historical framework metric. Do not use stale platform-availability statements on a Symbols page as dependency advice.

## Source-use rule (all references)

When a task needs an exact component metric not already pinned in the target project, open the relevant official component page and inspect the framework implementation for the pinned version. Do not use third-party summaries as normative evidence. Record the source URL, access date, framework version, and whether the value is a baseline, Expressive variant, or project override.
