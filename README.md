# Material UI Design Skills

一套面向产品、设计与研发协作的 Material 3 UI 设计 Skill。目前仓库只发布两个能力：

1. **产品原型 → Material UI**：把 HTML 原型、线框稿、截图、流程或需求整理成完整、可编辑、可交付的 Material 3 UI 设计。
2. **Material UI 细调**：在不破坏已确认产品方向的前提下，对现有 UI 做可测量、可回归、符合 Material 3 与无障碍要求的细节修正。

本次暂不发布 Jetpack Compose 与 Flutter 的代码实现 Skill。仓库中的内容负责“把产品意图变成可靠设计”和“把现有设计修到可交付状态”，不直接生成业务代码。

## 设计理念

### 1. 先理解产品，再画界面

原型表达的是产品流程、信息层级和业务意图，不等于已经符合 Material 3。Skill 会先识别用户、任务、路由、状态、内容和交互，再把这些意图映射到正确的 Material 组件、语义 Token 与自适应布局。

### 2. 先确认风格，再批量出图

主题色、明暗模式、Material 3 Baseline 或 Expressive、密度、圆角、图标、图片风格和动效强度都会显著影响结果。Skill 会先读取原型和已有品牌资产，只询问原型中无法确定且会改变结果的问题。方向不明确时，先用同一张代表性页面给出 2–3 个风格方向，再进入完整设计。

### 3. 用语义系统承接设计，而不是堆截图

颜色、文字、间距、形状、层级、图标和动效使用语义 Token；重复 UI 使用组件、属性和变体。最终交付不仅有页面图，还包含可继续维护的设计系统、状态矩阵、自适应矩阵和交付契约。

### 4. 产品转 UI 与 UI 细调使用同一份连续性契约

两个 Skill 共用 `material-ui-contract.json`、Material 基线、组件规格、动效规则、自适应与无障碍规则。细调阶段不会重新猜测设计意图，而是继承已确认的主题、组件、状态、资产和例外记录。

### 5. Material 合规必须有证据

“看起来像”不等于符合 Material。完成前需要检查语义组件、颜色对比度、触控目标、文字缩放、长文案、RTL、交互状态、窗口尺寸、系统栏、IME、动效和 reduced motion。Figma 还必须通过容器边界、裁剪、Auto Layout、区块间距和整页截图检查。

### 6. 原始资产优先，禁止占位图标进入交付

Logo 优先使用产品提供的原始 SVG；标准操作优先使用设计系统图标或 Material Symbols。黑点、普通圆形、方块、Emoji、字母和文本字符不能作为导航或操作图标的占位交付。只有状态点、分页点、单选标记等“形状本身就是含义”的场景可以使用圆点。

## 仓库包含什么

```text
skills/
├── material-android-ui-design/       # 产品原型 → Material UI
├── material-android-ui-refine/       # 已有 UI 的审计与细调
└── _material-android-ui-shared/      # 两个 Skill 共用的规范、契约、Schema 与校验工具
```

| Skill | 适用场景 | 不适用场景 |
|---|---|---|
| `material-android-ui-design` | 从产品原型、需求、流程、截图或线框稿开始设计完整 UI | 已有 UI 的局部修正、直接编写 Compose/Flutter 代码 |
| `material-android-ui-refine` | 审计和细调已有 Figma、UI 图、截图或原型 | 从零探索产品风格、直接修改业务实现代码 |

## 一、产品原型 → Material UI

### 原型有什么要求

产品同学不需要先把原型整理成某一种固定格式，可以直接提供：

- 可运行的 HTML/CSS 原型；
- Figma 线框稿或已有低保真页面；
- 页面截图、手绘草图或流程图；
- PRD、交互说明、真实文案与数据样例；
- Logo、图标、图片、视频、字体等品牌资产；
- 上述材料的组合。

原型越完整，生成结果越稳定。建议至少表达以下内容：

- 用户要完成的核心任务；
- 页面和页面之间如何跳转；
- 每个页面的主要内容和操作；
- 加载、空数据、错误、离线、权限、成功等业务状态；
- 已锁定的品牌内容或不能修改的区域；
- 目标设备范围，例如手机、折叠屏和平板。

如果原型缺少这些信息，Skill 会先从现有文件中提取能够确认的部分，只询问真正影响设计结果的缺口，不要求产品同学重复描述原型里已经存在的信息。

