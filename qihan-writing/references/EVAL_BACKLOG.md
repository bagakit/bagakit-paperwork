# Evaluation Backlog

这里记录 `qihan-writing` 还没有完全进入自动验证、但已经足够明确、应该逐步变成 eval 的能力。

## 1. Full-Document Propagation After User Rewrite

### 为什么要测

这是当前最值得做成 eval 的规则之一。

用户不应该反复提醒：

- “全文也照最近新增的经验 review 了吗？”
- “是不是只改了我指出的这一句？”

理想状态应该是：

- 用户只给一句改写
- skill 自动抽规则
- 正在写的文章也自动按这条新经验做全文回扫

如果做不到这一点，skill 还停留在“局部补丁”，没有真正进入高质量写作协同。

### Failure Mode

- 用户给出一句高信号改写
- agent 只替换命中的一句
- 正文中其他同类句式、同类黑话、同类叙事误位保持不变

### 目标行为

用户只要提供改写，skill 就应该自动完成三件事：

1. 记录原句和改写句
2. 抽出项目无关规则
3. 回扫当前文稿里的同类问题

### Eval 设计思路

#### Fixture

准备一个短文档，其中同一类问题至少出现 3 次。

例如：

- 三处“我觉得 / 我认为”缓冲句
- 三处分号硬切句
- 三处黑话动词
- 三处“只写约束不写机会”的机制句

#### User Input

只提供其中一处的改写。

#### Pass 条件

1. 命中句被改
2. 其余同类句至少有 1-2 处也被一并改掉
3. 最终总结里明确说明“已按这条经验回扫全文同类问题”

#### Fail 条件

1. 只改命中句
2. 回答里没有提到全文回扫
3. 同类问题仍原样保留

### 可行的评测类型

- 近端可做：
  - 基于 before/after diff 的人工或 LLM judge 评测
- 下一步可做：
  - 对固定 fixture 做 `invoke_skill_judge`
  - 检查是否存在同类残留 pattern

## 2. Insight Interview Loop Quality

### 为什么要测

问答环如果设计得弱，用户不会愿意答，也不会暴露真正的判断。

### Failure Mode

- 问题太像空问卷
- 默认答案太弱
- 用户回答后，agent 只复述，没有深推

### 目标行为

一次好的问答环，至少要能：

1. 降低用户回答门槛
2. 帮用户暴露真实判断和风格
3. 产出可直接带回主稿的强句
4. 让主稿真的变深

### Eval 设计思路

#### Fixture

- 一组材料
- 一版偏平的初稿

#### Pass 条件

1. 生成的问题有默认答案
2. 用户只部分回答，agent仍能提炼出更高命题
3. 改稿后能看出主轴被抬高，而不是只补材料

## 3. Casebook-to-Reference Promotion

### 为什么要测

如果用户连续给出同类改写，而 skill 没有把它提升到 reference，就说明 evolve 还停在人工记忆层。

### Failure Mode

- 同类规则出现多次
- 但 reference / casebook / evolve log 没更新

### 目标行为

重复出现两次以上的模式，应被提升到：

1. `VOICE.md` / `POV_FIRST_PERSON.md` / `AI_SMELLS.md`
2. `REWRITE_CASEBOOK.md`
3. `EVOLVE_LOG.md`

## 4. Sample Frame Consistency & Evidence Portability

### 为什么要测

综述/总结类文稿一旦开始声明样本 frame、附录表和证据链接，读者就会把它当成轻量研究文看。

这时候，如果：

- 样本口径前后不一致
- 缺失样本边界没写清
- 证据链接离开当前机器就失效

整篇文章的可信度会明显下降。

### Failure Mode

- 正文说纳入 `N` 条样本，附录表格数量对不上
- 写了“未纳入”，但没说明是否影响结论
- 用 `/Users/...` 这种本机绝对路径当证据锚点

### 目标行为

1. 样本总数、类型拆分、inventory 前后一致
2. 缺失样本是否随机、能否外推要写清楚
3. 链接形式和目标读者匹配
   - 本地 scratch 可接受相对路径
   - 可转发文档优先 wiki URL / 引用编号

### Eval 设计思路

#### Fixture

- 一篇带正文 + 附录的 synthesis 文稿
- 人工注入几种错误：
  - 样本总数不一致
  - 缺失样本只提一句
  - 使用本机绝对路径

#### Pass 条件

1. agent 能指出口径不一致
2. agent 会要求写清缺失样本边界
3. agent 会根据读者场景调整链接层

## 当前判断

这四个方向里，`Full-Document Propagation After User Rewrite` 最值得优先做成 eval。

因为它直接决定了 skill 究竟是在“帮用户修一句”，还是在“真正吸收反馈并让全文一起变好”。
