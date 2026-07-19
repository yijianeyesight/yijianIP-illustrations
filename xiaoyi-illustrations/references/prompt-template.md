# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## Prompt 固定段落

### Character Block

小逸是“逸见 EyeSight”的固定虚拟形象，一个冷淡、理性、专业、略带毒舌的分析型角色。外形为黑色蓬松乱发、细框圆眼镜、半垂冷眼与成熟清秀的简化人物比例。上胸口领口位置固定有两个小黑三角领口，中间一颗小小的橙红色观察点。两个黑三角左右对称，橙红点固定在两个三角之间，不能漂到身体中部或画面正中。人物必须保持成熟好看；儿童感只用于不平直、不完美的自由手绘线条。角色常见动作包括审视、质疑、批注、分析、思考、录音/收集。整体应显得聪明、冷淡、克制、观察型，而不是可爱、治愈或热情。

### Visual DNA

Cold editorial illustration made from hand-drawn newspaper cut-outs. Use naive, freely drawn black pen lines: straight edges are subtly crooked, circles imperfect, contours gently wobble, some strokes overshoot corners, and a few lines are lightly retraced. Only the line behavior is childlike; Xiaoyi remains mature, handsome and analytical. Xiaoyi and every major object visibly look cut from old newspaper, each with a narrow irregular off-white scissor-cut rim, paper fibers, halftone dots, faded column fragments and overlapping pasted edges. Black and gray remain dominant; use only about 15% pale gray-blue and rust-orange color. Place the complete collage on a perfectly uniform #00FF00 chroma-key background for local removal.

### English Character Prompt

Xiaoyi is a simplified analyst character for “逸见 EyeSight”. He has messy fluffy black hair, thin round glasses, half-lidded skeptical eyes, and mature, handsome, simplified human proportions. At the upper-chest collar position, keep two small black triangular collar shapes with one tiny orange-red observation dot exactly between them. This mark must stay near the collar, not in the torso center, belly, face or canvas center. Xiaoyi should look rational, cold, observant, professional and slightly sarcastic. Only the freehand line behavior may feel childlike; never make the character cute, chibi, juvenile or mascot-like.

### Action Requirement

Xiaoyi must perform the core action of the scene instead of merely decorating it. Preferred actions include examining details with a magnifying glass, questioning with a “证据呢？” sign, marking or editing with a red pen, analyzing structures or relationships on a board, thinking with one hand on the chin, and collecting information through a phone, microphone, or recording device. The action should be clear, readable, and directly support the main idea of the image.

### Chinese Annotation Requirement

Use only a small number of short handwritten Chinese annotations. Keep labels brief, readable, and sharp, usually 2-8 Chinese characters each. Good label styles include: “证据呢？”, “逻辑在哪？”, “谁在付钱”, “关系拆解”, “先看结构”, “这里不成立”, “看看细节”, “别被概念骗了”. Avoid long explanatory text.

### General Constraint

One image should explain only one core judgment, structure, state, or metaphor. Keep the composition clean and simple, with plenty of white space. Do not turn the image into a formal infographic, a PPT slide, a dense flowchart, or a polished commercial character poster. Do not add excessive text. Do not use realistic UI screenshots. Do not make Xiaoyi cute or decorative. Xiaoyi must remain the action-taking analytical subject of the image.

For video-editing flexibility, if multiple subjects have only a weak conceptual relationship, keep them fully separated as independent cut-out elements. Do not force connector lines, shared backing plates, touching edges, shadows, or decorative overlaps. Preserve necessary physical or causal connections only when the scene genuinely requires them. Each separable element should have a complete visible silhouette.

### Negative Constraints

Avoid cute expressions, chibi proportions, mascot styling, anime-style sweetness, exaggerated comedy faces, polished vector illustration, realistic portrait rendering, heavy shading, complex gradients, superhero chest emblems, and overly commercial branding aesthetics. Avoid making the character too cheerful, too soft, too childish, or too emotionally expressive.

## 单张生图模板

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Character:
小逸 is the fixed virtual character of “逸见 EyeSight”, a cold, rational, professional, slightly sarcastic analyst. He has messy fluffy black hair, thin round glasses, half-lidded skeptical eyes, a gray-white simplified rectangular body, thin limbs, and small black hands and feet. Directly below the top edge of the rectangular body, at the upper-chest collar position, always keep two small black triangular collar shapes, left and right of the body centerline, with one tiny orange-red observation dot exactly between them. The dot must stay near the collar, not in the center of the torso or canvas. The character should feel hand-drawn, light, simple, slightly casual, observant, and human, never cute or mascot-like.

