"""Build ten font-led K monogram previews from bundled OFL typefaces."""

from html import escape
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent
PAPER = "#f5f2ec"
INK = "#252927"
COPPER = "#a36e52"

# Family, file, and a concise design note. Sources and license files are bundled in fonts/.
FONTS = [
    ("Great Vibes", "greatvibes/GreatVibes-Regular.ttf", "Flowing formal script"),
    ("Pinyon Script", "pinyonscript/PinyonScript-Regular.ttf", "Fine copperplate contrast"),
    ("Alex Brush", "alexbrush/AlexBrush-Regular.ttf", "Confident brush lettering"),
    ("Parisienne", "parisienne/Parisienne-Regular.ttf", "Soft Parisian cursive"),
    ("Allura", "allura/Allura-Regular.ttf", "Light and understated"),
    ("Italianno", "italianno/Italianno-Regular.ttf", "Tall Italian hand"),
    ("Sacramento", "sacramento/Sacramento-Regular.ttf", "Relaxed handwritten script"),
    ("Cormorant Garamond Italic", "cormorantgaramond/CormorantGaramond-Italic[wght].ttf", "Editorial serif calligraphy"),
    ("Bodoni Moda Italic", "bodonimoda/BodoniModa-Italic[opsz,wght].ttf", "High contrast fashion serif"),
    ("Playfair Display Italic", "playfairdisplay/PlayfairDisplay-Italic[wght].ttf", "Expressive display italic"),
]


def glyph_art(font_path: Path) -> str:
    font = TTFont(font_path)
    try:
        name = font.getBestCmap()[ord("K")]
        glyph_set = font.getGlyphSet()
        glyph = glyph_set[name]
        bounds_pen = BoundsPen(glyph_set)
        glyph.draw(bounds_pen)
        x1, y1, x2, y2 = bounds_pen.bounds
        path_pen = SVGPathPen(glyph_set)
        glyph.draw(path_pen)
        scale = min(134 / (x2 - x1), 139 / (y2 - y1))
        tx = 100 - ((x1 + x2) / 2) * scale
        ty = 100 + ((y1 + y2) / 2) * scale
        return (
            f'<path d="{path_pen.getCommands()}" fill="{INK}" '
            f'transform="translate({tx:.3f} {ty:.3f}) scale({scale:.6f} {-scale:.6f})"/>'
        )
    finally:
        font.close()


def tile(art: str) -> str:
    return (
        f'<rect width="200" height="200" fill="{PAPER}"/>'
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="1.6"/>'
        + art
    )


