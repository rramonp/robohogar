# Archive 2026-04-19 cleanup

Archivo ejecutado como parte de FASE A del plan de debugging integral ROBOHOGAR (ver `/pipeline-debug` skill + plan original `C:\Users\bakal\.claude\plans\me-preocupa-que-el-optimized-shore.md`).

## Criterio

Archivos que NO estaban referenciados desde ningún skill `.claude/commands/*.md`, rule `.claude/rules/*.md`, `CLAUDE.md`, `docs/*.md` operativo, ni `content/*.md` vivo al correr el audit 2026-04-19. Candidatos a reactivación en FASE 5+ (growth agresivo / análisis competitivo sistemático).

## Archivos

| Archivo | Razón de archivo | Criterio de reactivación |
|---|---|---|
| `competencia-en.md` | Análisis competitivo en inglés — 0 citas en pipeline | Reactivar si se abre un ángulo editorial de benchmarking vs newsletters anglosajonas |
| `competencia-es.md` | Análisis competitivo ES — 0 citas en pipeline | Reactivar si se inicia estudio sistemático de competencia ES (Xataka Home, etc.) |
| `plataformas-comparativa.md` | Comparativa de plataformas (Beehiiv vs alternativas) — decisión ya tomada, sin uso operativo | Reactivar si Rafael plantea migrar de Beehiiv |

## Cómo reactivar

1. Mover el archivo de vuelta a `references/`.
2. Añadir cita desde el skill o rule que lo justifique.
3. Actualizar [`MEMORY.md`](../../../.claude/memory/MEMORY.md) si la decisión cambia el pipeline.

## Audit completo

Hallazgos de `writewithai/extractions/` (~35 archivos) quedan bajo observación: forman un corpus autocontenido que se referencia desde `00-index-completo.md`. Se reevaluará en la próxima ejecución de `/pipeline-debug refs`.
