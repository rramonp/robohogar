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
- [ ] **Cero referencias fantasma** — contrastar el HTML publicado contra promesas internas sin referente real. Grep + verificación manual:
  ```bash
  grep -nE "(tabla|gráfico|infografía|diagrama|imagen|sección|checklist|cuadro|bloque) (de abajo|abajo|arriba|que (te mostramos|verás|ves)|a continuación|más adelante|al final|al principio|al cierre)" <html-publicado>
  ```
  Para cada match, verificar que el referente existe en el cuerpo (`<table>`, `<img>`, `<div class="checklist">`, H2 correspondiente, etc.).

  **Triaje + acción (decisión 2026-04-20):**

  | Caso | Qué hace el skill |
  |---|---|
  | **Fantasma evidente + fix obvio** (p.ej. quitar "la tabla de abajo —" del subtítulo cuando no hay tabla; borrar un link cuyo URL destino no existe en `registro-articulos.md`; sustituir "Gartner" por la fuente correcta del cuerpo) | **Arreglar directamente** en `borrador.html` + `content/published/YYYY-MM-DD-<slug>.html`. Reportar el fix aplicado en el resumen final. NO preguntar a Rafael — las ediciones son obvias y de integridad editorial. Rafael las valida en el diff del commit. |
  | **Fantasma ambiguo / fix no evidente** (p.ej. un párrafo entero se apoya en una tabla inexistente y reescribir implica redactar el argumento de otra forma; una cifra sin fuente que podría ser correcta pero no está citada) | **PARAR y avisar** con la lista de promesas huérfanas + la propuesta de fix para cada una. Rafael decide. |

  **Regla operativa del auto-fix evidente:**
  - El cambio es ≤1 frase tocada por fantasma (quitar un sub-fragmento, sustituir un sustantivo, eliminar un link).
  - La frase mantiene sentido gramatical y semántico tras el recorte.
  - No altera la tesis ni el ángulo del artículo.
  - **Si el cambio obliga a reescribir >1 frase o cambia la estructura del bloque → ambiguo, consultar.**

  Regla completa: memoria [`feedback_robohogar_no_phantom_references.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_no_phantom_references.md) + `@rules/editorial.md § Cero referencias fantasma`. Incidente origen: artículo #8 humanoide-maraton (2026-04-20) — subtítulo prometía "tabla de Stanford abajo" inexistente; Rafael tuvo que reescribir post-publicación.

- [ ] **Datos con fuente rastreable** — verificar que cada cifra, dato o afirmación categórica del artículo publicado tiene fuente rastreable o framing que la marque como claim. Regla completa: `@rules/editorial.md § Datos con fuente rastreable`. Grep obligatorio:
  ```bash
  # (a) Cifras con unidades sin hipertexto cercano
  grep -nE '[0-9]+([.,][0-9]+)?\s*(%|€|\$|millones?|mil|unidades|valoraciones|hogares|kPa|kg|puntos|estrellas|/5)' <html-publicado> | grep -v 'href='

  # (b) Afirmaciones categóricas de exclusividad/primacía
  grep -niE '\b(el único|la única|únic[oa] que|el primer[oa]?|la primera|el mejor|la mejor|jamás|nunca antes|récord absoluto)\b' <html-publicado>

  # (c) Claims del fabricante sin framing "según X"
  grep -niE '(tests? internos|según la marca|según el fabricante|la marca afirma|la compañía dice)' <html-publicado>
  ```

  **Triaje (mismo patrón que § Fantasma):**

  | Caso | Qué hace el skill |
  |---|---|
  | **Evidente + fix obvio** (añadir framing "según Samsung", sustituir "mata el 99,99%" por "Samsung afirma que mata el 99,99%", suavizar "el único" → "uno de los únicos", quitar una cifra sin pilar editorial) | **Arreglar directamente** en `borrador.html` + `content/published/YYYY-MM-DD-<slug>.html`. Reportar el fix en el resumen final. NO preguntar. |
  | **Ambiguo** (cifra sin fuente que puede ser correcta pero no sé verificar en sesión; reescritura afecta al argumento central; dato histórico dudoso como "NaviBot desde 2003" que requiere fact-check) | **PARAR y avisar** con la lista de claims sin fuente + propuesta de fix por cada uno (añadir link, suavizar, eliminar). Rafael decide. |

  Fundamento: auditoría 2026-04-20 de los 8 primeros artículos detectó 14 claims sin fuente/framing (Samsung NaviBot 2003 probablemente erróneo, Tesla 20.000M sin cita, "el único compañero inteligente", 99,99% bacterias sin link, etc.). Corpus en [`references/audit-2026-04-20-unsourced-claims.md`](../../references/audit-2026-04-20-unsourced-claims.md).

### 2. Mover borrador a published

**Pre-check obligatorio — variantes elegidas:** contar bloques de cada patrón v1/v2/v3 en el borrador (hook, veredicto, ¿sabías que?). Si queda ≥2 de cualquiera, **PARAR y avisar a Rafael** — no eligió, el artículo publicado tendría 2-3 bloques redundantes visibles.

```bash
# Cada grep debe devolver exactamente 1 (Rafael dejó solo la variante elegida)
# 0 = el borrador nunca tuvo esa sección triplicada → continuar
# ≥2 = auto-detectar variante publicada desde la URL (ver algoritmo abajo), NUNCA preguntar a Rafael
grep -c 'class="callout-amber hook-option"'     content/articulos/<slug>/borrador.html
grep -c 'class="callout-amber veredicto-option"' content/articulos/<slug>/borrador.html
grep -c 'class="sabias-option"'                  content/articulos/<slug>/borrador.html

# Bloques image-optional: deben ser 0 antes de publicar (Rafael decidió sí/no)
grep -c 'class="image-optional"' content/articulos/<slug>/borrador.html
# Si devuelve ≥1: PARAR, avisar a Rafael que decida cada imagen opcional (borrar bloque completo o borrar solo el wrapper)
```

**Auto-detección de variantes publicadas (regla 2026-04-19 · obligatoria).** Si cualquier `*-option` devuelve ≥2, el skill **NUNCA pregunta a Rafael** cuál eligió. En su lugar, fetchea el post publicado y lo infiere por matching textual:

1. `WebFetch <URL>` con prompt que extraiga literalmente el texto del hook (primer callout), el veredicto (bajo H2 `"Nuestro veredicto"`) y la sección `"¿Sabías que…?"`.
2. Para cada bloque con ≥2 variantes en el borrador, comparar la primera frase distintiva del texto publicado contra cada variante v1/v2/v3 del borrador local. La coincidencia textual (aunque Rafael haya editado ligeramente al pegar) identifica la variante.
3. **Limpiar el borrador:** eliminar las 2 variantes no elegidas + el bloque `<p class="variant-reco">` + el comentario HTML `<!-- ... ELIGE UNO Y BORRA LOS OTROS 2 BLOQUES ... -->` + el comentario `<!-- ═ FIN ... ═ -->`. Dejar la variante ganadora sin el prefijo `[HOOK vN · xxx]` ni el atributo `data-variant` (limpieza final para que `published/YYYY-MM-DD-<slug>.html` refleje lo que realmente se publicó).
4. Continuar con `cp` a `content/published/`.

Ejemplo de matching: si el post publicado empieza el hook con *"Los 'top 10 robots aspiradores 2026' llevan empachando Google..."* y el borrador v1 empieza con *"Los listicles 'top 10 robots aspiradores 2026' llevan empachando Google..."*, es v1 (coincidencia ≥60% de tokens distintivos). Este pattern es el único que Rafael quiere — **nunca preguntarle qué variante eligió, ni cuando pega edits menores al texto**.

```bash
cp content/articulos/<slug>/borrador.html content/published/YYYY-MM-DD-<slug>.html
```

### 2.5. Validación tangibles — OBLIGATORIO (bloqueante)

Verificar que el borrador cumple las reglas de `@rules/tangibles.md` y [`content-draft.md §8.7 + §8.8`](content-draft.md) antes de archivar. Si alguna falla, **PARAR y pedir a Rafael que reescriba o ajuste** antes de continuar con los pasos 3-14.

```bash
# (a) Banner lead-magnet insertado si el artículo es consumer
# Leer frontmatter.category del borrador
CATEGORY=$(grep -E "^category:" content/articulos/<slug>/borrador.html | head -1 | sed 's/.*: //')
if [[ "$CATEGORY" =~ ^(aspirador|cortacésped|mascota-robot|fregasuelos|limpia-cristales)$ ]]; then
  BANNER_COUNT=$(grep -c 'class="banner-lead-magnet"' content/articulos/<slug>/borrador.html)
  if [[ "$BANNER_COUNT" -lt 1 ]]; then
    echo "❌ Artículo consumer ($CATEGORY) sin banner lead-magnet — reinsertar con el snippet de content/templates/banner-lead-magnet.html"
    exit 1
  fi
fi

# (b) Subtítulo menciona el tangible con cifra (regex: checklist/tabla/guía seguido de <40 chars + dígito)
SUBTITLE=$(grep -E '<p class="subtitle">' content/articulos/<slug>/borrador.html | head -1)
echo "$SUBTITLE" | grep -qE '(checklist|tabla|guía)[^<]{0,40}[0-9]+' || echo "⚠️  Subtítulo sin cifra/tangible concreto — revisar antes de publicar (regla tangibles.md § Promoción en subtítulo)"

# (c) Si el artículo referencia un tangible nuevo (slug en content/lead-magnets/<slug_tangible>/), verificar que beehiiv-ficha.md existe
for LM in $(grep -oE 'lm=[a-z0-9-]+' content/articulos/<slug>/borrador.html | sort -u | sed 's/lm=//'); do
  if [[ -d "content/lead-magnets/$LM" && ! -f "content/lead-magnets/$LM/beehiiv-ficha.md" ]]; then
    echo "❌ Tangible $LM referenciado sin beehiiv-ficha.md — regenerar con /pdf-brand <variante> $LM"
    exit 1
  fi
done
```

Reportar resultado a Rafael antes de continuar al paso 3.

### 3. Archivar variantes de hero no usadas

Mover todas las variantes de hero excepto la elegida (PNG + WebP) a `assets/_archive/`:
```bash
mkdir -p content/articulos/<slug>/assets/_archive
# Mantener solo hero-<slug>-v<elegida>.png y .webp en assets/
# Mover el resto de hero-<slug>-v*.png y .webp a assets/_archive/
```
Las variantes quedan accesibles en disco para re-usar como referencia visual o recuperación rápida sin necesidad de git. Nunca borrar — la regla del repo es archivar, no eliminar.

### 4. Actualizar guia-implementacion.md (tablero vivo)

Actualizar [`docs/guia-implementacion.md`](../../docs/guia-implementacion.md) en 3 lugares para mantener el tablero sincronizado con el pipeline. Reglas del tablero vivo: `docs/guia-implementacion.md § 🗓 Schedule semanal fijo § Regla de oro`.

**(a) Marcar checkboxes del sprint** en `§ 📍 Dónde estoy hoy — siguiente paso` correspondientes al artículo recién publicado:
```
- [x] Publicado → <URL>
```

**(b) Actualizar `§ 📍 Dónde estoy hoy § 📌 Próximos 3 next steps`:**
1. Marcar el bullet que correspondía al artículo publicado como `- [x]`.
2. Añadir un bullet nuevo al final tirando del backlog en [`content/calendario-editorial.md § Backlog`](../../content/calendario-editorial.md). Mantener siempre 3 bullets activos desmarcados (o 2 sin marcar + 1 recién marcado esperando commit).
3. Respetar el formato exacto: `- [ ] **Next N —** <acción> · frase trigger: *"<frase>"* · ruta: \`<archivo>\``.
4. Actualizar al final de la sección **"Último artículo publicado:"** con el número, título y fecha del artículo recién publicado.

**(c) Actualizar `§ 🎯 Roadmap actual § Prioridad 1`:**
- Bumpear el contador "X → Y artículos publicados" si aplica.
- Actualizar la línea "Último: [título](URL) (YYYY-MM-DD)" en la sección de estado al principio del Roadmap.

**(d) Si el artículo promociona un tangible nuevo o una versión nueva de tangible existente**, actualizar también `§ 🎯 Roadmap actual § Prioridad 3 Tangibles — Primer tangible activo` con la referencia (slug + versión).

**Regla anti-desfase:** si después de estos cambios los 3 next steps están todos marcados `[x]`, **parar y avisar a Rafael** — el backlog de calendario-editorial necesita refresh antes de continuar.

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

### 5.5. Asignar tags Beehiiv (manual copy-paste)

Beehiiv no expone API pública para tags desde el repo, así que este paso genera el copy-paste exacto para Rafael.

Consultar la tabla maestra en [`@rules/automation.md § Tags Beehiiv ROBOHOGAR`](../rules/automation.md) y emitir:

```
📋 TAGS A ASIGNAR EN BEEHIIV POST SETTINGS:

Post: <título>
URL: <URL>

Tags a marcar:
1. <tag-categoría> ← según frontmatter.category
2. <tag-tangible> ← si el artículo promociona un tangible vía banner (ej. "tangible-hoja-compra")
[+ cualquier tag extra si el artículo cruza categorías]

Automation que se disparará:
- <descripción de la automation activa o "(ninguna todavía)">
```

Mostrar a Rafael este bloque al final del paso 5. Pedir confirmación: "¿tags asignados en Beehiiv?" antes de continuar al paso 6. Si Rafael dice "no todavía", anotarlo en el resumen final (paso 14) y continuar.

### 5.7. Actualizar snippet archive Beehiiv (OBLIGATORIO)

Tras registrar el artículo, actualizar el snippet HTML del listado del archive de Beehiiv para que incluya la card del artículo recién publicado. Fichero fuente-de-verdad: [`content/templates/beehiiv-archive-snippet.html`](../../content/templates/beehiiv-archive-snippet.html).

Rafael pega este snippet en **Beehiiv → Settings → Website → Pages → Archive → Top content → `/html` → Custom HTML block** cada vez que hay un artículo nuevo. Este paso lo genera listo para copy-paste.

**(a) Extraer metadata del post publicado** con un solo `WebFetch <URL>` (reaprovechar el del paso 1 si ya se hizo):

- **Título** → `<h1>` del post publicado.
- **Subtítulo/dek** → `<p class="subtitle">` del post publicado (el que aparece bajo el H1). Si no existe, usar `meta_description` del frontmatter del borrador.
- **Hero URL** → `og:image` del `<head>` del post publicado (es la URL CDN de Beehiiv tipo `https://media.beehiiv.com/cdn-cgi/image/format=auto,fit=scale-down,onerror=redirect/uploads/asset/file/<uuid>/<filename>.webp`).

**(b) Mapear `frontmatter.category` al `data-category` del chip:**

| `frontmatter.category` | `data-category` del chip |
|---|---|
| `aspirador` · `fregasuelos` · `limpia-cristales` | `aspirador-suelos` |
| `cortacésped` | `cortacesped` |
| `humanoide` · `asistente-ia-escritorio` · `mascota-robot` | `humanoide-ia` |
| `ficcion` | `ficciones` |
| `editorial` (sin categoría de producto clara) | inferir por tag Beehiiv dominante (`humanoide-ia` si Humanoides/IA, `aspirador-suelos` si Aspiradores, etc.) |

**(c) Construir la card** con este template exacto (sustituir los 5 placeholders). El byline usa la URL del avatar de autor Beehiiv (hardcodeada — si Rafael cambia el avatar de autor en Beehiiv, actualizar ESTA url + la del template en `beehiiv-archive-snippet.html`).

**Regla especial para ficciones (`data-category="ficciones"`):** el `<TITULO>` SIEMPRE va prefijado con `🎧 ` (emoji auriculares + espacio) para señalar que el relato tiene audiolibro. Ej: `<h3 class="rbh-arc-card-title">🎧 El que viene a tomar café</h3>`. Es el único emoji permitido en las cards del archive (regla editorial "no emojis" se relaja aquí por decisión Rafael 2026-04-23). Aplica aunque el post no tenga audiolibro activo todavía — la 🎧 es marcador visual del pilar "Ficciones Domésticas", no de "tiene audio".

```html
    <a class="rbh-arc-card" data-category="<CHIP_SLUG>" href="<URL_ARTICULO>">
      <div class="rbh-arc-thumb"><img src="<HERO_URL>" alt=""></div>
      <h3 class="rbh-arc-card-title"><TITULO></h3>
      <p class="rbh-arc-card-dek"><SUBTITULO></p>
      <div class="rbh-arc-card-byline">
        <img class="rbh-arc-card-avatar" src="https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/user/profile_picture/864dc8b9-fd48-414a-ac12-0b53cb770fe9/profile-icon-1080x1080.png" alt="">
        <span>Rafael de ROBOHOGAR</span>
      </div>
    </a>
```

**(d) Insertar al principio del grid** del fichero `content/templates/beehiiv-archive-snippet.html`. El marcador `<!-- ══ NUEVAS CARDS SE INSERTAN AQUÍ (más reciente arriba) ══ -->` señala la posición exacta: la card nueva va inmediatamente **después** de ese comentario y **antes** de la primera `<a class="rbh-arc-card">` existente. Así el archivo mantiene orden cronológico descendente (más reciente arriba — patrón idéntico a `robohogar.com`).

**(e) Actualizar la metadata del comentario inicial** del fichero: línea `Último artículo añadido: <slug> (<fecha>)` con el slug y fecha del artículo recién publicado.

**(f) Guardar snapshot junto al artículo** — copiar el template actualizado a `content/articulos/<slug>/beehiiv-archive-snippet.html`. Esto deja un snapshot histórico del estado del archive justo después de que este artículo entró: útil para auditoría ("¿cómo estaba el archive el día que publiqué X?") y para recuperación rápida si el template central se edita mal.

```bash
cp content/templates/beehiiv-archive-snippet.html content/articulos/<slug>/beehiiv-archive-snippet.html
```

**(g) Entregar el snippet a Rafael** — mostrarle en el chat un bloque de código con el contenido ENTERO del fichero `content/templates/beehiiv-archive-snippet.html` actualizado (sin el comentario HTML de cabecera que es interno del repo), listo para copy-paste al Custom HTML block de Beehiiv. Recordarle la ruta: *"Settings → Website → Pages → Archive → Top content → /html → Custom HTML block → pegar (reemplaza el anterior)."*

**Regla anti-duplicados:** antes de insertar, grep el fichero por la URL del artículo nuevo (`grep -c "<URL_ARTICULO>"` en el fichero). Si devuelve ≥1, el artículo ya está en el archive — no insertar, avisar a Rafael *"Este artículo ya está en el snippet archive — no duplico."* y continuar al paso 6.

**Verificación pre-output:**
```bash
# El grid debe tener exactamente 1 card por artículo del registro.
# Usar ^\s* para excluir las menciones del comentario HTML de cabecera.
grep -cE '^\s*<a class="rbh-arc-card"' content/templates/beehiiv-archive-snippet.html
# Debe coincidir con el nº de artículos en content/registro-articulos.md
# (filas de la tabla, excluyendo encabezado + línea del campo Evergreen).
```

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