### 调用前会确认什么

完整 UI 输出前，Skill 会确认或记录默认值：

1. 主品牌色或主题种子色，以及静态色、Android 动态色或混合策略；
2. 浅色、深色、跟随系统的支持范围；
3. Material 3 Baseline 或 Material 3 Expressive；
4. 3–5 个风格关键词；
5. 标准、舒适或紧凑密度；
6. 柔和、平衡或几何化的形状方向；
7. 图标体系、图片处理和动效强度；
8. 目标窗口尺寸、语言、RTL 与无障碍要求；
9. Logo、字体、固定颜色、法务内容等品牌约束。

产品同学也可以直接授权使用推荐方案。例如：

```text
使用 $material-android-ui-design 处理这个 HTML 原型。

主题色使用 #D3FF5C，Logo 使用我提供的 SVG。
其余风格、密度、圆角和动效先按推荐方案。
目标是 Android 手机，同时给出平板自适应方案。
最终写入可编辑 Figma，不要把 HTML 当作最终交付。
```

### Skill 如何工作

1. 检查原型、需求、内容、资产和目标设备。
2. 整理路由、任务、信息层级、状态和交互事件。
3. 建立并持续更新 `material-ui-contract.json`。
4. 先建立浅色/深色颜色、排版、间距、形状、层级、图标和动效 Token。
5. 把每个 UI 元素映射到合适的 Material 组件；自定义组件需要记录原因。
6. 先完成灰度结构和关键流程，再应用已确认的视觉方向。
7. 建立可复用组件、状态变体和 Compact/Medium/Expanded 自适应页面。
8. 使用真实矢量图标和产品原始资产替换原型占位内容。
9. 补齐关键动效、状态反馈与 reduced-motion 方案。
10. 执行 Material、无障碍、自适应和 Figma 结构化验收。

### 最终产出是什么

当 Figma 可用时，默认产出是**可编辑 Figma 文件**，不是 HTML。HTML 只是原型输入或对照参考，除非产品明确要求 HTML 作为最终交付。

完整交付通常包含：

- `00 Brief & Decisions`：产品目标、已确认方向、默认值和待决事项；
- `01 Foundations`：颜色、排版、间距、形状、层级、图标、动效；
- `02 Components`：组件、尺寸、状态、属性和变体；
- `03 Patterns & Adaptive Templates`：导航、页面骨架和自适应模板；
- `04 Screens`：完整页面和主流程；
- `05 States & Motion`：加载、空、错误、权限、成功和关键动效；
- `06 Handoff & QA`：交付契约、状态矩阵、检查结果和例外；
- `material-ui-contract.json`：供 UI 细调与后续实现继续使用的结构化契约；
- 确定尺寸的页面导出、资产清单、Material 与无障碍报告。

如果没有可编辑 Figma 能力，Skill 仍应交付语义 Token、精确尺寸导出、状态矩阵、自适应矩阵、资产清单、交互说明和契约，而不是只给一组截图。

### 完成标准

以下内容缺失时不能声称“已经完成”或“完全符合 Material”：

- 必需页面、业务状态和交互状态；
- 浅色/深色与目标自适应分支；
- 文字缩放、长文案、中文/目标语言和 RTL 验证；
- 无障碍语义、顺序、对比度和触控目标；
- 原始 Logo、正常图标和合法资产来源；
- Figma 中零非预期溢出、零非预期裁剪、零区块重叠；
- 区块级与整页最终截图；
- 已记录的假设、例外和待决问题。

## 二、Material UI 细调

### 什么时候使用

使用 `material-android-ui-refine` 处理已经有明确设计方向的 UI，例如：

- 文字、图标、组件或卡片被裁剪；
- 间距、圆角、字号、基线或层级不一致；
- 导航和操作位置使用了黑点或临时图形；
- 组件尺寸、触控目标或状态不符合 Material；
- 深色模式、长文案、RTL、平板布局出现问题；
- 修改共享组件后，部分页面发生回归；
- 需要按照截图反馈精确修正 Figma。

如果请求会改变已经确认的品牌方向、核心信息架构或冻结内容，细调 Skill 不会把它伪装成小修复，而会要求重新确认设计决策或回到产品转 UI 流程。

### 需要提供什么

建议提供：

