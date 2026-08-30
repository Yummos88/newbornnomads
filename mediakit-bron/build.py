from weasyprint import HTML
HTML('mediakit.html', base_url='.').write_pdf('TheNewbornNomads-MediaKit-2026-08.pdf')
print("done")
