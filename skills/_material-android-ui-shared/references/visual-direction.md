# Art direction within Material

Verified against official sources on 2026-09-04. Read for a new visual identity or an authorized composition/font/icon redesign, not every minor correction. The decisions below are design heuristics unless explicitly attributed to Material.

## Separate three concerns

- Material rules govern semantics, usability, component behavior, token roles and accessibility.
- Product art direction governs what deserves attention and how the product feels.
- Presentation styling governs marketing collages, device frames and decorative backgrounds. It must not contaminate canonical implementation exports.

Google's Expressive research connects color, size, shape, motion and containment to attention and usability, not decoration for its own sake. Quiet expression is valid too. See [research](https://design.google/library/expressive-material-design-google-research) and [design-team discussion](https://design.google/library/design-notes-material-3-expressive-liam-spradlin).

## Make a visual hypothesis before composing components

### Ground the direction in visible references

Use supplied references and approved product screens first. Inspect the actual imagery and layout rather than inferring appearance from a page title or article text. If useful references are missing and exploration is authorized, discover a small relevant set, favoring original product/designer sources. A familiar brand or local defect does not require new research.

For a reference that materially changes a decision, retain a concise chain:

| Evidence | Decision to make |
|---|---|
| Source/link or supplied image; visible region | What composition, type, color relationship, asset treatment or motion is actually observable? |
| Effect relevant to this product | Why might this help its users, task or intended feeling? Mark this interpretation as a design hypothesis. |
| Transfer and limits | What principle transfers; what content, interaction, branding or decorative framing should not be copied? |
| Resulting screen/location | Where is the adapted treatment visible in the actual candidate export, and did it achieve the intended effect? |

Example: a reference makes the next action prominent through scale and a shared supporting surface. For a sales workflow, test a clear next-action area with quieter contextual rows while retaining all actions. The reference's music artwork, brand font and collage background need not transfer. This is an example of reasoning, not a sales-screen template.

Do not equate a homepage collage with a usable screen. Inspect the screen inside it, keep presentation decoration separate and respect asset licenses. If the source cannot be viewed, label it uninspected and do not invent a visual analysis.

### Compose and render a representative screen

Write a concise visual thesis: audience + primary task + intended feeling + one recognizable treatment. For example, a sales copilot might emphasize the next useful action and a calm conversation timeline; a music app might celebrate cover art and artist typography. These are examples, not default templates.

For the representative screen, decide:

- Attention: what is noticed first, next and last? Give a reason tied to the task.
- Composition: where do contrast, scale and negative space create hierarchy?
- Containment: which content genuinely needs a card, shared surface, row or divider?
- Rhythm: distinguish between-section spacing from within-group spacing using tokens.
- Color: decide where brand intensity belongs and where neutral surfaces reduce noise.
- Imagery: define subject, source, crop, palette, lighting and purpose; no irrelevant stock decoration.
- Signature: use a repeatable typographic, graphic, compositional or motion treatment only where it serves the product.

Reject equal-weight card stacks when they hide priority, not because cards are forbidden. Avoid uniform heading size, identical corner radius on every level, repetitive icon-title-body boxes and saturated backgrounds on every section. A dense operational screen can remain mostly plain rows.

Use the same realistic content, task, state and viewport when comparing directions. Keep information/actions available and use comparable asset quality. Change meaningful composition/type/image decisions, not just the accent hex. Explain the consequential difference and recommend a direction from the observed screens. A new direction needs a polished representative screen approved by the owner or selected under explicit delegated authority before batch production. Existing approved designs can be referenced; do not reopen delegated choices.

Use available real brand assets early. When imagery is central, source licensed or user-provided material, or use an available image-generation workflow for an appropriate bitmap asset. Record provisional media honestly. Use the established vector/icon system for functional icons and supplied logos. A text description of future imagery cannot demonstrate the final composition, and a generic decorative illustration is not obligatory.

## Typography is a project decision

