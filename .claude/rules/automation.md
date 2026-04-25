# Automation Rules

## Principio

Automatizar todo EXCEPTO juicio editorial y voz. La opinión y personalidad son manuales siempre.

## Pipeline de contenido

```
RSS feeds → Agente Research → Research Digest .md
Rafael elige temas + ángulos → Agente Escritura → Borrador → Rafael edita → Publicar
Borrador listo → Agente Imágenes → Hero branded (1200x630) + catálogo actualizado
Publicación → Agente Social → Posts para LinkedIn, X, IG, WhatsApp → Buffer
Audiolibro publicado (ficción) → Skill Distribute → MP4 YouTube + episodio RSS → Spotify/Apple/Amazon
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

## Invariante — feed RSS nunca referencia 404 (audiolibros)

Antes de publicar `content/podcast/feed.xml` a R2, **TODOS los assets referenciados** por el feed (`<itunes:image>` del canal, `<itunes:image>` por episodio, `<enclosure url>` por episodio) deben existir en R2 con respuesta 200 OK desde el dominio público (`feed.robohogar.com`). Si alguno falta, el upload del feed se aborta — no se publica un feed con referencias rotas.

**Por qué es regla dura.** Cuando una plataforma de podcast (Apple, Spotify, Amazon) hace su primer fetch del feed nuevo y al pedir un asset recibe 404, la plataforma cachea ese fallo y a menudo sustituye con un fallback procedural (otra imagen, placeholder genérico, recurso scrapeado del `<link>`). Aunque el asset luego exista en R2, la plataforma puede tardar horas o días en re-pedirlo. Resultado: episodio publicado con la imagen incorrecta hasta que se invalide el cache de la plataforma. Incidente origen: 2026-04-25 con `el-que-viene-a-tomar-cafe` — Spotify cacheó un asset distinto al hero v5 porque el cover-podcast-1400x1400 dio 404 al primer fetch.

**Implementación.** [`utilities/validate_podcast_assets.py`](../../utilities/validate_podcast_assets.py) hace HEAD a cada URL referenciada. Modo `--heal` sube las que falten desde la ruta local canónica (vía REST API Cloudflare). Si una falta y no hay local → aborta con mensaje específico. Los dos uploaders del feed ([`upload_rss_to_r2.py`](../../utilities/upload_rss_to_r2.py) y [`upload_rss_to_r2_via_api.py`](../../utilities/upload_rss_to_r2_via_api.py)) invocan este validador como pre-step obligatorio antes del upload del feed.

**Mapeo de keys canónicas R2 → ruta local** (ampliar este mapeo en `validate_podcast_assets.py § derive_paths` cuando se añadan tipos nuevos al feed):

| Key R2 | Local |
|---|---|
| `<slug>.mp3` | `assets/audio/ficciones/<slug>.mp3` |
| `covers/<slug>-podcast-1400x1400.jpg` | `assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg` |
| `podcast-canal-artwork-3000x3000.jpg` | `assets/branding/podcast-canal-artwork-3000x3000.jpg` |

Si el feed gana un asset con key fuera de los patrones canónicos, el validador lo marca "no reparable" y aborta — eso fuerza a actualizar este mapeo en lugar de fallar silenciosamente ante las plataformas.

**Cache busting cuando una plataforma ya cacheó un fallback.** Si una plataforma ya tiene cacheado un asset incorrecto (por un 404 anterior), añadir `?v=N` a la URL en `feed.xml` fuerza a la plataforma a re-fetchearlo — el validador soporta query strings en URLs (los strip antes de derivar key/path).

**Descripción y título del episodio NO se actualizan al re-publish del feed.** Amazon Music y Apple Podcasts congelan la metadata del episodio (description, itunes:summary, title) en su catálogo interno al primer ingest. Re-publicar el feed con la descripción corregida NO la actualiza para los oyentes — Amazon/Apple usan el snapshot guardado al primer fetch. Spotify sí suele auto-refrescar, pero no garantizado.

  **Implicación operativa:** corregir typos / quitar líneas / añadir links en la descripción de un episodio YA publicado requiere editar manualmente en cada dashboard:
  - Amazon Music for Podcasters → `creators.amazon.com` → Episodios → Edit description.
  - Apple Podcasts Connect → `podcastsconnect.apple.com` → Episodes → Edit.
  - Spotify for Podcasters → `creators.spotify.com` → Episodes → Edit (suele propagarse solo, pero por si acaso).
  
  **No cambiar el `<guid>`** para forzar re-ingest: las plataformas tratarían el episodio como nuevo y el viejo quedaría zombi en la app del oyente.

  **Prevención:** revisar el copy de la descripción ANTES del primer publish (en `generate_podcast_rss.py § build_item_xml`). El skill `/audiobook-distribute` paso 5 puede mostrar la descripción al chat antes del upload del feed para revisión, igual que ya hace con la descripción de YouTube paso 3.
