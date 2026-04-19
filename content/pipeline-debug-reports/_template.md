# Pipeline Debug Report — YYYY-MM-DD — scope: <scope>

> Generado por `/pipeline-debug <scope> [since:YYYY-MM-DD]`.
> Duración: ~X min · Invocación: <frase trigger de Rafael>

## Input

- **Scope:** <full | skills | rules | refs | tangibles | memory | docs | schedule>
- **Since:** <YYYY-MM-DD o "sin filtro">
- **Commits auditados:** <N> (output de `git log --since=...` si aplica)
- **Archivos tocados en la ventana:** <N>

## Resumen ejecutivo

<2-3 frases: estado general del pipeline. Ejemplos: "Pipeline 90% integrado tras sprint tangibles. Detectados 2 🔴 bloqueantes + 4 🟡 fricción. Sin cruft nuevo." o "Pipeline estable desde último debug. 1 🟡 — references huérfanas pendientes."

## Hallazgos priorizados

| Prioridad | Hallazgo | Scope | Archivo:línea | Acción propuesta |
|---|---|---|---|---|
| 🔴 | | | | |
| 🟡 | | | | |
| 🟢 | | | | |

### Detalle 🔴 críticos

<por cada 🔴: 2-3 frases de contexto + evidencia concreta (grep/línea) + por qué bloquea.>

### Detalle 🟡 fricción

<1-2 frases por item.>

### Detalle 🟢 tablero

<1-2 frases por item.>

## Regla de integración (scope=full)

Verificación de que las novedades desde `since:` están integradas:

- [ ] `CLAUDE.md § Skills del pipeline`
- [ ] `docs/guia-implementacion.md § 🗓 Schedule semanal fijo`
- [ ] `docs/guia-implementacion.md § 🎯 Roadmap actual`
- [ ] `content/calendario-editorial.md`
- [ ] `.claude/rules/automation.md § Tags Beehiiv`
- [ ] `.claude/memory/MEMORY.md`

<indicar cuáles fallan con referencia al hallazgo correspondiente.>

## Propuesta — Next 3 steps para Rafael

Copy-paste listo para `docs/guia-implementacion.md § 📌 Próximos 3 next steps`:

```
- [ ] **Debug N1 —** <acción> · frase trigger: *"<frase>"* · ruta: `<archivo>`
- [ ] **Debug N2 —** <acción> · frase trigger: *"<frase>"* · ruta: `<archivo>`
- [ ] **Debug N3 —** <acción> · frase trigger: *"<frase>"* · ruta: `<archivo>`
```

## Cobertura vs ejercicio manual

<si existe `2026-04-19-full-debug.md` de referencia, comparar: ¿este skill detectó lo mismo? ¿Qué se le escapó? Usar para calibrar el prompt de los agentes en iteraciones siguientes.>

## Notas para el próximo `/pipeline-debug`

<qué vigilar la próxima vez, patrones nuevos que surgieron, reglas que habría que añadir al skill.>
