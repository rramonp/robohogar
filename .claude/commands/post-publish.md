# Post-Publish — Limpieza y distribución tras publicar un artículo

Ejecuta TODAS las tareas post-publicación de un artículo en ROBOHOGAR.
Se invoca después de que Rafael confirme que el artículo está publicado en Beehiiv.

## When to activate

- "ya está publicado", "acabo de publicar", "post-publish"
- "limpieza post publicación", "tareas post artículo"
- Después de que Rafael comparta la URL del artículo publicado

## Input necesario

Preguntar si no lo ha dado: URL del artículo, tipo de publicación (`Email and web` / `Email only`), hero image elegida (ej: v10), slug.

## Workflow (ejecutar en orden)

### 1. Verificar artículo publicado

Antes de hacer nada, comprobar que el artículo se ve correctamente:

- [ ] **Fetch la URL** con WebFetch — verificar que carga, título correcto, estructura completa
- [ ] **OG image** — comprobar con `https://opengraph.xyz/<URL>` que la miniatura se ve bien y el WebP carga rápido. Reportar a Rafael si hay problemas
- [ ] **Links internos** — verificar que los links dentro del artículo funcionan (especialmente CTAs de suscripción y links a otros artículos)
- [ ] **Imágenes inline** — confirmar que todas las imágenes aparecen en el artículo publicado

### 2. Mover borrador a published

**Pre-check obligatorio — variantes elegidas:** contar bloques de cada patrón v1/v2/v3 en el borrador (hook, veredicto, ¿sabías que?). Si queda ≥2 de cualquiera, **PARAR y avisar a Rafael** — no eligió, el artículo publicado tendría 2-3 bloques redundantes visibles.

```bash
# Cada grep debe devolver exactamente 1 (Rafael dejó solo la variante elegida)
# 0 = el borrador nunca tuvo esa sección triplicada → continuar
# ≥2 = PARAR, avisar a Rafael que borre las variantes que no quiere
grep -c 'class="callout-amber hook-option"'     content/articulos/<slug>/borrador.html
grep -c 'class="callout-amber veredicto-option"' content/articulos/<slug>/borrador.html
grep -c 'class="sabias-option"'                  content/articulos/<slug>/borrador.html

# Bloques image-optional: deben ser 0 antes de publicar (Rafael decidió sí/no)
grep -c 'class="image-optional"' content/articulos/<slug>/borrador.html
# Si devuelve ≥1: PARAR, avisar a Rafael que decida cada imagen opcional (borrar bloque completo o borrar solo el wrapper)
```

```bash
cp content/articulos/<slug>/borrador.html content/published/YYYY-MM-DD-<slug>.html
```

### 3. Archivar variantes de hero no usadas

Mover todas las variantes de hero excepto la elegida (PNG + WebP) a `assets/_archive/`:
```bash
mkdir -p content/articulos/<slug>/assets/_archive
# Mantener solo hero-<slug>-v<elegida>.png y .webp en assets/
# Mover el resto de hero-<slug>-v*.png y .webp a assets/_archive/
```
Las variantes quedan accesibles en disco para re-usar como referencia visual o recuperación rápida sin necesidad de git. Nunca borrar — la regla del repo es archivar, no eliminar.

### 4. Actualizar guia-implementacion.md

Marcar todos los checkboxes del artículo como completados y añadir la URL publicada:
```
- [x] Publicado → <URL>
```

### 5. Actualizar registro de artículos (OBLIGATORIO)

Añadir el artículo a `content/registro-articulos.md` — la fuente de verdad de todo lo publicado:
```
| <N> | <fecha> | <título> | <slug> | <URL> | <tipo> | <tags> | <evergreen> |
```

Para el campo `Evergreen`:
- Si el frontmatter del borrador tiene `evergreen: true|false`, usar ese valor
- Si no existe (artículos antiguos), inferir por tipo: Comparativa/Review/Guía/Editorial de tesis → `✅ true`; Editorial reactivo sobre deal/lanzamiento/noticia con fecha → `❌ false` + nota de motivo
- Este flag lo consume `/social-content` para saber si el artículo va al backlog de repurposing social (FASE 4B+)

Este archivo se sincroniza a Obsidian automáticamente en el paso 12.

### 6. Regenerar llms.txt

