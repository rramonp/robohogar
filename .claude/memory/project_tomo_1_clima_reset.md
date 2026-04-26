---
name: Tomo 1 = clímax Reset → carpeta de archivo pre-Tomo 1
description: El detonante del Tomo 1 de la novela serializada es el Día 1 del Gran Reset. Relatos que lo spoilean se RESERVAN en _archive-pre-tomo-1/, no se descartan.
type: project
---

**Decisión editorial (Rafael 2026-04-26):** la novela serializada que va a montarse a partir del universo `el-gran-reset` cierra el Tomo 1 con el detonante del Reset (Día 1: cae el sistema financiero global, redes 4G/5G a mediodía, apagón eléctrico al atardecer). Ese clímax debe protegerse — los relatos cortos del newsletter que ocurren *durante* o *después* del Día 1 actúan como spoilers del libro y NO pueden publicarse antes del lanzamiento del Tomo 1.

**Why:** el universo `el-gran-reset` ya tiene world-bible canon en [`references/ficciones/world-bibles/el-gran-reset.md`](../../../references/ficciones/world-bibles/el-gran-reset.md) y al menos un relato terminado editorialmente (*La Unidad*, v3 cinematográfico). Publicar un relato que dramatice in medias res el Día 1 — y que en el bloque "Lo real detrás del relato" lo nombre explícitamente — quemaría el cliffhanger del libro entero. La novela depende de que el Reset llegue como ruptura percibida, no como evento ya conocido por el lector.

**How to apply:**

1. **Carpeta dedicada:** [`content/ficciones/_archive-pre-tomo-1/`](../../../content/ficciones/_archive-pre-tomo-1/) reserva relatos terminados que NO se publican por spoiler de Tomo 1. Distinto de `_descartados/` (relatos que NO funcionaron) y de "Drafts experimentales" del registro (relatos pendientes de decisión). README explica diferencias y operativa.
2. **Trigger de archivado:** cuando un relato terminado dramatiza el Día 1 del Reset, lo nombra en "Lo real detrás del relato", o ocurre en el período que el Tomo 1 va a cubrir (~21 horas Día 1 según setting `el-gran-reset` § 2) → mover a `_archive-pre-tomo-1/<universo>/` con `git mv` (preserva historia).
3. **World-bibles NO se mueven:** [`references/ficciones/world-bibles/el-gran-reset.md`](../../../references/ficciones/world-bibles/el-gran-reset.md) y bibles equivalentes de otros universos archivados son setting maestro del Tomo 1 y se siguen usando activamente — quedan donde están.
4. **Audiolibro Eleven Reader del vault Obsidian:** mover a `02-Drafts/Ficciones/_archive-pre-tomo-1/` para mantener simetría visual entre repo y vault. Ruta vault resoluble vía `python utilities/get_vault_path.py`.
5. **Registro:** sale de "Drafts experimentales" en [`content/registro-ficciones.md`](../../../content/registro-ficciones.md) y entra en sección dedicada **Archivo pre-Tomo 1 (no publicar hasta lanzamiento)** con columnas: fecha archivo · título · slug · universo · razón de archivo · estado.
6. **Tres caminos editoriales si Rafael no quiere desperdiciar el material:**
   - **(1) Reservar tal cual** → cold open / Capítulo 0 del Tomo 2, o bonus del ebook recopilatorio post-Tomo 1. Default elegido para *La Unidad* el 2026-04-26.
   - **(2) Reubicar** → reescribir el detonante a un evento más pequeño y verosímil (apagón regional, ransomware acotado a una entidad bancaria) y publicar como ficción doméstica suelta. Coste: ~30% reescritura del relato + reescritura entera del bloque "Lo real detrás".
   - **(3) Mover al Tomo 2** → reescribir como mundo post-colapso ya estabilizado. Coste: casi reescritura completa, pero queda asset preparado para Tomo 2.

**Cuándo desarchivar:**

- Cuando el Tomo 1 esté publicado (o cuando su clímax sea conocimiento público de la base lectora), el relato puede pasar a publicación normal en newsletter, o entrar al ebook bonus, según convenga.
- Si la cronología del universo cambia en revisiones futuras y el relato deja de spoilear, también puede desarchivarse.

**Inventario actual:**

| Universo | Relato | Razón | Fecha archivo |
|---|---|---|---|
| `el-gran-reset` | `2026-04-26-la-unidad.md` (v3 cinematográfico, 2780 palabras) | Dramatiza in medias res el Día 1 del Reset; el bloque "Lo real detrás del relato" lo nombra explícitamente como tal. | 2026-04-26 |

Cualquier relato futuro que entre al universo `el-gran-reset` o que toque el Día 1 / primeras 72 horas según setting maestro va al mismo destino salvo que se reescriba a (2) o (3).
