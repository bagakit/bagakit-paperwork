---
version: v4
based_on: v3
status: for_user_review
thinking_model_used:
  - scqa_opening_arc
  - pyramid_argument_order
  - mece_section_partition
techniques_added:
  - explicit_outline_first_workflow
  - section_question_driven_headings
  - claim_mechanism_evidence_triplet
  - stronger_bridge_sentences_between_sections
techniques_removed_or_tightened:
  - reduced_section_shape_variance
  - tightened_para_scope_to_one_question
  - reduced_unanchored_assertions
quality_target: anthropic_engineering_style_like
---

# Brainstorm 的自解释系统与专家论坛评审系统

> Coding 的尽头是项目管理

## 为什么这个问题现在必须解决

当项目进入跨会话、跨角色协作阶段，brainstorm 的主要风险不再是“缺想法”，而是“想法无法接力”。

讨论现场通常看起来完整，但执行阶段经常暴露断点：新成员无法判断哪些结论已闭环、哪些假设仍待验证、哪些争议只是被暂时搁置。结果是重复讨论、重复决策、重复返工。

这不是表达问题。它是系统问题。

## 失败通常发生在哪三个位置

第一，结构漂移：每轮都换一套阶段命名，历史记录失去可继承性。  
第二，证据漂移：结论先确定，证据后补写，导致结论强度不可审计。  
第三，完成态漂移：讨论结束被当作任务完成，但 handoff 去向并不明确。

这三类失败有同一个根因：决策接口不稳定。

## 一个可用答案：把讨论系统化为可验证交接

如果目标是持续交付，而不是单轮讨论效果，brainstorm 必须从“观点容器”升级为“决策基础设施”。

这个基础设施至少要同时满足四个条件：可继承、可收敛、可验证、可交接。它们分别回答四个问题：信息是否能沿用、争议是否能关闭、结论是否可信、结果是否可执行。

## 系统应该由四个职责清晰的模块组成

`input_and_qa.md` 负责边界与澄清，确保问题定义稳定。  
`finding_and_analyze.md` 负责选项与权衡，确保决策路径可解释。  
`expert_forum.md` 负责争议与证据，确保收敛过程可复核。  
`outcome_and_handoff.md` 负责去向与责任，确保结论进入执行链路。

模块命名必须脱离上下文仍可解释。否则协作会重新依赖个人口头记忆。

## 争议如何收敛，决定系统是否可靠

收敛不是“把话说完”，而是“把分歧关进同一个可审计场域”。

实践上，关键分歧只在 `expert_forum.md` 关闭。流程顺序固定为：先证据、后观点；先交叉评分、后结论。对于开放议题，`lightning_talk_forum` 先快速覆盖，再决定是否进入 deep-dive，通常比一开始全量深挖更有效率。

## 为什么 MVP 要同时验证观点和工具

没有实验的讨论，很容易退化为修辞竞争。

最小 MVP 的作用是回答两个不同维度的问题：观点是否成立，工具是否可用。只有两者都通过，结论才具备执行价值。为保证结果可信，实验改动必须隔离在 `experimental/` 目录内，源文保持不可变。

这条约束不是流程洁癖。它是证据可信度的底线。

## 完成态必须写成执行接口

“讨论完成”不等于“任务完成”。

一个执行就绪的完成态至少包含三项证据：结论可检索、评审状态明确、handoff 去向可追踪。缺少任意一项，都应判定为仍在讨论态。把用户评判作为硬门禁，目的正是避免“代理自洽完成”绕过真实共识。

## 落地顺序决定成本，不是细节

先稳定文件契约，再稳定论坛门禁，最后引入实验和归档约束。这一顺序的意义在于：先解决可继承性，再提升表达上限。

如果顺序反过来，团队常会在“看起来更完整”的流程里反复掉进基础问题。

## 边界与下一步

这套机制主要服务技术决策与工程写作。对于强创意、弱验证任务，部分规则应降级为指导性策略。

下一步建议两件事：统一“观点成立/工具可用”的实验报告格式；在不破坏核心契约前提下扩展文体 profile（blog、RFC、postmortem）。

## 结语

代码解决局部正确性，项目管理解决持续正确性。

当任务跨越多个会话与角色时，真正决定上限的不是单次写得多好，而是系统能否稳定保存、验证并交接决策。
