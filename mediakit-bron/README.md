# The Newborn Nomads — Media Kit (bron)

PDF opnieuw genereren:

    pip install weasyprint
    python3 build.py

Bestanden:
  mediakit.html   de volledige kit (7 pagina's A4) — hier pas je tekst aan
  build.py        rendert mediakit.html naar PDF
  stamp.png       het stempellogo
  fonts/          Fraunces (koppen), Karla (tekst), IBM Plex Mono (labels)

Pagina's:
  1 Cover
  2 Waypoint 01 · Why us
  3 Waypoint 02 · Our work   <- categorieen als aanbod, geen stills
  4 Waypoint 03 · Our services
  5 Waypoint 04 · The road ahead
  6 Waypoint 05 · How it works
  7 Waypoint 06 · Contact

Let op:
- De kit toont geen losse films. Nieuwe video's zetten op de site
  (thenewbornnomads.com); de kit hoeft dan niet opnieuw gegenereerd te worden.
- Bestemmingen en periodes op pagina 5 staan in de SVG onder "ROAD AHEAD".
FOTO'S TOEVOEGEN (2 plekken)

  Leg de bestanden naast mediakit.html, bijvoorbeeld:
    gezinsfoto.jpg   liggend, minstens 1600px breed  -> cover
    portret.jpg      vierkant, minstens 900x900      -> pagina 2

  Cover, vervang:
    <div class="photo-slot">
      <span class="cap">Family photo - golden hour - travel context</span>
    </div>
  door:
    <div class="photo-slot has-photo">
      <img src="gezinsfoto.jpg" alt="The Newborn Nomads">
    </div>

  Pagina 2, vervang:
    <div class="photo-circle"><span class="cap">Family photo</span></div>
  door:
    <div class="photo-circle has-photo"><img src="portret.jpg" alt="The Newborn Nomads"></div>

  De has-photo-klasse haalt de stippellijn weg en laat het beeld het kader vullen.
  Daarna opnieuw: python3 build.py
