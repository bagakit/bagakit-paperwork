# Version v10 Techniques Handbook

## 0) 本版目标

本版的目标不是“换一种好听说法”，而是系统性降低 AI 味。这里的 AI 味指的是：文本读起来正确、完整、礼貌，但缺少具体语境、责任主体和可复盘路径。

## 1) AI 味成因（基于检索结论）

### 1.1 风格同质化

多项研究发现，AI 文本在风格上更容易聚成一类，句式变化和个人笔触差异更小。结果是“每段都顺，但整篇像同一个模具”。  
来源：Nature 的风格计量研究与相关综述。

### 1.2 形式正确但语义抽象

AI 文本常见问题是名词化和抽象词偏多，动作对象偏少。读者会看到很多“优化、提升、机制”，但很难回答“谁在做、做什么、怎么验收”。

### 1.3 可读性与信息密度错配

在技术写作场景里，AI 文本常出现“句子通顺但有效信息密度偏低”或“结构完整但例子不足”的情况，导致阅读成本高于信息收益。

### 1.4 标题与段落过度模板化

当标题大量使用“问题/机制/策略/闭环”这类抽象类目词，读者需要先翻译标题再理解内容，扫描效率会明显下降。  
来源：Microsoft 与政府 Plain Language 指南都强调标题要具体、可独立理解。

### 1.5 责任主体缺失

过度被动语态或无主语表达，会让论证看起来客观，却无法执行。技术文章尤其需要写清“谁负责、何时判断、依据是什么”。  
来源：Digital.gov 与 Google Technical Writing 对主动语态和受众导向的建议。

## 2) 对应改写策略（从“症状”到“动作”）

### 2.1 术语收敛：从“概念堆叠”到“最小词表”

- 每篇先锁定 6~10 个核心术语。
- 同一概念不换叫法。
- 术语首次出现就给工作定义。

### 2.2 动词落地：从“抽象评价词”到“执行动词”

- 用 `定义/验证/回填/归档/复盘` 替代泛化词。
- 每个动作必须有对象和验收条件。

### 2.3 段落优先：从“全篇列表化”到“叙述主导，列表点缀”

- 正文以自然段为主，列表只用于并列且可单条验收的信息。
- 每个关键段落至少包含：判断句 + 证据锚点 + 下一步约束。

### 2.4 证据梯度：从“口号式结论”到“可复核链路”

- 固定链路：`现象 -> 机制 -> 最小实验/案例 -> 验证信号 -> 行动`。
- 不允许直接从现象跳到行动建议。

### 2.5 反例压力：从“单向宣讲”到“可证伪论证”

- 每个核心判断至少给一个失败路径。
- 同段写明：为何失败、如何修复、如何验收。

## 3) 图示策略（避免“图只是装饰”）

- 架构图：回答“哪些模块相互依赖”。
- 流程图：回答“执行顺序与回退条件”。
- 循环图：回答“系统如何长期运行”。

图后必须跟一段“读图说明”，把图中关系映射回正文判断。

## 4) v10 写作约束

- 禁用高口号密度表达（例如过度拟人化、机械化比喻）。
- 减少固定三段式口号句，增加具体场景和具体责任。
- 正文分点比例控制在低位，重点信息才列表化。
- 标题尽量写“读者问题句”，避免纯抽象类目词。

## 5) 快速质检清单

- [ ] 开篇是否写清“这篇帮谁解决什么问题”
- [ ] 是否出现“动作对象不明”的句子
- [ ] 是否存在“结论先行但无证据支撑”的段落
- [ ] 是否至少有一处反例与修复闭环
- [ ] 图示是否承担结构信息，而非重复正文
- [ ] 读者能否在 30 秒内说出文章核心判断与执行入口

## 6) 检索来源

- [Nature: Human and AI language can be differentiated by stylistic differences](https://www.nature.com/articles/s41599-025-04686-7)
- [Frontiers: Human-authored and AI-generated text styles across writing tasks](https://www.frontiersin.org/articles/10.3389/frai.2025.1628853/full)
- [arXiv: AI-generated Text Detection and Classification: A Survey](https://arxiv.org/abs/2504.13379)
- [Google Technical Writing: Audience](https://developers.google.com/tech-writing/one/audience)
- [Google Technical Writing: Active voice](https://developers.google.com/tech-writing/one/active-voice)
- [Digital.gov: Plain language](https://digital.gov/guides/plain-language/)
- [Microsoft Writing Style Guide: Headings](https://learn.microsoft.com/en-us/style-guide/scannable-content/headings)
