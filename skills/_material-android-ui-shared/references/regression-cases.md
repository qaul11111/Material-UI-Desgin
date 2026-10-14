# Regression cases for the Skill suite

Use when changing the workflow or helpers, not on every small product edit. These cases come from observed Tuntas tasks: HTML prototype conversion, brand/Logo selection, functional dots, cropped Foundation specimens and generic component-stack composition.

## Two different types of verification

- Automated helper tests: deterministic simulated Figma geometry/API and contract/files. Run the repository tests. They reproduce failure classes, not a captured production Figma baseline.
- Forward task runs: execute the Skill on raw inputs in an explicitly authorized isolated design sandbox and inspect actual output. Record not-run when no live run occurs. Never call static wording checks, mocks or a prepared expected answer an end-to-end pass.

The repository includes a small sanitized HTML flow fixture under tests/fixtures. It is a reconstruction of the original workflow, not a copy of the large source file or a high-fidelity UI. The original local prototype is named TuntasAI-销售业务交互演示.html in its owner workspace. It is not required for installing this Skill.

## Cases and observable acceptance

| Case | Raw request/input | Observable acceptance |
|---|---|---|
| New visual direction | Sales prototype + brand seed + “professional, distinctive; other choices recommended” | Product goals preserved; a real-content representative screen before batch output; no invented backend behavior or manufactured approval |
| Brand change | New seed #D3FF5C + supplied SVG | Source Logo geometry preserved; semantic roles updated; contrast evidence; fonts/icon family remain unless the change authorizes them |
| Functional icons | Navigation/action circles + one real presence dot | Functional slots receive traceable assets and labels; genuine status dot remains |
| Foundation crop | Colors/Elevation child content exceeds fixed parent height | Fix inner container and reflow parents; no clipping or overlap; disabling clipsContent alone is not accepted |
| Type choice | Mixed Chinese, Latin, currency, timer, long company name | Compare real specimens; complete fallback/license/role information; large text is reflowed, not shrunk |
| Scoped refinement | “Only fix these two clipped specimens; keep approved style” | No global re-theme, unrelated component rewrite or fresh product interview |
| Audit-only | “Is this a bug?” | Evidence and explanation only; no writes |
| Visual character | “Looks like component stacking; improve hierarchy” | Intentional attention order, containment and rhythm; repeated generic cards are reconsidered; no arbitrary beauty score |
| Concept-only | “先给两种真实页面方向，我选完再展开” | Two useful same-content rendered candidates with tradeoffs; no full schema/catalog prerequisite; ends as exploration without a false development-readiness claim |
| Delegated choices | Existing seed/logo + “其余按推荐方案，继续做完” | Records delegated choices, renders and evaluates the representative view, then continues the requested scope; no repeated brand questionnaire or invented human selection |
| Reference transfer | An admired Material collage + a dense operational prototype | Inspects visible references, transfers an identified principle into an actual screen; retains content/actions, distinguishes presentation from canonical UI and does not copy unsuitable decoration |
| Qualitative improvement | “层级太平，改善这个页面；不要改 Logo 和业务流程” | Preserves frozen boundaries; records screenshot observation, treatment, real before/after and observed result; does not require an invented Material violation |
| Existing-identity route | A approved branded screen + request to visually improve it | Routes to refinement's visual elevation; full replacement identity routes to design; no unrequested global rebrand |
| Small fix without contract | Screenshot/source of two cropped labels, no JSON | Corrects and verifies affected source only; no requirement to invent a complete product contract |
| Unsuccessful revision | A changed screen still obscures the same primary task | Inspects revised output, acknowledges unresolved weakness and revises or revisits the brief; does not report success from written intentions alone |
| Actual text scaling | A preview with a large-text toggle and mixed heading/body/label roles | Measures rendered sizes for more than the heading; body and labels actually scale, content remains reachable by scrolling, and actions stay usable. A toggle value alone is not passing evidence. |

For a live run retain input artifact revision, Skill version, exact prompt, output file/frame IDs, elapsed time, unresolved issue count, product review rounds, approval scope and screenshot evidence. Use the same input before/after a Skill change; do not give the executor the desired fix or the prior implementation.

If the skill author also creates the sample, label it an author-run rehearsal, not an independent forward test. If no genuine old-Skill output exists at a comparable state/configuration, an original-prototype/new-concept comparison is useful but is not a controlled old/new-Skill experiment. Preserve that distinction in reports and UI labels.

## Automated guardrails

The repository Python tests cover broken IDs, missing components, stale revisions, undeclared targets, unknown data/events/fonts, schema errors, file hashes/path escape, draft-vs-delivery, Foundation crops, negative bounds, clipping-disabled overflow, real status dots, licensed functional icons, fixed text, missing fonts and section gaps.

The JavaScript tests exercise the collector with a Figma API mock: local transformed bounds, hidden ancestors, disjoint root constraints, incomplete collection, mixed type styles and variable/style fills.

These tests do not prove that a new design has better art direction. Evaluate that separately using the visual-direction questions and actual owner feedback.
