# Xiaoyi Illustrations

> 把中文内容里的关键判断、结构漏洞、利益关系和认知动作，变成一张张稚拙手绘、报纸剪纸、冷幽默但成熟的透明正文配图。
>
> 16:9 横版 | 小逸 IP | 报纸剪纸 | 约 15% 铁锈橙 × 灰蓝轻彩 | #00FF00 绿幕转透明 PNG | Codex Skill

---

## 这个仓库是什么

Xiaoyi Illustrations 是一个深度定制的 Codex Skill，方法来自Ian Xiaohei Illustrations

用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档、方法论内容、社会观察、经济分析、AI 科普、自媒体分析和商业拆解生成正文配图。

它不是通用插画 prompt，也不是 PPT 信息图模板。它的核心目标是：先理解内容里的认知锚点，再把其中一个关键判断、结构漏洞、利益关系或认知动作，变成一张有记忆点的 16:9 手绘解释图。

默认视觉 IP 是“小逸”：一个黑色蓬松乱发、细框圆眼镜、半垂冷眼、成熟清秀简化比例的冷脸分析员。上胸口领口位置固定有两个小黑三角领口和一颗很小的橙红观察点，作为稳定识别标志。

一句话：**让 AI 不只是“配一张图”，而是把内容里的一个关键判断、结构漏洞、利益关系或认知动作画出来。**

---

## 适合谁用

特别适合：

- 写中文文章，需要正文配图和文章插图的人
- 做社会观察、经济分析、AI 科普、自媒体分析、商业拆解和方法论内容的人
- 想把抽象判断画成具体隐喻的人
- 想要一种比 PPT 信息图更轻、更怪、更有个人识别度的配图风格的人
- 用 Codex 做内容生产，希望稳定复用一套视觉语言的人

不适合：

- 想要商业插画、品牌 KV 或精致扁平插画的人
- 想要传统 PPT 信息图、复杂架构图或正式流程图的人
- 想要儿童卡通、可爱 IP、日系萌角色或表情包风格的人
- 想把大量正文、长段解释或完整课程页塞进一张图里的人
- 需要严格可编辑矢量源文件的人

---

## 它会产出什么

默认输出：

- 16:9 横版正文配图
- 一篇文章的 4-8 张 shot list
- 每张图的主题、核心意思、结构类型、小逸动作和中文标注建议
- 最终 RGBA 透明 PNG 与可复用的 `#00FF00` 绿幕源图，保存到 workspace 的 `assets/<article-slug>-illustrations/`

默认不输出：

- PPTX / PDF / Keynote
- SVG / HTML / Canvas 可编辑图
- 商业海报或封面 KV
- 大段文字型信息图
- 精致商业插画
- 真实 UI 截图

---

## 视觉风格

这个 skill 默认使用“小逸冷感编辑剪纸”风格：

- 人物保持成熟、清秀；“儿童感”只来自不平直、不完美的自由手绘线条
- 直线轻微歪斜，圆形不绝对规整，允许少量断线、复线和越过拐角
- 人物和主要物件像从旧报纸剪下，保留不规则米白剪口、纸纤维、网点与叠贴边缘
- 黑灰米白约占 85%，铁锈橙与低饱和灰蓝轻彩约占 15%
- 身体顶边下方的上胸口领口位置保留两个小黑三角领口和一颗很小的橙红观察点
- 生图使用统一 `#00FF00` 绿幕，本地抠除后交付透明 PNG
- 默认不写标题；确需标注时保持极少、极短
- 一张图只表达一个核心动作、结构、状态或隐喻
- 小逸必须参与核心判断或操作动作，不能只是装饰
- 怪诞、聪明、冷淡、轻微毒舌，但不幼稚、不卖萌

---

## 参考素材

小逸角色参考图：

- `assets/xiaoyi-reference/xiaoyi-turnaround.png`：三视图参考，包含正面、侧面、背面和头像近景。
- `assets/xiaoyi-reference/xiaoyi-modes.png`：模式参考，包含批注模式、质问模式、录音模式、分析模式、辩证模式。

示例图片只用于校准线条密度、留白、颜色克制和角色参与方式，不是构图模板。使用时应该从当前文章重新发明隐喻，不要照抄旧案例的物件和构图。

