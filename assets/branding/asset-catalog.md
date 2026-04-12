# ROBOHOGAR — Asset Catalog

Catálogo vivo de todos los assets visuales generados. **Actualizar después de cada generación con Nano Banana.**

---

## Mascota — Poses (11/11 completadas)

| Pose | Archivo | master/ (2K) | flash-1K/ (1K) | Uso principal |
|---|---|---|---|---|
| Principal (café) | `robohogar-mascot-principal.png` | ✅ | ✅ | Avatar, og-image, favicon, redes sociales |
| A — Saludando | `robohogar-mascot-saludando.png` | ✅ | ✅ | Welcome email, onboarding, página "Sobre" |
| B — Con casita | `robohogar-mascot-casita.png` | ✅ | ✅ | Landing page hero, sección "Robots para el hogar" |
| C — Leyendo | `robohogar-mascot-leyendo.png` | ✅ | ✅ | Cabecera artículos, blog, roundups |
| E — Thumbs up | `robohogar-mascot-thumbsup.png` | ✅ | ✅ | Confirmación suscripción, CTAs, gracias |
| F — Detective | `robohogar-mascot-detective.png` | ✅ | ✅ | Análisis profundo, deep dives, investigación |
| G — Herramientas | `robohogar-mascot-herramientas.png` | ✅ | ✅ | Domótica, integración, setup, tutoriales |
| H — Megáfono | `robohogar-mascot-megafono.png` | ✅ | ✅ | Noticias, lanzamientos, alertas |
| I — Pensativo | `robohogar-mascot-pensativo.png` | ✅ | ✅ | Opinión, editorial, debates |
| J — Compras | `robohogar-mascot-compras.png` | ✅ | ✅ | Guías de compra, ofertas, afiliados Amazon |
| K — Trofeo | `robohogar-mascot-trofeo.png` | ✅ | ✅ | "Robot del mes", rankings, premios |

## Mascota — En contexto

| Archivo | Carpeta | Descripción |
|---|---|---|
| `robohogar-mascot-referencia.png` | `con-fondo/` | Mascota en contexto hogar — usada como `--reference` para anclar estilo |

## Artículos / General

| Archivo | Carpeta | Fecha | Descripción |
|---|---|---|---|
| _(vacío)_ | `images/` | — | Aún no hay imágenes de artículos |

---

## Estructura de carpetas

| Carpeta | Resolución | Propósito |
|---|---|---|
| `assets/branding/master/` | 2K | Assets definitivos — web, landing, print, social cards |
| `assets/branding/flash-1K/` | 1K | Borradores, previews rápidos, tests |
| `assets/branding/con-fondo/` | Variable | Mascota en escenas/contextos — referencias de estilo |
| `assets/images/` | Variable | Imágenes para artículos, banners, newsletter |

## Reglas

- **NUNCA sobrescribir** un archivo existente — usar sufijo versionado (-v2, -v3)
- **SIEMPRE actualizar este catálogo** después de generar una imagen nueva
- Antes de generar, revisar este catálogo para evitar duplicados
- Nuevas poses de mascota → `master/` (modelo 2/pro) + `flash-1K/` (modelo flash)
- Imágenes de artículos → `images/` con nombre descriptivo en kebab-case