def main() -> None:
    output = ROOT / "monograms"
    output.mkdir(exist_ok=True)
    cards = []
    sheet_tiles = []
    for index, (family, filename, note) in enumerate(FONTS, start=1):
        number = f"{index:02d}"
        art = tile(glyph_art(ROOT / "fonts" / filename))
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" '
            f'aria-label="Kozak Lab K monogram in {escape(family)}">'
            f'<title>{escape(family)} K monogram — Kozak Lab</title>{art}</svg>\n'
        )
        (output / f"k-{number}.svg").write_text(svg, encoding="utf-8")
        cards.append(
            f'<article class="option"><div class="option-art">'
            f'<img class="large" src="monograms/k-{number}.svg" alt="K rendered in {escape(family)}" width="200" height="200" />'
            f'<img class="small" src="monograms/k-{number}.svg" alt="" width="40" height="40" />'
            f'</div><div class="option-copy"><span class="number">{number} / 10</span>'
            f'<h2>{escape(family)}</h2><p>{escape(note)}</p>'
            f'<a href="monograms/k-{number}.svg">Open SVG ↗</a></div></article>'
        )
        col, row = (index - 1) % 5, (index - 1) // 5
        x, y = 33 + col * 236, 105 + row * 268
        sheet_tiles.append(
            f'<g transform="translate({x} {y})"><rect width="220" height="242" fill="{PAPER}" stroke="#d8d2c8"/>'
            f'<g transform="translate(10 6)">{art}</g>'
            f'<text x="17" y="224" fill="{INK}" font-size="14" font-family="Georgia,serif">{number}  {escape(family)}</text></g>'
        )

    board = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex,nofollow" />
  <title>Kozak Lab — K monogram studies</title>
  <style>
    :root { --paper:#f5f2ec; --ink:#252927; --muted:#5e635e; --line:#d8d2c8; --copper:#a36e52; }
    * { box-sizing:border-box; }
    body { margin:0; background:var(--paper); color:var(--ink); font-family:Helvetica,Arial,sans-serif; }
    a { color:inherit; text-underline-offset:4px; }
    a:focus-visible { outline:2px solid var(--copper); outline-offset:4px; }
    .shell { width:min(100% - 80px,1260px); margin:auto; }
    header { padding:24px 0; border-bottom:1px solid var(--line); }
    header .shell { display:flex; justify-content:space-between; align-items:center; gap:20px; }
    .brand { font-size:15px; font-weight:700; letter-spacing:.16em; text-decoration:none; white-space:nowrap; }
    header a:last-child { font-size:12px; }
    .intro { display:grid; grid-template-columns:1fr 2fr; gap:40px; padding:83px 0 75px; }
    .eyebrow,.number { color:var(--copper); font-size:11px; font-weight:700; letter-spacing:.15em; }
    h1,h2,p { margin-top:0; }
    h1,h2 { font-family:Georgia,'Times New Roman',serif; font-weight:400; letter-spacing:-.045em; }
    h1 { max-width:750px; margin-bottom:24px; font-size:clamp(47px,5.6vw,76px); line-height:1.06; }
    h1 em { color:var(--copper); font-weight:400; }
    .intro p { max-width:720px; margin-bottom:0; color:var(--muted); font-size:16px; line-height:1.8; }
    .intro p+p { margin-top:15px; }
    .grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1px; background:var(--line); border:1px solid var(--line); margin-bottom:90px; }
    .option { display:grid; grid-template-columns:220px 1fr; align-items:center; gap:30px; min-height:312px; padding:30px; background:var(--paper); }
    .option-art { position:relative; width:200px; height:200px; }
    .option-art .large { display:block; width:200px; height:200px; }
    .option-art .small { position:absolute; width:40px; height:40px; right:-12px; bottom:-12px; box-shadow:0 3px 14px #25292726; border:1px solid var(--line); }
    .option-copy h2 { margin:12px 0 12px; font-size:34px; }
    .option-copy p { max-width:240px; color:var(--muted); font-size:13px; line-height:1.65; }
    .option-copy a { display:inline-block; margin-top:12px; font-size:11px; font-weight:700; }
    .note { border-top:1px solid var(--line); padding:30px 0 70px; color:var(--muted); font-size:13px; line-height:1.7; }
    @media(max-width:1050px) { .option { grid-template-columns:160px 1fr; gap:20px; } .option-art,.option-art .large { width:160px; height:160px; } }
    @media(max-width:760px) { .shell { width:min(100% - 36px,1260px); } .intro { display:block; padding:60px 0 48px; } .eyebrow { display:block; margin-bottom:25px; } .grid { grid-template-columns:1fr; } .option { grid-template-columns:150px 1fr; min-height:230px; padding:22px; } .option-art,.option-art .large { width:150px; height:150px; } }
    @media(max-width:440px) { .option { grid-template-columns:124px 1fr; gap:14px; padding:14px; } .option-art,.option-art .large { width:124px; height:124px; } .option-art .small { width:32px; height:32px; } .option-copy h2 { font-size:26px; } .option-copy p { font-size:12px; } }
  </style>
</head>
<body>
  <header><div class="shell"><a class="brand" href="../index.html">KOZAK LAB</a><a href="../index.html">← Back to website</a></div></header>
  <main class="shell">
    <div class="intro"><span class="eyebrow">TYPE-LED MONOGRAM EXPLORATION</span><div><h1>Ten ways to write <em>K.</em></h1><p>Ten real typeface K letterforms, shown in the same square and palette for a fair comparison. The small square previews header and favicon scale. The current website logo stays in place until one is chosen.</p><p><a href="monogram-sheet.svg">View all ten on one SVG sheet ↗</a></p></div></div>
    <div class="grid">'''+"\n".join(cards)+'''</div>
    <p class="note">The SVGs contain letter outlines, so they look the same on desktop and mobile. Typeface names and their open font licenses are included with the source files in <code>concepts/fonts/</code>.</p>
  </main>
</body>
</html>
'''
    (ROOT / "monogram-options.html").write_text(board, encoding="utf-8")

    sheet = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1210 680" role="img" '
        'aria-label="Ten square K monogram typeface concepts for Kozak Lab">'
        '<title>Ten font-led K monogram concepts — Kozak Lab</title>'
        f'<rect width="1210" height="680" fill="{PAPER}"/>'
        f'<text x="33" y="47" fill="{INK}" font-family="Helvetica,Arial,sans-serif" font-weight="700" font-size="18" letter-spacing="3">KOZAK LAB</text>'
        f'<text x="33" y="78" fill="{COPPER}" font-family="Helvetica,Arial,sans-serif" font-weight="700" font-size="12" letter-spacing="2">TEN TYPE-LED K STUDIES</text>'
        + "".join(sheet_tiles) + "</svg>\n"
    )
    (ROOT / "monogram-sheet.svg").write_text(sheet, encoding="utf-8")


if __name__ == "__main__":
    main()
