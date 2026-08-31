# Figma delivery and structural QA

Read this reference only when the editable destination or source is Figma. It defines the shared construction, repair, and verification gate for prototype-to-UI design and UI refinement.

## Build for continued editing

- Use named variables and styles for semantic color, typography, spacing, shape, elevation, and motion.
- Use components, component properties, variants, and instances for repeated UI. Avoid detached copies and flattened screenshot-only screens.
- Use Auto Layout for related content and prefer parent padding plus item gaps over manual child offsets.
- Let content-owning sections hug their content when practical. Fix the canonical screen viewport, not arbitrary internal rows whose content can wrap or grow.
- Size wrapped grids, token specimens, text blocks, and state galleries from their actual child bounds. Do not infer a container height from only the first visible row.
- Keep `clipsContent` only for intentional scrolling, masks, or media crops. Record the reason and scroll/crop behavior in the handoff.
- When using the Plugin API, remember that a resize can reset axis sizing modes. Preserve or restore the intended HUG/FILL/FIXED relationship after resizing, then inspect downstream reflow.

## Asset and icon gate

Use this source order:

1. supplied product assets, especially the original logo SVG;
2. the file's design-system icon component;
3. a suitable Material Symbol;
4. another approved, licensed vector icon.

Icons must be real vector nodes or component instances with semantic names. Verify their visible bounds, slot size, optical centering, semantic color, RTL mirroring policy, state treatment, and accessible touch target. Do not ship black dots, generic circles/squares, emoji, letters, or text glyphs as action/navigation placeholders. A circle is acceptable only when the shape itself is the intended product symbol, such as a presence dot, pagination indicator, radio mark, or recorded-state indicator.

## Mandatory structural audit

Run this audit after the last design mutation and again after any layout fix:

1. Screenshot every major or changed section at a resolution where labels and card bottoms are readable.
2. Screenshot each representative screen/state and the full root page/frame.
3. For every relevant container, compute the maximum child right and bottom bounds. Acceptance requires `maxChildRight <= container.width` and `maxChildBottom <= container.height`, unless an intentional clip is documented.
4. Check sibling section boundaries. No section may overlap the next; inter-section gaps must resolve to the selected spacing token.
5. Check text at realistic longest content, selected locales, RTL where in scope, and supported font scales. Fixed-height text containers fail if any glyph or line is clipped.
6. Check every icon slot and navigation/action surface for real icons, correct semantic names, and complete rest/selected/pressed/disabled states.
7. Check light/dark themes and every required compact/medium/expanded branch.

For a container with children, the practical bounds check is:

```text
maxChildRight  = max(child.x + child.width)
maxChildBottom = max(child.y + child.height)
overflowRight  = max(0, maxChildRight - container.width)
overflowBottom = max(0, maxChildBottom - container.height)
```

Both overflow values must be zero unless the clip is intentional and documented.

## Repair order

When the audit finds clipping or overlap:

1. Fix the innermost incorrect container first.
2. Derive its required size from all child bounds plus the selected bottom/end padding token.
3. Restore the intended sizing modes after resize.
4. Let ancestor Auto Layout frames recompute heights and downstream positions.
5. Manually reposition downstream sections only when the parent is not an Auto Layout flow.
6. Re-run the local section screenshot, full-page screenshot, bounds audit, and gap audit.

Do not hide an overflow failure by disabling clipping, shrinking content, or moving children outside their semantic container.

## Evidence to retain

Store the following in `06 Handoff & QA` or the external handoff report:

- audited frame/section names and node IDs;
- width/height, maximum child bounds, and overflow results;
- resolved section-gap tokens;
- section and full-page screenshots from the final state;
- documented intentional clips;
- icon-source mapping and any approved deviations.
