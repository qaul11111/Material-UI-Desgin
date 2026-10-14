const assert = require("node:assert/strict");
const {test} = require("node:test");
const {spawnSync} = require("node:child_process");
const path = require("node:path");
const {collectMaterialSnapshot} = require("../skills/_material-android-ui-shared/scripts/collect_figma_snapshot.js");

function scene(id, children = [], props = {}) {
  const node = {id, name: id, type: "FRAME", width: 100, height: 100, visible: true,
    relativeTransform: [[1, 0, 0], [0, 1, 0]], fills: [], children, ...props};
  children.forEach(child => child.parent = node);
  return node;
}

test("collects exact local transformed bounds without changing source", async () => {
  const child = scene("child", [], {width: 20, height: 10,
    relativeTransform: [[0, -1, 30], [1, 0, 5]]});
  const root = scene("root", [child]);
  const before = child.relativeTransform.map(row => [...row]);
  const result = await collectMaterialSnapshot({rootIds: ["root"], revision: "r1"}, {getNodeByIdAsync: async () => root});
  assert.deepEqual(result.nodes[1].boundsInParent, {x: 20, y: 5, width: 10, height: 20});
  assert.deepEqual(child.relativeTransform, before);
  assert.equal(result.nodes[1].parentId, "root");
});

test("hidden subtrees omitted, hidden roots rejected", async () => {
  const hidden = scene("hidden", [scene("hidden-child")], {visible: false});
  const root = scene("root", [hidden, scene("shown")]);
  const result = await collectMaterialSnapshot({rootIds: ["root"], revision: "r1"}, {getNodeByIdAsync: async () => root});
  assert.deepEqual(result.nodes.map(n => n.id), ["root", "shown"]);
  await assert.rejects(collectMaterialSnapshot({rootIds: ["hidden-child"], revision: "r1"},
    {getNodeByIdAsync: async () => hidden.children[0]}), /hidden/);
});

test("empty scope and missing roots rejected", async () => {
  await assert.rejects(collectMaterialSnapshot({rootIds: [], revision: "r1"}, {}), /required/);
  await assert.rejects(collectMaterialSnapshot({rootIds: ["missing"], revision: "r1"},
    {getNodeByIdAsync: async () => null}), /existing/);
});

test("node cap does not return a partial success", async () => {
  const root = scene("root", [scene("child")]);
  await assert.rejects(collectMaterialSnapshot({rootIds: ["root"], revision: "r1", maxNodes: 1},
    {getNodeByIdAsync: async () => root}), /limit exceeded/);
});

test("mixed fonts and styles preserved for review", async () => {
  const text = scene("text", [], {type: "TEXT", hasMissingFont: true, textAutoResize: "NONE",
    getStyledTextSegments: () => [{fontName: {family: "Roboto"}, textStyleId: "s1"},
                                {fontName: {family: "Noto Sans SC"}, textStyleId: ""}]});
  const result = await collectMaterialSnapshot({rootIds: ["text"], revision: "r1"}, {getNodeByIdAsync: async () => text});
  assert.equal(result.nodes[0].textStyleStatus, "raw-or-mixed");
  assert.deepEqual(result.nodes[0].fontFamilies, ["Roboto", "Noto Sans SC"]);
  assert.equal(result.nodes[0].hasMissingFont, true);
});

test("style/paint bindings are not mistaken for raw fills", async () => {
  const root = scene("root", [
    scene("style", [], {fillStyleId: "s", fills: [{type: "SOLID"}]}),
    scene("bound", [], {fills: [{type: "SOLID", boundVariables: {color: {id: "v"}}}]}),
    scene("raw", [], {fills: [{type: "SOLID"}]})]);
  const result = await collectMaterialSnapshot({rootIds: ["root"], revision: "r1"}, {getNodeByIdAsync: async () => root});
  assert.deepEqual(result.nodes.map(n => n.rawSolidFills), [0, 0, 0, 1]);
});

test("collector output is consumed by the Python auditor and catches actual overflow", async () => {
  const root = scene("root", [scene("child", [], {height: 120})]);
  const data = await collectMaterialSnapshot({rootIds: ["root"], revision: "r1"},
    {getNodeByIdAsync: async () => root});
  const result = spawnSync("python3", [
    path.join(__dirname, "../skills/_material-android-ui-shared/scripts/audit_figma_snapshot.py"),
    "/dev/stdin"], {input: JSON.stringify(data), encoding: "utf8"});
  assert.equal(result.status, 1, result.stderr);
  assert.equal(JSON.parse(result.stdout).findings[0].ruleId, "figma.bounds");
});

test("overlapping roots rejected", async () => {
  const child = scene("child"), root = scene("root", [child]);
  await assert.rejects(collectMaterialSnapshot({rootIds: ["root", "child"], revision: "r1"},
    {getNodeByIdAsync: async id => id === "root" ? root : child}), /disjoint roots/);
});

test("failed text read is retained as incomplete evidence", async () => {
  const text = scene("text", [], {type: "TEXT", getStyledTextSegments: () => {throw new Error("missing API");}});
  const data = await collectMaterialSnapshot({rootIds: ["text"], revision: "r1"},
    {getNodeByIdAsync: async () => text});
  assert.equal(data.errors.length, 1);
  assert.equal(data.errors[0].nodeId, "text");
});
