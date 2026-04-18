# Template master — ROBOHOGAR

**Único template canónico:** `content/templates/articulo-beehiiv-master.html`.

Exportado desde Beehiiv tras la publicación del review Samsung Jet Bot Steam Ultra (2026-04-18). Incluye la última iteración de **formato, CTAs, footer, tagline landing y estilos inline** — aplicar a TODO tipo de artículo nuevo (review, comparativa, editorial, guía, newsletter). No hay templates por tipo de contenido — la estructura se adapta al tipo variando los bloques internos, no el esqueleto.

## Cómo se usa

1. Copiar `articulo-beehiiv-master.html` como base del nuevo borrador.
2. Reemplazar:
   - `<title>` + H1 con título del nuevo artículo
   - Subtítulo, autor/fecha/tiempo de lectura
   - Cuerpo (H2 + párrafos + tablas + imágenes)
   - Bloques internos según tipo (review = producto por producto; comparativa = tabla + ranking; editorial = tesis + desarrollo + cierre; guía = pasos numerados)
3. **Mantener intactos:** hero image slot, intro callout ámbar, separadores `<hr>`, CTA mid-article ámbar, CTA final de suscripción, footer con trust text `100% gratis · Sin spam · Cancela cuando quieras`, links sociales.
4. Validar render en móvil 375px antes de publicar (regla `design.md`).

## Cuándo actualizar este master

Cuando Rafael publique un artículo con **cambios de formato significativos respecto al master actual** (nuevo tipo de bloque, rediseño de CTA, cambio de footer, reestructura de trust text):

1. Exportar el HTML final desde Beehiiv.
2. Archivar el master actual como `_archive/articulo-beehiiv-master-YYYY-MM-DD.html` (no borrar — versionado histórico).
3. Guardar el nuevo export como `articulo-beehiiv-master.html`.
4. Actualizar este documento con la fecha del nuevo master y los cambios principales.

## Historial de masters

| Fecha | Origen (artículo publicado) | Cambios vs master anterior |
|---|---|---|
| 2026-04-18 | Samsung Jet Bot Steam Ultra review | Master inicial unificado. Sustituye los 2 templates anteriores (`review-comparativa-beehiiv-export.html` + `editorial-opinion-beehiiv-export.html`). Incluye tagline landing nuevo (`Cada semana, comparativas, reviews, editoriales y relatos`), trust text solo en footer, tablas mobile-first (máx 4 cols), política de negritas actualizada (col 1 tbody sí, resto tablas y headings no). |

## Archivo

Los 2 templates anteriores (review-comparativa, editorial-opinion) + el `.md` descriptivo viven en `_archive/` con fecha. Son referencia histórica; no usar para borradores nuevos.

## Checklist PASOS.md

Seguir usando `PASOS-template.md` (no se ha consolidado con este master — son piezas distintas: PASOS.md es el checklist de publicación, el HTML master es el esqueleto del borrador).
