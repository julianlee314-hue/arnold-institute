"""Build research/the-way-back-to-the-table.html from the signed-off public preview.

Source (public, anonymous only): /workspace/digestion-scale/preview-public.html and
bowl-0..10.svg, path.svg. Inline SVGs are swapped for files in research/assets/,
and Google Fonts is swapped for self-hosted fonts so the site loads no external resources.
"""
import re, shutil, sys
SRC = sys.argv[1] if len(sys.argv) > 1 else "/workspace/digestion-scale"
A = "research/assets/the-way-back-to-the-table"
s = open(f"{SRC}/preview-public.html", encoding="utf-8").read()

def fix(t):  # bare "&" in aria-labels (e.g. "Soft & Simple") is invalid XML in a standalone .svg
    return re.sub(r"&(?!amp;|lt;|gt;|quot;|#)", "&amp;", t)
for n in [f"bowl-{i}" for i in range(11)] + ["path"]:
    open(f"{A}/{n}.svg", "w").write(fix(open(f"{SRC}/{n}.svg").read()))
# Tier 10 sits on a dark card: light-stroke variant (preview used currentColor = #F4EEE1).
open(f"{A}/bowl-10-light.svg", "w").write(open(f"{A}/bowl-10.svg").read().replace("#1F1C18", "#F4EEE1"))

# 1. Fonts: drop Google Fonts, use self-hosted woff2.
s = re.sub(r'\s*<link rel="preconnect"[^>]*>', "", s)
s = re.sub(r'\s*<link href="https://fonts.googleapis.com[^>]*>', "", s)
fonts = """
    @font-face{font-family:'Cormorant Garamond';font-style:normal;font-weight:500;font-display:swap;src:url(../assets/fonts/cormorant-garamond-500.woff2) format('woff2')}
    @font-face{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-display:swap;src:url(../assets/fonts/cormorant-garamond-500-italic.woff2) format('woff2')}
    @font-face{font-family:Inter;font-style:normal;font-weight:400 600;font-display:swap;src:url(../assets/fonts/inter-latin.woff2) format('woff2')}"""
s = s.replace("<style>", "<style>" + fonts, 1)

# 2. Head: site title, no-referrer, description.
s = s.replace("<title>The Way Back to the Table</title>",
  '<meta name="referrer" content="no-referrer">\n    <meta name="description" content="A 0–10 scale of how hard each food works your stomach, for easing back after a stomach bug, plus guidance on movement and the gut.">\n    <title>The Way Back to the Table — The Arnold Institute of Broscience</title>')

# 3. Inline SVGs -> asset files.
svgs = list(re.finditer(r'<svg\b.*?</svg>', s, re.S))
assert len(svgs) == 12, len(svgs)
def label(m): return re.search(r'aria-label="([^"]*)"', m.group(0)).group(1)
out, last = [], 0
for i, m in enumerate(svgs):
    out.append(s[last:m.start()])
    if i < 11:
        f = "bowl-10-light.svg" if i == 10 else f"bowl-{i}.svg"
        out.append(f'<img src="assets/the-way-back-to-the-table/{f}" width="120" height="90" alt="{fix(label(m))}">')
    else:
        out.append(f'<img src="assets/the-way-back-to-the-table/path.svg" width="240" height="64" alt="{label(m)}" class="pathm">')
    last = m.end()
out.append(s[last:]); s = "".join(out)
s = s.replace(".bowl svg{width:132px;height:auto;display:block;color:var(--ink)}", ".bowl img{width:132px;height:auto;display:block}")
s = s.replace(".nope .bowl svg{color:#F4EEE1}", "")
s = s.replace(".bowl svg{width:84px}", ".bowl img{width:84px}")
assert "<svg" not in s and ".bowl svg" not in s

# 4. Site bar + back-to-home link, styled to sit quietly above the signed-off design.
css = """
    .site{border-bottom:1px solid var(--hair);background:var(--card)}
    .site .in{max-width:900px;margin:0 auto;padding:14px 32px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px 18px;font-size:14px}
    .site a{color:var(--ink);text-decoration:none} .site a:hover{text-decoration:underline}
    .site .brand{font-weight:600} .site nav a{margin-left:18px;color:#5a5249}
    .back{text-align:center;margin:22px 0 0;font:400 14px/1.5 Inter,system-ui,sans-serif}
    .back a{color:var(--brass)}
    .move .pathm{max-width:420px}
    @media (max-width:640px){.site .in{padding:12px 18px} .site nav a{margin:0 14px 0 0}}
    </style>"""
s = s.replace("</style>", css, 1)
bar = ('<div class="site"><div class="in"><a class="brand" href="../index.html">The Arnold Institute of Broscience</a>'
       '<nav><a href="../index.html">Home</a><a href="../index.html#research">Research</a><a href="../privacy.html">Privacy Policy</a></nav></div></div>')
s = s.replace('<body><div class="wrap">', '<body>' + bar + '<main class="wrap">', 1)
s = s.replace('</footer></div></body></html>',
  '</footer>\n    <p class="back"><a href="../index.html">← Back to the Institute home page</a> · <a href="../privacy.html">Privacy Policy</a></p></main></body></html>')
assert '<main class="wrap">' in s and 'class="back"' in s
open("research/the-way-back-to-the-table.html", "w", encoding="utf-8").write(s)
print("ok", len(s))
