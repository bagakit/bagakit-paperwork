# MVP Experiment Notes

## Hypothesis (观点)
通过“问题 -> 机制 -> 验证 -> 完成定义”的重排，可以让文章更快进入可执行叙事，而不是停留在口号。

## Version Baseline Gate (新增，强制)

每次新增版本前，必须先完成基线读取与回填，避免新技巧引入时造成旧能力退化。

强制步骤：
1. 阅读上一版本的 `versions/v*/techniques.md`。
2. 阅读上一版本的 gap 分析（如 `v*-gap-analysis.md`）和最新审计结论。
3. 生成本轮“保留项/新增项/收紧项”清单，再开始改稿。

适用范围：
- 正文写作（`versions/v*/article.md`）
- 技巧文档写作（`versions/v*/techniques.md`）
- 与 skill 相关的规范文档写作（流程、门禁、README 说明等）

验收标准：
- 新版本文档中必须显式说明“基于上一版技巧的继承与变化”；
- 不得出现“可读性上升但可执行性回退”的未解释回退。

## Tool Usability (工具)
用一个可复现脚本在实验目录内完成：
1. 复制源文到 `versions/v0/source-copy.md`（保留原文快照）。
2. 生成候选稿 `versions/v1/candidate.md`。
3. 运行 `tools/check_experiment.py` 产出 `versions/v1/metrics/experiment-metrics.json`。

## Boundary
- Source file immutable: yes
- All edits constrained in experimental dir: yes
