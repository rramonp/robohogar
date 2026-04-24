---
name: ROBOHOGAR guía — incluir triggers/prompts siempre
description: Cuando añado contenido a docs/guia-implementacion.md (o cualquier doc de workflow en ROBOHOGAR), DEBO incluir las frases trigger exactas y prompts que Rafael tiene que decirme para invocar cada paso u obtener cada output esperado
type: feedback
originSessionId: 5fad1a2c-7ed8-451b-9039-ede2e6a9eca3
---
Cada vez que añado una fase, sección o workflow a `docs/guia-implementacion.md` de ROBOHOGAR (o a cualquier documento de workflow del proyecto), incluir OBLIGATORIAMENTE:

1. **Frase trigger exacta** que Rafael debe pronunciar para retomar/invocar el workflow — en forma de tabla o bloque destacado
2. **Prompts literales** para cada skill/comando invocable (ej: `/pdf-brand guia "tema" 1-pagina`)
3. **Inputs esperados** de cada invocación (argumentos obligatorios + opcionales)
4. **Outputs esperados** en rutas concretas del repo (o mensaje concreto de Claude)

**Why:** Rafael trabaja en sesiones espaciadas (3-5 h/semana). Cuando vuelve tras días/semanas, no debe tener que recordar cómo invocarme — la guía debe ser autocontenida. Sin triggers documentados, cada retoma requiere contexto adicional y fricción.

**How to apply:**
- Al final de cada nueva FASE/sección de la guía → añadir bloque "📌 Frases trigger para retomar"
- Al documentar un skill → incluir ejemplos de invocación completos (no solo descripción)
- Al mencionar un output → anclar ruta exacta (no "el PDF final" sino `assets/lead-magnets/<slug>-v1.pdf`)
- Si el workflow tiene fases secuenciales → una frase trigger por fase
- Regla binding en repo: `.claude/rules/guide-authoring.md`

Precedente: digest research 2026-04-17 (bloque "📌 Recomendación ROBOHOGAR — Para retomar" al principio con frase exacta) + FASE 4B guía (4 frases trigger). Este patrón es el estándar a partir de ahora.
