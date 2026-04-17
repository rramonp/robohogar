# Tangibles — principio editorial

Cada pieza de contenido publicada DEBE incluir al menos 1 tangible descargable generado con `/pdf-brand`. Sin excepciones (salvo redifusiones).

**Objetivo:** el lector siempre se lleva algo concreto. Modelo Write With AI (que siempre ofrece prompts) aplicado a robótica doméstica.

## Mapeo tipo de contenido → tangible

| Contenido | Tangible | +Esfuerzo | Variante skill |
|---|---|---|---|
| Review | Checklist compra + specs 1-pager | +15 min | `cheatsheet` |
| Comparativa | Tabla comparativa PDF standalone | +15 min | `comparativa` |
| Editorial/Opinión | "3 datos clave" mini-dossier | +20 min | `cheatsheet` |
| Guía/How-to | Flowchart decisión o checklist paso a paso | +25 min | `guia` |
| Ficción Doméstica | Mini-poster (ilustración + quote + dato real) | +30 min | `relato` |
| Newsletter (futuro) | Cheatsheet "Lo esencial en 3 minutos" | +20 min | `cheatsheet` |

## Reglas operativas

- **Límite 30 min por tangible:** si tarda más, simplificar u omitir. 4 tangibles "ok" > 2 "perfectos"
- **Skill obligatorio:** todos los PDFs pasan por `/pdf-brand` — nunca Canva a mano. Garantiza brand consistency
- **Versionar, nunca sobrescribir:** cada regeneración produce v2/v3 (memoria `feedback_never_overwrite_images.md`)
- **Mobile-first:** PDF legible en pantalla 375px sin zoom. Fuente mínima 11pt
- **Anti-patterns prohibidos en tangibles** (heredados de `editorial.md`): "honesta", "sin filtro", superlativos vacíos ("revolucionario", "increíble", "game-changer", "el mejor")

## Catalogación obligatoria

Cada tangible generado se cataloga en:
- `assets/branding/asset-catalog.md` — entrada con PDF + preview webp
- `content/calendario-editorial.md` — tracking de publicación
- Vault Obsidian: sync automático

## Roadmap

- **Mes 1-2 (0-30 subs):** 4-5 tangibles. Bootstrap
- **Mes 3 (~100 subs):** ~15 tangibles. Activar sección "Descargas" en landing
- **Mes 6:** ~30 + 1 bundle temático
- **Mes 12:** ~55 + ebook recopilatorio. Masa crítica para paid tier

Plan completo: `../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md`.
Documentación operativa: `docs/guia-implementacion.md` § FASE 4B.