---

## 安装

复制 skill 到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./xiaoyi-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，在 Codex 里使用：

```text
Use $xiaoyi-illustrations 为这篇中文文章设计并生成 5 张小逸冷脸正文配图。
```

---

## 怎么用

### 只做配图规划

```text
Use $xiaoyi-illustrations 先不要生图。
请分析下面这篇文章哪里值得配图，输出 5 张左右的 shot list。
每张图写清楚：放在哪段后、主题、核心意思、结构类型、小逸在做什么、建议中文标注词。

<粘贴文章>
```

### 直接生成正文配图

```text
Use $xiaoyi-illustrations 把下面这篇文章生成 4 张小逸冷脸正文配图。
要求：16:9 横版、稚拙不平直的黑色手绘线、报纸剪纸白边、约 15% 铁锈橙与灰蓝轻彩，最终交付透明 PNG。

<粘贴文章>
```

### 为单个概念生成一张图

```text
Use $xiaoyi-illustrations 为“信任不是喊出来的，而是一块证据一块证据铺过去”生成一张正文配图。
画面要怪诞但清爽，小逸必须承担核心判断或操作动作。
```

### 去掉图里的标题或错误文字

```text
Use $xiaoyi-illustrations 帮我编辑这张图，去掉左上角的“流程图”标题，其他内容保持不变。
```

更多示例见 [examples/prompts.md](examples/prompts.md)。

---

## 工作流程

这个 skill 的流程是：

1. 读取文章、Markdown、Notion 内容、截图或用户给的主题
2. 提炼核心观点、认知转折、流程结构和适合视觉化的段落
3. 先输出 shot list：每张图只选一个认知锚点
4. 为每张图选择结构类型：Workflow、系统局部、前后对比、角色状态、概念隐喻、方法分层、地图路线、小漫画分镜、剪辑台分析、证据链拆解或利益称量
5. 重新发明一个低科技、怪诞但成立的物理隐喻
6. 让小逸承担核心判断或操作动作
7. 每张图单独调用图像模型生成
8. 在统一 `#00FF00` 绿幕上生成，保留人物与物件的米白剪纸边
9. 本地抠除绿幕，检查透明通道、绿边、剪纸边、小逸动作、非 PPT 感和非旧案例复刻
10. 同时保存绿幕源图与透明 PNG，并报告用途和路径

---

## 目录结构

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── XIAOYI_AVATAR_BRIEF.md
├── assets/
│   └── xiaoyi-reference/
│       ├── xiaoyi-turnaround.png
│       └── xiaoyi-modes.png
├── examples/
│   ├── images/
│   └── prompts.md
└── xiaoyi-illustrations/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   ├── examples/
    │   └── xiaoyi-reference/
    ├── references/
        ├── style-dna.md
        ├── xiaoyi-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        ├── qa-checklist.md
        └── transparent-output.md
    └── scripts/
        └── remove_chroma_key.py
```

真正需要安装到 Codex 的是子目录：

```text
xiaoyi-illustrations/
```

根目录的 README、LICENSE、NOTICE、brief 和 examples 是 GitHub 分享文档。

---

## 注意事项

- 图片里的中文文字越短越稳定。
- 每张图只讲一个核心结构，不要把文章做成说明书。
- 小逸必须承担核心判断或操作动作；如果去掉小逸画面仍然完全成立，说明小逸太装饰了。
- 参考图只用于校准人物一致性、线条密度、留白和颜色克制，不要复刻构图。
- 固定绿幕色号是 `#00FF00`，不要为不同图片随意更换色号。
- 透明化默认使用 `xiaoyi-illustrations/scripts/remove_chroma_key.py`；优先 `--despill`，只有细绿边残留时才加 `--edge-contract 1`。
- AI 图像模型可能出现错字、幻觉标签、风格漂移或多余标题，生成后需要检查。
- 如果中文错字严重，优先减少标注词并重生成。

---

## Attribution

This project is adapted from Ian Xiaohei Illustrations by Ian. See [NOTICE.md](NOTICE.md) for attribution details.

---

## License

MIT License. See [LICENSE](LICENSE).
