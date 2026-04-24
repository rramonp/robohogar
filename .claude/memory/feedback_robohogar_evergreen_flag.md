---
name: ROBOHOGAR — flag evergreen para repurposing social
description: Cada artículo se clasifica evergreen true/false para decidir si entra en el backlog de reutilización social cuando haya audiencia (FASE 4B+)
type: feedback
originSessionId: 1559aa39-1092-4b1c-8e0f-36547af35b33
---
Todo artículo ROBOHOGAR debe clasificarse con `evergreen: true|false` al publicarse. El flag vive en:
1. Frontmatter YAML del borrador (`content/articulos/<slug>/borrador.html`) — fuente primaria
2. Columna "Evergreen" en `content/registro-articulos.md` — fuente replicada consultable

**Regla de clasificación:**
- `true` = comparativa, review, guía, editorial de tesis atemporal → reutilizable en redes con meses de retraso (revisar precios/estado antes de reutilizar)
- `false` = editorial reactivo sobre deal/lanzamiento/noticia con fecha concreta → caducable en 3-6 meses, NO entra en backlog social

**Why:** Rafael escribe con 0 subs (abr 2026). Los posts generados por `/social-content` no se programan en Buffer mientras no haya audiencia en los canales (LinkedIn/IG/WhatsApp bloqueados o sin contactos). Cuando llegue a FASE 4B (≥50 subs activables), el banco de posts evergreen acumulado = 3-6 meses de cadencia social sin producir contenido extra. Los reactivos se descartan — no tiene sentido publicar en agosto un deal del 12-abril.

**How to apply:**
- `/content-draft`: incluir `evergreen: true|false` + `evergreen_note` en el frontmatter YAML del borrador generado
- `/post-publish`: paso 5 replicar el flag en `registro-articulos.md` (columna Evergreen con ✅/❌ + nota de motivo si es relevante)
- `/social-content`: paso 1 leer el flag y marcar los `.md` sociales con cabecera indicando si van al backlog de reutilización
- Retroactivo (abr 2026): 5 artículos ya clasificados en registro-articulos.md. Los 4 primeros (mejor-asistente, humanoides-en-casa, roborock, humanoides-2026) = `true`. NEO-EQT = `false` (deal reactivo).

Documentación operativa:
- `.claude/commands/content-draft.md` sección "3. Generar borrador" (campo obligatorio en frontmatter)
- `.claude/commands/post-publish.md` paso 5 (replicación en registro)
- `.claude/commands/social-content.md` sección "1. Identificar fuente" (consumo del flag)
- `content/templates/PASOS-template.md` incluye campo Evergreen en tabla SEO
