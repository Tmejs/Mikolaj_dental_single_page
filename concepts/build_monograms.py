"""Generate portable SVG studies for the Kozak Lab K monogram.

The K paths are drawn for this concept set; they do not depend on local fonts.
"""

from pathlib import Path
from html import escape

INK = "#252927"
COPPER = "#a36e52"
PAPER = "#f5f2ec"

STUDIES = [
    (
        "01", "Signature", "A light signature stroke with an open lower sweep.",
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="1.5"/>'
        f'<path d="M85 49 C73 43 63 52 68 61 C73 67 82 62 81 56 C78 69 74 88 74 111 L74 143 C74 155 81 159 91 150" fill="none" stroke="{INK}" stroke-width="5.5" stroke-linecap="round"/>'
        f'<path d="M75 105 C93 95 108 81 121 63 C126 56 132 55 135 60 C138 66 133 69 128 66" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M93 94 C103 110 117 132 135 149 C144 157 151 156 157 150" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M56 151 C68 157 76 157 88 151" fill="none" stroke="{COPPER}" stroke-width="1.5"/>',
    ),
    (
        "02", "Quill", "A broad pen stem and a crisp, restrained diagonal.",
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="2"/>'
        f'<path d="M68 48 C77 45 88 51 86 61 C80 64 78 72 78 82 L78 141 C78 147 82 151 88 153 C77 158 65 154 65 143 L65 73 C65 61 66 54 68 48 Z" fill="{INK}"/>'
        f'<path d="M76 112 C88 97 106 74 123 58 C129 52 138 50 145 55 C132 55 126 64 117 75 L91 106 Z" fill="{INK}"/>'
        f'<path d="M94 100 C109 119 122 139 139 151 C146 156 153 155 158 150 C151 161 140 163 131 157 C113 143 99 121 88 108 Z" fill="{INK}"/>'
        f'<path d="M52 160 H78" stroke="{COPPER}" stroke-width="2"/>',
    ),
    (
        "03", "Scribe", "Fine vertical rhythm and a long copper flourish.",
        f'<path d="M20 20 H180 V180 H20 V20" fill="none" stroke="{INK}" stroke-width="1"/>'
        f'<path d="M72 48 C80 45 85 52 81 58 C77 65 73 78 73 92 L73 145 C73 153 77 158 85 154" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M72 108 C91 96 107 80 123 60 C129 53 139 51 146 57" fill="none" stroke="{INK}" stroke-width="2.7" stroke-linecap="round"/>'
        f'<path d="M93 92 C98 115 113 140 129 150 C141 157 151 151 164 143" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
        f'<path d="M59 166 C88 146 110 160 138 158 C150 157 159 150 165 143" fill="none" stroke="{COPPER}" stroke-width="1.7" stroke-linecap="round"/>',
    ),
    (
        "04", "Ribbon", "A folded nib effect with a soft centre crossing.",
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="1.5"/>'
        f'<path d="M70 52 C79 46 87 49 89 57 C82 59 79 66 79 76 L79 146 C74 153 67 155 61 148 C67 145 69 138 69 129 L69 70 C69 62 69 56 70 52 Z" fill="{INK}"/>'
        f'<path d="M77 113 C93 98 110 78 125 63 C132 55 139 52 148 55 C137 59 130 66 122 76 C108 93 97 104 86 112 Z" fill="{INK}"/>'
        f'<path d="M88 104 C99 106 109 122 118 136 C129 153 141 157 153 150 C142 162 127 165 116 153 C103 139 95 118 82 112 Z" fill="{INK}"/>'
        f'<path d="M96 100 C104 98 108 97 113 96" fill="none" stroke="{PAPER}" stroke-width="2"/>',
    ),
    (
        "05", "Ink seal", "A dark field for a bolder, more memorable mark.",
        f'<rect x="18" y="18" width="164" height="164" fill="{INK}"/>'
        f'<rect x="25" y="25" width="150" height="150" fill="none" stroke="{PAPER}" stroke-opacity=".55" stroke-width="1"/>'
        f'<path d="M78 53 C69 48 62 54 68 61 C74 66 82 62 79 56 C75 70 73 90 73 114 L73 143 C73 151 79 155 87 149" fill="none" stroke="{PAPER}" stroke-width="6.5" stroke-linecap="round"/>'
        f'<path d="M75 108 C93 95 113 73 128 59 C133 55 139 54 144 58" fill="none" stroke="{PAPER}" stroke-width="3.4" stroke-linecap="round"/>'
        f'<path d="M94 94 C105 116 121 139 137 150 C143 154 150 154 155 149" fill="none" stroke="{PAPER}" stroke-width="5.8" stroke-linecap="round"/>'
        f'<circle cx="149" cy="149" r="3" fill="{COPPER}"/>',
    ),
    (
        "06", "Open frame", "An airy K in a square interrupted by the stroke.",
        f'<path d="M20 89 V20 H180 V180 H20 V124" fill="none" stroke="{INK}" stroke-width="1.5"/>'
        f'<path d="M73 48 C84 43 89 53 83 61 C76 73 72 88 72 109 L72 141 C72 151 77 157 86 152" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="M73 109 C90 101 110 82 125 61 C132 53 142 50 149 55" fill="none" stroke="{INK}" stroke-width="2.3" stroke-linecap="round"/>'
        f'<path d="M94 97 C105 119 120 141 136 151 C143 156 151 155 158 149" fill="none" stroke="{INK}" stroke-width="4.4" stroke-linecap="round"/>'
        f'<path d="M19 108 H54" fill="none" stroke="{COPPER}" stroke-width="1.4"/>',
    ),
    (
        "07", "Copper nib", "A warm accent follows the movement of the pen.",
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="1.5"/>'
        f'<path d="M66 49 C77 44 86 52 83 60 C76 76 75 96 75 121 L75 143 C75 152 82 155 90 151" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="M75 108 C93 99 110 82 128 60 C134 54 141 53 147 56" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="M94 95 C105 119 117 137 133 150 C143 158 153 156 159 149" fill="none" stroke="{INK}" stroke-width="7.5" stroke-linecap="round"/>'
        f'<path d="M83 56 C79 76 79 91 79 102 M105 118 C114 134 124 145 132 149" fill="none" stroke="{COPPER}" stroke-width="1.9" stroke-linecap="round"/>',
    ),
    (
        "08", "Heritage", "A double hairline frame and a classical flourish.",
        f'<rect x="18" y="18" width="164" height="164" fill="none" stroke="{INK}" stroke-width="1"/>'
        f'<rect x="24" y="24" width="152" height="152" fill="none" stroke="{INK}" stroke-width=".6"/>'
        f'<path d="M76 51 C65 45 60 55 67 60 C76 65 84 60 82 53 C76 69 73 88 73 107 L73 143 C73 152 78 158 90 151" fill="none" stroke="{INK}" stroke-width="5.5" stroke-linecap="round"/>'
        f'<path d="M73 108 C93 96 109 81 123 62 C130 53 140 52 148 59 C141 55 135 60 134 65" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>'
        f'<path d="M94 93 C103 113 117 137 134 149 C145 156 155 153 159 145" fill="none" stroke="{INK}" stroke-width="5.7" stroke-linecap="round"/>'
        f'<path d="M56 156 C67 153 77 153 88 157 M143 59 C151 57 157 58 162 63" fill="none" stroke="{COPPER}" stroke-width="1.2"/>',
    ),
    (
        "09", "Modern stroke", "A simplified handwritten K that stays clear when small.",
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="2"/>'
        f'<path d="M73 51 C79 48 84 51 81 57 C75 70 74 85 74 105 L74 148" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
        f'<path d="M76 109 C91 100 111 81 130 58" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M96 95 C104 114 120 139 143 152" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="M64 155 C76 156 85 154 92 150" fill="none" stroke="{COPPER}" stroke-width="2" stroke-linecap="round"/>',
    ),
    (
        "10", "Atelier", "An expressive K with a long lower return stroke.",
        f'<rect x="20" y="20" width="160" height="160" fill="none" stroke="{INK}" stroke-width="1.3"/>'
        f'<path d="M87 50 C72 42 62 52 69 61 C77 69 86 61 82 55 C74 75 72 91 72 109 L72 143 C72 155 81 157 91 151" fill="none" stroke="{INK}" stroke-width="5.8" stroke-linecap="round"/>'
        f'<path d="M74 108 C96 97 111 81 125 63 C131 54 142 53 150 61" fill="none" stroke="{INK}" stroke-width="2.7" stroke-linecap="round"/>'
        f'<path d="M93 95 C107 123 122 145 139 152 C151 156 158 147 154 139 C147 130 135 138 139 146" fill="none" stroke="{INK}" stroke-width="5.5" stroke-linecap="round"/>'
        f'<path d="M50 160 C68 155 81 158 93 163 C106 167 122 166 138 153" fill="none" stroke="{COPPER}" stroke-width="1.6" stroke-linecap="round"/>',
    ),
]


