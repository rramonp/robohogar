"""
Aplica los 5 cambios sugeridos al template HTML exportado de Beehiiv.

Cambios:
1. Línea de specs rápidas (Precio/Suscripción/Lo clave) antes de Lo bueno
2. "Para quién es" cambia de H3 a párrafo en negrita
3. CTA mid-article después del primer producto
4. Fondo #F2F2F2 en el bloque de opinión (🤖 Mi opinión)
5. Sección "📚 Más en ROBOHOGAR" antes del footer

Input: C:/Users/bakal/Downloads/post-html-e8bf7d8a-6144-450f-9270-c8c00729ca74.html
Output: C:/Users/bakal/Downloads/template-review-comparativa-mejorado.html
"""

import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

INPUT = "C:/Users/bakal/Downloads/post-html-e8bf7d8a-6144-450f-9270-c8c00729ca74.html"
OUTPUT = "C:/Users/bakal/Downloads/template-review-comparativa-mejorado.html"

with open(INPUT, "r", encoding="utf-8") as f:
    html = f.read()

# --- CAMBIO 1: Specs rápidas antes de cada 👍 Lo bueno ---
# Párrafo con Precio / Suscripción / Lo clave
specs_html = (
    '<p style="font-family:\'Inter\',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;'
    'font-weight:400;color:#0C0C0C;font-size:16px;line-height:1.5;'
    'padding-bottom:12px;padding-top:12px;">'
    '<span class="bold">Precio:</span> ~XXX\u20ac \u00b7 '
    '<span class="bold">Suscripci\u00f3n:</span> S\u00ed/No \u00b7 '
    '<span class="bold">Lo clave:</span> [1 frase]</p>'
)

# Insertar specs antes de cada H3 que contenga "Lo bueno"
lo_bueno_pattern = re.compile(r'(<h3[^>]*>[^<]*\U0001f44d[^<]*Lo bueno[^<]*</h3>)', re.IGNORECASE)
matches = list(lo_bueno_pattern.finditer(html))
print(f"Cambio 1: Encontradas {len(matches)} secciones 'Lo bueno'")
for m in reversed(matches):
    html = html[:m.start()] + specs_html + html[m.start():]

# --- CAMBIO 2: "Para quién es" de H3 a párrafo bold ---
para_quien_pattern = re.compile(
    r'<h3[^>]*>[^<]*\U0001f4a1[^<]*Para\s+quien\s+es[^<]*</h3>',
    re.IGNORECASE
)
para_quien_replacement = (
    '<p style="font-family:\'Inter\',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;'
    'font-weight:700;color:#0C0C0C;font-size:16px;line-height:1.5;'
    'padding-bottom:12px;padding-top:16px;">'
    '\U0001f4a1 <span class="bold">Para qui\u00e9n es:</span></p>'
)
count2 = len(para_quien_pattern.findall(html))
html = para_quien_pattern.sub(para_quien_replacement, html)
print(f"Cambio 2: Reemplazadas {count2} secciones 'Para quién es'")

# --- CAMBIO 3: CTA mid-article después del primer producto ---
mid_cta_html = (
    '<table width="100%" cellpadding="0" cellspacing="0" border="0" '
    'style="margin:20px 0;">'
    '<tr><td style="background-color:#F2F2F2;border-radius:10px;padding:20px;'
    'text-align:center;">'
    '<p style="font-family:\'Inter\',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;'
    'font-style:italic;font-size:16px;line-height:1.5;color:#0C0C0C;'
    'padding:0;margin:0;">'
    '\u00bfTe est\u00e1 sirviendo? Publicamos esto cada 2 semanas.</p>'
    '<p style="padding:8px 0 0 0;margin:0;">'
    '<a href="https://robohogar.com" style="color:#F5A623 !important;'
    'font-weight:bold;text-decoration:none;'
    'font-family:\'Inter\',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;'
    'font-size:16px;">Suscr\u00edbete gratis \u2192</a></p>'
    '</td></tr></table>'
)

