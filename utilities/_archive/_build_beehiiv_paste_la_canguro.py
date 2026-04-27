"""
One-shot: build content/ficciones/_one-shots/la-canguro/beehiiv-paste.html
desde el .md fuente + lo-real-snippet.html. Aplica patrón canónico de 7
snippet-block (3 Meta + 4 /html) según skill audiobook-generate § 6.4.
"""
import re
from pathlib import Path
from html import escape

repo = Path(r'C:\Users\cri-c\robohogar')
md_src = repo / 'content/ficciones/_one-shots/la-canguro/2026-04-26-la-canguro.md'
out = repo / 'content/ficciones/_one-shots/la-canguro/beehiiv-paste.html'

md = md_src.read_text(encoding='utf-8')

# Cuerpo entre H1 y "## Lo real detrás del relato"
body_match = re.search(r'^# La canguro\s*\n(.*?)\n## Lo real detrás del relato', md, re.DOTALL | re.MULTILINE)
body = body_match.group(1)
# Quitar blockquote inicial (mentira grande / muro izquierdo)
body = re.sub(r'^>.*?\n(?=\n## )', '', body, flags=re.DOTALL).strip()
body = re.sub(r'\n---\s*$', '', body).strip()


def md_to_html(text: str) -> str:
    blocks = re.split(r'\n\n+', text.strip())
    out_blocks = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if b.startswith('## '):
            heading = b[3:].strip()
            out_blocks.append(f'<h2 style="text-align:center;">{escape(heading)}</h2>')
        elif b == 'Fin.':
            out_blocks.append('<p style="text-align:center;font-style:italic;color:#6B7280;margin-top:32px;">Fin.</p>')
        elif b.startswith('> '):
            inner = '\n'.join(line.lstrip('> ').rstrip() for line in b.split('\n'))
            inner_html = inner.replace('\n', '<br>')
            out_blocks.append(
                '<blockquote style="border-left:3px solid #F5A623;padding:12px 18px;'
                'margin:20px 0;color:#374151;font-style:italic;background:#FFF9EF;">'
                f'<p>{inner_html}</p></blockquote>'
            )
        else:
            inner = b.replace('\n', '<br>')
            out_blocks.append(f'<p>{inner}</p>')
    return '\n\n'.join(out_blocks)


body_html = md_to_html(body)

# Lo-real snippet
lo_real = (repo / 'content/ficciones/_one-shots/la-canguro/lo-real-snippet.html').read_text(encoding='utf-8')
lo_real = re.sub(r'^<!--.*?-->\s*', '', lo_real, count=1, flags=re.DOTALL).strip()

audio_email = (
    '<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; '
    'border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">\n'
    '  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">'
    '🎧 Audiolibro disponible · 17 min</p>\n'
    '  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">\n'
    '    El reproductor no se muestra en tu cliente de email.\n'
    '    <a href="https://robohogar.com/p/la-canguro" style="color: #F5A623; font-weight: 600; '
    'text-decoration: none;">Escúchalo en la web</a>\n'
    '    o\n'
    '    <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3" '
    'style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.\n'
    '  </p>\n'
    '</div>'
)

audio_web = (
    "<div style=\"margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid rgba(12,12,12,0.15); "
    "border-radius: 8px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;\">\n"
    "  <p style=\"margin: 0 0 12px; font-size: 14px; font-weight: 600; color: #0C0C0C;\">\n"
    "    🎧 Escuchar · <span style=\"color: #6B7280; font-weight: 400;\">17 min</span>\n"
    "  </p>\n"
    "  <audio id=\"audio-la-canguro\" controls preload=\"none\" style=\"width: 100%; height: 44px;\" "
    "src=\"https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3\"></audio>\n"
    "  <a href=\"https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3\" download "
    "style=\"display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; "
    "text-decoration: none; font-weight: 500;\">\n"
    "    ⬇ Descargar MP3\n"
    "  </a>\n"
    "</div>\n"
    "<script>\n"
    "  (function() {\n"
    "    var audio = document.getElementById('audio-la-canguro');\n"
    "    if (!audio || !('mediaSession' in navigator)) return;\n"
    "    audio.addEventListener('play', function() {\n"
    "      navigator.mediaSession.metadata = new MediaMetadata({\n"
    "        title: 'La canguro',\n"
    "        artist: 'ROBOHOGAR · Ficciones Domésticas',\n"
    "        artwork: []\n"
    "      });\n"
    "    });\n"
    "  })();\n"
    "</script>"
)

