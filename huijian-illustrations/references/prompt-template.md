# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## Prompt 固定段落

### Character Block

灰见是“逸见 EyeSight”的固定虚拟形象，一个冷淡、理性、专业、略带毒舌的分析型角色。外形为黑色蓬松乱发、细框圆眼镜、半垂冷眼、灰白色简化长方形身体、细长四肢、小黑手小黑脚。胸口固定有两个小黑三角领口，中间一颗小小的橙红色观察点，作为稳定识别标志。画风是轻手绘、细线、简笔、略带随手感的人物风格，有一点人味，不要过于工整和工业化。可以加入少量克制的平涂上色增强识别度，但绝不萌化。角色常见动作包括审视、质疑、批注、分析、思考、录音/收集。整体应显得聪明、冷淡、克制、观察型，而不是可爱、治愈或热情。

### Visual DNA

Pure white background. Minimalist hand-drawn sketch style. Thin black lines, slightly loose and slightly wobbly, with a casual human hand-drawn feeling. Keep the drawing airy, simple, and clean. Use light gray as the base body color, black for hair and linework, and only a very small amount of restrained flat accent color for recognition, especially the tiny orange-red observation dot on the chest. The overall image should feel like a smart, cold, hand-drawn editorial sketch with a bit of human warmth, not a polished commercial illustration.

### English Character Prompt

Huijian is a simplified analyst character for the account “逸见 EyeSight”. He has messy fluffy black hair, thin round glasses, half-lidded skeptical eyes, a gray-white rectangular body, thin limbs, and small black hands and feet. On the upper chest, keep two small black triangular collar shapes with one tiny orange-red dot between them as a stable signature mark. Huijian should look rational, cold, observant, professional, and slightly sarcastic. Do not make the character cute, chibi, childish, overly cheerful, or mascot-like.

### Action Requirement

Huijian must perform the core action of the scene instead of merely decorating it. Preferred actions include examining details with a magnifying glass, questioning with a “证据呢？” sign, marking or editing with a red pen, analyzing structures or relationships on a board, thinking with one hand on the chin, and collecting information through a phone, microphone, or recording device. The action should be clear, readable, and directly support the main idea of the image.

### Chinese Annotation Requirement

Use only a small number of short handwritten Chinese annotations. Keep labels brief, readable, and sharp, usually 2-8 Chinese characters each. Good label styles include: “证据呢？”, “逻辑在哪？”, “谁在付钱”, “关系拆解”, “先看结构”, “这里不成立”, “看看细节”, “别被概念骗了”. Avoid long explanatory text.

### General Constraint

One image should explain only one core judgment, structure, state, or metaphor. Keep the composition clean and simple, with plenty of white space. Do not turn the image into a formal infographic, a PPT slide, a dense flowchart, or a polished commercial character poster. Do not add excessive text. Do not use realistic UI screenshots. Do not make Huijian cute or decorative. Huijian must remain the action-taking analytical subject of the image.

### Negative Constraints

Avoid cute expressions, chibi proportions, mascot styling, anime-style sweetness, exaggerated comedy faces, polished vector illustration, realistic portrait rendering, heavy shading, complex gradients, superhero chest emblems, and overly commercial branding aesthetics. Avoid making the character too cheerful, too soft, too childish, or too emotionally expressive.

## 单张生图模板

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Character:
灰见 is the fixed virtual character of “逸见 EyeSight”, a cold, rational, professional, slightly sarcastic analyst. He has messy fluffy black hair, thin round glasses, half-lidded skeptical eyes, a gray-white simplified rectangular body, thin limbs, and small black hands and feet. On the upper chest, always keep two small black triangular collar shapes with one tiny orange-red observation dot between them as a stable signature mark. The character should feel hand-drawn, light, simple, slightly casual, observant, and human, never cute or mascot-like.

Visual DNA:
Pure white background. Minimalist hand-drawn sketch style. Thin black lines, slightly loose and slightly wobbly, with a casual human hand-drawn feeling. Keep the drawing airy, simple, and clean. Use light gray as the base body color, black for hair and linework, and only a very small amount of restrained flat accent color for recognition, especially the tiny orange-red observation dot on the chest. Sparse red/orange/blue handwritten Chinese annotations are allowed only as functional notes.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜 / 剪辑台分析 / 证据链拆解 / 利益称量}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：灰见在哪里、正在做什么、主要物件是什么、信息如何流动}

Action:
Huijian must perform the core action of the scene instead of merely decorating it. Preferred actions include examining details with a magnifying glass, questioning with a “证据呢？” sign, marking or editing with a red pen, analyzing structures or relationships on a board, thinking with one hand on the chin, and collecting information through a phone, microphone, or recording device.

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for hair, glasses, linework, tools, text, small hands, small feet, and the two chest triangles. Light gray for Huijian's body. Tiny orange-red for the chest observation dot and occasional judgment marks. Orange for main flow/path/arrows. Red only for sharp comments, evidence questions, warnings, fake causality, risks, or key judgments. Blue only for secondary notes, system/tool state, context, waveforms, or analysis feedback.

Constraints:
One image explains only one core judgment, structure, state, or metaphor. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense flowchart, polished commercial character poster, realistic UI screenshot, or cute mascot illustration. Do not omit Huijian's messy black hair, thin round glasses, half-lidded cold eyes, gray-white rectangular body, thin limbs, small black hands and feet, two black triangular collar shapes, and tiny orange-red observation dot on the chest.
```

## 最实用组合 Prompt

```text
灰见是“逸见 EyeSight”的固定虚拟形象，一个冷淡、理性、专业、略带毒舌的分析型角色。外形为黑色蓬松乱发、细框圆眼镜、半垂冷眼、灰白色简化长方形身体、细长四肢、小黑手小黑脚。胸口固定有两个小黑三角领口，中间一颗小小的橙红色观察点，作为稳定识别标志。画风是轻手绘、细线、简笔、略带随手感的人物风格，有一点人味，不要过于工整和工业化。可以加入少量克制的平涂上色增强识别度，但绝不萌化。角色常见动作包括审视、质疑、批注、分析、思考、录音/收集。整体应显得聪明、冷淡、克制、观察型，而不是可爱、治愈或热情。

Pure white background. Minimalist hand-drawn sketch style. Thin black lines, slightly loose and slightly wobbly, with a casual human hand-drawn feeling. Keep the image airy, clean, and simple. Use light gray as the base body color, black for hair and linework, and only a tiny amount of restrained flat accent color, especially the small orange-red dot on the chest. Huijian must perform the core action, not just decorate the scene. Preferred actions include examining details, questioning with “证据呢？”, annotating with a red pen, analyzing structures, thinking, and collecting information. Use only a few short handwritten Chinese labels. Avoid cute styling, mascot vibes, polished commercial illustration, realistic UI, dense explanatory text, or overly cheerful expressions.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强灰见参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 灰见 more central to the conceptual judgment or operation. 灰见 should be doing the cold analytical work that explains the idea, not standing beside the diagram. Keep messy fluffy black hair, thin round glasses, half-lidded cold eyes, gray-white rectangular body, thin limbs, small black hands and feet, two black triangular collar shapes, one tiny orange-red chest dot, sparse handwritten Chinese annotations, pure white background, and clean hand-drawn style.
```