def main() -> None:
    target = Path(__file__).resolve().parent / "monograms"
    target.mkdir(exist_ok=True)
    for number, name, description, artwork in STUDIES:
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" '
            f'role="img" aria-label="Kozak Lab K monogram concept {number}: {name}">'
            f'<title>{name} — Kozak Lab monogram concept {number}</title>'
            f'<rect width="200" height="200" fill="{PAPER}"/>{artwork}</svg>\n'
        )
        (target / f"k-{number}.svg").write_text(svg, encoding="utf-8")

    cards = "\n".join(
        f'''<article class="option">
          <div class="option-art"><img class="large" src="monograms/k-{number}.svg" alt="K monogram {number}: {escape(name)}" width="200" height="200" /><img class="small" src="monograms/k-{number}.svg" alt="" width="40" height="40" /></div>
          <div class="option-copy"><span class="number">{number} / 10</span><h2>{escape(name)}</h2><p>{escape(description)}</p><a href="monograms/k-{number}.svg">Open SVG ↗</a></div>
        </article>'''
        for number, name, description, _ in STUDIES
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
    <div class="intro"><span class="eyebrow">MONOGRAM EXPLORATION / 01</span><div><h1>Ten ways to write <em>K.</em></h1><p>Ten calligraphic directions for the square Kozak Lab mark. The large view shows the character of each stroke; the small square tests whether it survives in a header or favicon. These are comparisons only—the current site logo stays as it is until one is chosen.</p></div></div>
    <div class="grid">'''+cards+'''</div>
    <p class="note">Every option is a self-contained SVG drawn for this study, with no external font or image dependency. Pick a number to refine; colour, frame weight, and stroke can still change.</p>
  </main>
</body>
</html>
'''
    (target.parent / "monogram-options.html").write_text(board, encoding="utf-8")


if __name__ == "__main__":
    main()
