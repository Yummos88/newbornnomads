# newbornnomads

Bron van [thenewbornnomads.com](https://thenewbornnomads.com), gehost op Netlify
(project `whimsical-platypus-ef39e0`).

Statische site: één `index.html` plus twee afbeeldingen. Er is **geen buildstap** —
wat hier staat wordt direct gedeployed.

## "CURRENTLY IN" bijwerken

De locatietekst staat in `index.html` rond regel 302, in het blok
`<div class="hero-meta">`:

```html
<span class="pin">📍</span>CURRENTLY IN <b>Alphen aan den Rijn</b>
```

Pas de plaatsnaam tussen `<b>…</b>` aan en push naar `main`; Netlify deployt automatisch.

## Media kit

De site linkt naar `TheNewbornNomads-MediaKit.pdf` (vaste bestandsnaam — die naam
niet wijzigen bij een nieuwe versie). De bron staat in `mediakit-bron/`:
pas `mediakit.html` aan en genereer de PDF opnieuw. Dat kan met WeasyPrint
(`python build.py`, vereist GTK op Windows) of met Chrome headless:

```
chrome --headless=new --no-pdf-header-footer --print-to-pdf=TheNewbornNomads-MediaKit.pdf mediakit-bron/mediakit.html
```

Gedateerde PDF-archieven (`TheNewbornNomads-MediaKit-*.pdf`) blijven buiten git.
