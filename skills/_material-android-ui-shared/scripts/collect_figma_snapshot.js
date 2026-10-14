/* Read-only Figma Plugin API collector. Load in a supported Figma execution tool.
 * Call collectMaterialSnapshot({rootIds: ["1:2"], revision: "design-r2"}).
 * It does not resize, clone, export, load fonts, change selection or set plugin data.
 */
async function collectMaterialSnapshot(options, api = figma) {
  if (!options || !Array.isArray(options.rootIds) || !options.rootIds.length ||
      typeof options.revision !== "string" || !options.revision.trim()) {
    throw new Error("Explicit rootIds and a nonempty contract revision are required");
  }
  const ids = [...new Set(options.rootIds)];
  const roots = await Promise.all(ids.map(id => api.getNodeByIdAsync(id)));
  if (roots.some(n => !n || !Number.isFinite(n.width) || !Number.isFinite(n.height))) {
    throw new Error("Every root must be an existing scene node with geometry");
  }
  // Reject overlapping roots instead of returning two inconsistent parent graphs.
  for (const root of roots) {
    let parent = root.parent;
    while (parent) {
      if (ids.includes(parent.id)) throw new Error("Choose disjoint roots");
      parent = parent.parent;
    }
  }
  const nodes = [];
  const visited = new Set();
  const errors = [];
  function bounds(node) {
    const t = node.relativeTransform;
    if (!t) return null;
    const points = [[0, 0], [node.width, 0], [0, node.height], [node.width, node.height]]
      .map(([x, y]) => [t[0][0] * x + t[0][1] * y + t[0][2],
                       t[1][0] * x + t[1][1] * y + t[1][2]]);
    const xs = points.map(p => p[0]), ys = points.map(p => p[1]);
    return {x: Math.min(...xs), y: Math.min(...ys),
            width: Math.max(...xs) - Math.min(...xs),
            height: Math.max(...ys) - Math.min(...ys)};
  }
  function visit(node, parentId) {
    if (node.visible === false) return; // Effective hidden descendants are omitted.
    if (visited.has(node.id)) throw new Error("Repeated node");
    visited.add(node.id);
    if (visited.size > (options.maxNodes || 10000)) throw new Error("Snapshot limit exceeded; narrow scope");
    const fills = Array.isArray(node.fills) ? node.fills.filter(p => p.visible !== false) : [];
    const style = typeof node.fillStyleId === "string" && !!node.fillStyleId;
    let textStyleStatus = "none", fontFamilies = [];
    if (node.type === "TEXT") {
      try {
        const segments = node.getStyledTextSegments(["fontName", "textStyleId"]);
        fontFamilies = [...new Set(segments.map(s => s.fontName.family))];
        textStyleStatus = !segments.length ? "none" :
          segments.every(s => !!s.textStyleId) ? "styled" : "raw-or-mixed";
      } catch (error) {
        errors.push({nodeId: node.id, operation: "text-segments", message: String(error)});
      }
    }
    nodes.push({
      id: node.id, name: node.name, type: node.type, parentId,
      width: node.width, height: node.height,
      boundsInParent: parentId === null ? null : bounds(node),
      clipsContent: node.clipsContent === true,
      hasMask: "children" in node && node.children.some(c => c.visible !== false && c.isMask),
      layoutMode: typeof node.layoutMode === "string" ? node.layoutMode : "NONE",
      rawSolidFills: style ? 0 : fills.filter(p => p.type === "SOLID" && !p.boundVariables?.color).length,
      textStyleStatus, fontFamilies,
      hasMissingFont: node.type === "TEXT" && node.hasMissingFont === true,
      textAutoResize: node.type === "TEXT" ? node.textAutoResize : null
    });
    if ("children" in node) for (const child of node.children) visit(child, node.id);
  }
  for (const root of roots) {
    // Root visibility alone is insufficient when an ancestor is hidden.
    let current = root;
    while (current && current.type !== "DOCUMENT") {
      if (current.visible === false) throw new Error("Root is effectively hidden: " + root.id);
      current = current.parent;
    }
    visit(root, null);
  }
  return {schemaVersion: "1.0", revision: options.revision,
          capturedAt: new Date().toISOString(), roots: ids, nodes, errors,
          collector: "material-visible-descendants-v1"};
}

if (typeof module !== "undefined") module.exports = {collectMaterialSnapshot};
