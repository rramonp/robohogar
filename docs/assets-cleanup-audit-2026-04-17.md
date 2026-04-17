# Auditoría de referencias rotas — cleanup de assets 2026-04-17

**Commit cleanup:** `03923fd`
**Archivos borrados:** 62 · **Nuevos:** 14
**Fecha auditoría:** 2026-04-17

## Resumen ejecutivo

- Total ficheros con referencias al conjunto borrado: **12**
- 🔴 Críticas: **0**
- 🟡 Secundarias: **4** (3 docs estratégicos + 1 catálogo de needs)
- 🟢 Históricas / ya resueltas por convivir en `master/`: **4** (incluye `landing.html` y artículos publicados)
- ⚪ Menciones en texto: **1**
- 🔵 Self-references en catálogos (asset-catalog.md, mascota-prompt.md, BRAND-DECK.md, BRAND-DECK-generate.sh): **4**

**Veredicto:** [X] Repo OK — sin rupturas críticas. Hay limpieza cosmética pendiente en docs/ y catálogos.

---

## Observaciones clave (leer primero)

1. **Las 11 mascotas borradas de `flash-1K/` tienen gemelas con el mismo basename en `master/`.** Cualquier referencia que resolvía a `flash-1K/robohogar-mascot-*.png` ya no existe, PERO no hemos encontrado NINGUNA ruta codificada a `flash-1K/`. Todas las referencias activas usan `master/…mismo-nombre…png` → siguen resolviendo.
2. **`assets/landing.html` es seguro.** Sus 5 `<img src="branding/master/robohogar-mascot-*.png">` (detective, saludando, leyendo, trofeo, herramientas) apuntan a `master/`, donde los ficheros siguen existiendo.
3. **Los 2 artículos publicados** (`content/published/2026-04-15-*.html`, `2026-04-16-*.html`) y sus borradores (`content/articulos/*/borrador.html`) sólo contienen URLs al CDN de Beehiiv (`media.beehiiv.com/.../robohogar-logo-icon-v6.png`). Nada depende del repo local.
4. **`BRAND-DECK.md` + `BRAND-DECK-generate.sh`** son el script de generación histórica del brand deck (rutas de **salida**, no de entrada). Las salidas borradas ya no se re-generan; el fichero hoy es documentación del proceso de generación ejecutado una vez. No hay imágenes huérfanas que ningún consumidor cargue.

---

## 🔴 Hallazgos críticos (arreglar YA)

*Ninguno.* No existe ningún HTML/template/skill activo que intente cargar un asset borrado por ruta local.

---

## 🟡 Hallazgos secundarios

### 1. `docs/guia-implementacion.md:248`
- **Asset roto:** `social-card-template.png` (1080x1080)
- **Cita exacta:** `| **Social card template** | \`social-card-template.png\` (1080x1080) | Compartir artículos en redes | P2 |`
- **Reemplazo sugerido:** `social-card-template-v2.png` (existe en `assets/images/`)
- **Acción:** reemplazar referencia por `-v2.png`

### 2. `docs/assets-needed.md:30`
- **Asset roto:** `social-card-template.png`
- **Cita exacta:** `| \`social-card-template.png\` | 1080x1080 | Template cuadrado para posts sociales. Mascota esquina inferior, espacio para titular. Acento #F5A623. | \`mascot-megafono\` |`
- **Reemplazo sugerido:** `social-card-template-v2.png`
- **Acción:** actualizar — o marcar la línea como "ya cubierto" y moverla a la sección de hecho. Fichero parece ser un "to-do list" de assets — la fila corresponde a un asset ya generado (v2).

### 3. `assets/branding/mascota-prompt.md` (líneas 77-173)
- **Asset roto:** 11 mascotas catalogadas como `robohogar-mascot-<nombre>.png` sin prefijo de carpeta
- **Cita exacta:** e.g. `### Principal — Con café (\`robohogar-mascot-principal.png\`)`
- **Reemplazo sugerido:** añadir explícitamente el prefijo `master/` o al menos una nota "ahora viven en `master/` (las copias de `flash-1K/` se han eliminado)"
- **Acción:** clarificar ruta única. Como texto catálogo es tolerable, pero es engañoso.

### 4. `docs/guia-implementacion.md:46, 143` y `docs/plan-v2.md:48`
- **Asset roto:** NINGUNO técnicamente. Las rutas apuntan a `assets/branding/master/robohogar-mascot-principal.png` y `…leyendo.png`, que **existen** en `master/`.
- **Nota:** listadas aquí sólo porque los mismos basenames fueron borrados en `flash-1K/`. Si Rafael en el futuro mueve los ficheros de master/ a otra subcarpeta, estos tres puntos se romperán. Monitor only.
- **Acción:** ninguna ahora.

---

## 🟢 Históricas (informativo, NO arreglar)

