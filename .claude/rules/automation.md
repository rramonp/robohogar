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

Detalle completo: `docs/plan-v2.md` sección 4.

## Agentes

| Agente | Skill | Qué hace | Output |
|---|---|---|---|
| **Research** | `/research-digest` | Scrape RSS + Firecrawl, categoriza con Claude API | `content/drafts/YYYY-MM-DD-raw-digest.md` |
| **Escritura** | `/content-draft` | Genera borrador SEO desde digest seleccionado | `content/drafts/YYYY-MM-DD-slug.md` |
| **Imágenes** | `/nano-banana` | Genera hero branded por artículo, cataloga en `asset-catalog.md` | `assets/images/art-slug.png` |
| **Social** | `/social-content` | Genera posts adaptados por plataforma | Posts listos para Buffer |

Cada agente es invocable individualmente o como parte del pipeline semanal (FASE 7).

## Agente de imágenes

Resumen: 3 variantes hero por artículo (`flash`, `landscape`, `1K`), estilo product-hero cinematográfico, WebP para OG/redes. Imágenes inline = originales de fabricante.
Reglas completas de composición, prompts y estilo → `assets/branding/asset-catalog.md`.

## Estructura de carpetas por artículo

SIEMPRE: `content/articulos/<slug>/borrador.html` + `assets/hero-<slug>.png`. Slug = URL slug SEO.

## Herramientas externas

| Tool | Función | Coste |
|---|---|---|
| Make.com | Orquestación RSS→Claude→Buffer | 9€/mes |
| Buffer | Programación social (LinkedIn, X, Threads) | 6€/mes |
| Firecrawl | Scraping (MCP + API) | Free tier (500 créditos/mes) |
| Claude API | Categorización + generación borradores | ~$0.10/run |

## Reglas de automatización

- NUNCA publicar contenido auto-generado sin revisión manual de Rafael
- Scripts deben ser idempotentes (re-ejecutar no duplica)
- Outputs intermedios van a `content/drafts/` con fecha en filename
- Logs de ejecución a stdout, no a archivos (por ahora)
