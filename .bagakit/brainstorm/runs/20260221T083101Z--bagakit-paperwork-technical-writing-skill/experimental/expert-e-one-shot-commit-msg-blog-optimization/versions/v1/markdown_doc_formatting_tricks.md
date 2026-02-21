# Markdown 与文档格式实战技巧（GitHub + Mermaid）

这份文档聚焦“写完就能用”的格式技巧，目标是减少渲染歧义、降低评审沟通成本，并让文档在 GitHub 场景下保持稳定可读。

## 1) Mermaid 节点换行：先分清字符串类型

这是最容易踩坑的一条。  
在 Mermaid **传统字符串**里，节点内换行通常依赖 `<br>` 标签；在 Mermaid **Markdown strings** 里，官方说明可以直接使用换行字符，并且会自动换行。

实务建议：
- 如果你不确定当前图是否启用了 Markdown strings，优先使用 `<br/>`，兼容性更稳。
- 如果你明确使用 Markdown strings，可以直接换行并利用自动换行能力。

## 2) Mermaid 文本过长：优先用 Markdown strings，再决定是否手动断行

Flowchart 文档指出 Markdown strings 支持自动换行，且可通过配置关闭自动换行。  
这意味着你可以先用自动换行，只有在视觉控制要求较高时再手动加 `<br/>`。

## 3) Mermaid 的保留词与易错语法要主动规避

官方文档明确提到：在部分图里直接使用小写 `end` 可能导致解析异常。  
同时，连接语法里某些写法会被解释为特殊边（例如 `o` / `x` 相关）。  
建议在团队模板里写成“统一规避项”，不要等到渲染失败再查原因。

## 4) Markdown 文件里的换行，不等于 issue 评论里的换行

GitHub 文档场景有差异：
- 在 issue/PR/discussion 评论中，换行通常会自动渲染。
- 在 `.md` 文件中，普通换行通常会被当作软换行。

在 `.md` 文件里，需要显式硬换行时可用三种方式：
- 行尾两个空格
- 行尾反斜杠 `\`
- `<br/>`

## 5) 表格前保留空行，避免渲染歧义

GitHub 表格语法对前后文比较敏感。官方建议在表格前留空行。  
这个小动作能显著减少“本地看着像表格，线上却没渲染”的问题。

## 6) 代码块用围栏 + 语言标识，降低评审成本

围栏代码块（```）是基础，但语言标识（如 `bash`、`json`、`mermaid`）决定了可读性和扫描效率。  
对文档评审来说，这一步通常比“段落润色”更有收益。

## 7) 细节信息用 `<details>` 折叠，主线信息放正文

当文档既要给管理层看结论、又要给执行者看细节时，最稳的做法不是删细节，而是折叠细节。  
GitHub 官方支持 `<details><summary>...</summary>...</details>`，非常适合放“执行附录、字段清单、长日志”。

## 8) Mermaid 图和正文要分工，不要互相复读

经验上，图最适合表达三类信息：
- 依赖关系（架构图）
- 回退条件（流程图）
- 长期迭代（循环图）

正文负责解释“为什么这样设计”，图负责“结构一眼看懂”。  
如果图文都在讲同一句话，通常意味着信息冗余。

## 9) 技术文档里的“可执行约束”建议用表格承载

像门禁字段、指标口径、回退处理这类信息，用表格表达最稳定。  
段落适合论证，表格适合核对。两者分开后，阅读体验和执行效率都会提升。

## 10) 一条团队级规则：格式策略要写进基线，不靠个人习惯

最容易失控的不是某一处语法错误，而是团队成员各写各的。  
把以上规则写入版本基线（例如“新增版本前必读技巧文档”）后，文档质量会明显更稳定。

## 参考资料

- Mermaid Flowchart Syntax（Markdown strings / `<br>` / 自动换行）  
  [https://mermaid.js.org/syntax/flowchart.html](https://mermaid.js.org/syntax/flowchart.html)
- Mermaid Sequence Diagram（Line breaks）  
  [https://mermaid.js.org/syntax/sequenceDiagram.html](https://mermaid.js.org/syntax/sequenceDiagram.html)
- Mermaid Timeline（`<br>` 强制换行）  
  [https://mermaid.js.org/syntax/timeline.html](https://mermaid.js.org/syntax/timeline.html)
- GitHub Basic writing and formatting syntax（`.md` 换行规则）  
  [https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- GitHub Working with advanced formatting  
  [https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting](https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting)
- GitHub Tables  
  [https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)
- CommonMark Spec（Hard line breaks）  
  [https://spec.commonmark.org/0.29/](https://spec.commonmark.org/0.29/)
