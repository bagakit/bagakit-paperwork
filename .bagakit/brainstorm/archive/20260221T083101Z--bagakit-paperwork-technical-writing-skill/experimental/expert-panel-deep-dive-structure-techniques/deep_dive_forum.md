---
stage_status: complete
forum_mode: deep_dive_forum
discussion_clear: true
final_one_liner: "v7 的骨架已经稳定，但“反例压力、读者画像、证据梯度”三块仍不够；建议引入 8 条进阶技巧后再出 v8。"
user_review_status: pending
user_review_note: "请先审阅本 deep dive 结论，再决定是否进入 v8 改写。"
participants:
  - name: "周衡 (Expert A)"
    domain_strength: "信息架构与认知负载"
    thinking_model: "约束驱动 + 信息分层"
    persona: "deep thinker"
  - name: "林栖 (Expert B)"
    domain_strength: "技术叙事与编辑策略"
    thinking_model: "问题驱动 + 叙事收敛"
    persona: "creative explorer"
  - name: "顾砺 (Expert C)"
    domain_strength: "质量门禁与红队审查"
    thinking_model: "反例推演 + 失败模式优先"
    persona: "constructive challenger"
key_issues:
  - "v7 是否还存在“讲得通但压不住反例”的段落。"
  - "结构已达标后，哪些语言技巧能显著拉高刊载质感。"
  - "哪些改动必须进入 v8，哪些可以延后到 profile 层。"
key_insights:
  - "v7 通过了结构底线，但“读者画像 -> 反例 -> 验证信号”链条仍偏短。"
  - "提升质感的关键不只是句子润色，而是证据梯度和段间张力设计。"
  - "可先加 8 条通用技巧，不必等 profile 才做。"
references:
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - "https://developers.google.com/tech-writing/one/audience"
  - "https://developers.google.com/tech-writing/one/active-voice"
  - "https://learn.microsoft.com/en-us/style-guide/scannable-content/headings"
  - "https://www.plainlanguage.gov/guidelines/organize/"
  - "https://owl.purdue.edu/owl/general_writing/the_writing_process/transitions_and_transitional_devices/index.html"
scoring_rules:
  peer_score_scale: "0~10"
  experiment_bonus_scale: "1~5"
  experiment_root: ".bagakit/brainstorm/runs/20260221T083101Z--bagakit-paperwork-technical-writing-skill/experimental/expert-panel-deep-dive-structure-techniques/"
---

# 详细结论

- 当前判断：`v7` 不差，但还没到“刊载级强解释力”的稳定态。
- 主要缺口：
  - 缺少“读者是谁、为什么现在要解决”的显式契约。
  - 反例与失败路径描述偏短，读者难判断方案边界。
  - 证据梯度不够完整，常出现“结论 -> 规则”，但少“反例 -> 回应 -> 信号”。
- 建议动作：
  - 进入 `v8`，优先引入 8 条进阶技巧（见后文）。
  - 只改实验目录，不回写源文。

## 外部审计输入（新增回填）

- 结论采纳：
  - 对外可读性目标下，`v7` 作为主稿方向正确。
  - 对内流程落地能力上，`skills/blogs` 的制度化表达值得吸收。
- 审计评分（10分制）：
  - 读者代入与叙事：`v7 8.9` vs `skills/blogs 7.2`
  - 论证一致性：`v7 8.6` vs `skills/blogs 6.8`
  - 可执行性与制度化：`v7 7.9` vs `skills/blogs 9.0`
  - 信息架构与扫描效率：`v7 8.2` vs `skills/blogs 8.4`
  - 发布友好度：`v7 7.6` vs `skills/blogs 8.0`
  - 总体（公开技术写作）：`v7 8.2` vs `skills/blogs 7.9`
- 关键问题确认：
  - `skills/blogs` 中存在“先判断后证据”与“先结论后证据是反模式”的表达冲突。
  - 结论：`v8` 需要明确区分“读者导航层的结论先行”与“论证层的证据先行”。

# 背景和专家组介绍

## 议题背景

- 主题：`v7 结构是否清楚 + 是否可继续引入高级技巧`
- 目标：识别 v7 中仍模糊的讨论点，并给出可执行的进阶技巧清单。
- 资料范围：`v7/article.md` + 外部写作指南 + 本地结构探针实验结果。

## 决策目标与准出条件

- 决策目标：确定是否进入 `v8` 改写，以及改写的最小必要改动集。
- 准出条件（必须全部满足）：
  - 结构问题是“可定位、可改写、可验收”的，而不是主观偏好。
  - 新技巧能映射到具体段落改动。
  - 有最小实验信号证明工具可复现。

## 专家组介绍