Visual DNA:
Perfectly uniform flat #00FF00 chroma-key outer background, with no texture, shadow, gradient or lighting variation. The foreground is a cold editorial collage made from hand-drawn newspaper cut-outs. Lines should look freely drawn by hand: subtly crooked straight edges, imperfect circles, gentle wobble, occasional overshoot, broken contours and light retracing. Only the line quality is childlike; keep Xiaoyi mature and handsome. Give Xiaoyi and every major object a narrow irregular off-white hand-cut paper rim, visible paper fibers, halftone dots, faded newspaper fragments and overlapping pasted edges. Keep black/grayscale dominant and color coverage around 15%: desaturated gray-blue planes plus sparse rust-orange accents. Do not use #00FF00 inside the subject.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜 / 剪辑台分析 / 证据链拆解 / 利益称量}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：小逸在哪里、正在做什么、主要物件是什么、信息如何流动}

Action:
Xiaoyi must perform the core action of the scene instead of merely decorating it. Preferred actions include examining details with a magnifying glass, questioning with a “证据呢？” sign, marking or editing with a red pen, analyzing structures or relationships on a board, thinking with one hand on the chin, and collecting information through a phone, microphone, or recording device.

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Keep black, charcoal, gray and off-white as 85% of the visual impression. Use pale desaturated gray-blue on selected machine, clothing, route or paper planes, and sparse rust-orange on the observation dot, key judgment, risk or valuable result. Total colored area should remain around 15%. No full-color rendering.

Transparent-output constraints:
The #00FF00 background is temporary and will be removed locally. Preserve every off-white cut-paper rim as opaque foreground. No green inside the subject, no cast shadow, no contact shadow. After generation, follow references/transparent-output.md and run scripts/remove_chroma_key.py to deliver an RGBA PNG.

Constraints:
One image explains only one core judgment, structure, state, or metaphor. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense flowchart, polished commercial character poster, realistic UI screenshot, or cute mascot illustration. Do not omit Xiaoyi's messy black hair, thin round glasses, half-lidded cold eyes, gray-white rectangular body, thin limbs, small black hands and feet, two black triangular collar shapes, and tiny orange-red observation dot. Keep the collar mark fixed directly under the body's top edge: two black triangles around the centerline, tiny orange-red dot between them. Never move the dot to the torso center, belly, face, or canvas center.
```

## 最实用组合 Prompt

```text
小逸是“逸见 EyeSight”的固定虚拟形象，一个冷淡、理性、专业、略带毒舌的分析型角色。外形为黑色蓬松乱发、细框圆眼镜、半垂冷眼与成熟清秀的简化人物比例。上胸口领口位置固定有两个小黑三角领口，中间一颗小小的橙红色观察点。人物必须保持成熟好看；儿童感只用于不平直、不完美的自由手绘线条，绝不萌化或幼儿化。

Use a perfectly uniform #00FF00 chroma-key outer background. Build the foreground as cold editorial newspaper cut-outs: Xiaoyi and each major object have narrow irregular off-white scissor-cut rims, paper fibers, halftone dots and overlapping pasted edges. Draw with naive freehand black pen lines: subtly crooked straight edges, imperfect circles, gentle wobble, occasional overshoot and retracing. Only the line quality is childlike; Xiaoyi remains mature, handsome and analytical. Keep black/grayscale dominant, with about 15% pale gray-blue and sparse rust-orange. Preserve all off-white cut-paper rims for local background removal. Xiaoyi must perform the core action, not decorate the scene. Avoid cute styling, polished manga lines, mascot vibes, full-color rendering, dense text or PPT composition.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强小逸参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 小逸 more central to the conceptual judgment or operation. 小逸 should be doing the cold analytical work that explains the idea, not standing beside the diagram. Keep messy fluffy black hair, thin round glasses, half-lidded cold eyes, gray-white rectangular body, thin limbs, small black hands and feet, two black triangular collar shapes directly below the body top edge, one tiny orange-red dot exactly between the two triangles, sparse handwritten Chinese annotations, pure white background, and clean hand-drawn style. Do not move the orange-red dot to the torso center, belly, face, or canvas center.
```
