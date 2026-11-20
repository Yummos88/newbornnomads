"""Bouwt de merken-secties op de site (EN + NL) en pagina 3 van de mediakits uit brands/brands.json.

Gebruik:  python tools/build_brands.py
Vereist:  pip install pymupdf fonttools brotli
Logo's:   brands/<id>.png (transparant PNG, max ~120 px hoog, in merkkleur)
"""
import json, html, io, pathlib
import pymupdf as fitz
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "brands/brands.json").read_text(encoding="utf-8"))["brands"]
WORKED = [b for b in DATA if b["status"] == "worked"]
UPCOMING = [b for b in DATA if b["status"] == "upcoming"]

TXT = {
    "en": {"worked": "Brands we've worked with", "upcoming": "Coming up",
           "kit_upcoming": "COMING UP", "more": "+{n} more on thenewbornnomads.com"},
    "nl": {"worked": "Merken waarmee we samenwerkten", "upcoming": "Binnenkort",
           "kit_upcoming": "BINNENKORT", "more": "+{n} meer op thenewbornnomads.com"},
}
SITES = {"en": ROOT / "index.html", "nl": ROOT / "nl/index.html"}
KITS = {"en": ROOT / "1794403769453_The Newborn Nomads – Media Kit EN.pdf",
        "nl": ROOT / "1794403769452_The Newborn Nomads – Mediakit NL.pdf"}

# ---------------- site ----------------
START, END = "<!-- BRANDS:START (gegenereerd door tools/build_brands.py) -->", "<!-- BRANDS:END -->"

def tiles(items):
    return "".join(f'        <div class="brand-logo"><img src="/brands/{b["id"]}.png" alt="{html.escape(b["name"])}" loading="lazy"></div>\n' for b in items)

def site_block(lang):
    t = TXT[lang]
    out = [START, '    <div class="brands">',
           f'      <p class="brands-label">{html.escape(t["worked"])}</p>',
           '      <div class="brands-grid">', tiles(WORKED).rstrip("\n"), '      </div>']
    if UPCOMING:
        out += [f'      <p class="brands-label" style="margin-top:2.4rem">{html.escape(t["upcoming"])}</p>',
                '      <div class="brands-grid">', tiles(UPCOMING).rstrip("\n"), '      </div>']
    out += ['    </div>', "    " + END]
    return "\n".join(out)

def build_site(lang):
    p = SITES[lang]; s = p.read_text(encoding="utf-8")
    if START not in s:  # eerste keer: bestaand <div class="brands"> vervangen
        i = s.index('    <div class="brands">')
        j = s.index("\n    </div>\n", s.index('<div class="brands-grid">', i)) + len("\n    </div>\n")
        s = s[:i] + "    " + START + "\n" + s[j:]
        s = s.replace("    " + START + "\n", "    " + START + "\n    " + END + "\n", 1)
    i, j = s.index(START), s.index(END) + len(END)
    s = s[:i] + site_block(lang).removeprefix("") [len(""):] + s[j:] if False else s[:i] + site_block(lang) + s[j:]
    p.write_text(s, encoding="utf-8"); print("site", lang, len(WORKED), "+", len(UPCOMING))

# ---------------- mediakit (pagina 3) ----------------
PAGEBG = (0.964706, 0.941176, 0.894118)
TILE = (0.937255, 0.905882, 0.847059)
LINE = (0.788235, 0.733333, 0.627451)
LABEL = (0x7F / 255, 0x85 / 255, 0x69 / 255)
X0, X1 = 51.0, 544.2756
PER_ROW, GAP, TH = 8, 6, 28
ROW1_Y, LABEL2_Y, ROW2_Y = 596.5, 636.0, 641.5   # blok "See the films" begint op 677.4

def plex():
    f = TTFont(str(ROOT / "mediakit-bron/fonts/ibm-plex-mono-latin-400-normal.woff2")); f.flavor = None
    buf = io.BytesIO(); f.save(buf); return buf.getvalue()

def tracked(page, x, y, text, size=7, track=1.68, right=False, fontbuf=None):
    font = fitz.Font(fontbuffer=fontbuf)
    w = sum(font.text_length(c, size) + track for c in text) - track
    if right: x -= w
    tw = fitz.TextWriter(page.rect)
    for c in text:
        tw.append((x, y), c, font=font, fontsize=size); x += font.text_length(c, size) + track
    tw.write_text(page, color=LABEL)

def tile_row(page, items, y):
    tw = (X1 - X0 - GAP * (PER_ROW - 1)) / PER_ROW
    for i, b in enumerate(items[:PER_ROW]):
        r = fitz.Rect(X0 + i * (tw + GAP), y, X0 + i * (tw + GAP) + tw, y + TH)
        page.draw_rect(r, color=LINE, fill=TILE, width=0.7, radius=5 / TH)
        png = ROOT / f"brands/{b['id']}.png"; pm = fitz.Pixmap(str(png))
        maxh = 18 if pm.width / pm.height < 1.85 else 13
        s = min((tw - 9) / pm.width, maxh / pm.height); w, h = pm.width * s, pm.height * s
        cx, cy = r.x0 + tw / 2, r.y0 + TH / 2
        page.insert_image(fitz.Rect(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), filename=str(png))

def build_kit(lang):
    t = TXT[lang]; path = KITS[lang]; d = fitz.open(path); p = d[2]
    p.add_redact_annot(fitz.Rect(45, 592, 550, 674), fill=PAGEBG)
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_REMOVE,
                       graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                       text=fitz.PDF_REDACT_TEXT_REMOVE)
    fb = plex()
    kw = [b for b in WORKED if b.get("kit")]; ku = [b for b in UPCOMING if b.get("kit")]
    tile_row(p, kw, ROW1_Y)
    if ku:
        tracked(p, X0, LABEL2_Y, t["kit_upcoming"], fontbuf=fb)
        hidden = len(WORKED) + len(UPCOMING) - len(kw[:PER_ROW]) - len(ku[:PER_ROW])
        if hidden > 0:
            tracked(p, X1, LABEL2_Y, t["more"].format(n=hidden), size=6.5, track=0.9, right=True, fontbuf=fb)
        tile_row(p, ku, ROW2_Y)
    tmp = path.with_suffix(".tmp.pdf"); d.save(tmp, garbage=4, deflate=True); d.close(); tmp.replace(path)
    print("kit", lang, len(kw), "+", len(ku))

if __name__ == "__main__":
    for lang in ("en", "nl"):
        build_site(lang); build_kit(lang)
