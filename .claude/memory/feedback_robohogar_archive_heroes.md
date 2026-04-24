---
name: ROBOHOGAR — archivar heroes no usados (no borrar)
description: Tras /post-publish, variantes hero no elegidas van a assets/_archive/, nunca rm
type: feedback
originSessionId: 1559aa39-1092-4b1c-8e0f-36547af35b33
---
Tras publicar un artículo ROBOHOGAR, las variantes de hero no elegidas se mueven a `content/articulos/<slug>/assets/_archive/` — NUNCA se borran con `rm`.

**Why:** Rafael prefiere acceso visual inmediato a las iteraciones descartadas (referencia para re-usar composiciones, prompts o estilo en futuros artículos) sin depender de git show/git log. Establecido 2026-04-17 tras ver que las variantes v1-v7, v9 del artículo NEO-EQT se perdieron al borrarse en la misma sesión en que se generaron (no quedaron en ningún commit).

**How to apply:**
- Skill `/post-publish` paso 3 ya actualizado con esta convención (commit `c7e1b52`)
- También aplica en cualquier workflow que limpie heros: mover a `_archive/`, no `rm`
- Consistente con la convención ya existente en `utilities/_archive/` del repo
- Documentado en `assets/branding/asset-catalog.md` sección "Estructura de carpetas por artículo"
