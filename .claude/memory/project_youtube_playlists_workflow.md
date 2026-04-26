---
name: Playlists YouTube de audiolibros — workflow + naming canónico
description: Sistema de playlists ROBOHOGAR (master + específicas con middot). Auto-asigna en cada upload public; backfill idempotente para mantenimiento.
type: project
---

**Decisión editorial (Rafael 2026-04-26):** los audiolibros de Ficciones Domésticas en el canal YouTube ROBOHOGAR se organizan en **playlists públicas** con esta arquitectura:

- **Master cronológica:** `Ficciones Domésticas` (ID `PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS`) — TODOS los relatos, en orden de inserción = orden de publicación.
- **Específica de standalones:** `Ficciones Domésticas · One-shots` (ID `PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon`).
- **Específica por serie** (creación lazy al primer episodio): `Ficciones Domésticas · <SerieDisplay>` con middot (` · `) coherente con la convención de títulos del skill.

**Why:** discovery primario del catálogo entero desde la master + descubrimiento por categoría desde las específicas. Algoritmo YouTube agrupa por strings repetidos en títulos/playlists. El middot coincide con el separador del título YouTube del skill (ej: *"La objeción · Cartas a MAIA #3 — Ficciones Domésticas"*) — coherencia visual entre nombres de playlist y nombres de vídeo.

**How to apply (operativa):**

1. **Cada upload `public` futuro** se autoasigna sin acción manual. [`utilities/upload_youtube.py`](../../../utilities/upload_youtube.py) llama a `assign_video_to_playlists()` tras `thumbnails.set`. Los uploads `--private` se saltan (las playlists son public).

2. **Routing** (en [`utilities/youtube_playlists.py § determine_target_playlists`](../../../utilities/youtube_playlists.py)):
   - SIEMPRE: master `Ficciones Domésticas`.
   - Si `frontmatter.serie` declara slug real (no placeholder) → playlist de la serie.
   - Else (placeholder YAML `null`/`~`/`None`, `_one-shots`, o campo vacío) → `Ficciones Domésticas · One-shots`. Ver `_normalized_serie()` para la lista de equivalencias.

3. **Para añadir una serie nueva al sistema** (ej: nueva serie `crisálida-azul`):
   - Editar [`utilities/audiobook_constants.py § SERIES_DISPLAY_NAMES`](../../../utilities/audiobook_constants.py) → añadir `"crisalida-azul": "Crisálida Azul"`.
   - Sin entrada explícita, fallback a Title-case del slug (`crisalida-azul` → `Crisalida Azul`) — funciona pero menos pulido.
   - El primer relato de la serie con audiolibro creará la playlist al subirse — no hay setup manual.

4. **Backfill / mantenimiento idempotente**: `python utilities/backfill_youtube_playlists.py` escanea todos los `distribucion-snapshot.md`, extrae videoId, lee frontmatter, asigna a playlists. Idempotente — re-ejecutar no duplica nada (ensure_playlist busca por título exacto, find_video_in_playlist filtra por playlistId+videoId antes de insertar). Flags útiles: `--dry-run` (lista qué haría sin tocar YouTube) · `--slug <X>` (procesar solo un relato).

5. **Cuándo invocar el backfill manualmente:**
   - Tras añadir una serie a `SERIES_DISPLAY_NAMES` si quieres re-encarrillar episodios ya distribuidos a la nueva playlist específica.
   - Si alguien borra una playlist desde YouTube Studio y queremos recrearla con todos los items.
   - Auditoría periódica para confirmar que cada vídeo está en sus playlists canónicas.

**Caveats técnicos no obvios:**

- **Race condition post-create**: tras `playlists.insert`, YouTube tarda ~1-3s en hacer la playlist findable por `playlistItems.list` o `.insert`. El helper lo cubre con `_insert_with_retry_on_404` (4 intentos con delay creciente 1.5s · 3.0s · 4.5s · 6.0s) y skipea el `find_video_in_playlist` cuando la playlist se acaba de crear (sabemos que está vacía). Sin esto, el primer vídeo en una playlist recién creada falla con `404 playlistNotFound`.
- **Privacy**: helper crea playlists `public` por default. Si en el futuro se necesitan privadas (drafts, listas de testing), pasar `privacy="private"` o `"unlisted"` a `ensure_playlist()`.
- **Orden dentro de la playlist**: default = orden de inserción al añadir vídeo (= orden de publicación si se añade al subir). Sin reordenamiento automático; cambios manuales desde YouTube Studio si quieres otro orden.
- **OAuth scopes**: el skill ya pide `youtube.upload + youtube + youtube.force-ssl` desde el setup inicial. No requiere re-consent para gestionar playlists.

**Coste API (irrelevante vs los 10.000 units/día):**

- Por relato nuevo en régimen estable: ~102 units (1 list playlists + 2*51 inserts = master + específica).
- Setup inicial con K playlists nuevas + N vídeos: 50*K (creates) + 50*N*2 (inserts) ≈ 350-500 units para canal pequeño. $0.
- Re-ejecución idempotente del backfill: ~3 units por vídeo (solo los list calls, todo skip path). Trivial.

**Inventario actual (2026-04-26 PM tarde):**

| Playlist | ID | Items | Privacy |
|---|---|---|---|
| `Ficciones Domésticas` (master) | `PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS` | 3 | public |
| `Ficciones Domésticas · One-shots` | `PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon` | 3 | public |

Vídeos asignados (orden de inserción cronológico):
1. `el-operador-nocturno` (OgWaX-rcVfU)
2. `el-que-viene-a-tomar-cafe` (rQsqXqj-Uyw)
3. `la-objecion` (BFliK-JcwGc)

**Documentación operativa**: [`@.claude/commands/audiobook-distribute.md § paso 4.5`](../../commands/audiobook-distribute.md). Snapshot template ampliado con bloque "Playlists asignadas" — los snapshots históricos pre-2026-04-26 fueron retroactivamente actualizados con sección `## Actualización 2026-04-26 — Playlists asignadas` añadida al final.