# Buscar la primera opinión (🤖 Mi opinión) y luego el primer divider después
# Nota: Beehiiv usa \xa0 (non-breaking space) entre el emoji y el texto
opinion_pattern = re.compile(r'\U0001f916[\s\xa0]*(?:<i>)?Mi opini\u00f3n', re.IGNORECASE)
opinion_match = opinion_pattern.search(html)
if opinion_match:
    # Buscar el siguiente divider/separator (border-top o hr) después de la opinión
    divider_search = re.search(r'(<table[^>]*>.*?border-top.*?</table>)', html[opinion_match.end():], re.DOTALL)
    if divider_search:
        insert_pos = opinion_match.end() + divider_search.end()
        html = html[:insert_pos] + mid_cta_html + html[insert_pos:]
        print("Cambio 3: CTA mid-article insertado después del primer producto")
    else:
        print("Cambio 3: WARN - No se encontró divider después de la primera opinión")
else:
    print("Cambio 3: WARN - No se encontró bloque de opinión")

# --- CAMBIO 4: Fondo en blockquote de opinión ---
# Envolver el contenedor de la opinión con fondo
opinion_container_pattern = re.compile(
    r'(<td[^>]*>)((?:<[^>]*>)*[\s\xa0]*\U0001f916[\s\xa0]*(?:<em>|<i>)?Mi opini\u00f3n:)',
    re.IGNORECASE
)
count4 = len(opinion_container_pattern.findall(html))
html = opinion_container_pattern.sub(
    r'\1<div style="background-color:#F2F2F2;border-radius:8px;padding:12px 16px;border-left:4px solid #F5A623;">\2',
    html
)
# Cerrar el div antes del cierre del td
if count4 > 0:
    # Buscar cada opinión y cerrar el div
    close_pattern = re.compile(
        r'(border-left:4px solid #F5A623;">.*?Mi opini\u00f3n:.*?</p>)',
        re.DOTALL
    )
    html = close_pattern.sub(r'\1</div>', html)
print(f"Cambio 4: Fondo aplicado a {count4} bloques de opinión")

# --- CAMBIO 5: Sección "Más en ROBOHOGAR" antes del Share/footer ---
mas_section_html = (
    '<table width="100%" cellpadding="0" cellspacing="0" border="0" '
    'style="margin:10px 0 20px 0;">'
    '<tr><td>'
    '<h2 style="font-family:\'DM Sans\',Lato,Montserrat,sans-serif;'
    'font-weight:600;font-size:24px;color:#0C0C0C;line-height:1;'
    'padding-bottom:4px;padding-top:16px;">'
    '\U0001f4da M\u00e1s en ROBOHOGAR</h2>'
    '<p style="font-family:\'Inter\',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;'
    'font-weight:400;color:#0C0C0C;font-size:16px;line-height:1.5;'
    'padding-bottom:6px;padding-top:12px;">'
    '\u2022 <a href="https://robohogar.com" style="color:#F5A623 !important;'
    'font-weight:bold;text-decoration:none;">T\u00edtulo art\u00edculo relacionado 1</a></p>'
    '<p style="font-family:\'Inter\',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;'
    'font-weight:400;color:#0C0C0C;font-size:16px;line-height:1.5;'
    'padding-bottom:12px;padding-top:6px;">'
    '\u2022 <a href="https://robohogar.com" style="color:#F5A623 !important;'
    'font-weight:bold;text-decoration:none;">T\u00edtulo art\u00edculo relacionado 2</a></p>'
    '</td></tr></table>'
)

# Insertar antes de "Share on" o del footer
share_pos = html.find("Share on")
if share_pos > 0:
    # Retroceder para encontrar el inicio de la tabla que contiene Share
    table_start = html.rfind("<table", 0, share_pos)
    if table_start > 0:
        html = html[:table_start] + mas_section_html + html[table_start:]
        print("Cambio 5: Sección 'Más en ROBOHOGAR' insertada antes del Share")
    else:
        print("Cambio 5: WARN - No se encontró tabla de Share")
else:
    print("Cambio 5: WARN - No se encontró 'Share on'")

# --- Guardar resultado ---
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nGuardado en: {OUTPUT}")
