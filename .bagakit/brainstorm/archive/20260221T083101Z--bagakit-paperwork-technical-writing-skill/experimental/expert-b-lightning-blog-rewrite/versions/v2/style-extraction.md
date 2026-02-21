# Style Extraction from Anthropic Engineering Article

Source reference:
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## 1) 观点表达设计（Claim Design）

Observed pattern:
1. 先定义一个真实、可感知的问题场景（不是抽象价值观）。
2. 立即指出“看起来可行但实际上不够”的方案。
3. 明确失败模式（通常 2~4 个），并给出行为后果。
4. 用一句分解句把问题拆成可执行子问题（例如“这个问题可以拆成两部分”）。
5. 每个子问题对应一个机制与操作规范。
6. 结尾保留边界与后续工作，不装作“问题已彻底解决”。

Writing implication:
- 观点不应停留在“我们认为”；应落实到“如果不这样做，会发生什么”。

## 2) 术语使用设计（Term Discipline）

Observed pattern:
- 核心术语数量少且复用稳定，例如：`failure mode`、`incremental progress`、`clean state`。
- 同一概念不频繁换同义词，避免语义漂移。
- 术语出现后会给 operational definition（可操作定义）。

Writing implication:
- 每篇文最多 4~6 个核心术语，并在首次出现时定义。
- 术语后面紧跟“如何判定/如何执行”。

## 3) 转折词汇设计（Transition Design）

Observed pattern:
- 高频过渡词是逻辑功能词，不是修辞词：
  - 问题推进：`However`、`This happens even...`
  - 结构分解：`This decomposes the problem into...`
  - 条件推进：`Given this...`、`Once...`
  - 保留边界：`Some issues remain...`

Writing implication:
- 每个段落开头先说“本段逻辑功能”：反驳、分解、推进、边界。

## 4) 句子结构与长短节奏（Sentence Rhythm）

Observed pattern:
- 长句用于解释因果链与背景约束。
- 短句用于下判断、给规则、收口。
- 常见节奏是“长 + 短 + 中”：
  - 长句描述问题
  - 短句给判断
  - 中句给执行方法

Writing implication:
- 连续三句都很长会显著降低可读性。
- 关键段落的末句尽量短，作为控制点。

## 5) 可执行写作清单（Reusable Checklist）

1. 是否先给了具体问题场景？
2. 是否写清“已有方案为什么不够”？
3. 是否列出了可验证失败模式？
4. 是否有明确分解句，把问题拆成若干机制？
5. 每个机制是否都能映射到动作与证据？
6. 结尾是否保留了边界与后续工作？

## 6) 反模式（Anti-patterns）

- 先喊结论，后补背景。
- 术语频繁替换，读者难以建立稳定映射。
- 全文都是口号句，缺少失败模式和证据。
- 把“写作方法论名称”当作正文主角，喧宾夺主。
