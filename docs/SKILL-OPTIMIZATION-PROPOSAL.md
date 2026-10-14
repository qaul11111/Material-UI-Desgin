# Material UI Skills 优化方案（评审稿）

> 2026-09-04 更新：用户已批准优先实施“Figma 可执行检查、代表页面确认、真实案例回归、交接契约校验”，并轻量精简入口。下文原 P0/P1/P2 是历史候选方案，不再代表本轮全部实施范围。视觉方向、图标、字体研究及真实验证边界见 [本轮实施说明](2026-09-04-VISUAL-DIRECTION-UPDATE.md)。本轮暂不推送，不发布开发 Skill。

> 状态：Draft，仅供评审  
> 日期：2026-08-31  
> 当前阶段：只新增文档，不修改 Skill，不提交、不推送  
> 对比基线：[hamen/material-3-skill](https://github.com/hamen/material-3-skill)（调研时 README 标注 v1.1.1）

## 1. 目的与范围

本文用于确定现有 Material UI Skills 下一轮优化的方向、边界、验收标准和实施顺序。

评审范围：

- material-android-ui-design：产品原型 → Material 3 UI 设计稿。
- material-android-ui-refine：已有 UI → Material 3 审计、细调与回归。
- _material-android-ui-shared：设计、细调、开发共用规范与交接契约。
- compose-material-ui-implementation：UI → Jetpack Compose，作为后续优化对象，当前不发布。
- flutter-material-ui-implementation：UI → Flutter / 内嵌 WebView，作为后续优化对象，当前不发布。

本文不做：

- 不直接修改上述 Skill。
- 不把 Compose、Flutter Skill 推送到当前远程仓库。
- 不照搬参考仓库内容。
- 不在尚未读取目标工程版本时固定 Compose、Flutter 或第三方库 API。

## 2. 结论摘要

现有方案的主架构应保留，不建议合并为一个大型 Skill。

建议继续维持以下连续流程：

    产品原型
      ↓ material-android-ui-design
    可编辑 Material 3 UI + material-ui-contract.json
      ↓ material-android-ui-refine
    已审计 UI + 更新后的契约
      ├─ compose-material-ui-implementation
      └─ flutter-material-ui-implementation
           ↓
    平台代码、适配、测试、视觉对比和业务接入边界

参考项目最值得吸收的是四类工程化能力：

1. 快速任务路由：先识别模式，再加载相关规范。
2. 可检索组件目录：建立组件、状态、平台实现与测试要求的映射。
3. 结构化审计：用硬性门禁和评分卡共同表达结果。
4. 仓库工程化：版本、脚本、CI、安装检查和断链检查。

优先级建议：

- P0：任务路由、跨平台组件矩阵、可执行审计、WebView Token 导出。
- P1：评分卡、版本感知代码配方、项目组件覆盖表、CI 与版本治理。
- P2：插件化分发、自动评测集、Figma 审计工具库和正式发布体系。

## 3. 现有方案应保留的优势

### 3.1 按产品生命周期拆分

设计、细调、Compose 开发和 Flutter 开发的输入、输出、风险和验收方式不同。保持独立 Skill 能降低上下文噪声，让产品、设计和开发只处理当前阶段需要的决策。

### 3.2 设计前有产品和风格澄清

现有设计 Skill 会确认品牌、页面目标、信息密度、圆角倾向、图形语言、动效程度和参考方向，而不是只根据主题色套模板。这应继续作为原型转 UI 的必要环节。

### 3.3 输出是可编辑设计资产

主交付目标是可编辑的 Figma 页面、组件、变量和样式；预览图只用于评审。这样才能支撑产品细调、状态补齐、Token 追踪以及 Compose、Flutter 的持续还原。

### 3.4 用连续性契约连接设计与开发

material-ui-contract.json 是当前方案的重要差异点，应继续作为跨 Skill 的机器可读交接层。它至少记录：

- Light/Dark 语义色。
- 字体、间距、形状、层级和动效 Token。
- 页面、组件、状态与断点。
- 资源来源、命名和复用键。
- WebView 主题桥接约束。
- 已批准 Material 偏差及原因。

### 3.5 细调阶段以测量和证据为准

现有流程强调先审计、再修复、再回归，并检查裁切、状态、触控目标、排版、布局、图标、可访问性和 Figma 结构。自动化只能增强这套流程，不能用简单评分替代证据。

### 3.6 开发 Skill 已具备生产工程意识

Compose、Flutter 方向已覆盖最小无状态组件、状态提升、单向数据流、业务逻辑分离、网络与存储接口边界、资源分类、窗口适配、UI 测试、视觉对比和 WebView 安全。这些能力应继续保持一等优先级。

## 4. 参考项目中值得吸收的能力

参考项目入口见 [SKILL.md](https://github.com/hamen/material-3-skill/blob/master/skills/material-3/SKILL.md)，组件资料见 [component-catalog.md](https://github.com/hamen/material-3-skill/blob/master/skills/material-3/references/component-catalog.md)。

### 4.1 模式化任务路由

参考项目把请求归类为 component、theme、layout、scaffold、audit 等模式。建议借鉴“先分类、后加载”的机制，但为我们的四个生命周期分别设计路由。

### 4.2 可搜索组件目录

参考项目覆盖大量 Material 3 组件，并给出用途、选择逻辑和平台示例。建议升级为“跨平台组件实现矩阵”，额外回答：

- Figma 中有哪些组件和 Variant。
- 必须覆盖哪些状态。
- Compose、Flutter 分别如何映射。
- 两个平台有哪些能力差异。
- 绑定哪些 Token。
- 验证哪些可访问性和测试项。
- WebView 是否允许承担该组件职责。

### 4.3 审计评分框架

多分类评分适合快速表达薄弱项，可以吸收，但必须增加两层保护：

- 硬性门禁先于评分，严重问题不能被平均分掩盖。
- N/A 与 0 分分开，未使用的能力不应被判失败。

### 4.4 仓库结构和 CI

参考项目提供了清晰的分发与测试入口，见 [bin/ci](https://github.com/hamen/material-3-skill/blob/master/bin/ci) 和 [plugin_layout_test.sh](https://github.com/hamen/material-3-skill/blob/master/tests/plugin_layout_test.sh)。

我们的仓库后续应增加：

- Skill 文件布局和元数据检查。
- Markdown 引用断链检查。
- JSON Schema 和契约示例校验。
- 审计脚本与 Token 导出脚本的行为测试。
- 发布范围检查，避免 Compose、Flutter 被意外打包。

## 5. 不建议照搬的部分

### 5.1 不合并成单个超长 Skill

单入口适合查询，但会混合产品、设计、审计和开发语境。我们的阶段边界和连续性更明确，分阶段更容易维护与验收。

### 5.2 不把 Flutter 作为次级支持

公司交付同时覆盖 Compose、Flutter 和 WebView。Flutter 必须拥有与 Compose 同等深度的 Token、适配、状态管理、可访问性、测试和资源管理规则。

### 5.3 不固化未经工程确认的 API

代码示例必须基于目标工程的 SDK、依赖锁文件和实验 API 配置生成，并记录验证日期、适用版本和降级策略。

### 5.4 不让总分替代发布门禁

即使总体得分很高，文字裁切、触控目标不足、对比度失败、关键状态缺失或危险 WebView Bridge 都应直接阻止交付。

### 5.5 不默认采用 Material Web

WebView 应优先复用目标项目现有 Web 技术栈，通过 CSS Token 和主题桥接实现一致性。只有工程已经采用相应 Web 组件库并完成兼容验证时，才使用该实现。

## 6. 总体优化原则

1. 生命周期分离：每个 Skill 只负责一个阶段的主要决策。
2. 契约连续：设计、细调和开发共享同一机器可读 UI 契约。
3. 官方规范优先：Material、Android、Compose、Flutter 官方文档是事实基线。
4. 工程版本优先：代码以目标仓库实际版本为准。
5. 硬门禁优先：安全、可访问性、裁切、状态和导航错误先阻断。
6. 渐进加载：入口保持短小，按模式读取 references。
7. 平台平权：Compose 与 Flutter 对共同承诺能力使用同级标准。
8. 自动化稳定规则：可重复判断交给脚本，产品取舍保留人工确认。
9. 偏差可追溯：所有非标准 Material 决策记录原因、范围和替代规则。
10. 证据驱动：结论指向节点、截图、契约路径、代码位置或测试。

## 7. 目标目录规划

以下仅为规划，不代表本评审稿已经创建这些文件：

    Material-UI-Desgin/
    ├── CHANGELOG.md                              # P1
    ├── VERSION                                   # P1
    ├── bin/ci                                    # P1
    ├── docs/SKILL-OPTIMIZATION-PROPOSAL.md
    ├── skills/
    │   ├── _material-android-ui-shared/
    │   │   ├── references/
    │   │   │   ├── component-implementation-matrix.md
    │   │   │   ├── platform-capability-matrix.md
    │   │   │   ├── audit-scorecard.md
    │   │   │   └── source-governance.md
    │   │   ├── schemas/material-ui-contract.schema.json
    │   │   ├── scripts/
    │   │   │   ├── validate_contract.py
    │   │   │   ├── audit_material_usage.py
    │   │   │   └── export_webview_tokens.py
    │   │   └── examples/audit-config.example.json
    │   ├── material-android-ui-design/
    │   │   └── references/request-router.md
    │   └── material-android-ui-refine/
    │       └── references/request-router.md
    └── tests/
        ├── repository_layout_test.sh
        ├── reference_links_test.py
        ├── contract_validation_test.py
        └── token_export_test.py

Compose、Flutter 规划内容先留在父工作区，完成真实项目验证后再决定是否发布。

## 8. P0 优化项

### P0-1：为每个 Skill 增加请求路由

目标：在读取大量资料前，先识别任务类型、必要输入与输出形式。

设计 Skill 建议模式：

| 模式 | 典型输入 | 核心输出 |
|---|---|---|
| prototype-to-ui | HTML、线框图、原型截图、流程说明 | 完整可编辑 UI、状态页、契约 |
| theme | 品牌色、Logo、品牌规则 | Light/Dark 主题、语义 Token、预览 |
| component-library | 产品组件清单或已有页面 | Figma 组件、Variants、变量绑定 |
| flow | 多页面业务流程 | 连续页面、状态转换、原型连线 |

细调 Skill 建议模式：

| 模式 | 用途 | 结果 |
|---|---|---|
| audit | 只检查，不修改 | 问题台账、证据、优先级、评分 |
| fix | 根据问题修正 | 修改后的 Figma、变更清单、契约更新 |
| regression | 修改后复验 | 已关闭问题、遗留风险、回归证据 |

Compose、Flutter 分别支持 theme、component、screen、scaffold、adaptive、webview、audit。

验收标准：

- 典型请求可以唯一落到主模式。
- 混合请求能明确主次顺序。
- 只询问会实质改变设计方向的缺失信息。
- 路由后不加载无关的大型参考文件。
- 不依赖某个模型私有且不可移植的格式。

### P0-2：建立跨平台组件实现矩阵

目标：把组件目录升级为设计和开发共用的事实表。

建议字段：

| 字段 | 说明 |
|---|---|
| componentId | 稳定内部标识，如 navigation_bar |
| Material 职责 | 适用场景、不可替代场景、选择条件 |
| 设计复用键 | Figma 组件集、Variant 属性、命名规则 |
| 必需状态 | default、pressed、focused、disabled、loading、error 等 |
| Compose 映射 | 官方组件、替代策略、版本证据 |
| Flutter 映射 | 官方组件、替代策略、版本证据 |
| Token 钩子 | color、type、shape、elevation、motion、spacing |
| 自适应规则 | compact、medium、expanded 下的变化 |
| 可访问性 | 语义、触控目标、焦点、朗读、对比度 |
| 测试要求 | 单元、UI、截图或 Golden、交互状态 |
| WebView 职责 | native、web、hybrid 或禁止 |
| 来源与日期 | 官方链接、验证日期、适用版本 |

使用约束：

- 全量组件目录只作为查询库。
- 每个项目单独生成“实际使用组件覆盖表”。
- 设计验收和代码验收共用 componentId。
- 平台差异必须显式记录，不能伪造一致性。

### P0-3：增加可执行审计

第一阶段范围：

1. 契约审计：Schema、必需 Token、语义角色、页面与状态、批准偏差。
2. Figma 审计：未绑定变量、文字裁切、固定高度、临时图标、组件脱离、Variant 缺失、触控目标与 Auto Layout 风险。
3. Compose 静态审计：散落硬编码、状态未提升、UI 直接持有网络或存储逻辑、Insets 与语义高风险位置。
4. Flutter 静态审计：散落 Color/TextStyle/固定尺寸、业务状态过重、SafeArea/TextScaler/Semantics/响应式风险。
5. WebView 审计：明文加载、危险 JS Bridge、任意导航、文件访问、主题与返回行为缺失。

输出 JSON 与 Markdown 两种格式。单条问题至少包含：

    {
      "ruleId": "figma.icon.placeholder",
      "severity": "blocker",
      "status": "fail",
      "location": "Flow 03/Header/Action",
      "evidence": "使用纯色圆点代替可识别图标",
      "suggestion": "替换为 Material Symbol，保留至少 48dp 触控区域",
      "confidence": "high"
    }

约束与验收：

- 默认只报告，不自动修改。
- 支持 allowlist，但必须写原因和失效条件。
- 低置信度结果进入人工复核，不自动阻断。
- 同一输入得到确定性结果。
- 结果可定位到 Figma 节点、契约路径或代码文件。
- 关键规则至少有一个通过和一个失败 fixture。

### P0-4：从 UI 契约导出 WebView Token

输入：

- material-ui-contract.json。
- Light/Dark 语义色。
- 字体、间距、形状、层级和动效 Token。
- WebView 可用资源及限制。

输出：

- tokens-light.css。
- tokens-dark.css。
- 可选的自动主题切换 tokens.css。
- Token 名称和来源摘要。

宿主桥接要求：

- Android/Flutter 向 WebView 传递主题、字体缩放、语言和安全区域。
- Web 页面只消费受控 Token 与桥接协议。
- 主题切换、系统字号和页面恢复有测试。
- 绝不因视觉一致性自动生成危险脚本桥。

验收：

- 重复导出结果一致。
- Light/Dark Token 完整可追溯。
- CSS 名称稳定，变更有兼容策略。
- 主题切换行为明确且经过验证。

## 9. P1 优化项

### P1-1：硬门禁 + 10 分类评分

硬门禁包括：

- 文字或关键内容裁切。
- 黑点、字符、Emoji 或临时形状充当最终功能图标。
- 触控目标、对比度、语义或焦点顺序严重失败。
- loading、empty、error、disabled 等关键状态缺失。
- 导航和系统返回行为错误。
- WebView 存在高风险配置。
- 使用目标版本不支持的 API 且无降级方案。

评分分类：

1. Color & theme
2. Typography
3. Shape & elevation
4. Components & states
5. Layout & spacing
6. Navigation & system UI
7. Motion & feedback
8. Accessibility
9. Adaptive behavior
10. Delivery structure & traceability

每项包含分数、证据、置信度和适用性。N/A 不计平均值；总分只用于趋势，不决定发布。

### P1-2：版本感知代码配方

不保存大段“永久正确”的模板，只保存：

- 任务意图。
- 需要先检查的工程文件。
- 官方 API 选择条件。
- 最小实现骨架。
- 版本与实验状态风险。
- 验证命令和对应测试。

执行前必须读取目标项目事实：

- Android：AGP、Kotlin、Compose BOM、Material3、minSdk。
- Flutter：Flutter/Dart SDK、pubspec.lock、主题和状态管理。
- WebView：Web 技术栈、构建工具、浏览器兼容范围。

### P1-3：项目级组件覆盖表

示例：

| 组件 | 设计状态 | Compose | Flutter | A11y | 测试 | 结论 |
|---|---|---|---|---|---|---|
| Navigation Bar | 5/5 | 已映射 | 已映射 | 通过 | UI + Golden | Ready |
| Snackbar | 3/4 | 已映射 | 已映射 | 待复核 | 缺错误态 | Blocked |

覆盖表同时服务设计交付、开发计划和验收，避免为了“目录完整”制造无关工作。

### P1-4：来源与时效治理

容易变化的参考资料记录：

- 官方来源 URL。
- 最后验证日期。
- 适用平台与版本。
- 是否涉及 experimental API。
- 替代和降级策略。

事实优先级：目标工程 > 当前官方文档 > Skill 历史快照 > 第三方示例。

### P1-5：CI、版本与发布边界

CI 至少检查：

- 必需 Skill 文件存在且可读取。
- 相对引用可解析。
- JSON 示例符合 Schema。
- Token 导出确定。
- 审计 fixtures 通过。
- README 安装路径真实存在。
- 当前发布包只包含设计、细调和共享内容。
- 版本、变更日志和 Git Tag 一致。

## 10. P2 优化项

### P2-1：插件化分发

在目录、版本、迁移和安装测试稳定后，再评估打包为公司内部 Codex Plugin，统一安装、升级和回滚。

### P2-2：任务级评测集

建立真实样例：

- HTML 原型转 UI。
- 主题色和 Logo 替换。
- 黑点占位替换为真实图标。
- Foundation 页裁切与固定高度修复。
- Compact/Medium/Expanded 适配。
- Compose 与 Flutter 同屏还原。
- WebView Light/Dark 同步。

每个样例保存输入、预期行为、阻断项和验收证据，不只判断是否生成文件。

### P2-3：Figma 审计工具库

封装可复用检查：

- 未绑定变量。
- 疑似占位图标。
- 溢出和裁切风险。
- Auto Layout 与约束。
- 组件实例和 Variant 覆盖。
- 设计交付报告。

工具只负责采集和确定性判断，修改仍由细调 Skill 根据上下文完成。

## 11. 各 Skill 的拟修改摘要

| Skill | 保留 | 拟增强 | 不加入 |
|---|---|---|---|
| 产品原型 → UI | 产品/风格询问、Figma 可编辑交付、契约 | 请求路由、组件覆盖、主题来源、交付审计 | 开发框架细节 |
| UI 细调 | 测量、问题台账、修改、回归 | audit/fix/regression、硬门禁、评分卡、自动发现 | 无证据的一键美化 |
| Compose 开发 | 状态提升、最小组件、自适应、测试、资源管理 | 平台矩阵、版本配方、静态审计、WebView Token | 固定版本大型样板 |
| Flutter 开发 | 与 Compose 同级的架构和还原 | TextScaler、Golden/A11y、自适应、静态审计 | 次级或近似支持 |
| Shared | 契约、基础规范、官方来源 | 组件矩阵、审计、Token 导出、Schema、CI | 单项目业务规则 |

## 12. 原型 → UI Skill 的重点优化

### 12.1 原型不是视觉真值

HTML、线框图和截图用于提取信息架构、流程、内容优先级、交互意图和业务状态；不默认继承原型的颜色、字体、间距、占位图标、固定尺寸或非 Material 控件。

### 12.2 图标必须语义化

- 黑点、圆点、字母、Emoji、Unicode 字符和随手几何形状不能作为最终功能图标。
- 优先使用语义一致的 Material Symbols 或批准的品牌图标。
- 图标视觉尺寸和触控容器分开，例如 24dp 图标位于至少 48dp 交互区域。
- 同一动作跨页面使用同一图标、名称和可访问性标签。
- 没有合适标准图标时，必须显式设计并登记资产。

### 12.3 Foundation 示例必须完整显示

- Color、Elevation、Shape、Typography 示例必须完整可见。
- 不允许用固定高度容器隐藏说明、色块或阴影样例。
- 需要横向展示时优先扩展画板或重新分组。
- 交付前检查文字换行、字体回退、Auto Layout hug/fill 和 clipContent。

### 12.4 主题色必须生成语义角色

用户提供 #D3FF5C 代表品牌种子或关键品牌色，不表示所有按钮、容器和文字都直接使用该值。Skill 应生成或确认 Light/Dark 色彩方案，检查前景对比，区分 primary、primary-container、surface、outline、error 等角色，并记录生成方式与人工偏差。

### 12.5 最终交付必须做结构性 QA

- 页面、Flow 和关键状态完整。
- 文字、色板、阴影样例无裁切。
- 无占位图标和临时资源。
- 组件真正复用，而非只使用相似名称。
- 变量、样式和 Token 已绑定。
- 契约、Figma 和预览图一致。

## 13. UI 细调 Skill 的重点优化

### 13.1 默认先审计

每个问题至少记录页面与节点、违反规则、证据、严重级别、修改方案、影响范围和回归结果。

### 13.2 修改共享组件前评估影响

优先修复组件主定义并检查全部实例。局部差异使用显式 Variant 或属性，不通过 detach instance 绕开复用。

### 13.3 同时关闭视觉和结构问题

“色板没显示全”不能只加高画板，还要确认是否由父容器固定高度、Auto Layout 模式、clipContent、子节点越界或字体回退造成。回归证据要同时说明视觉和结构结果。

### 13.4 同步更新连续性契约

Token、组件状态、断点、资产或批准偏差发生变化时，必须同步 material-ui-contract.json，避免开发 Skill 读取旧事实。

## 14. 开发 Skill 的后续方向

本节只确定方向，当前不进入发布仓库。

### 14.1 Compose

- 基于目标工程版本选择 Material 3 API。
- Screen 接收状态与事件，状态由 ViewModel 或上层提升。
- 小组件保持无状态、可 Preview、可测试。
- WindowSizeClass、Insets、字体缩放和横竖屏共同参与适配。
- 主题、Typography、Shape 和语义色与契约映射。
- 图片、图标、视频、音频、字体、raw 资源分类管理。
- WebView 使用受控导航、主题桥、加载/错误状态和安全配置。
- 用 Compose UI Test 和截图对比覆盖关键页面和状态。

### 14.2 Flutter

- 识别工程现有架构和状态管理，不擅自引入第二套方案。
- Stateless Widget 优先，业务状态提升到现有状态层。
- LayoutBuilder、MediaQuery、SafeArea、TextScaler 与断点共同适配。
- ThemeExtension 或等价机制承载产品 Token。
- 图片、SVG、视频、音频、字体和 Web 资源统一分类。
- WebView 使用最小权限桥接、导航白名单和主题同步。
- 用 Widget、Semantics、Golden Test 和真机尺寸验证。

### 14.3 99% 还原度的可执行定义

- 指定基准尺寸做像素差异对比。
- 动态文本、系统字体缩放和不同语言以无裁切、层级和节奏一致为目标。
- 系统控件差异可显式豁免，但必须记录。
- 颜色、字体、间距、形状、图标、资源和状态逐项追踪。
- 差异区分为实现缺陷、平台差异、动态内容和批准偏差。

## 15. 分阶段实施计划

### Phase 0：基线冻结

- 保存现有四个 Skill 与共享契约基线。
- 选取 3–5 个真实页面作为回归样例。
- 记录当前已知问题和人工耗时。

### Phase 1：共享 P0 能力

- 建立组件实现矩阵。
- 完成契约校验器。
- 完成第一批审计规则和 fixtures。
- 完成 WebView Token 导出器。

### Phase 2：设计与细调 Skill

- 接入请求路由和组件覆盖表。
- 接入硬门禁与审计结果模型。
- 回归图标、裁切、变量和组件复用问题。
- 通过评审后再推送设计与细调版本。

### Phase 3：Compose 与 Flutter Skill

- 分别增加版本感知配方和平台矩阵。
- 接入契约、Token、审计和视觉对比。
- 至少在一个真实 Android 项目和一个 Flutter 项目验证。
- 继续留在父工作区，未经批准不推送。

### Phase 4：工程化发布

- 增加 CI、版本、变更日志和安装检查。
- 明确发布包边界。
- 回归通过后再创建 Tag 和发布说明。

## 16. 总体验收标准

1. 产品原型能稳定转为可编辑、可复用、无占位图标、无裁切的 Material 3 UI。
2. 主题种子被转换为完整语义方案，不在页面散落原始色值。
3. 细调输出带证据的问题台账，并完成结构和视觉回归。
4. Figma、契约、预览图和代码引用同一组稳定标识。
5. 每个项目只要求覆盖实际组件，同时保留全量查询能力。
6. Compose、Flutter 对共同承诺功能使用同级标准。
7. WebView 消费同一套主题 Token 并满足安全门禁。
8. 自动审计确定、可定位、可配置，不冒充产品判断。
9. 严重问题不能被高平均分掩盖。
10. 易变化的开发规则有来源、日期、版本和降级说明。
11. CI 能阻止断链、无效契约、脚本回归和错误发布范围。
12. Compose、Flutter 未经明确批准不会进入当前远程仓库。

## 17. 风险与应对

| 风险 | 影响 | 应对 |
|---|---|---|
| 规则过多 | 上下文膨胀 | 路由、按需 references、项目组件表 |
| 自动审计误报 | 团队不信任 | 置信度、allowlist、fixtures、人工复核 |
| 官方 API 变化 | 示例失效 | 工程版本优先、来源日期、最小配方 |
| 评分被当 KPI | 严重缺陷被忽略 | 硬门禁优先，N/A 单独处理 |
| 强行跨平台一致 | 违背平台习惯 | 共享语义，显式记录能力差异 |
| 契约与 Figma 漂移 | 开发读取旧事实 | 细调同步更新，CI 校验 |
| WebView 视觉通过但不安全 | 生产风险 | 安全独立硬门禁 |
| 过早发布开发 Skill | 使用未验证规则 | 本地真实项目验证后单独审批 |

## 18. 需要评审确认的决策

1. 是否保留“设计、细调、Compose、Flutter”四阶段结构。
2. 是否批准 P0 四项：请求路由、组件矩阵、可执行审计、WebView Token 导出。
3. 是否采用“硬门禁 + 10 分类评分”模型。
4. 是否保持 Compose、Flutter 不进入当前远程仓库，直到真实项目验证完成。
5. WebView Token 是否先采用 CSS Custom Properties 输出。
6. 当前仓库仅面向公司内部 Codex，还是需要兼容其他 Agent/IDE。
7. 是否把真实业务页面纳入评测集；如纳入，需先确定脱敏规则。

## 19. 参考能力取舍表

| 参考能力 | 处理方式 | 原因 |
|---|---|---|
| 任务模式与决策树 | 吸收并按四阶段重构 | 减少误路由和上下文浪费 |
| 30+ 组件目录 | 升级为跨平台矩阵 | 支撑设计到代码连续性 |
| 多分类评分 | 有条件吸收 | 必须加硬门禁、N/A 和证据 |
| Compose 示例 | 只参考配方结构 | API 以目标工程版本为准 |
| Flutter 辅助支持 | 不采用 | Flutter 是一等交付平台 |
| Material Web 近似实现 | 不作为默认 | WebView 应适配现有技术栈 |
| 单个大型 Skill | 不采用 | 与生命周期和职责边界冲突 |
| Plugin/CI 布局 | 分阶段吸收 | 改善安装、版本和回归治理 |

## 20. 初稿阶段的变更边界（2026-08-31 历史记录）

2026-08-31 初稿只新增本优化文档；以下“不修改”描述仅指当日状态。2026-09-04 已按文首批准范围实施本地修改，仍未提交或推送。

初稿当时：

- 未修改设计 Skill。
- 未修改细调 Skill。
- 未修改共享规范与契约。
- 未修改 Compose、Flutter Skill。
- 未提交 Git Commit。
- 未推送远程仓库。

评审确认后，再按 P0 → P1 → P2 形成具体变更清单和实施提交。
