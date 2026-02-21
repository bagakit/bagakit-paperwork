---
version: v7
based_on: v6
status: for_user_review
thinking_model_used:
  - hierarchical_pyramid_structure
  - reader_question_headings
  - bullet_paragraph_hard_rules
techniques_added:
  - synthesized_playbook_driven_rewrite
  - stronger_heading_specificity
  - denser_case_signal_pairs
  - clearer_causal_bridges
techniques_removed_or_tightened:
  - reduced_generic_section_labels
  - reduced_list_overuse_for_causal_content
  - tightened_claim_to_signal_mapping
quality_target: anthropic_engineering_style_like
---

# Brainstorm 的自解释系统与专家论坛评审系统

> Coding 的尽头是项目管理

## 一、讨论为什么总在交接时失效

### 1) 一个你很可能见过的交接错位

周一会上，A 说“先把结构打稳，再润色表达”。周三 B 接手时，只记住了“文章要更好看”，于是先改句子。两个人都在认真推进，但下周复盘时发现：结构没定，润色也要重做。

这个错位的核心不在能力，而在接口。结论没有被写成可接手、可验证的交接信息。

### 2) 三个高频失效点（这里用分点，因为三条彼此独立）

- 结构漂移：同一阶段反复改名，历史产物无法直接继承。
- 证据漂移：结论先行、证据后补，结论强度无法复核。
- 完成态漂移：讨论结束被当成任务完成，但 handoff 去向缺失。

### 3) 这类失效为什么会反复出现

因为团队在“讨论层”达成了共识感，却没有在“执行层”形成接口定义。只要“谁接、接什么、凭什么接”三件事不落在文档里，下一轮就会重复上一轮。

## 二、内容应该怎么组织，读者才不会迷路

### 1) 哪些信息该写成段落

凡是需要说明因果关系的内容，都应写成段落。

例如“为什么先证据后结论”：先结论后证据会诱发选择性佐证；先证据后结论会把反例提前暴露。这里有明确因果链，如果改成分点，逻辑会断。

### 2) 哪些信息适合分点

凡是并列、独立、可单条验收的信息，应该分点。

例如完成态检查就适合分点：
- frontmatter 写明结论与关键洞察；
- 用户评判状态已回填；
- action/memory handoff 路径明确；
- archive 证据可追溯。

每条都可以单独检查，所以分点更高效。

### 3) 四个文件如何分工（职责用分点，关系用段落）

- `input_and_qa.md`：定边界与澄清。
- `finding_and_analyze.md`：定选项与权衡。
- `expert_forum.md`：定争议与证据。
- `outcome_and_handoff.md`：定去向与责任。

它们不是模板装饰，而是决策链上的四个断点补丁。少一个，都可能回到“口头共识 + 人脑补全”。

## 三、如何把“说得通”变成“做得到”

### 1) 论坛收敛靠顺序，不靠气势

`lightning_talk_forum` 的关键顺序是：先证据、后观点；先交叉评分、后结论。这样能把“谁更会说”转成“谁的证据更稳”。

本轮实际做法是：结构专家给标题与层级约束，叙事专家给转折与句法约束，红队专家把“用户评判”拉入硬门禁。三条约束先独立，再合并。

### 2) MVP 必须同时过两道门

很多讨论在“观点听起来成立”就停下，但执行失败往往出在工具不可用。

所以 MVP 必须同时回答：
- 观点是否成立；
- 工具是否可用。

本轮对应信号：改稿能否把问题-机制-执行链写清；检查脚本能否复现并证明源文未改。

### 3) 一个最小 before/after

Before：
- “这篇写得不够好，大家再润一下。”

After：
- 问题定义：标题平铺，读者无法定位主论点。  
- 改动规则：H2 保持 3~5 块，H3 承担诊断/机制/信号。  
- 验证信号：结构检查通过，用户评判状态可追踪，handoff 路径可定位。

这就是“意见”与“接口”的区别。

## 四、怎么落地，才不会又回到旧问题

### 1) 上线顺序

先稳接口，再扩能力：
1. 固定文件契约；
2. 固定论坛门禁；
3. 固定实验隔离与归档格式；
4. 最后扩文体 profile。

顺序反过来，流程会更重，但错误不会更少。

### 2) 边界与降级策略

对高创意、弱验证任务，可以把部分规则降级为建议项。

但只要任务进入多人执行链路，三项硬约束不建议降级：证据顺序、评判状态、handoff 去向。

### 3) 下一步

下一步先做两个小而硬的增量：
- 统一“观点成立/工具可用”实验报告模板；
- 按 `bagakit-paperwork-xxx` 扩展文体 profile（blog、RFC、postmortem）。

## 结语

代码解决局部正确性，项目管理解决持续正确性。

当任务跨会话、跨角色推进时，真正决定上限的，不是一次写得多漂亮，而是内容能否被稳定接手、验证并执行。
