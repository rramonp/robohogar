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

```
$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/
```

`$HBX_VAULT` se resuelve automáticamente según la máquina:
- Desktop (cri-c): `C:\Users\cri-c\OneDrive - HBX Group\Desktop\DEMAND\Obsidian`
- Laptop (bakal): `C:\Users\bakal\OneDrive - HBX Group\Desktop\DEMAND\Obsidian`

## Estructura del vault

Subcarpetas principales de `05-01_Robotica Newsletter/`: `_archive/`, `Issues/`, `Metricas/`, `Research/` (+ `Clippings/`), `Templates/`, `Wiki/` (`Robots/`, `Empresas/`, `Conceptos/`, `Mercado/`), `02-Drafts/`, `03-Published/`, `06-Calendar/`. MOC: `Proyecto ROBOHOGAR.md`.

## Modos de operación

### 1. `sync-published` — Sincronizar artículos publicados

Copia artículos de `content/published/` al vault `03-Published/`.
- Añade frontmatter si no tiene (type: published, tags, fecha)
- Actualiza wikilinks internos a formato Obsidian `[[Page Name]]`
- NO sobreescribe archivos existentes en el vault
- **SIEMPRE sincronizar `content/registro-articulos.md`** al vault como `Registro Articulos.md`

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
| `content/registro-articulos.md` | `Registro Articulos.md` | Catálogo de artículos publicados — fuente de verdad |
| `content/calendario-editorial.md` | `Calendario Editorial.md` | Cadencia semanal, backlog de temas, planificación |
| `content/registro-newsletters.md` | `Registro Newsletters.md` | Catálogo de newsletters enviados |

```bash
VAULT="$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter"
cp docs/guia-implementacion.md         "$VAULT/Guia Implementacion.md"
cp content/registro-articulos.md       "$VAULT/Registro Articulos.md"
cp content/calendario-editorial.md     "$VAULT/Calendario Editorial.md"
cp content/registro-newsletters.md     "$VAULT/Registro Newsletters.md"
```

**Importante:** los 4 archivos son fuente de verdad en el repo; el vault es mirror. CUALQUIER modo del skill debe sincronizar los 4, no solo los del ejemplo antiguo. Evita desfases como el detectado 2026-04-17 (calendario-editorial 5h atrás del repo).

**Nota:** estos archivos se copian al área editorial (05_Personal) para que Rafael los trabaje en Obsidian. El `repo-mirror` (Mode 7) los copia TAMBIÉN al área de mirror (03_Resources) como parte del backup completo. Ambas copias son válidas — editorial para uso diario, mirror para disaster recovery.

## Ejecución autónoma (sin modo específico)

Sin modo explícito → ejecutar: 1) Sync always-sync files, 2) Repo mirror, 3) Audit, 4) Resumen.

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
