#!/usr/bin/env python3
"""Draw thumbnails for unasanu.xyz.

1. Main page social-media image (og:image), 1920x1080:
   content/thumbnail.png. It is referenced by `image` in content/_index.md
   and published by zola as https://unasanu.xyz/thumbnail.png.
   It shows the core idea of the article: an algorithm plus all simulation
   steps is just one big natural number. All cells, bits and the number itself
   come from a real B3/S23 simulation.

2. Small thumbnail for the blog post list, 1280x720 (the blog shows it at
   ~200px wide): glider logo + name on the same background.
   ../blog_zola/content/p/unasanu/thumbnail.webp

Both follow the look of the site header: 120deg black -> #26bf73 gradient,
white glider logo, Rubik font.

Requirements: Python 3, Pillow (with WOFF2 and WebP support), numpy.
Usage: python3 draw_thumbnail.py [--main PATH] [--small PATH]
"""

import argparse
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MAIN = os.path.join(ROOT, "content", "thumbnail.png")
DEFAULT_SMALL = os.path.join(ROOT, "..", "blog_zola", "content", "p", "unasanu", "thumbnail.webp")

SS = 2  # supersampling factor for smooth edges

# Colors from sass/_sizes.scss
HEADER_BG = (0x26, 0xBF, 0x73)
HEADER_BG_SECONDARY = (0x00, 0x00, 0x00)
WHITE = (255, 255, 255)
ACCENT = (0x7D, 0xF5, 0xB1)  # light version of the header green, for highlights
ORANGE = (0xFF, 0xB8, 0x4D)  # "Algorithm" box, as in number.drawio.svg

RUBIK = os.path.join(ROOT, "static/fonts/Rubik/iJWKBXyIfDnIV7nBrXw.woff2")  # latin
MONO = os.path.join(ROOT, "static/fonts/JetBrainsMono/"
                    "tDbv2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKwBNntkaToggR7BYRbKPxDcwg.woff2")
# Site fonts have no "∈ ℕ" glyphs, so take them from a system font.
SYMBOL_FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "C:/Windows/Fonts/seguisym.ttf",
]


def s(v):
    """Scale a design-space value to the supersampled canvas."""
    return int(round(v * SS))


def font(path, size, weight=None):
    f = ImageFont.truetype(path, s(size))
    if weight is not None:
        f.set_variation_by_axes([weight])
    return f


def symbol_font(size):
    for path in SYMBOL_FONTS:
        if os.path.exists(path):
            return ImageFont.truetype(path, s(size))
    sys.exit("no font with '∈ ℕ' glyphs found, add one to SYMBOL_FONTS")


def rgba(color, alpha):
    return (*color, int(round(255 * alpha)))


# ---------------------------------------------------------------- Game of Life

def life_step(grid, wrap=True):
    if not wrap:
        grid = np.pad(grid, 1)
    n = sum(np.roll(np.roll(grid, dy, 0), dx, 1)
            for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy, dx) != (0, 0))
    new = ((n == 3) | ((grid == 1) & (n == 2))).astype(np.uint8)
    return new if wrap else new[1:-1, 1:-1]


GLIDER = np.array([[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 1]], dtype=np.uint8)


def glider_generations(size, count):
    grid = np.zeros((size, size), dtype=np.uint8)
    grid[0:3, 0:3] = GLIDER
    gens = [grid]
    for _ in range(count - 1):
        gens.append(life_step(gens[-1], wrap=False))
    return gens


def bits_of(grid):
    return "".join(str(v) for v in grid.flatten())


# ---------------------------------------------------------------- drawing helpers

def css_linear_gradient(w, h, angle_deg, c0, c1):
    """Same geometry as CSS `linear-gradient(<angle>, c0, c1)`. Returns image and t in [0, 1]."""
    a = np.radians(angle_deg)
    dx, dy = np.sin(a), -np.cos(a)
    length = abs(w * dx) + abs(h * dy)
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    t = ((xs - w / 2) * dx + (ys - h / 2) * dy) / length + 0.5
    t = np.clip(t, 0, 1)
    img = np.array(c0, np.float32) * (1 - t[..., None]) + np.array(c1, np.float32) * t[..., None]
    return Image.fromarray(img.round().astype(np.uint8), "RGB").convert("RGBA"), t


