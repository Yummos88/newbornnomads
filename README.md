# newbornnomads

Bron van [thenewbornnomads.com](https://thenewbornnomads.com), gehost op **GitHub Pages**
(vanaf branch `main`, map `/`).

Statische site: `index.html`, de Nederlandse versie in `nl/`, twee foto's en de PDF's.
Er is **geen buildstap** — wat hier staat wordt direct gedeployed. Elke push naar `main`
zet de site binnen ongeveer een minuut live.

`CNAME` bevat het domein en `.nojekyll` schakelt Jekyll-verwerking uit; die twee
bestanden niet verwijderen.

## "CURRENTLY IN" bijwerken

De locatietekst staat op **twee plekken** in het blok `<div class="hero-meta">`:

- `index.html` (Engels): `CURRENTLY IN <b>The Netherlands</b>`
- `nl/index.html` (Nederlands): `NU IN <b>Nederland</b>`

Pas de plaatsnaam tussen `<b>…</b>` op beide plekken aan en push naar `main`;
Netlify deployt automatisch.

## Nederlandse versie

`nl/index.html` is de Nederlandse vertaling van de site (bereikbaar via `/nl/`,
schakelaar rechtsboven). Zelfde lay-out, vertaalde teksten, plus een extra blok
"Nederlands gesproken" met een leeg telefoonframe — vervang de placeholder daar
door een Vimeo-embed zodra de eerste Nederlandse video klaar is.
Inhoudelijke wijzigingen aan de site altijd in **beide** bestanden doorvoeren.

## Media kit

De site linkt naar `TheNewbornNomads-MediaKit.pdf` (vaste bestandsnaam — die naam
niet wijzigen bij een nieuwe versie). De bron staat in `mediakit-bron/`:
pas `mediakit.html` aan en genereer de PDF opnieuw. Dat kan met WeasyPrint
(`python build.py`, vereist GTK op Windows) of met Chrome headless:

```
chrome --headless=new --no-pdf-header-footer --print-to-pdf=TheNewbornNomads-MediaKit.pdf mediakit-bron/mediakit.html
```

Gedateerde PDF-archieven (`TheNewbornNomads-MediaKit-*.pdf`) blijven buiten git.

## DNS

Het domein staat bij Hostinger. De site wijst naar GitHub Pages:

| Type  | Naam | Waarde |
|-------|------|--------|
| A     | @    | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 |
| CNAME | www  | yummos88.github.io |

De MX- en TXT-records van het domein horen bij Google-mail (`smtp.google.com` en het
SPF-record) — die **nooit** aanpassen bij een hostingwissel, anders stopt de e-mail.

## Merken (site + mediakit)

Alle merken staan in **`brands/brands.json`**, de logo's in `brands/<id>.png`
(transparante PNG in merkkleur, max ~120 px hoog). Per merk:

- `status`: `worked` (content geleverd) of `upcoming` (afgesproken, nog niet geleverd)
- `kit`: `true` = staat in de mediakit (max 8 per rij; de rest telt mee in "+N more")

Na een wijziging:

```
pip install pymupdf fonttools brotli
python tools/build_brands.py
```

Dat werkt de merkenblokken op `index.html` en `nl/index.html` bij (tussen de
`BRANDS:START`/`BRANDS:END`-markers) én pagina 3 van beide gelinkte mediakit-PDF's.
Merk van upcoming naar geleverd? Alleen `status` aanpassen en het script draaien.