Material supplies a role system, not an obligation for every brand to look like Roboto. Its [theming codelab](https://developer.android.com/codelabs/m3-design-theming) supports custom type choices. First test one family; add a complementary display family only when it improves hierarchy.

Specify:

- Reading/UI family for body, labels and functional controls.
- Display/editorial family for selected prominent moments; it may be the same family.
- The primary product language's reading/display families first, then companion Latin/numeric and other script fallbacks. In a Chinese-first product, Chinese type participates in the main design decision; it is not only a fallback after choosing an English font.
- Actual files, version, source/license, available weights and variable axes.
- Role mapping, line height, tracking, numeric alignment, truncation/wrapping and scaling behavior.
- Figma availability and equivalent runtime rendering; an unavailable font must not be silently substituted.

The official [font guidance](https://m3.material.io/styles/typography/fonts) distinguishes Roboto, Roboto Flex, Roboto Serif, Roboto Mono and Noto. Roboto Flex does not by itself cover Chinese; use a verified script fallback. Font names alone are insufficient: test actual mixed-script glyphs and baseline/weight balance.

Create a specimen using actual product language, for example:

    客户跟进 / Customer follow-up
    上海智联科技有限公司 · Enterprise
    ¥128,640.50   +18.6%   09:41   138 **** 8821
    一段真实的两行正文；一条足够长的按钮或错误提示。

Inspect specimens inside the actual candidate screen at canonical phone size and enlarged text; consider type and icon weight together before fixing density and vertical spacing. Do not shrink the type to hide layout errors. Prefer tabular figures for changing aligned data where supported; do not turn all body text into monospace.

[Editorial treatments](https://m3.material.io/styles/typography/editorial-treatments) allow expressive custom sizes and variable axes for content-led showcase moments. Material asks that such treatments be consistent/tokenized and not used as ordinary informational labels. Keep body/label roles readable; do not reject a valid editorial size just because it differs from the baseline scale.

Do not name the exact typeface in a reference screenshot without evidence. Do not reuse a brand font without checking its actual license. Font acquisition, missing glyphs, loading/fallback and package size are delivery concerns.

## One icon profile per coherent product system

Different projects MAY use different icon styles; they do not HAVE to. Preserve an established company icon system unless the product calls for a deliberate exception.

Material Symbols supports Outlined, Rounded and Sharp, with fill, weight, grade and optical size customization. Record a stable profile and coordinate its optical weight with typography. See [Material icon overview](https://m3.material.io/styles/icons/overview) and [Symbols guide](https://developers.google.com/fonts/docs/material_symbols).

Profile fields:

- Family/style and verified source/version.
- Weight, grade, optical size and default fill.
- Selected/unselected treatment and semantic label mapping.
- Slot, visible artwork bounds, optical corrections and touch container.
- RTL mirroring policy and approved exceptions.

Outlined/Rounded/Sharp describe family treatment, not selected state; fill can vary within one family for state. Do not mix families arbitrarily between adjacent controls. Do not simulate heavier icons with a generic SVG stroke if an intended axis/asset exists.

For custom functional icons, use [Material's icon design guidance](https://m3.material.io/styles/icons/designing-icons): clear silhouette, coherent proportions/keylines, optical balance and a consistent set. The baseline grid is 24dp with a 20dp live area; component-specific icons can use other prescribed sizes. The visible grid is not the touch target.

Separate functional icons from decorative illustrations and logos. A colorful illustration or organic hero shape is not a reason to make navigation icons 3D or obscure. Real status dots and radio marks are legitimate; anonymous circles used as action placeholders are not.

Figma handoff favors named vector/components for reliable assets. Production can use a properly configured icon font: this is different from using an arbitrary text character as a placeholder. Verify actual font loading, semantics and fallback rather than banning every font-based icon.

## Capture the decision

During exploration, a short visual study with source references, constraints, candidates/exports, observations, revisions and recommendation is sufficient. Include the viewport/state/locale and actual source revision. Do not make a schema-complete contract or a new document for every tiny fix. At structured handoff, link the study in verification evidence and carry its selected decisions into the existing contract fields below.

Use the optional structured meta.visualDirection field of contract schema 1.1:

- thesis, emphasis, containment, imagery and signature;
- status: proposed / approved / delegated / inherited;
- approvalEvidence and approvedBy, accurately reflecting user authority;
- representativeExports and sourceRevision;
- iconProfile with axes/state policy;
- fontProfile with role families, script fallbacks and font asset IDs.

Record font assets in assets with kind=font, license and destinationHint; record icon family/version and individual semantic mappings. Store editorial roles under theme.typography tokens. Preserve these decisions during refinement.

## Rendered critique and revision

Inspect the actual screen at readable device size and as a whole composition. Use the questions below to locate weaknesses; answers alone are not evidence that the design was improved.

1. Can the primary task be found without reading every card?
2. Does the composition communicate product identity beyond its logo and accent?
3. Are containment, size and whitespace intentional?
4. Do typography, icon weight and imagery belong together?
5. Is expression concentrated where useful, while dense tasks stay usable?
6. Are the same decisions viable in dark mode, longer Chinese text and enlarged text?

For a consequential weakness, record **observed region → task/identity impact → proposed change → revised export → observed result**. State when an observation is qualitative. For example: “The next action has the same visual weight as metadata; regroup the metadata and strengthen the action; compare the revised screen to see whether the task is easier to identify.” Do not invent user-test results or convert taste into a precise score.

Apply the justified change, render again, then inspect for both the intended improvement and regressions. Preserve a genuine earlier export; do not manufacture a weak 'before' screen. Compare matching content/configurations and disclose any differences that prevent a controlled comparison. If no consequential concern is found, retain the inspected export and reason; do not force an ornamental edit or an arbitrary number of iterations. Revisit the brief after repeated unsuccessful revisions instead of endlessly producing variants.

Before expanding a new direction, try a relevant content-heavy or alternate-state view and the in-scope longer-text/enlarged-text/dark configuration that is most likely to challenge it. This should verify that the design decisions carry beyond a showcase. Do not turn a small correction into full-product testing.

Keep unresolved concerns visible and distinguish designer judgment from actual product-owner selection. A geometry checker cannot judge taste; a visually exciting screen cannot override accessibility or state failures.