def smoothstep(e0, e1, x):
    x = np.clip((x - e0) / (e1 - e0), 0, 1)
    return x * x * (3 - 2 * x)


def alpha_layer(alpha):
    """Black RGBA layer with the given per-pixel alpha (float array in [0, 1])."""
    arr = np.zeros((*alpha.shape, 4), np.uint8)
    arr[..., 3] = (np.clip(alpha, 0, 1) * 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")


def gaussian_blob(shape, cx, cy, rx, ry, strength):
    ys, xs = np.mgrid[0:shape[0], 0:shape[1]].astype(np.float32)
    return strength * np.exp(-(((xs - cx) / rx) ** 2 + ((ys - cy) / ry) ** 2))


def draw_cells(draw, grid, x0, y0, cell, gap, color):
    for (r, c), v in np.ndenumerate(grid):
        if v:
            x = x0 + c * cell
            y = y0 + r * cell
            draw.rectangle([x + gap, y + gap, x + cell - gap - 1, y + cell - gap - 1], fill=color)


def text_center(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)


def curly_brace(draw, x0, x1, y, depth, color, width):
    """Horizontal curly brace opening upwards, with its tip pointing down at the center."""
    r = depth / 2
    mid = (x0 + x1) / 2
    pts = []

    def arc(cx, cy, a0, a1, steps=24):
        for i in range(steps + 1):
            a = np.radians(a0 + (a1 - a0) * i / steps)
            pts.append((cx + r * np.cos(a), cy + r * np.sin(a)))

    arc(x0 + r, y, 180, 90)                # left end curls down
    arc(mid - r, y + depth, -90, 0)        # into the tip
    arc(mid + r, y + depth, 180, 270)      # out of the tip
    arc(x1 - r, y, 90, 0)                  # right end curls up
    draw.line(pts, fill=color, width=width, joint="curve")


def background(w, h, cell, seed=2023_08_28, max_alpha=0.17):
    """Site header gradient + a real Game of Life soup that fades in towards the green side.

    w, h, cell are in design-space pixels. Returns the supersampled RGBA image.
    """
    cw, ch = s(w), s(h)
    img, t = css_linear_gradient(cw, ch, 120, HEADER_BG_SECONDARY, HEADER_BG)

    rows, cols = h // cell + 1, w // cell + 1
    rng = np.random.default_rng(seed)  # article date, for reproducibility
    soup = (rng.random((rows, cols)) < 0.33).astype(np.uint8)
    for _ in range(90):
        soup = life_step(soup)

    tex = Image.new("RGBA", img.size, (0, 0, 0, 0))
    td = ImageDraw.Draw(tex)
    for r in range(rows + 1):  # faint grid lines
        td.line([(0, s(r * cell)), (cw, s(r * cell))], fill=rgba(WHITE, 0.035), width=s(1))
    for c in range(cols + 1):
        td.line([(s(c * cell), 0), (s(c * cell), ch)], fill=rgba(WHITE, 0.035), width=s(1))
    pad = max(2, cell / 15)
    for (r, c), v in np.ndenumerate(soup):
        if v:
            cx, cy = s(c * cell + cell / 2), s(r * cell + cell / 2)
            k = t[min(cy, ch - 1), min(cx, cw - 1)]
            alpha = 0.03 + max_alpha * np.clip((k - 0.25) / 0.75, 0, 1) ** 1.5
            td.rectangle([s(c * cell + pad), s(r * cell + pad),
                          s(c * cell + cell - pad) - 1, s(r * cell + cell - pad) - 1],
                         fill=rgba(WHITE, alpha))
    img = Image.alpha_composite(img, tex)

    # Darken the brightest (bottom-right) corner a little: both the green and the cells there.
    img = Image.alpha_composite(img, alpha_layer(0.28 * smoothstep(0.6, 1.0, t)))
    return img


def wordmark(d, x, glider_bottom, logo_cell, font_size):
    """Glider logo + "unasanu", text baseline sitting on the glider's bottom edge.

    All values are in design-space pixels. Returns total width of the wordmark.
    """
    top = glider_bottom - 3 * logo_cell
    draw_cells(d, GLIDER, s(x), s(top), s(logo_cell), s(logo_cell / 15), rgba(WHITE, 1))
    title_font = font(RUBIK, font_size, 700)
    text_x = x + 3 * logo_cell + logo_cell * 1.13
    d.text((s(text_x), s(glider_bottom)), "unasanu", font=title_font, fill=rgba(WHITE, 1), anchor="ls")
    return text_x - x + d.textlength("unasanu", font=title_font) / SS


def finish(img, layer, w, h, out, **save_args):
    img = Image.alpha_composite(img, layer)
    img = img.convert("RGB").resize((w, h), Image.LANCZOS)
    img.save(out, **save_args)
    print(f"saved {out} ({img.width}x{img.height})")


# ---------------------------------------------------------------- main page picture

def draw_main(out):
    W, H = 1920, 1080
    cw, ch = s(W), s(H)
    img = background(W, H, cell=30)

    # Soft dark veil behind the text so the texture never competes with it.
    veil = gaussian_blob((ch, cw), s(600), s(330), s(900), s(330), 0.45)
    veil += gaussian_blob((ch, cw), s(960), s(800), s(1250), s(260), 0.40)
    img = Image.alpha_composite(img, alpha_layer(veil))

    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    # Logo (glider, as in the main page header) + title.
    left = 150
    wordmark(d, left, glider_bottom=266, logo_cell=46, font_size=200)

    # Tagline: un-iverse as a nu-mber, with the letters that form the name highlighted.
    bold = font(RUBIK, 76, 600)
    light = font(RUBIK, 76, 300)
    parts = [("un", True), ("iverse ", False), ("as", True), (" ", False),
             ("a", True), (" ", False), ("nu", True), ("mber", False)]
    x, y = s(left + 4), s(338)
    for txt, hi in parts:
        f = bold if hi else light
        d.text((x, y), txt, font=f, fill=rgba(ACCENT, 1) if hi else rgba(WHITE, 0.88))
        x += d.textlength(txt, font=f)

    # Diagram: algorithm + simulation steps = one natural number.
    n_last = 8
    gens = glider_generations(6, n_last + 1)
    rule_bits = "".join(f"{ord(c):08b}" for c in "B3/S23")

    box_y, box_h = 520, 250
    gap = 22
    boxes = [("Algorithm", 360, "algo"), ("Step 0", 250, 0), ("Step 1", 250, 1),
             ("Step 2", 250, 2), ("…", 110, None), ("Step N", 250, n_last)]
    total = sum(b[1] for b in boxes) + gap * (len(boxes) - 1)
    x = (W - total) / 2

    label_font = font(RUBIK, 34, 500)
    bits_font = font(MONO, 27, 400)
    rule_font = font(MONO, 58, 700)
    small_font = font(RUBIK, 24, 400)
    dots_font = font(RUBIK, 64, 500)

    for label, bw, kind in boxes:
        cx = x + bw / 2
        if kind is None:
            text_center(d, s(cx), s(box_y + box_h / 2 - 44), "…", dots_font, rgba(WHITE, 0.85))
            text_center(d, s(cx), s(box_y + box_h + 20), "…", bits_font, rgba(WHITE, 0.7))
            x += bw + gap
            continue

        is_algo = kind == "algo"
        edge = ORANGE if is_algo else WHITE
        d.rounded_rectangle([s(x), s(box_y), s(x + bw), s(box_y + box_h)], radius=s(18),
                            fill=rgba(edge, 0.13 if is_algo else 0.09),
                            outline=rgba(edge, 0.75 if is_algo else 0.45), width=s(2.5))
        text_center(d, s(cx), s(box_y + 20), label, label_font, rgba(edge, 1))

        if is_algo:
            text_center(d, s(cx), s(box_y + 96), "B3/S23", rule_font, rgba(WHITE, 1))
            text_center(d, s(cx), s(box_y + 180), "Conway's Game of Life", small_font, rgba(WHITE, 0.7))
            bits = rule_bits[:13] + "…"
        else:
            grid = gens[kind]
            mc = 23
            gx, gy = cx - 3 * mc, box_y + 80
            for r in range(7):
                d.line([(s(gx), s(gy + r * mc)), (s(gx + 6 * mc), s(gy + r * mc))], fill=rgba(WHITE, 0.16), width=s(1.5))
            for c in range(7):
                d.line([(s(gx + c * mc), s(gy)), (s(gx + c * mc), s(gy + 6 * mc))], fill=rgba(WHITE, 0.16), width=s(1.5))
            draw_cells(d, grid, s(gx), s(gy), s(mc), s(2), rgba(WHITE, 1))
            bits = bits_of(grid)[:9] + "…"

        text_center(d, s(cx), s(box_y + box_h + 20), bits, bits_font, rgba(WHITE, 0.78))
        x += bw + gap

    # Brace and the resulting number.
    bx0, bx1 = (W - total) / 2, (W + total) / 2
    curly_brace(d, s(bx0), s(bx1), s(box_y + box_h + 68), s(36), rgba(WHITE, 0.8), s(3))

    all_bits = rule_bits + "".join(bits_of(g) for g in gens)
    number = str(int("1" + all_bits, 2))  # leading 1 keeps leading zeros meaningful
    shown = number[:24] + "…" + number[-22:]
    num_font = font(MONO, 50, 600)
    sym_font = symbol_font(48)
    tail = " ∈ ℕ"
    nw = d.textlength(shown, font=num_font) + d.textlength(tail, font=sym_font)
    ny = s(box_y + box_h + 132)
    nx = s(W / 2) - nw / 2
    d.text((nx, ny), shown, font=num_font, fill=rgba(WHITE, 1))
    d.text((nx + d.textlength(shown, font=num_font), ny - s(2)), tail, font=sym_font, fill=rgba(ACCENT, 1))

    # Footer: domain.
    foot_font = font(RUBIK, 30, 400)
    d.text((s(W - 150), s(1026)), "unasanu.xyz", font=foot_font, fill=rgba(WHITE, 0.75), anchor="rs")

    finish(img, layer, W, H, out, optimize=True)


# ---------------------------------------------------------------- small blog thumbnail

def draw_small(out):
    W, H = 1280, 720
    cw, ch = s(W), s(H)
    # Bigger cells than on the main picture: it is shown ~200px wide.
    img = background(W, H, cell=48, max_alpha=0.15)

    logo_cell, font_size = 45, 195
    glider_h = 3 * logo_cell

    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # Measure once to center the wordmark, then draw.
    width = wordmark(ImageDraw.Draw(Image.new("RGBA", (1, 1))), 0, glider_h, logo_cell, font_size)
    x = (W - width) / 2
    glider_bottom = (H + glider_h) / 2

    veil = gaussian_blob((ch, cw), s(W / 2), s(H / 2), s(width * 0.75), s(glider_h * 1.6), 0.45)
    img = Image.alpha_composite(img, alpha_layer(veil))

    wordmark(d, x, glider_bottom, logo_cell, font_size)
    finish(img, layer, W, H, out, quality=90, method=6)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--main", default=DEFAULT_MAIN, help="main page og:image (png, 1920x1080)")
    ap.add_argument("--small", default=DEFAULT_SMALL, help="small blog thumbnail (webp, 1280x720)")
    args = ap.parse_args()

    draw_main(args.main)
    if os.path.isdir(os.path.dirname(os.path.abspath(args.small))):
        draw_small(args.small)
    else:
        print(f"skipped small thumbnail: directory of {args.small} does not exist")


if __name__ == "__main__":
    main()
