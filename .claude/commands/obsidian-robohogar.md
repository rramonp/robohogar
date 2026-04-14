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

```
05-01_Robotica Newsletter/
  _archive/              # Contenido archivado
  _deliverables/         # PDFs, exports finales
  Issues/                # Backup de cada issue (EP001/, EP002/...)
  Metricas/              # Suscriptores, tráfico, ingresos
  Research/              # Research digests auto-generados
    Clippings/           # Artículos guardados manualmente
  Templates/             # Plantillas Obsidian (6 templates)
  Wiki/                  # BASE DE DATOS CRECIENTE
    Robots/              # Una nota por robot/producto
    Empresas/            # Una nota por empresa
    Conceptos/           # Temas evergreen
    Mercado/             # Datos acumulativos
  02-Drafts/             # Borradores de artículos (mirror del repo)
  03-Published/          # Artículos publicados (mirror del repo)
  06-Calendar/           # Planificación editorial
  Guia Implementacion.md
  Proyecto ROBOHOGAR.md  # MOC principal
  Research Mercado EN.md
  Research Mercado ES.md
```

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

## Archivos que SIEMPRE se sincronizan al vault

Al ejecutar CUALQUIER modo de este skill, sincronizar estos archivos del repo al vault:

| Repo | Vault | Notas |
|------|-------|-------|
| `docs/guia-implementacion.md` | `Guia Implementacion.md` | Guía maestra del proyecto |
| `content/registro-articulos.md` | `Registro Articulos.md` | Catálogo de artículos publicados — fuente de verdad |

```bash
cp "$HOME/robohogar/content/registro-articulos.md" "$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Registro Articulos.md"
cp "$HOME/robohogar/docs/guia-implementacion.md" "$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md"
```

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

| Aspecto | vault-organizer (RRP-DEV) | obsidian-robohogar (este skill) |
|---|---|---|
| Scope | TODO el vault HBX | Solo `05-01_Robotica Newsletter/` |
| Función | Estructura, naming, binarios, indexes | Contenido editorial, wiki, research |
| Mode 12 (repo-mirror) | Sincroniza repo → vault como notas | NO duplicar — dejar que vault-organizer haga esto |
| Conflictos | 0 — este skill NO toca nada fuera de 05-01 | 0 — vault-organizer NO gestiona contenido editorial |