- 可编辑 Figma 链接或现有设计源文件；
- 问题截图和需要修改的位置；
- 当前 `material-ui-contract.json`；
- 哪些区域允许修改、哪些区域必须保持；
- 目标主题、设备尺寸、语言、字体缩放和状态；
- 运行时截图时对应的版本、窗口尺寸和系统栏/IME 情况。

只有截图但没有设备、主题、状态和版本信息时，截图只能作为视觉参考，不能直接作为严格通过/失败证据。

### Skill 如何细调

1. 冻结修改前基线，确认设计、契约、导出和运行时版本一致。
2. 建立问题台账，记录位置、严重级别、测量值、目标规则、根因和影响范围。
3. 按依赖顺序修复：结构与自适应 → 基础 Token → 共享组件 → 页面实例 → 交互 → 导出与契约。
4. 优先修共享根因，不逐页面重复打补丁。
5. 对 Figma 裁剪问题从最内层错误容器开始，恢复正确 HUG/FILL/FIXED，再让父级 Auto Layout 自动重排。
6. 使用正常矢量图标替换操作/导航占位图形，并检查图标可视边界与槽位边界。
7. 检查所有受影响主题、状态、窗口尺寸、语言和文字缩放。
8. 保留修改前后证据，并同步更新契约和回归矩阵。

### 调用示例

```text
使用 $material-android-ui-refine 细调这个 Figma 页面。

保持已经确认的主题色、字体和页面结构不变。
把导航栏、顶部操作和卡片里的黑点替换成合适的 Material 图标。
修复 Colors、Shape、Elevation 中被裁剪的卡片和文字。
修改后检查所有子元素边界、区块间距和整页 Auto Layout，提供修改前后证据。
```

### 细调产出

- 修正后的可编辑设计源；
- 修改前后精确配置截图；
- 已解决的问题台账；
- 更新后的 `material-ui-contract.json` 和资产清单；
- 受影响页面、组件、状态、主题和窗口尺寸的回归矩阵；
- Figma 子元素溢出、区块间距、裁剪与整页截图证据；
- 仍存在的风险、已批准例外和后续实现影响。

## 安装

克隆仓库：

```bash
git clone git@git.tuntas.ai:wowo/Material-UI-Desgin.git
cd Material-UI-Desgin
```

将两个 Skill 和共享目录复制到个人 Codex Skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R skills/material-android-ui-design ~/.codex/skills/
cp -R skills/material-android-ui-refine ~/.codex/skills/
cp -R skills/_material-android-ui-shared ~/.codex/skills/
```

三个目录必须保持同级，否则 Skill 中的相对引用无法解析：

```text
~/.codex/skills/
├── material-android-ui-design/
├── material-android-ui-refine/
└── _material-android-ui-shared/
```

## 使用建议

- 新产品或风格尚未确认：先用 `$material-android-ui-design`。
- 已有设计，只需纠错和细调：用 `$material-android-ui-refine`。
- 产品转 UI 完成后再细调：把同一份 Figma 与 `material-ui-contract.json` 交给细调 Skill。
- 尽量提供真实文案、最长数据、错误样例和原始资产，减少后期返工。
- 对主题色和风格没有意见时，可以明确授权“其余按推荐方案”，但品牌、合规、安全和不可逆行为不会被静默假设。
- Figma 产出应保持可编辑组件和 Auto Layout；截图只用于验收，不能替代设计源。

## 共享资源

`_material-android-ui-shared` 包含两个 Skill 共同依赖的内容：

- Material 3 基础 Token 与排版、颜色、间距、形状、层级规则；
- 常用组件尺寸和交互状态规格；
- 动效、状态层和 reduced-motion 规则；
- Android 自适应、文字缩放、RTL 与无障碍检查；
- Figma 图标、裁剪、Auto Layout 与结构化 QA；
- `material-ui-contract.json` Schema 与示例；
- 视觉对比辅助脚本。

## 当前发布边界

本仓库当前不包含：

- Jetpack Compose UI 代码生成；
- Flutter UI 代码生成；
- Flutter 内嵌 WebView 实现；
- 网络接口、状态管理、数据存储或业务逻辑实现；
- Android/Flutter UI 单元测试模板。

这些实现类 Skill 将在设计与细调流程稳定后单独发布，避免产品设计能力与工程实现能力混在同一个调用入口中。
