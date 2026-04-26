# Obsidian ROBOHOGAR — Gestión de contenido editorial

Mantiene la sección ROBOHOGAR del vault de Obsidian: wiki, research, artículos,
calendario editorial. Skill autónomo — NO depende del vault-organizer de RRP-DEV.

## When to activate

- "actualiza obsidian", "sync vault", "wiki update", "organiza vault robohogar"
- "importa digest", "copia al vault", "actualiza wiki"
- "calendario editorial", "planifica issues", "periodic notes"
- "audita vault robohogar", "revisa obsidian"
- "archiva artículos viejos", "limpia vault"

## Vault Path

**Resolver SIEMPRE vía helper** (regla dura 2026-04-26):

```bash
VAULT=$(python utilities/get_vault_path.py)
```

`utilities/get_vault_path.py` autodetecta la ruta absoluta del vault Obsidian ROBOHOGAR sin depender de variables de entorno externas. El vault está sincronizado vía OneDrive HBX Group + Syncthing entre las dos máquinas de Rafael (laptop bakal · desktop cri-c) y SIEMPRE está accesible. Estrategias del helper (en orden): `$HBX_VAULT` → layouts conocidos hardcoded → autodetect por `$USERPROFILE` → búsqueda en OneDrive. Si una máquina nueva entra al pipeline, basta con añadir su ruta a `KNOWN_LAYOUTS` en el helper.

**Layouts canónicos:**
- Laptop (bakal): `C:\Users\bakal\OneDrive - HBX Group\Desktop\DEMAND\Obsidian\RRP\RRP_ONEDRIVE\HBX\05_Personal\05-01_Robotica Newsletter`
- Desktop (cri-c): `C:\Users\cri-c\OneDrive - HBX Group\Desktop\DEMAND\Obsidian\RRP\RRP_ONEDRIVE\HBX\05_Personal\05-01_Robotica Newsletter`

**Prohibido** (regla dura): usar literal `$HBX_VAULT/...` en bash o asumir que la variable está exportada en el shell. NO está. Usar siempre el helper.

**Incidente origen 2026-04-26:** durante un `/post-publish` el skill marcó "vault no accesible" porque `$HBX_VAULT` no resuelve en el shell de Bash que ejecuta Claude Code. Rafael lo confirmó: el vault SÍ está siempre accesible (Syncthing + OneDrive), el problema era exclusivamente la variable. Helper resuelve sin depender de ella.

## Estructura del vault

Subcarpetas principales de `05-01_Robotica Newsletter/`: `_archive/`, `02-Drafts/`, `03-Published/`, `06-Calendar/`, `Docs/` (setup operativo: welcome flow y similares), `Issues/`, `Metricas/`, `Research/` (+ `Clippings/`; aloja también los snapshots `Research Mercado ES.md` / `Research Mercado EN.md`), `Templates/`, `Wiki/` (`Robots/`, `Empresas/`, `Conceptos/`, `Mercado/`). MOC: `Proyecto ROBOHOGAR.md`.

## Modos de operación

### 1. `sync-published <slug>` — Umbrella post-publicación (invocado por `/post-publish` paso 12)

**Invocación:** `/obsidian-robohogar sync-published <slug-del-articulo>`

Ejecuta en orden las 3 acciones que el post-publish necesita tras publicar un artículo:

1. **Copiar artículo publicado** de `content/published/YYYY-MM-DD-<slug>.html` al vault `03-Published/` con el mismo nombre
   - Añade frontmatter si no tiene (type: published, tags, fecha)
   - Actualiza wikilinks internos a formato Obsidian `[[Page Name]]`
   - NO sobreescribe archivos existentes en el vault

2. **Auto-sync de los 5 archivos editoriales** (ver § "Archivos que SIEMPRE se sincronizan") — `guia-implementacion`, `plan-v2`, `registro-articulos`, `calendario-editorial`, `registro-newsletters`

3. **Invocar `wiki-update`** (mode 2) para crear/actualizar fichas de robots y empresas mencionados en el artículo publicado

**Output esperado:** resumen ✅/❌ de las 3 acciones. Si alguna falla, continuar con el resto y reportar el fallo.

### 2. `wiki-update` — Actualizar base de datos wiki

Escanea artículos recientes en `content/drafts/` y `content/published/`:
- Para cada robot/empresa mencionado:
  - Si NO existe nota → crear desde template (`Templates/Template Robot Wiki.md` o `Template Empresa Wiki.md`)
  - Si existe → añadir bullet: `- YYYY-MM-DD — [noticia/dato] (fuente: [[artículo]])`
- Paths: `Wiki/Robots/[Nombre Robot].md`, `Wiki/Empresas/[Nombre Empresa].md`
- Wikilinks bidireccionales: el artículo enlaza al robot, el robot enlaza al artículo

### 3. `digest-import` — Importar research digest

Copia el digest más reciente de `content/drafts/research-digest-*.md` al vault `Research/`.
- Usa template `Templates/Template Research Digest.md`
- Añade frontmatter con fecha, fuentes procesadas, categorías

### 4. `calendar-update` — Calendario editorial

Actualiza o crea nota mensual en `06-Calendar/`:
- Formato: `YYYY-MM Editorial.md`
- Contenido: issues planificados, artículos web, deadlines, temas pendientes
- Marca issues publicados como completados

### 5. `archive` — Archivar contenido antiguo

Mueve a `_archive/`:
- Research digests de hace >3 meses
- Borradores abandonados (>2 meses sin editar)
- NO archiva wiki entries (son acumulativas, siempre activas)
- NO archiva templates

### 6. `audit` — Auditoría del vault (read-only)

Escanea y reporta sin modificar:
- Archivos sin frontmatter
- Filenames >60 chars (rompen SyncThing)
- Wikilinks rotos `[[Page]]` que no apuntan a nada
- Notas huérfanas (sin backlinks)
- Carpetas vacías

