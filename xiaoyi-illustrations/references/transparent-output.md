# 透明 PNG 与固定绿幕流程

## 固定规范

- 绿幕色号：`#00FF00`（RGB `0, 255, 0`）。
- 绿幕只用于主体外部背景，必须完全均匀，不要纹理、阴影、渐变、地面、反射或光照变化。
- 人物、机器、纸张与其他物件的米白剪纸边属于主体，必须保持不透明。
- 主体内部禁止出现 `#00FF00` 或近似荧光绿色。
- 最终交付 PNG 必须为 `RGBA`，同时保留绿幕源图。

## 生图固定段落

```text
Place the complete newspaper cut-out collage on a perfectly uniform flat solid #00FF00 chroma-key background. The green background must have no texture, paper grain, shadow, gradient, lighting variation, floor plane or reflection. Preserve every narrow irregular off-white hand-cut paper rim around Xiaoyi and every object as opaque foreground. Do not use #00FF00 anywhere inside the subject. No cast shadow, no contact shadow, no text, no watermark.
```

优先一次生成绿幕成品；如果已有构图稳定的白底图，可以只编辑外围背景为 `#00FF00`，严格锁定人物、剪口、构图和配色。

## 本地抠除

依赖 Pillow：

```bash
python -m pip install pillow
```

默认命令：

```bash
python scripts/remove_chroma_key.py \
  --input path/to/source-green.png \
  --out path/to/final-transparent.png \
  --key-color "#00FF00" \
  --soft-matte \
  --transparent-threshold 12 \
  --opaque-threshold 220 \
  --despill
```

如果模型输出的绿色不是精确 `#00FF00`，改用边缘采样：

```bash
python scripts/remove_chroma_key.py --input source.png --out final.png --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill
```

只有边缘仍出现细绿线时，追加 `--edge-contract 1`。不要默认羽化；剪纸边应保持清楚。

## 验收

- 文件模式是 `RGBA`。
- 未接触主体的画布角落 alpha 为 `0`。
- 大面积背景完全透明，没有绿色残留。
- 人物头发、眼镜、手指、传送带支架和纸纤维没有被吃掉。
- 米白剪纸边连续、清晰、保持不透明或仅在最外缘轻微半透明。
- 不出现绿色描边、灰色底板或残留背景纸纹。
- 透明预览器常用黑色显示透明区域；黑底不代表图片实际有黑色背景。
