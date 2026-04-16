# Próxima sesión: Optimización repo ROBOHOGAR (fases 2-6)

> Se completó FASE 1 (fixes críticos). Quedan 5 fases de optimización.
> Plan completo: `.claude/plans/dreamy-tickling-hejlsberg.md`

## Estado actual

- 2 artículos publicados (review + editorial)
- 0 suscriptores (crecimiento orgánico SEO)
- Pipeline funcional pero con duplicaciones y verbose excesivo en skills
- Falta calendario editorial y workflow de newsletter

## Lo que se hizo (FASE 1 — completada)

1. Creado `content/drafts/` (referenciado en 5+ skills pero no existía)
2. Corregido `borrador.md` → `borrador.html` en 4 archivos
3. Corregida numeración duplicada en content-draft.md
4. Corregido `Web only` → `Email and web` en guia-implementacion.md
5. Marcado research_aggregator.py como FASE 10 (no implementado)
6. Eliminadas 3 carpetas vacías con hero images experimentales

## Lo que falta (FASES 2-6)

### FASE 2: Consolidar duplicaciones

Hay contenido duplicado entre archivos que viola la regla anti-duplication del proyecto. Establecer owner único por concepto y reemplazar duplicados con referencias.

**Archivos a modificar:**
- `.claude/commands/content-draft.md` — eliminar sección "Prohibiciones" (7 líneas duplicadas de editorial.md) + eliminar template markdown inline de 40 líneas (duplica estructura-templates.md)
- `.claude/commands/social-content.md` — reducir regla plural a 1 línea referenciando editorial.md
- `.claude/rules/newsletter.md` — benchmarks duplican email-marketing-playbook.md, condensar a resumen + referencia
- `.claude/rules/automation.md` — reglas de imagen duplican asset-catalog.md, condensar a resumen + referencia

**Mapa de ownership:**

| Concepto | Owner (fuente de verdad) |
|---|---|
| Reglas editoriales/voz | `rules/editorial.md` |
| Regla primera persona plural | `rules/editorial.md` |
| Benchmarks email | `references/newsletter/email-marketing-playbook.md` |
| Composición/estilo imágenes | `assets/branding/asset-catalog.md` |
| Estructura templates HTML | `content/templates/estructura-templates.md` |
| Tipos de publicación (Email and web / Email only) | `rules/newsletter.md` |

### FASE 3: Limpieza de labels y referencias muertas

1. **"Mi opinión" → "Nuestra opinión"** en `content/templates/estructura-templates.md` y `content/templates/review-comparativa.md` (solo templates, no artículos publicados)
2. **FASE 3 de guia-implementacion.md** — marcar como completada. Los templates .md de Obsidian se borraron; el workflow real usa HTML exports. Actualizar tabla de templates
3. **FAQ landing** — añadir nota en guia explicando que Q1 se omitió en implementación final
4. **Limpiar templates antiguos** — `content/templates/review-comparativa-beehiiv.html` y `review-comparativa-output.html` son versiones anteriores al export definitivo. Borrar, quedar solo con los `-export.html`

### FASE 4: Eficiencia de tokens

Condensar skills verbose que se cargan como contexto:

| Archivo | Líneas actuales | Objetivo |
|---|---|---|
| `content-draft.md` | ~217 | ~150 (tras FASE 2 + comprimir weight table + PASOS example) |
| `obsidian-robohogar.md` | ~197 | ~155 (comprimir tabla relación, sección autónoma, reglas) |
| `post-publish.md` | ~178 | ~150 (comprimir ejemplo resumen, sección input) |
| `automation.md` | ~71 | ~55 (tras FASE 2 eliminar reglas imagen duplicadas) |

### FASE 5: Calendario editorial + newsletter workflow

Crear el sistema que falta:

1. **`content/calendario-editorial.md`** — cadencia semanal definida:
   - Lunes: research digest (interno, no se publica)
   - Martes 9:00 CET: newsletter semanal → `Email only`
   - Miércoles/flexible: artículo web → `Email and web`
   - Secciones: backlog de temas, temas usados (no repetir)

2. **`content/registro-newsletters.md`** — catálogo de newsletters enviados (# | fecha | subject | temas | open rate | CTR)

3. **Actualizar skills** para que referencien el calendario:
   - content-draft.md: consultar calendario antes de elegir tema
   - research-digest.md: actualizar backlog del calendario tras research
   - obsidian-robohogar.md: sincronizar calendario al vault

4. **Archivar** `docs/next-session-calendar-editorial.md` (sus decisiones se integran en el calendario nuevo)

### FASE 6: Verificación cruzada final

1. `git grep "borrador\.md"` → confirmar 0 resultados
2. `git grep "Web only"` → confirmar solo en contextos correctos (tabla comparativa en newsletter.md)
3. Verificar que todos los archivos referenciados en skills existen
4. Verificar numeración de pasos en content-draft.md y post-publish.md
5. Actualizar tabla Key Directories de CLAUDE.md (añadir calendario, registro-newsletters, content/drafts/)
6. Contar líneas: rules <40, skills <160

## Commits esperados (1 por fase)

```
2. refactor: consolidate duplications — single owner per concept
3. cleanup: fix labels, remove dead refs, delete stale templates
4. optimize: condense verbose skills for token efficiency
5. feat: editorial calendar + newsletter registry
6. verify: cross-reference check + CLAUDE.md update
```

## Decisiones ya tomadas (no re-discutir)

- Artículos = `Email and web` (aparecen en landing + se envían por email)
- Newsletter = `Email only` (solo inbox, NO en landing)
- Primera persona SIEMPRE plural ("hemos", "nos"). Excepción: bio Rafael
- Hero images: 3 variantes, close-up, sin neones, estilo "Creación de Adán" como referencia
- WebP obligatorio para thumbnails (<500 KB)
- Post-publish tiene 13 pasos obligatorios incluyendo wiki-update y registro de artículos
- Templates de Obsidian: solo Robot Wiki + Empresa Wiki. Los demás se borraron
