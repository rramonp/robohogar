# Automation Rules

## Principio

Automatizar todo EXCEPTO juicio editorial y voz. La opinión y personalidad son manuales siempre.

## Pipeline de contenido

```
RSS feeds → Agente Research → Research Digest .md
Rafael elige temas + ángulos → Agente Escritura → Borrador → Rafael edita → Publicar
Borrador listo → Agente Imágenes → Hero branded (1200x630) + catálogo actualizado
Publicación → Agente Social → Posts para LinkedIn, X, IG, WhatsApp → Buffer
```

Tabla de skills, inputs y outputs → `CLAUDE.md` sección "Skills del pipeline". Flujo detallado → `docs/plan-v2.md` sección 4.

## Hero image (resumen)

3 variantes por artículo (`flash`, `landscape`, `1K`), estilo product-hero cinematográfico, WebP para OG/redes. Imágenes inline = originales de fabricante. Reglas completas → `assets/branding/asset-catalog.md` + `assets/branding/nano-banana-prompt-base.md`.

## Estructura de carpetas por artículo

SIEMPRE: `content/articulos/<slug>/borrador.html` + `assets/hero-<slug>-v<N>.png`. Slug = URL slug SEO.

## Herramientas externas

| Tool | Función | Coste |
|---|---|---|
| Make.com | Orquestación RSS→Claude→Buffer | 9€/mes |
| Buffer | Programación social (LinkedIn, X, Threads) | 6€/mes |
| Firecrawl | Scraping (MCP + API) | Free tier 500 créditos/mes |
| Claude API | Categorización + generación borradores | ~$0.10/run |

## Reglas de automatización

- NUNCA publicar contenido auto-generado sin revisión manual de Rafael
- Scripts deben ser idempotentes (re-ejecutar no duplica)
- Outputs intermedios van a `content/drafts/` con fecha en filename
- Logs a stdout, no a archivos
