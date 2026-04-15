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

## Agente de imágenes — reglas específicas

- Hero de artículo: estilo product-hero/YouTube thumbnail — SIN mascota, cinematográfico
- El producto/robot protagonista es el centro, iluminación dramática ámbar, contexto hogar
- Imágenes inline: usar originales de la fuente/fabricante (no generar)
- Cada imagen generada se registra en `assets/branding/asset-catalog.md`
- Consultar el catálogo ANTES de generar para evitar duplicados
- Modelo: `flash`. Aspect: `landscape`. Size: `1K`
- **Ruta de output por artículo:** `content/articulos/<slug>/assets/hero-<slug>.png`
- Templates genéricos (newsletter header, social card) → `assets/images/`
- Prompt base y reglas de estilo completas en `assets/branding/asset-catalog.md`

## Estructura de carpetas por artículo

Cada artículo tiene su propia carpeta con assets. SIEMPRE crear esta estructura:
```
content/articulos/<slug>/
  borrador.md
  assets/
    hero-<slug>.png
```
El slug viene del URL slug SEO definido en la guía de implementación.

## Scripts (utilities/)

- `research_aggregator.py` — fetch RSS, scrape con Firecrawl, categoriza con Claude API

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