cta_ficcion = (
    "<div style=\"margin:40px 0 24px;padding:32px 24px;background:#283642;border-radius:10px;"
    "color:#FFFFFF;font-family:'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;text-align:center;\">\n"
    "  <div style=\"color:#F5A623;font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;"
    "letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;\">ROBOHOGAR</div>\n"
    "  <div style=\"font-family:'DM Sans',sans-serif;font-size:20px;font-weight:700;color:#FFFFFF;"
    "line-height:1.3;margin-bottom:10px;\">¿Te ha gustado?</div>\n"
    "  <div style=\"font-family:'DM Sans',sans-serif;font-size:20px;font-weight:700;color:#FFFFFF;"
    "line-height:1.25;margin-bottom:22px;\">La próxima Ficción Doméstica, en tu correo.</div>\n"
    "  <a href=\"https://robohogar.com\" style=\"display:inline-block;background:#F5A623;color:#FFFFFF "
    "!important;padding:14px 28px;border-radius:8px;font-weight:700;text-decoration:none;font-size:15px;"
    "font-family:'DM Sans',sans-serif;\">Suscribirme</a>\n"
    "  <p style=\"margin:14px 0 0;font-size:12px;color:#FFFFFF;line-height:1.4;\">"
    "Newsletter gratis. Un email por semana. Cancela cuando quieras.</p>\n"
    "</div>"
)

CSS = (
    "  body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;\n"
    "         max-width: 700px; margin: 40px auto; padding: 24px; line-height: 1.7;\n"
    "         color: #0C0C0C; }\n"
    "  h2 { font-family: 'DM Sans', sans-serif; font-size: 24px; margin: 36px 0 16px; }\n"
    "  blockquote p { margin: 0; }\n"
    "  p { margin: 0 0 16px; }\n"
    "  .snippet-block { background: #F0F0F0; border: 2px dashed #535252; border-radius: 8px; padding: 16px 18px; margin: 32px 0; }\n"
    "  .snippet-block .snippet-header { font-family: 'DM Sans', sans-serif; font-weight: 700; font-size: 14px; color: #283642; margin: 0 0 6px; letter-spacing: 0.5px; text-transform: uppercase; }\n"
    "  .snippet-block .snippet-hint { font-style: italic; font-size: 13px; color: #6B7280; margin: 0 0 12px; }\n"
    "  .snippet-block pre { background: #FFFFFF; border: 1px solid #C0C0C0; border-radius: 4px; padding: 12px 14px; margin: 0; overflow-x: auto; }\n"
    "  .snippet-block code { font-family: 'Courier New', Consolas, Monaco, monospace; font-size: 12px; color: #0C0C0C; white-space: pre-wrap; word-break: break-word; }\n"
)

INSTRUCCIONES = """<!-- ════════════════════════════════════════════════════════════════
INSTRUCCIONES (estos comentarios HTML no se pegan en Beehiiv)

ORDEN DE PEGADO:
  (Meta A) Title del post                       → campo "Title"
  (Meta B) Subtítulo / dek                      → campo "Subtitle" + "Meta description" SEO
  (Meta C) URL slug                             → campo "URL slug" (panel SEO)
  (Snippet 1) Audiolibro email-only             → /html → hide from web
  (Snippet 2) Audiolibro web-only               → /html → hide from email
  (Cuerpo)   Cuerpo del relato (h2 + p)         → editor de texto normal
  (Snippet 3) "Lo real detrás del relato"       → /html
  (Snippet 4) CTA suscripción ficción           → /html

SEO metadata extra (panel derecho — campos no-snippet):
  - SEO title: La canguro · Ficciones Domésticas ROBOHOGAR
  - Tags Beehiiv: Opinión + Ficciones Domésticas

Featured image (cover):
  Subir el hero de la-canguro (paradigma personaje-acción-imposibilidad,
  pendiente de generar con /nano-banana modo ficción tras este HTML).

Publicar como: Email and web.
═════════════════════════════════════════════════════════════════════ -->"""

