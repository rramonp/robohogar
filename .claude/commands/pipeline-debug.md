# /pipeline-debug [scope] [since:YYYY-MM-DD]

Auditoría repetible y escalable del pipeline ROBOHOGAR. Detecta drift entre reglas, skills, references, memoria, guía operativa y contenido real — antes de que se acumule.

## When to activate

Invocar `/pipeline-debug` cuando:

- Se introduce **una novedad mayor**: nuevo skill, pivote editorial, nuevo formato de contenido (tangible nuevo, banner nuevo, automation nueva), memoria crítica añadida.
- **Cada 4-6 semanas** como mantenimiento preventivo (schedule semanal de la guía lo programa para el último viernes de cada mes).
- **Antes de cada revisión mensual** (FASE 6 § Revisión mensual) — para que la revisión incluya un tablero limpio.
- Cuando Rafael siente drift: *"hay piezas que no encajan"*, *"no sé en qué estamos"*, *"tengo dudas si todo sigue integrado"*.

Frases trigger equivalentes: *"pipeline debug"*, *"/pipeline-debug"*, *"audit del repo"*, *"repasar el pipeline"*.

## Inputs

- **`scope`** (opcional, default `full`): limita qué auditar. Opciones:
  - `full` — todos los scopes.
  - `skills` — `.claude/commands/*.md`.
  - `rules` — `.claude/rules/*.md`.
  - `refs` — `references/` (huérfanas, duplicadas, cruft).
  - `tangibles` — flujo end-to-end del pivote Cole (banner, ficha, checklist, PDFs, automation).
  - `memory` — `.claude/memory/` + referencias cruzadas con RRP-DEV.
  - `docs` — `docs/guia-implementacion.md`, `docs/plan-v2.md`, `content/registro-*.md`, `content/calendario-editorial.md`.
  - `schedule` — coherencia del `§ 🗓 Schedule semanal fijo` con skills reales.
- **`since:YYYY-MM-DD`** (opcional): audita sólo cambios en el repo desde esa fecha (vía `git log --since=...`). Útil tras una sesión de sprint.

## Pasos

### 1. Preparación

