#!/usr/bin/env python3
"""Convert a flat chroma-key background to a transparent PNG."""

from __future__ import annotations

import argparse
from pathlib import Path
from statistics import median

from PIL import Image


def parse_hex(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("Use a six-digit RGB hex value such as #00FF00")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def sample_border(image: Image.Image) -> tuple[int, int, int]:
    rgb = image.convert("RGB")
    w, h = rgb.size
    step = max(1, min(w, h) // 256)
    samples = []
    for x in range(0, w, step):
        samples.extend((rgb.getpixel((x, 0)), rgb.getpixel((x, h - 1))))
    for y in range(0, h, step):
        samples.extend((rgb.getpixel((0, y)), rgb.getpixel((w - 1, y))))
    return tuple(round(median(pixel[c] for pixel in samples)) for c in range(3))


def smoothstep(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3 - 2 * value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--key-color", type=parse_hex, default=parse_hex("#00FF00"))
    parser.add_argument("--auto-key", choices=("none", "border"), default="none")
    parser.add_argument("--soft-matte", action="store_true")
    parser.add_argument("--transparent-threshold", type=float, default=12)
    parser.add_argument("--opaque-threshold", type=float, default=220)
    parser.add_argument("--despill", action="store_true")
    parser.add_argument("--edge-contract", type=int, choices=(0, 1), default=0)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    src, out = Path(args.input), Path(args.out)
    if out.exists() and not args.force:
        parser.error(f"output exists: {out}; pass --force to overwrite")
    image = Image.open(src).convert("RGBA")
    key = sample_border(image) if args.auto_key == "border" else args.key_color
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, old_alpha = pixels[x, y]
            distance = max(abs(r - key[0]), abs(g - key[1]), abs(b - key[2]))
            if args.soft_matte:
                ratio = (distance - args.transparent_threshold) / max(1, args.opaque_threshold - args.transparent_threshold)
                alpha = round(255 * smoothstep(ratio))
            else:
                alpha = 0 if distance <= args.transparent_threshold else 255
            alpha = round(alpha * old_alpha / 255)
            if args.despill and alpha < 252 and g > max(r, b):
                g = max(r, b)
            pixels[x, y] = (r, g, b, alpha)

    if args.edge_contract:
        from PIL import ImageFilter
        image.putalpha(image.getchannel("A").filter(ImageFilter.MinFilter(3)))
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out, "PNG")
    print(f"Wrote {out} with key #{key[0]:02X}{key[1]:02X}{key[2]:02X}")


if __name__ == "__main__":
    main()
