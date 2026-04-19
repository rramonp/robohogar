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

## Tags Beehiiv ROBOHOGAR (plan Scale)

Tabla única de tags. `/post-publish` paso 5.5 los asigna según `frontmatter.category` y tangibles referenciados en el artículo.

| Tag | Quién lo asigna | Cuándo | Automation que dispara |
|---|---|---|---|
| `newsletter-general` | Beehiiv (default signup) | Todo suscriptor nuevo | Welcome flow MVP 2 emails |
| `aspirador` | `/post-publish` | Artículo con `category: aspirador` | (futuro) secuencia aspirador |
| `cortacésped` | `/post-publish` | Artículo con `category: cortacésped` | — |
| `humanoide` | `/post-publish` | `category: humanoide` | — |
| `mascota-robot` | `/post-publish` | `category: mascota-robot` | — |
| `fregasuelos` | `/post-publish` | `category: fregasuelos` | — |
| `limpia-cristales` | `/post-publish` | `category: limpia-cristales` | — |
| `ficciones` | `/post-publish` | `category: ficcion` | (futuro) secuencia ficción quincenal |
| `tangible-hoja-compra` | Beehiiv Digital Product (auto-tag al descargar) | Suscriptor descarga Hoja de Compra | Email delivery PDF + welcome variant |
| `tangible-guia-primer-mes` | Beehiiv Digital Product | Descarga Guía primer mes (cuando variante `guia` de `/pdf-brand` esté activa) | — |

**Regla:** al introducir una categoría de contenido nueva o un tangible nuevo, añadir la fila aquí PRIMERO; luego `/post-publish` y Beehiiv automation. Si no está en esta tabla, no existe.

## Welcome flow MVP (2 emails, plan Scale activo)

- **Email 0 (Double Opt-In):** plain-text Beehiiv default.
- **Email 1 (Welcome):** plain-text, CTA al tangible descargado (si vino por lead magnet) o a los 3 artículos más recientes (si signup orgánico). Detalle: `docs/welcome-flow-setup.md`.
- **Expansión a 4 emails:** diferida hasta ≥200 subs + open rate welcome >50% estable (memoria `feedback_welcome_flow_mvp.md`).

## Reglas de automatización

- NUNCA publicar contenido auto-generado sin revisión manual de Rafael
- Scripts deben ser idempotentes (re-ejecutar no duplica)
- Outputs intermedios van a `content/drafts/` con fecha en filename
- Logs a stdout, no a archivos
