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
| <N> | <fecha> | <título> | <slug> | <URL> | <tipo> | <tags> |
```

Este archivo se sincroniza a Obsidian automáticamente en el paso 11.

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

### 9. Actualizar templates HTML (si aplica)

Evaluar si el artículo publicado implica cambios en los templates:

**Si el artículo usa un template existente** (Review/Comparativa o Editorial/Opinión):
- Descargar el HTML final publicado desde Beehiiv (pedir a Rafael el export HTML)
- Si Rafael ha hecho cambios de formato significativos respecto al template anterior (nuevos bloques, cambio de estructura, nuevos estilos), reemplazar el HTML base en `content/templates/`:
  - `review-comparativa-beehiiv-export.html` para reviews
  - `editorial-opinion-beehiiv-export.html` para editoriales
- Actualizar `content/templates/estructura-templates.md` si la estructura de bloques ha cambiado

**Si el artículo es de un tipo NUEVO** (ej: primer Newsletter, primer Roundup):
- Pedir a Rafael el export HTML de Beehiiv
- Guardarlo como nuevo template: `content/templates/<tipo>-beehiiv-export.html`
- Documentar la estructura de bloques en `estructura-templates.md` (nueva sección)
- Actualizar la tabla de templates en `content-draft.md`

**Si no hay cambios de formato:** no hacer nada en este paso.

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

Tres acciones:

1. **Sync guía** al vault:
```bash
cp docs/guia-implementacion.md "$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md"
```

2. **Sync artículo publicado** — si `/obsidian-robohogar sync-published` está disponible, invocar para copiar el artículo al vault en `03-Published/`

3. **Wiki update (OBLIGATORIO)** — ejecutar `/obsidian-robohogar wiki-update`: crear fichas de robots en `Wiki/Robots/` y empresas en `Wiki/Empresas/` para TODOS los mencionados en el artículo. Usar templates del vault. Si la ficha ya existe, añadir bullet con la noticia

### 13. Commit y push

Commit con todos los cambios de esta sesión post-publicación:
```
Post-publish: <título artículo>

Published: <URL>
Cleaned <N> unused hero variants, updated sources/catalog, synced Obsidian.
```

Push automático.

### 14. Reportar resumen

Mostrar a Rafael un resumen con 4 secciones: **Verificación** (artículo, OG, links, imágenes), **Repo** (published, limpieza, fuentes, catalog, llms.txt, commit), **Distribución** (social + welcome email), **Obsidian** (guía, artículo, wiki). Cada línea con ✅/❌. Incluir recordatorio de pegar `content/llms.txt` en Beehiiv.

## Rules

- NUNCA cambiar el Welcome Email sin confirmación de Rafael
- NUNCA publicar social content automáticamente — solo generar para revisión
- Si algún paso falla, continuar con los demás y reportar el fallo al final
- El artículo en `content/articulos/<slug>/` NO se borra — se mantiene como carpeta de trabajo con assets
- Recordar SIEMPRE a Rafael que programe los posts en Buffer tras revisarlos