| Archivo origen | Refs. | Nota |
|---|---|---|
| `assets/landing.html` | 6 | Todas resuelven a `master/` — los basenames borrados de `flash-1K/` conviven en `master/` |
| `content/published/2026-04-15-humanoides-en-casa-cuanto-falta.html` | 2 | Sólo URLs CDN de Beehiiv (`robohogar-logo-icon-v6.png`), no depende del repo |
| `content/published/2026-04-16-roborock-saros-z70-review.html` | 2 | Idem |
| `content/articulos/*/borrador.html` (2 ficheros) | 4 | Idem — export Beehiiv, toda imagen ya está en su CDN |
| `content/templates/review-comparativa-beehiiv-export.html` | 3 | 1 menciona `robohogar-mascot-casita.png` pero es URL CDN de Beehiiv ya subida; las otras dos son del logo icon-v6 CDN |
| `.claude/commands/nano-banana.md:49` | 1 | `master/robohogar-mascot-principal.png` — existe |
| `.claude/memory/project_landing_fase1.md:57` | 1 | `master/robohogar-mascot-principal-tight.png` — existe |
| `.claude/rules/design.md:22` | 1 | `master/robohogar-logo-monogram-v11.png/jpg` — existe |

---

## ⚪ Menciones en texto (OK)

- `references/writewithai/extractions/images.md:34` — "Logo monogram R (robohogar-logo-monogram-v11)" — menciona el superviviente, no el borrado.

---

## 🔵 Auto-referencias en catálogos y scripts de generación

Listado para que Rafael decida si limpia ahora o después. **Expectativa:** un catálogo que documenta assets debería limpiarse tras una purga.

### `assets/branding/asset-catalog.md` (fichero canónico del catálogo)
Entradas obsoletas que referencian archivos borrados:
- L.11-21: 11 filas de mascotas (todas usan el mismo basename que la versión `master/` superviviente — ambiguo, conviene dejar explícito que el path canónico es `master/`)
- L.36 `robohogar-logo-lockup-horizontal-white.jpg` — reemplazo: `robohogar-logo-lockup-horizontal-white.png` o `.jpg` (hay ambos en master/ hoy) ✓ verificar casing
- L.37 `robohogar-logo-badge-white.jpg` — sólo queda `.png` ahora (reemplazar extensión)
- L.340-346 tabla logos: entradas `robohogar-logo-lockup-horizontal.png`, `-v2.png`, `robohogar-logo-badge.png`, `robohogar-logo-monogram.png`, `-v2.png`, `robohogar-logo-header-dark.png` → borradas. Reemplazo: v11 (monogram), `-v2/-white` (badge/lockup), `header-v3-bahnschrift.png` (header)
- L.387-393 tabla youtube: 6 filas (`youtube-banner.png`, `…-endcard`, `…-lower-third`, `…-watermark`, `…-thumb-vs`, `…-thumb-editorial`) → no hay reemplazo, borrar tabla o marcar "pendiente de regenerar"
- L.399-402 patterns (3 filas) → reemplazo parcial por `pattern-hexagon-tech.png`
- L.411-417 iconos v1 (6 filas) → reemplazo directo por `-v2.png` ya existentes
- L.426, L.436 `email-cta-button.png`, `cta-banner-wide.png` → reemplazo: `email-cta-button-v2.png` (existe); `cta-banner-wide` no tiene reemplazo directo (sí hay `cta-banner-inline.png`/`-square.png`)
- L.443-450 tabla slides (8 filas) → ninguna reemplazo, eliminar tabla

### `assets/branding/mascota-prompt.md`
Ya listado en 🟡 #3 — catálogo con basenames sueltos; añadir prefijo `master/`.

### `BRAND-DECK.md`
40+ referencias como `--reference assets/branding/master/robohogar-mascot-*.png` y comandos `generate "assets/branding/slides/slide-0X-*.png" …` Es el **mega-script histórico** de generación (la fuente de por qué se crearon los ficheros borrados). Como documentación de proceso se puede conservar; como ejecutable está obsoleto. Recomendación: añadir banner en cabecera: "⚠️ Histórico — assets generados aquí fueron purgados en commit 03923fd. No re-ejecutar sin revisar."

### `BRAND-DECK-generate.sh`
Hermano de lo anterior — shell script que genera todos los slides, YouTube banner, patterns, iconos v1, email-cta, cta-banner-wide. Rafael debería decidir: ¿se borra el `.sh` (ya no se re-ejecuta), se archiva a `utilities/_archive/`, o se conserva como referencia?

---

## Recomendación priorizada

1. **[2 min]** 🟡 `docs/guia-implementacion.md:248` y `docs/assets-needed.md:30` → reemplazar `social-card-template.png` por `social-card-template-v2.png` (o mover la fila de assets-needed a "hecho").
2. **[5 min]** 🟡 `assets/branding/mascota-prompt.md` → añadir nota al principio: "Todos los paths son relativos a `assets/branding/master/`; las copias de `flash-1K/` se eliminaron en 03923fd".
3. **[10-15 min]** 🔵 Limpieza `assets/branding/asset-catalog.md` — eliminar/actualizar filas de: tabla youtube (L.387-393), tabla slides (L.443-450), tabla logos obsoletos (L.340-346 → apuntar a v11/v2/white/header-v3), patterns v1 (L.399-402), iconos v1 (L.411-417 → apuntar a `-v2`), banners CTA/email (L.426, L.436). Este catálogo ES el source of truth de branding, conviene mantenerlo al día.
4. **[Opcional]** Archivar `BRAND-DECK-generate.sh` a `utilities/_archive/` o añadir header de "histórico" a `BRAND-DECK.md`. No urgente — nadie lo re-ejecuta automáticamente.

**No hay trabajo bloqueante.** El repo renderiza correctamente, la landing está OK, los artículos publicados no dependen de nada local.