### 7. `repo-mirror` — Mirror del repositorio al vault

Sincroniza el repo completo a `03_Resources/03-01_Claude/Repo Mirrors/ROBOHOGAR/` como notas Markdown navegables. Motor: `skills/vault_sync/repo_mirror.py` + `config.py`. Reconciliación incremental por hash SHA-256 (`--full` para rebuild completo).

```bash
python skills/vault_sync/repo_mirror.py [vault_path] [repo_path] [--full] [--dry-run]
```

## Archivos que SIEMPRE se sincronizan al vault

Al ejecutar CUALQUIER modo de este skill, sincronizar estos archivos del repo al área editorial del vault:

| Repo | Vault (editorial area) | Notas |
|------|-------|-------|
| `docs/guia-implementacion.md` | `Guia Implementacion.md` | Guía maestra del proyecto |
| `docs/plan-v2.md` | `Plan v2.md` | Estrategia macro 12 meses — consulta estratégica |
| `content/registro-articulos.md` | `Registro Articulos.md` | Catálogo de artículos publicados — fuente de verdad |
| `content/calendario-editorial.md` | `Calendario Editorial.md` | Cadencia semanal, backlog de temas, planificación |
| `content/registro-newsletters.md` | `Registro Newsletters.md` | Catálogo de newsletters enviados |

```bash
VAULT=$(python utilities/get_vault_path.py)
cp docs/guia-implementacion.md         "$VAULT/Guia Implementacion.md"
cp docs/plan-v2.md                     "$VAULT/Plan v2.md"
cp content/registro-articulos.md       "$VAULT/Registro Articulos.md"
cp content/calendario-editorial.md     "$VAULT/Calendario Editorial.md"
cp content/registro-newsletters.md     "$VAULT/Registro Newsletters.md"
```

**Importante:** los 5 archivos son fuente de verdad en el repo; el vault es mirror. CUALQUIER modo del skill debe sincronizar los 5, no solo los del ejemplo antiguo. Evita desfases como el detectado 2026-04-17 (calendario-editorial 5h atrás del repo). `Plan v2.md` añadido 2026-04-18 para consulta estratégica desde Obsidian (móvil/tablet incluidos).

**Nota:** estos archivos se copian al área editorial (05_Personal) para que Rafael los trabaje en Obsidian. El `repo-mirror` (Mode 7) los copia TAMBIÉN al área de mirror (03_Resources) como parte del backup completo. Ambas copias son válidas — editorial para uso diario, mirror para disaster recovery.

## Ejecución autónoma (sin modo específico)

Sin modo explícito → ejecutar en orden: 1) Sync always-sync files, 2) **Reconcile `03-Published/`**, 3) Repo mirror, 4) Audit, 5) Resumen.

### Reconcile `03-Published/` (paso 2 del modo autónomo)

Objetivo: detectar artículos en `content/published/` del repo que NO están en el vault `03-Published/` y copiarlos automáticamente. Evita que un fallo histórico de `/post-publish` paso 12 deje el vault desfasado indefinidamente.

**Lógica:**
- Listar todos los `.html` en `content/published/` del repo
- Listar todos los `.html` en `$VAULT/03-Published/`
- Para cada archivo presente en repo y ausente en vault → copiar sin sobreescribir
- Reportar los copiados en el resumen (sección "Reconcile")
- Si no hay desfases → reportar "`03-Published/` alineado (N archivos)"

**Implementación (bash, heredable por cualquier invocación autónoma):**

```bash
VAULT=$(python utilities/get_vault_path.py)
copied=0; skipped=0
for src in content/published/*.html; do
  name=$(basename "$src")
  dst="$VAULT/03-Published/$name"
  if [ ! -f "$dst" ]; then
    cp "$src" "$dst" && copied=$((copied+1)) && echo "+ $name"
  else
    skipped=$((skipped+1))
  fi
done
echo "Reconcile: $copied copiados, $skipped ya presentes"
```

**Alcance:** solo copia archivos faltantes. No sobreescribe, no modifica frontmatter, no invoca `wiki-update` (eso es prerrogativa de `sync-published` cuando el artículo se publica por primera vez). Es una red de seguridad, no un pipeline de primera publicación.

**Why:** incidente 2026-04-20 — al ejecutar el modo autónomo se detectaron 2 artículos publicados (`humanoides-en-casa-cuanto-falta`, `mejor-robot-aspirador-2026`) ausentes del vault porque `/post-publish` paso 12 no los procesó en su momento. Sin reconcile automático, el desfase sólo se descubre por casualidad.

## Reglas de Obsidian (heredadas del vault-organizer)

1. **Filenames < 60 chars** — SyncThing limit
2. **Wikilinks** `[[Page Name]]` — NUNCA markdown links para archivos internos
3. **Frontmatter YAML obligatorio** en toda nota:
   ```yaml
   ---
   type: [research|draft|published|wiki|calendar|template]
   tags: [robohogar, categoría]
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   ---
   ```
4. **Sacred files INTOCABLES:** `All Deliverables.md` y `Presentation Index.md` en vault root
5. **Deepest-first** para renames — empezar por archivos más profundos
6. **Update wikilinks** después de mover/renombrar cualquier archivo
7. **Auto-apply** operaciones rutinarias sin preguntar
8. **Preguntar** antes de: borrar >10 archivos, archivar >3 carpetas, cambios estructurales

## Relación con vault-organizer de RRP-DEV

Este skill opera SOLO en `05-01_Robotica Newsletter/` + `Repo Mirrors/ROBOHOGAR/`. El vault-organizer de RRP-DEV maneja el resto del vault. Sin conflictos — scopes disjuntos.
