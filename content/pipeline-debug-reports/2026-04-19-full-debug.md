# Pipeline Debug Report — 2026-04-19 — scope: full

> Ejercicio manual fundacional (precede al skill `/pipeline-debug`). Resultado del ejercicio que Rafael pidió: *"debugging completo tras sprint de tangibles 2026-04-18"*.
> Plan fuente: `C:\Users\bakal\.claude\plans\me-preocupa-que-el-optimized-shore.md`.
> Este archivo sirve de **baseline de cobertura** — cada ejecución futura del skill compara contra él para calibrar.

## Input

- **Scope:** full
- **Since:** 2026-04-05 (inicio del sprint tangibles)
- **Commits auditados:** 5 (98da760, 64448dd, a9259d4, c004d9c, f777a43)

## Resumen ejecutivo

Pipeline ~65% integrado tras el sprint de tangibles. Reglas claras (rules <100 LOC, sin duplicación real), skills funcionales, pero **3 automatizaciones faltantes** convertirían al sprint en one-shot: (a) banner lead-magnet no se inserta automáticamente desde `/content-draft`, (b) `automation.md` sin tabla de tags Beehiiv → welcome flow no se dispara, (c) variante `guia` del `/pdf-brand` sin template → tangible `guia-primer-mes-aspirador` muerto. Además, guía operativa sin schedule semanal con días/horas fijos + sin mirror local de analytics.

## Hallazgos priorizados

| Prioridad | Hallazgo | Scope | Archivo:línea | Acción propuesta |
|---|---|---|---|---|
| 🔴 | Banner lead-magnet no se inserta automáticamente | skills/tangibles | `content-draft.md §8.8` | Convertir §8.8 de descripción a paso ejecutable con decisión por `frontmatter.category` |
| 🔴 | `automation.md` vago sobre tags Beehiiv | rules | `automation.md` | Añadir tabla de tags + regla "post-publish paso 5.5 asigna" |
| 🔴 | 3 memorias tangibles solo en RRP-DEV | memory | `RRP-DEV/.claude/memory/feedback_tangible_*.md` | Copiar a `/robohogar/.claude/memory/` + registrar en MEMORY.md |
| 🔴 | Variante `guia` de `/pdf-brand` no existe | tangibles | `skills/pdf_brand/templates/` | Crear `guia.html.jinja2` step-by-step |
| 🔴 | Ficha Beehiiv Digital Product se copia a mano | tangibles | `post-publish.md` | Añadir paso 2.5 validación tangibles (banner + subtítulo + ficha) |
| 🟡 | ~30 references huérfanas (competencia-*, plataformas-comparativa, extractions no citadas) | refs | `references/` | Archivar 3 top-level a `_archive/2026-04-19-cleanup/` (extractions bajo observación) |
| 🟡 | Anti-IA §1/§2 duplicado verbatim en content-draft y ficcion-draft | skills | `content-draft.md §8.5` + `ficcion-draft.md §8` | Compactar a referencia al canonical `references/anti-ia-checklist.md` |
| 🟡 | `ficcion-draft` aislado del roadmap tangibles | skills | `ficcion-draft.md` | Añadir bloque roadmap `/pdf-brand relato` F2 |
| 🟡 | `/post-publish` no valida pivote tangibles | skills | `post-publish.md` | Añadir pasos 2.5 (validación) y 5.5 (tags) |
| 🟢 | Sin schedule semanal con días/horas fijos | docs | `docs/guia-implementacion.md` | Insertar `§ 🗓 Schedule semanal fijo` antes de Roadmap |
| 🟢 | "📍 Dónde estoy hoy" sin plantilla fija de 3 next steps | docs | `docs/guia-implementacion.md` | Añadir bloque `§ 📌 Próximos 3 next steps` con frases trigger |
| 🟢 | FASE 6 Métricas sin mirror local | docs | `docs/guia-implementacion.md` | Añadir tabla semanal + SLOs por fase + trigger optim |
| 🟢 | `/post-publish` no actualiza dashboard automáticamente | skills | `post-publish.md §4` | Enhanceen paso 4 para tocar los 3 bloques del tablero |
| 🟢 | `/pdf-brand` no actualiza dashboard al generar | skills | `pdf-brand.md` | Añadir paso final "Actualizar tablero vivo" |

## Acciones ejecutadas en esta sesión (2026-04-19)

Plan en fases A-F ejecutado parcialmente:

### ✅ FASE A — Sanity check documental
- A1: Tabla tags Beehiiv + welcome flow MVP añadidos a `automation.md`.
- A2: 3 memorias tangibles copiadas a `/robohogar/.claude/memory/` + MEMORY.md actualizado.
- A3: `competencia-en.md`, `competencia-es.md`, `plataformas-comparativa.md` archivadas a `references/_archive/2026-04-19-cleanup/` + README.
- A4: Anti-IA §1/§2 compactado en content-draft §8.5 y ficcion-draft §8 (referencia única a canonical).
- A5: Roadmap `/pdf-brand relato` añadido a ficcion-draft.
- A6: CLAUDE.md skills detalle (PDF + ficha Beehiiv + `/pipeline-debug`).

