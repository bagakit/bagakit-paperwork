---
version: v1
based_on: source-copy
status: baseline
techniques_added:
  - problem_first_opening
  - state_vs_execution_distinction
  - quick_review_sectioning
techniques_removed_or_tightened:
  - none
known_gaps:
  - failure_modes_not_explicit
  - decomposition_sentence_weak
  - transition_density_low
---

# Brainstorm 的自解释系统与专家论坛评审系统

> Coding 的尽头是项目管理

## 问题不是“写不出想法”，而是“想法无法接力”

多数团队并不缺 brainstorm。缺的是可持续决策系统：
- 讨论结束后，结论无法复用；
- 下一轮会议重新解释同一问题；
- 产物存在，但责任和去向不清晰。

当工程进入跨会话、跨角色协作阶段，失败往往不是代码层面，而是管理层面的信息失真。所谓“写作质量差”，经常只是“决策结构不稳定”的外在表现。

## 系统目标：把讨论变成可验证交接

一个可运行的 brainstorm 系统至少要同时满足四个条件：
1. 可继承：不同轮次能沿用同一上下文，而不是重建背景。
2. 可收敛：争议在同一个场域收敛，而不是旁路决策。
3. 可验证：结论有证据与实验，不是语气更强就算赢。
4. 可交接：结束意味着可执行，而不是“看起来像结束”。

这四点不是文档偏好，而是工程约束。

## 机制设计：四个文件对应四个职责

- `input_and_qa.md`：定义边界与澄清，解决“问题到底是什么”。
- `finding_and_analyze.md`：管理选项与权衡，解决“为什么选这个”。
- `expert_forum.md`：集中争议与证据，解决“凭什么信这个”。
- `outcome_and_handoff.md`：定义去向与责任，解决“接下来谁做什么”。

文件自解释，协作才不会依赖个人记忆。

## 论坛不是形式，而是收敛装置

专家论坛的目的不是增加仪式感，而是压缩决策噪声：
- 先证据，再观点；
- 先交叉评分，再收敛结论；
- 对可实验的问题，优先做最小 MVP。

MVP 的价值不在“做大”，而在快速回答两个问题：
- 观点是否成立；
- 工具是否可用。

## 完成定义：讨论结束不等于任务完成

真正的完成态应满足：
- 关键结论已写入 frontmatter 并可检索；
- `discussion_clear` 与用户评判状态明确；
- handoff 目标可定位，归档证据可追踪。

如果这三项缺一，系统就还在“讨论态”，不在“执行态”。

## 结语

代码解决局部正确性，项目管理解决持续正确性。

当任务简单时，代码能力决定速度；当任务复杂时，管理能力决定上限。所谓“Coding 的尽头是项目管理”，本质上是在说：系统化协作，才是复杂工程的生产力核心。