Actualizar `content/llms.txt` con el artículo recién publicado. El archivo sigue la spec de [llmstxt.org](https://llmstxt.org) y ayuda a los LLMs a entender el sitio cuando lo citan.

- Leer `content/llms.txt` actual
- Insertar el nuevo artículo en la sección `## Artículos publicados` (orden cronológico inverso: el más reciente primero) con el formato:
  ```
  - [<título>](<URL>): <descripción de 1-2 frases que ayude al LLM a saber cuándo citarlo>
  ```
- La descripción debe ser útil para un LLM —evitar superlativos, incluir marcas/modelos concretos y el ángulo del artículo
- Revisar si el nuevo artículo introduce una categoría nueva que merezca aparecer en `## Categorías de contenido`. Si sí, añadirla
- Verificar que el tamaño total sigue por debajo de los 6.144 caracteres (límite de Beehiiv)
- **Recordar a Rafael:** copiar el contenido de `content/llms.txt` y pegarlo en la sección SEO de Beehiiv (link directo: https://app.beehiiv.com/website_builder_v2/settings/seo → campo "llms.txt" → "Paste your own llms.txt content here"). Beehiiv NO se sincroniza solo; requiere paste manual cada vez

### 7. Verificar fuentes en fuentes-por-categoria.md

Leer el artículo publicado y verificar que TODAS las fuentes usadas están catalogadas en `references/fuentes-por-categoria.md`. Si falta alguna, añadirla con URL, tipo y notas. Incluir fuentes de:
- Datos y cifras citadas en el artículo
- Imágenes inline descargadas de fuentes oficiales
- Estudios o reportajes enlazados

### 8. Actualizar asset-catalog.md

Registrar el hero image elegido en la sección de assets generados del catálogo:
```
| hero-<slug>-v<N> | <fecha> | <prompt resumido> | <modelo> |
```

### 9. Actualizar template master (si aplica)

Template único del proyecto: `content/templates/articulo-beehiiv-master.html`. Sirve para todos los tipos (review, comparativa, editorial, guía, newsletter).

**Actualizar solo si Rafael ha hecho cambios de formato significativos** respecto al master actual — nuevo bloque, rediseño de CTA, cambio de footer, reestructura del trust text, nueva política de tabla, etc. Cambios de contenido normales del artículo NO cuentan.

Si aplica:
1. Pedir a Rafael el export HTML desde Beehiiv del artículo recién publicado.
2. Archivar el master actual: `mv content/templates/articulo-beehiiv-master.html content/templates/_archive/articulo-beehiiv-master-<YYYY-MM-DD>.html` (versionado histórico, nunca borrar).
3. Guardar el nuevo export como `content/templates/articulo-beehiiv-master.html`.
4. Actualizar `content/templates/estructura-templates.md` → tabla "Historial de masters" con fecha, origen (artículo que generó el export) y resumen de cambios vs master anterior.

**Si no hay cambios de formato:** saltar este paso.

### 10. Sugerir actualización de Welcome Email

Evaluar si el artículo nuevo debería reemplazar o complementar el link del Welcome Email actual. Mostrar a Rafael:
- El link actual del Welcome Email
- El link del artículo nuevo
- Recomendación: ¿cambiar el link? ¿añadir como segundo link? ¿dejarlo como está?

Rafael decide. NO cambiar automáticamente.

### 11. Generar contenido social

Invocar `/social-content` con el artículo publicado para generar posts para:
- LinkedIn (1 post)
- X/Twitter (3 posts)
- Instagram (caption para Reel)
- WhatsApp Channel (mensaje)

Recordar a Rafael: **programar los posts en Buffer** después de revisarlos. Generar no es publicar.

### 12. Sincronizar con Obsidian

Invocar `/obsidian-robohogar sync-published <slug>`. Ese modo cubre:
1. Copiar el artículo publicado a `03-Published/YYYY-MM-DD-<slug>.html`
2. Auto-sync de los 4 archivos editoriales: `guia-implementacion.md`, `registro-articulos.md`, `calendario-editorial.md`, `registro-newsletters.md`
3. Wiki update — crear/actualizar fichas de robots y empresas mencionados en el artículo (`Wiki/Robots/`, `Wiki/Empresas/`). Si la ficha ya existe, añadir bullet con la noticia y bumpear `updated:` del frontmatter

Si `sync-published` falla o no está disponible, hacer las 3 tareas manualmente (leer `.claude/commands/obsidian-robohogar.md` secciones 1-2 y "Archivos que SIEMPRE se sincronizan").

### 13. Commit (NO push automático)

Commit con todos los cambios de esta sesión post-publicación:
```
post-publish: <título artículo>

Published: <URL>
Cleaned <N> unused hero variants, updated sources/catalog, synced Obsidian.
```

**NO pushear automáticamente.** Preguntar a Rafael: "¿Hago `git push`?". Regla del proyecto (CLAUDE.md): no auto-push a menos que Rafael lo pida.

### 14. Reportar resumen

Mostrar a Rafael un resumen con 4 secciones: **Verificación** (artículo, OG, links, imágenes), **Repo** (published, limpieza, fuentes, catalog, llms.txt, commit), **Distribución** (social + welcome email), **Obsidian** (guía, artículo, wiki). Cada línea con ✅/❌. Incluir recordatorio de pegar `content/llms.txt` en Beehiiv.

## Rules

- NUNCA cambiar el Welcome Email sin confirmación de Rafael
- NUNCA publicar social content automáticamente — solo generar para revisión
- Si algún paso falla, continuar con los demás y reportar el fallo al final
- El artículo en `content/articulos/<slug>/` NO se borra — se mantiene como carpeta de trabajo con assets
- Recordar SIEMPRE a Rafael que programe los posts en Buffer tras revisarlos