### ✅ FASE B — Integración automatizada tangibles (parcial)
- B1: `content-draft §8.8` convertido a paso ejecutable con algoritmo + verificación pre-output.
- B2: `post-publish paso 2.5 "Validación tangibles"` añadido (banner + subtítulo + ficha).
- B3: `post-publish paso 5.5 "Asignar tags Beehiiv"` añadido.
- ⏳ B4: Variante `guia` de `/pdf-brand` — **diferido** a sesión con tests end-to-end.
- ⏳ B5: Retrofit batch banner en 4 artículos consumer — **diferido** con B4.

### ✅ FASE C + D — Tablero vivo en guía + SLOs
- C1: `§ 🗓 Schedule semanal fijo` insertado con 7 filas + mantenimiento mensual + regla de oro.
- C2: `§ 📌 Próximos 3 next steps` con 3 bullets + frases trigger + rutas + último artículo / último tangible.
- C3: FASE 6 ampliada con SLOs por fase (F1/F2/F3) + trigger de optimización + tabla semanal viva.
- C4: `post-publish paso 4` reescrito para tocar 3 bloques del tablero (checkbox artículo + next 3 steps + roadmap).
- C5: `pdf-brand § Paso final` añadido para actualizar último tangible + prioridad 3 + next steps.

### ✅ FASE E — Skill /pipeline-debug
- Creado `.claude/commands/pipeline-debug.md` con scopes (full/skills/rules/refs/tangibles/memory/docs/schedule), since filter, 3 prompts de agentes, regla de integración, template de report.
- Creado `content/pipeline-debug-reports/_template.md`.
- Este archivo (`2026-04-19-full-debug.md`) queda como baseline de cobertura.

### ⏳ FASE F — Cierre
- Commit consolidado pendiente.
- Primer dogfooding: próximo lunes 2026-04-20 (*"Ritual lunes — digest + métricas"*).

## Regla de integración (scope=full)

- [x] `CLAUDE.md § Skills del pipeline` — pdf-brand detalle + `/pipeline-debug` añadido.
- [x] `docs/guia-implementacion.md § 🗓 Schedule semanal fijo` — creado.
- [x] `docs/guia-implementacion.md § 🎯 Roadmap actual` — no tocado estructuralmente, sigue reflejando sprint actual.
- [ ] `content/calendario-editorial.md` — **pendiente:** añadir día/hora fija por ritual (se difiere — la regla de oro de la guía ya apunta al backlog).
- [x] `.claude/rules/automation.md § Tags Beehiiv` — tabla añadida.
- [x] `.claude/memory/MEMORY.md` — 4 entradas nuevas (3 tangibles + voz autoridad cross-link desde RRP-DEV).

## Propuesta — Next 3 steps para Rafael

Copy-paste listo para `docs/guia-implementacion.md § 📌 Próximos 3 next steps`:

```
- [ ] **Debug N1 —** Activar variante `guia` de `/pdf-brand` end-to-end con `guia-primer-mes-aspirador` (B4) · frase trigger: *"Retomamos tangibles — variante guía"* · ruta: `skills/pdf_brand/templates/` + `content/lead-magnets/guia-primer-mes-aspirador/`
- [ ] **Debug N2 —** Retrofit batch banner lead-magnet en 4 artículos consumer sin banner (B5) · frase trigger: *"Retofit banners consumer"* · ruta: `content/articulos/` (filtrar category ∈ aspirador/cortacésped/mascota-robot/fregasuelos/limpia-cristales)
- [ ] **Debug N3 —** Primer dogfooding lunes 2026-04-20 del schedule semanal nuevo · frase trigger: *"Ritual lunes — digest + métricas"* · ruta: `docs/guia-implementacion.md § 🗓 Schedule semanal fijo`
```

## Cobertura vs ejercicio manual

N/A — este ES el ejercicio manual fundacional. Sirve de baseline para iteraciones futuras del skill `/pipeline-debug`.

## Notas para el próximo `/pipeline-debug`

- Vigilar si el retrofit banner B5 se completó antes del siguiente debug (conteo de `class="banner-lead-magnet"` por categoría en `content/articulos/`).
- Cuando llegue el primer nuevo tangible post-Hoja-de-Compra, verificar que el paso final de `/pdf-brand` (actualizar tablero vivo) se ejecutó realmente.
- Si `calendario-editorial.md` incorpora días/horas fijas explícitas, eliminar la nota de "pendiente" en la regla de integración.
- Cobertura de memorias: al copiar más memorias de RRP-DEV a `/robohogar/.claude/memory/`, considerar añadir un scope `cross-memory` al skill.