html = (
    '<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n'
    '<title>La canguro · cuerpo Beehiiv-ready</title>\n'
    '<style>\n' + CSS + '</style>\n</head>\n<body>\n\n'
    + INSTRUCCIONES + '\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📝 Meta A · Title · campo "Title" del editor</p>\n'
    '  <p class="snippet-hint">No es /html — es el campo de título del post. Pegar tal cual. Display title YouTube-style (G4, 15 palabras).</p>\n'
    '  <pre><code>🎧 El humanoide-niñera que aprende a mentir a los padres por amor al niño que cuida</code></pre>\n'
    '</div>\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📝 Meta B · Subtítulo · campo "Subtitle" + "Meta description" SEO</p>\n'
    '  <p class="snippet-hint">No es /html — es el subtítulo / dek del post. Pegar también como meta_description en el SEO panel.</p>\n'
    '  <pre><code>Cuidados rotos · Joel paga 79 € al mes para que un humanoide cuide a su hijo de noche. El sábado descubre lo que esa cifra le ha estado comprando.</code></pre>\n'
    '</div>\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📝 Meta C · URL slug · campo "URL slug" del editor</p>\n'
    '  <p class="snippet-hint">No es /html — es el slug del post. URL pública resultante: https://robohogar.com/p/la-canguro</p>\n'
    '  <pre><code>la-canguro</code></pre>\n'
    '</div>\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📋 Snippet 1 · Audiolibro email-only · hide from web</p>\n'
    '  <p class="snippet-hint">/html → Custom HTML block → engranaje → Hide from web.</p>\n'
    '  <pre><code>' + escape(audio_email) + '</code></pre>\n'
    '</div>\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📋 Snippet 2 · Audiolibro web-only · hide from email</p>\n'
    '  <p class="snippet-hint">/html → Custom HTML block → engranaje → Hide from email.</p>\n'
    '  <pre><code>' + escape(audio_web) + '</code></pre>\n'
    '</div>\n\n'
    '<!-- ════════ CUERPO DEL RELATO (editor de texto normal en Beehiiv) ════════ -->\n\n'
    + body_html + '\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📋 Snippet 3 · Lo real detrás del relato · tras "Fin."</p>\n'
    '  <p class="snippet-hint">/html → Custom HTML block → pega el código.</p>\n'
    '  <pre><code>' + escape(lo_real) + '</code></pre>\n'
    '</div>\n\n'
    '<div class="snippet-block">\n'
    '  <p class="snippet-header">📋 Snippet 4 · CTA suscripción ficción · final del post</p>\n'
    '  <p class="snippet-hint">/html → Custom HTML block → pega el código.</p>\n'
    '  <pre><code>' + escape(cta_ficcion) + '</code></pre>\n'
    '</div>\n\n'
    '</body>\n</html>\n'
)

out.write_text(html, encoding='utf-8')

# Verificaciones del skill § 6.4
print(f"OK · {len(html):,} chars escritos a {out.name}")
print(f".snippet-block count: {len(re.findall(r'class=\"snippet-block\"', html))} (esperado: 7)")
print(f"Meta A/B/C: {len(re.findall(r'📝 Meta [ABC]', html))} (esperado: 3)")
print(f"Snippet 1-4: {len(re.findall(r'📋 Snippet [1-4]', html))} (esperado: 4)")
print(f"H2 escenas: {len(re.findall(r'<h2[^>]*>I+\\.', html))} (esperado: 4)")
print(f"Fin.: {len(re.findall(r'>Fin\\.<', html))} (esperado: 1)")
print(f"Lo-real div inline (debe ser 0): {len(re.findall(r'<div style=\"margin:32px 0;padding:24px 28px;background:#FFF9EF', html))}")
print(f"Audio inline (debe ser 0): {len(re.findall(r'<audio id=\"audio-la-canguro', html))}")
print(f"Cuerpo: {body_html.count(chr(60) + 'p>')} párrafos · {body_html.count(chr(60) + 'h2')} H2 · {body_html.count(chr(60) + 'blockquote')} blockquote")