- Verificar working directory = `c:\Users\bakal\robohogar\`.
- Crear `content/pipeline-debug-reports/` si no existe.
- Fecha del report = `YYYY-MM-DD` del día actual. Path = `content/pipeline-debug-reports/<YYYY-MM-DD>-<scope>-debug.md`.
- Si `since:` se pasó, `git log --since=<fecha> --name-status` para acotar el universo.

### 2. Lanzar 3 agentes Explore en paralelo

Cada agente cubre un ángulo y reporta ≤400 palabras. Si `scope` es distinto de `full`, filtrar los agentes a lo pertinente (ej. scope=`skills` → sólo agente 1).

#### Agente 1 — Skills + Rules

> Audita `.claude/commands/` y `.claude/rules/`.
>
> 1. Inventario de skills: 1 línea de propósito + LOC por archivo.
> 2. Rules >100 LOC (regla `feedback_rules_max_lines.md`).
> 3. Referencias cruzadas `@rules/` y `@references/` — detectar rotas.
> 4. Duplicación real entre rules (mismo concepto en 2+ sitios).
> 5. Skills que NO integran novedades recientes (buscar: banner lead-magnet, tags Beehiiv, ficha Digital Product, tangibles como producto, anti-IA checklist).
> 6. Pasos duplicados entre skills (mismo procedimiento operativo).
> 7. Novedades desde `since:` que no están referenciadas en ningún skill/rule.

#### Agente 2 — Guía operativa + docs + registros

> Audita `docs/guia-implementacion.md` + `docs/*.md` + `content/registro-*.md` + `content/calendario-editorial.md`.
>
> 1. ¿El schedule semanal del `§ 🗓 Schedule semanal fijo` cubre todo skill activo? ¿Falta algún ritual o sobra?
> 2. ¿Los 3 bullets de `§ 📌 Próximos 3 next steps` son accionables, tienen frase trigger y ruta concreta?
> 3. ¿La `§ 🎯 Roadmap actual § Prioridad N` refleja el estado real (comparar con `content/registro-articulos.md` y `content/lead-magnets/`)?
> 4. ¿La tabla semanal de FASE 6 se rellena? ¿Cuántas semanas vacías hay?
> 5. Docs obsoletos o duplicados en `docs/`.
> 6. Registros (`registro-articulos`, `registro-newsletters`, `calendario-editorial`) vs realidad del repo (`content/articulos/` vs `content/published/`).

#### Agente 3 — References + Memoria + Integración tangibles

> Audita `references/`, `.claude/memory/` y flujo tangibles end-to-end.
>
> 1. References huérfanas (no citadas en ningún skill/rule/doc operativo vivo) — candidatas a `references/_archive/<fecha>-cleanup/`.
> 2. References duplicadas/solapadas.
> 3. Memoria `.claude/memory/MEMORY.md`: índice coherente, entradas que apuntan a archivos inexistentes, conflictos con memoria en `RRP-DEV/.claude/memory/`.
> 4. **Flujo tangibles end-to-end** — para cada tangible activo en `content/lead-magnets/<slug>/`:
>    - [ ] `contenido.md` existe.
>    - [ ] `data.py` existe.
>    - [ ] PDF v<N> generado.
>    - [ ] `beehiiv-ficha.md` existe y pasa validators (sin roadmap, sin fechas, sin byline).
>    - [ ] Artículos consumer referencian el tangible vía banner con `?lm=<slug>&src=<articulo>`.
>    - [ ] El tangible aparece en `§ 🎯 Roadmap actual § Prioridad 3`.
> 5. Artículos consumer recientes en `content/articulos/` SIN banner lead-magnet insertado.

### 3. Consolidación

Generar tabla priorizada:

| Prioridad | Hallazgo | Scope | Archivo | Acción propuesta |
|---|---|---|---|---|
| 🔴 | <descripción> | skills/rules/refs/tangibles/memory/docs/schedule | path:line | <acción concreta> |
| 🟡 | … | … | … | … |
| 🟢 | … | … | … | … |

Criterio:
- 🔴 Bloquea automatización o rompe una regla del pipeline (banner no se inserta, ref rota, ficha falta, etc.)
- 🟡 Fricción/cruft — skill funciona pero tiene deuda (duplicación, references huérfanas, doc obsoleto)
- 🟢 Tablero operativo — gaps en guía viva, schedule vs realidad, next steps desfasados

### 4. Next 3 steps propuestos

Formato exacto (para copy-paste al `§ 📌 Próximos 3 next steps` de la guía):

```
- [ ] **Debug N1 —** <acción 🔴> · frase trigger: *"<frase>"* · ruta: `<archivo>`
- [ ] **Debug N2 —** <acción 🔴 o 🟡> · …
- [ ] **Debug N3 —** <acción 🟡 o 🟢> · …
```

Rafael decide cuáles aceptar y cuáles posponer. El skill **NO edita el repo automáticamente** — solo reporta y propone.

### 5. Escribir report

Path: `content/pipeline-debug-reports/<YYYY-MM-DD>-<scope>-debug.md`.

Estructura: `content/pipeline-debug-reports/_template.md`.

### 6. Regla de integración (scope=full)

Si `scope=full`, verificar que toda novedad detectada desde `since:` esté integrada en:

- [ ] `CLAUDE.md § Skills del pipeline` (si es skill nuevo)
- [ ] `docs/guia-implementacion.md § 🗓 Schedule semanal fijo` (si aporta un ritual)
- [ ] `docs/guia-implementacion.md § 🎯 Roadmap actual` (si cambia prioridades)
- [ ] `content/calendario-editorial.md` (si afecta cadencia de contenido)
- [ ] `.claude/rules/automation.md § Tags Beehiiv` (si introduce tag nuevo)
- [ ] `.claude/memory/MEMORY.md` (si es decisión editorial fuerte)

Cada `[ ]` sin marcar = hallazgo 🔴 o 🟡 en el report.

### 7. Reporte a Rafael

Mensaje final a Rafael (en chat, no en archivo):

```
✅ Pipeline debug completado — scope=<scope>, since=<fecha>.

Hallazgos:
- 🔴 Críticos: <N>
- 🟡 Fricción: <N>
- 🟢 Tablero: <N>

Report: content/pipeline-debug-reports/<archivo>.md

Propuesta de next steps (para ir a 📌 Próximos 3 next steps):
<bullet 1>
<bullet 2>
<bullet 3>

¿Aceptas los 3, o te paso sólo los 🔴 de inmediato?
```

## Rules

- **No editar el repo automáticamente.** Sólo leer y generar el report. La ejecución de cambios requiere aprobación explícita de Rafael.
- **Read-only sobre skills/rules/references** durante la auditoría — evitar side-effects.
- **Anti-duplicación:** el report se escribe una vez por día + scope. Si se ejecuta dos veces el mismo día con el mismo scope, sobrescribir con `v2` en el filename.
- **Escalable:** al añadir un formato de contenido nuevo (ej. vídeo corto, podcast, newsletter pago), añadir en esta skill un nuevo scope (`videos`, `paid`, etc.) con su prompt de agente dedicado. El template del report soporta scopes nuevos sin cambios.
- **Memoria externa (RRP-DEV):** siempre cross-checkear `c:\Users\bakal\RRP-DEV\.claude\memory\MEMORY.md` contra `.claude/memory/MEMORY.md` local para detectar memorias tangibles/editoriales solo en un repo.

## Ejemplos de invocación

- `/pipeline-debug` — full scope, todo el repo.
- `/pipeline-debug tangibles` — sólo flujo tangibles end-to-end.
- `/pipeline-debug full since:2026-04-18` — auditar todo con foco en cambios del sprint tangibles.
- `/pipeline-debug skills` — sólo `.claude/commands/`.
- `/pipeline-debug refs since:2026-03-01` — huérfanas y cruft desde el último cleanup.

## Fuentes y referencias

- Plan fundador: `C:\Users\bakal\.claude\plans\me-preocupa-que-el-optimized-shore.md`
- Ejercicio manual precedente (2026-04-19): `content/pipeline-debug-reports/2026-04-19-full-debug.md` — comparar cada ejecución automática contra este para calibrar cobertura.
- Reglas que este skill vigila: `@.claude/rules/automation.md`, `@.claude/rules/tangibles.md`, `@.claude/rules/editorial.md`, `feedback_rules_max_lines.md`.
- Skill code: puramente prompt-driven (no tiene código Python aparte; orquesta agentes Explore + lectura de archivos).
