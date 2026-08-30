# newbornnomads

Bron van [thenewbornnomads.com](https://thenewbornnomads.com), gehost op Netlify
(project `whimsical-platypus-ef39e0`).

Statische site: één `index.html` plus twee afbeeldingen. Er is **geen buildstap** —
wat hier staat wordt direct gedeployed.

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