| 专家 | 擅长领域 | 思考模型 | 人格特征 | 在本议题中的职责 |
|------|----------|----------|----------|------------------|
| 周衡 (Expert A) | 信息架构与认知负载 | 约束驱动 + 信息分层 | deep thinker | 判断结构是否仍有认知断点 |
| 林栖 (Expert B) | 技术叙事与编辑策略 | 问题驱动 + 叙事收敛 | creative explorer | 给出可读性与张力增强技巧 |
| 顾砺 (Expert C) | 质量门禁与红队审查 | 反例推演 + 失败模式优先 | constructive challenger | 挑战“看起来清楚但不可执行”的段落 |

# 讨论过程

## 论坛议程（deep_dive_forum）

1. 拆分 v7 的结构与证据链，定位不清楚位置。
2. 每位专家给出线上检索证据，并映射到改写策略。
3. 做交叉评分（0~10），过滤掉“好看但不可执行”的建议。
4. 执行最小本地实验，验证“观点成立 + 工具可用”。
5. 收敛 v8 的最小必要改动集。

## 专家检索与证据陈述

| 专家 | 检索关键词 | 最有用参考 | 该参考如何支持观点 |
|------|------------|------------|--------------------|
| 周衡 (Expert A) | technical writing audience + organize information | [Google: Audience](https://developers.google.com/tech-writing/one/audience), [PlainLanguage: Organize](https://www.plainlanguage.gov/guidelines/organize/) | 支撑“先定义读者任务，再决定结构粒度”，避免结构只对作者清楚。 |
| 林栖 (Expert B) | engineering article transitions + active voice | [Anthropic: Effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [Google: Active voice](https://developers.google.com/tech-writing/one/active-voice) | 支撑“先现象再机制再实践”的推进节奏，以及更直接的动作句。 |
| 顾砺 (Expert C) | heading clarity + transition devices | [Microsoft: Headings](https://learn.microsoft.com/en-us/style-guide/scannable-content/headings), [Purdue: Transitions](https://owl.purdue.edu/owl/general_writing/the_writing_process/transitions_and_transitional_devices/index.html) | 支撑“标题要可独立理解，段间必须有可检查转折”，降低跳段断裂。 |

## 交叉评分（0~10）

| 评分人 | 被评分专家 | 分数(0~10) | 评分理由 |
|--------|------------|------------|----------|
| 周衡 (Expert A) | 林栖 (Expert B) | 9 | 把“语气优化”落成“动作句 + 过渡句”两类可执行规则。 |
| 周衡 (Expert A) | 顾砺 (Expert C) | 9 | 标题清晰度规则可直接转成 gate。 |
| 林栖 (Expert B) | 周衡 (Expert A) | 8 | 读者画像约束必要，但需要给更短的写法模板。 |
| 林栖 (Expert B) | 顾砺 (Expert C) | 8 | 风险识别完整，建议补“反例段落示例”。 |
| 顾砺 (Expert C) | 周衡 (Expert A) | 9 | 结构断点定位准确，利于回归测试。 |
| 顾砺 (Expert C) | 林栖 (Expert B) | 9 | 叙事技巧和验证信号绑定紧密。 |

## 实验设计与本地 MVP

- 实验路径：`experimental/expert-panel-deep-dive-structure-techniques/`
- 假设：`v7` 的主要问题不是标题数量，而是“证据梯度”和“段间张力”不够。
- 最小实现：
  - 编写结构探针 `structure_probe.py`；
  - 对 `versions/v7/article.md` 运行探针，输出 `v7-structure-metrics.json`。
- 观点成立验证（claim validation）：
  - 探针显示 `h2_count=5`、`h3_count=12`，说明骨架合规；
  - 但 `no_example_sections` 仍有 3 个分区，印证“证据密度不均”这一判断。
- 工具可用验证（tool usability）：
  - 脚本可重复执行，输出稳定 JSON 结果；
  - 输出字段可直接接入后续 gate（例如 `no_example_sections`）。
- 验证信号：
  - `diagnostic_flags.no_example_sections` 非空；
  - `issues` 包含可操作问题而非主观评价。
- 结果：支持“进入 v8，但改动重点应从结构数量转向证据与叙事梯度”。
- 对结论影响：确认需要补技巧，不需要推翻 v7 骨架。

## MVP验证结果（观点成立/工具可用）

| 实验 | 观点成立验证 | 工具可用验证 | 结论 |
|------|--------------|--------------|------|
| v7 structure probe | 骨架达标但证据分布不均，存在可定位缺口 | 脚本可复现并输出稳定结构诊断 | Deep dive 必要，且可进入 v8 精修 |

## 实验改动边界（强制）

- 源文改动：禁止
- 实验副本路径：`experimental/expert-panel-deep-dive-structure-techniques/`
- 约束声明：所有改动仅限 `experimental/` 目录；源文与业务代码不直接修改。

## 实验附加分（1~5）

- 实验数量：1
- 附加分：4
- 理由：同时给出“观点成立 + 工具可用”证据，且结果可复现。

## 讨论不清楚点（需要在 v8 解决）

1. 读者契约仍隐含：
   文章没有明确写出“谁会在什么任务场景下使用这套系统”。
2. 反例压力偏弱：
   讲了正确路径，但对“为什么旧路径会失败”还不够具象。
3. 证据梯度偏短：
   一些段落从判断直接跳到建议，中间缺“证据或信号”。
4. 结尾收束偏快：
   给了方向，但缺一个“上线后怎么判定成功”的最小指标集。

## 可引入的进阶技巧（v8 候选）

### 用词层

- 术语稳定表（Term Ledger）：开篇锁定 6~10 个核心术语，全篇不漂移。
- 动词分层：诊断段用“暴露/解释”，执行段用“定义/验证/回填”。

### 句子与段落层

- Topic Sentence Contract：每个关键段首句必须是可争辩判断句。
- 证据锚点句：每个判断段至少一处“信号/案例/反例”锚点。
- 转折句协议：段间至少一个“承接前文 + 引入新约束”的过渡句。

### 叙事层

- 反例先行法：关键模块先给一个失败样本，再给机制修复。
- 证据梯度法：`现象 -> 机制 -> 最小实验 -> 验证信号 -> 行动`。
- 收束清单法：结尾固定回答“先做什么、怎么验收、何时降级”。

## 新增检索回合：AI 味成因与修复策略（v10）

- 触发：你指出 v9 里“返工机器”“接得住”等口号化表达有明显 AI 味。
- 检索结论（摘要）：
  - 风格同质化是 AI 文本高频问题，容易导致“全篇一个语气模具”；
  - 过度抽象与名词化会让文本失去动作主体；
  - 列表密度过高会削弱自然叙述与阅读节奏；
  - 标题抽象化与被动表达会降低扫描效率和执行清晰度。
- 对应沉淀：
  - `versions/v10/techniques.md` 新增“AI 味成因 -> 改写动作”映射；
  - `versions/v10/article.md` 采用段落主导写法，降低口号词与清单密度。
- 关键来源：
  - https://www.nature.com/articles/s41599-025-04686-7
  - https://www.frontiersin.org/articles/10.3389/frai.2025.1628853/full
  - https://arxiv.org/abs/2504.13379
  - https://developers.google.com/tech-writing/one/active-voice
  - https://digital.gov/guides/plain-language/
  - https://learn.microsoft.com/en-us/style-guide/scannable-content/headings

## 新增审计回合：v10 -> v11（可执行性回退修复）

- 审计输入要点：
  - 发布稿含内部元数据（不适合直接发布）；
  - 与 v9 相比，可执行门禁表达回退；
  - 全段落化导致扫读锚点不足；
  - 去口号化未完全闭环。
- v11 修复动作：
  - 发布稿正文移除迭代元数据；
  - 恢复字段级门禁表（含失败处理）；
  - 恢复 H3 扫读锚点；
  - 进一步弱化口号式句子。
- 过程治理增强：
  - 在 `experiment-notes.md` 增加“版本基线门禁”强制规则；
  - 明确要求正文、技巧文档、skill 文档都执行同一基线读取流程。

## 新增审计回合：v11 -> v12（术语统一与分层发布）

- 审计输入要点：
  - 术语轻微漂移：标题“专家评审系统”与正文“专家论坛”并存；
  - 发布叙事与执行字段仍有混写；
  - 指标缺采样口径；
  - 正文信息量偏紧凑。
- v12 修复动作：
  - 主称谓统一为“专家论坛”；
  - 字段级门禁下沉为执行附录，主稿保持叙述连续性；
  - 新增指标采样口径表（对象/样本量/周期/阈值）；
  - 扩写机制解释段，提升信息密度。

## 结论收敛记录

- 共识：v7 的结构不需要重做，但必须补“读者契约 + 反例压力 + 证据梯度”。
- 分歧：是否在 v8 引入量化指标（如阅读时长、返工率）作为正文内容。
- 需后续验证项：你是否希望 v8 更“工程化”还是更“刊载化”。

## 用户评判与确认

- 评判人：你
- 评判结论（`approved` / `changes_requested`）：pending
- 评判意见摘要：待你确认是否按本 deep dive 技巧进入 `v8` 改写
- 回填要求：确认后更新 `user_review_status` 并记录你偏好的风格侧重。
