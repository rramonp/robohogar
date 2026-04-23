# Content Draft — Borrador de artículos ROBOHOGAR

Genera borradores de artículos para Beehiiv desde research digests o temas libres.
Aplica reglas editoriales, SEO, y formato Beehiiv automáticamente.

## When to activate

- "escribe artículo", "draft", "borrador", "nuevo artículo"
- "escribe un review de", "comparativa de", "guía de compra"
- "artículo editorial sobre", "artículo de opinión"
- "genera contenido", "prepara un post"

## Workflow

### 1. Determinar tipo de artículo

Preguntar si no está claro:

| Tipo | Contenido | Beehiiv publish | Ejemplo |
|---|---|---|---|
| **Review/Comparativa** (70%) | Producto real, specs, precios, opinión, veredicto | `Email and web` | "Robots de escritorio con IA" |
| **Guía de compra** (70%) | Selección de productos, recomendaciones por presupuesto | `Email and web` | "Mejor robot aspirador 2026" |
| **Editorial** (30%) | Futuro, opinión, tendencias, humanoides | `Email and web` | "Humanoides en casa" |
| **Personal** (30%) | Experiencia propia, anécdota, reflexión | `Email and web` | "Mi vida con un aspirador robot" |
| **Newsletter** (semanal) | 3-5 noticias curadas + editorial + dato + enlace | `Email only` | "ROBOHOGAR #01" |

> **IMPORTANTE:** Artículos = `Email and web` (aparecen en landing + se envían por email).
> Newsletter = `Email only` (solo inbox, NO aparece en la landing).

### 1 bis. Diagnóstico editorial — ángulo 4A + memoria de los últimos 5 artículos

Objetivo: romper monotonía. Evitar que el nuevo artículo clone combo (título · subtítulo · secciones · checklist · cierre · longitud) del anterior. Regla completa + tablas A-F: [`@references/writewithai/10-fundamentals-5-lessons.md`](../../references/writewithai/10-fundamentals-5-lessons.md) (§ Lección 1 y § Matriz de variedad editorial).

**(a) Leer los últimos 5 `PASOS.md`** de `content/articulos/*/PASOS.md` ordenados por fecha descendente (por frontmatter `created` o mtime). De cada uno extraer el bloque `## Decisiones editoriales` si existe (generado desde este paso 1 bis en adelante) y listar los 6 campos editoriales: ángulo 4A · headline template · subtítulo variante · longitud bucket · tangible · cierre · métodos de expansión. Si el artículo es anterior a esta regla y no tiene el bloque, inferir a mano 4A + template + longitud bucket leyendo subtítulo, H2 y cierre — basta estimación.

**(b) Elegir ángulo 4A** (uno de los cuatro de Cole): **Analytical** (*"aquí está el análisis"*) · **Aspirational** (*"te enseño el estado futuro posible"*) · **Anthropological** (*"aquí está la psicología detrás"*) · **Actionable** (*"paso a paso"*). Regla anti-repetición: no repetir el mismo 4A en 2 de los últimos 3 artículos; en ventana de 5, aspirar a ≥3 ángulos distintos. Si la restricción deja 1 opción forzada, declarar el porqué en PASOS.md. Si deja 2-3 opciones, elegir por criterio editorial del tema y documentar.

Salida obligatoria de este paso: una mini-tabla mental con las 6 columnas de los últimos 5 artículos + la decisión provisional para el nuevo. Esa tabla se formaliza en PASOS.md § Decisiones editoriales (paso 8).

### 2. Recopilar input

- **Consultar `content/calendario-editorial.md`** — verificar backlog de temas y temas usados (no repetir)
- Leer el research digest más reciente de `content/drafts/research-digest-*.md`
- Consultar fuentes catalogadas en `references/fuentes-por-categoria.md` (organizado por tags de Beehiiv)
- Si Rafael da un tema específico, investigar con Firecrawl/WebSearch
- Identificar keyword SEO principal y 2-3 secundarias (consultar `rules/seo.md`)
- **Si tipo = Newsletter:** consultar también `references/newsletter/email-marketing-playbook.md` para subject lines (<25 chars), estructura 1-3-1, y best practices de email

### 2.5. Validación mercado ES (OBLIGATORIO antes de escribir)

Regla: `@.claude/rules/editorial.md § Filtro mercado ES/LATAM`. Antes de generar el borrador, confirmar al usuario:

1. **Distribución ES del producto/marca:** ¿aparece en Amazon.es, MediaMarkt, Leroy Merlin, El Corte Inglés o Carrefour? Validar con WebSearch si es dudoso.
2. **Keyword SEO en ES:** ¿la palabra clave principal tiene volumen medible en castellano? Comprobar Google Trends España si hay duda.
3. **Cobertura ES en 4 semanas:** ¿alguna fuente Tier 1-2 de `@references/fuentes-es-master.md` (categorías A/B/C) ha cubierto el tema o su categoría?

Si 2 de 3 son "no" → avisar a Rafael con el texto exacto: *"Este tema parece viralidad anglosajona sin salida ES — distribución ES: [sí/no] · keyword ES: [sí/no] · cobertura ES: [sí/no]. ¿Seguro que lo quieres? Alternativa sugerida: [proponer ángulo con salida ES]."*

Excepción: si la marca es Apple, Tesla, Google, Samsung o Xiaomi → pasar directamente (editorial mainstream). No bloquear.

### 3. Generar borrador

**Decisiones de variedad editorial — OBLIGATORIO antes de abrir el template** (aplicar las tablas del § 1 bis contra los últimos 5 artículos):

- **Longitud bucket** — elegir 1 de 4: `flash` 600-900w · `medio` 1000-1500w · `largo` 1800-2500w · `pillar` 2500+. Anti-repetición: máximo 2 artículos consecutivos del mismo bucket. El nº de H2 escala con el bucket (flash 3 · medio 4-5 · largo 5-6 · pillar 6-7); no clonar el nº exacto del artículo anterior. Declarar en PASOS.md. Tabla C: [`10-fundamentals-5-lessons.md § Tabla C`](../../references/writewithai/10-fundamentals-5-lessons.md).
- **Headline (H1 + subtítulo + meta_description)** — elegir **1 de las 5 Headline Templates Cole** con trípode **WHO / WHAT / WHY** completo: `List` · `Story` · `Opinion` · `Question` · `Framework`. Anti-repetición en template vs últimos 3. **Subtítulo: elegir 1 de 3 variantes**: `cifra+tangible` (default compatible con § 8.7) · `pregunta-gancho` · `afirmación-provocadora`; anti-repetición de variante vs últimos 3. Respetar ≤55 chars title tag (`@rules/seo.md`) + `@rules/editorial.md § Honestidad` + `@rules/editorial.md § Anti-anglicismos`. Tablas A-B: [`10-fundamentals-5-lessons.md § Lección 4`](../../references/writewithai/10-fundamentals-5-lessons.md).
- **Template estructural** — elegir 1 de los 3 (`problem-solution` · `mistakes` · `how-to` → sección "Templates estructurales" al final de este skill) con anti-repetición vs últimos 3. El template dicta la escaleta de H2, no el contenido concreto.
- **Desarrollo por sección: 5 Métodos de Expansión** — cada `<section>` del cuerpo aplica 1 de los 5 métodos Cole: `Reasons` · `Mistakes` · `Action Steps` · `Personal Story` · `Curated Examples`. Prohibido repetir método en secciones contiguas. En artículo con 5 H2, aspirar a 5 métodos distintos. `Personal Story` se entiende SIEMPRE como análisis editorial real del equipo (*"comparamos 14 modelos y descartamos 8 tras cruzar ficha oficial + 3 reviews internacionales"*), NUNCA experimento físico (`@rules/editorial.md § Honestidad de primera persona`). Asignación método↔sección se declara en PASOS.md. Detalle: [`10-fundamentals-5-lessons.md § Lección 5`](../../references/writewithai/10-fundamentals-5-lessons.md).

**Template único — todos los tipos:** `content/templates/articulo-beehiiv-master.html`. Copiar el HTML master y reemplazar el contenido. No hay templates por tipo — el esqueleto es el mismo y la estructura interna se adapta según review, comparativa, editorial, guía o newsletter.

**Proceso:** leer `articulo-beehiiv-master.html`, reemplazar `<title>`, H1, subtítulo, autor/fecha/tiempo y body (H2 + párrafos + tablas + imágenes). **Mantener intactos:** hero image slot, intro callout ámbar, separadores, CTA mid-article ámbar, CTA final de suscripción, footer con trust text. Doc de referencia: `content/templates/estructura-templates.md`.

**Tags de Beehiiv disponibles:** Aspiradores, Cortacéspedes, Humanoides, Asistentes IA, Robot Mascotas, Smart Home, Noticias, Opinión, Guías

Para **Review/Comparativa**, seguir la estructura completa del template:
1. Hook (1-2 frases) → Contexto (1 párrafo) → Criterios de selección
2. Producto por producto: qué es, lo bueno, lo malo, para quién, precio + afiliado, opinión personal
3. Los que NO recomiendo → Tabla resumen comparativa → Veredicto final
4. CTA suave + Disclaimer afiliados

**Tabla resumen — badges clickables OBLIGATORIOS:** la columna de estado (Pre-order / A la venta / Pre-anuncio) debe envolver cada `<span class="badge ...">` en `<a href="URL-oficial" target="_blank" rel="noopener nofollow" style="text-decoration:none;">` apuntando a la página oficial del fabricante (o a la fuente documentada en PASOS.md si no hay página oficial de pre-order). Añadir ` ↗` al final del texto del badge para indicar visualmente que es enlace externo.

```html
<td>
  <a href="https://www.fabricante.com/producto" target="_blank" rel="noopener nofollow" style="text-decoration:none;">
    <span class="badge badge-amber">Pre-order ↗</span>
  </a>
</td>
```

Reusar las URLs de la tabla "Fuentes del artículo" del PASOS.md (la columna `Cómo verificar` ya documenta el dominio oficial). Si una URL no es firme, marcar con comentario `<!-- TODO: confirmar URL oficial -->` junto al `<a>`.

Para otros tipos (editorial, guía, newsletter), usar el mismo master `articulo-beehiiv-master.html` variando los bloques internos — no hay template distinto. Incluir siempre frontmatter YAML con: `title`, `seo_title`, `meta_description`, `slug`, `tags`, `type`, `status`, `created`, `affiliate`, **`evergreen`** (true/false), **`evergreen_note`** (motivo).

**Campo `evergreen`** — clasificar al generar el borrador:
- `true` = comparativa, review, guía, editorial de tesis atemporal → reutilizable en redes meses después (FASE 4B+ repurposing)
- `false` = editorial reactivo sobre noticia/deal/lanzamiento concreto con fecha → caducable en 3-6 meses

El flag se replica en `content/registro-articulos.md` (columna Evergreen) como fuente de verdad del backlog social.

### 3 bis. Diversificación de tangible y cierre

Complementa las decisiones del § 3 con las dos dimensiones que más clonaban artículos consecutivos (feedback Rafael 2026-04-22): checklist idéntica siempre + cierre clonado. Reglas y ejemplos: [`@references/writewithai/10-fundamentals-5-lessons.md § Tablas D-E`](../../references/writewithai/10-fundamentals-5-lessons.md).

- **Tangible** — `@rules/tangibles.md § Checklist accionable` ya contempla sustitución por decision tree / dossier 3-datos / cuadro qué-sí-qué-no. Activar esa sustitución sistemáticamente con anti-repetición: no repetir el mismo tangible en 2 de los últimos 3 artículos. Menú operativo de 5: (a) `checklist` accionable 3-7 ítems · (b) `decision-tree` mini 4-6 bifurcaciones · (c) `dossier-3-datos` clave con fuente · (d) `cuadro-si-no` (qué-sí / qué-no en 2 columnas) · (e) `tabla-standalone` comparativa con ganador marcado. La regla "toda guía publicable lleva 1 bloque accionable visible" del § 8.7 sigue vigente — lo que rota es el **formato** del bloque, no su presencia.
- **Cierre** — elegir 1 de 6 variantes con anti-repetición vs últimos 3: (a) `checklist-CTA` (checklist final + banner suscripción) · (b) `veredicto` suelto 2-3 frases sin checklist · (c) `pregunta` abierta al lector · (d) `manifiesto` 3-5 frases de posición editorial · (e) `tabla-resumen` como último bloque · (f) `minimo-banner` (solo CTA sin prosa). El snippet canónico de banner CTA suscripción (`@rules/newsletter.md § Snippet canónico`) se inserta SIEMPRE al final; lo que varía es **solo la prosa que lo precede**. Tabla E con ejemplos detonantes: [`10-fundamentals-5-lessons.md § Tabla E`](../../references/writewithai/10-fundamentals-5-lessons.md).

Ambas decisiones se declaran en PASOS.md § Decisiones editoriales (paso 8).

### 4. Checklist SEO (de `rules/seo.md`)

- [ ] Título: keyword principal + gancho (max 60 chars)
- [ ] Meta description: resumen con CTA (max 155 chars)
- [ ] H1: 1 por página, incluye keyword
- [ ] H2/H3: variaciones semánticas
- [ ] Alt text en todas las imágenes
- [ ] Internal linking: 2-3 artículos relacionados
- [ ] Mínimo 800 palabras para artículos SEO

### 5. Output

- **Carpeta del artículo:** `content/articulos/<slug>/borrador.html`
- **Assets:** `content/articulos/<slug>/assets/`
- **Vault Obsidian:** `$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/02-Drafts/YYYY-MM-DD-slug.md`
  (usar template vault: `Templates/Template Article Draft.md`)
  `$HBX_VAULT` se resuelve automáticamente en cada máquina (desktop=cri-c, laptop=bakal)

### 6. Generar hero image (OBLIGATORIO — 3 variantes)

Generar 3 variantes con composiciones distintas → `content/articulos/<slug>/assets/hero-<slug>-v{1,2,3}.png`. Script: `$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py`.

**⚠️ Configuración obligatoria (regla dura 2026-04-21 — reincidente):**
- Modelo: `--model 2` (o `--model pro`). **NUNCA `flash`** — el `flash` (gemini-2.5-flash-image) ignora silenciosamente el parámetro `--aspect` y genera siempre cuadrado 1024×1024, rompiendo el estándar OG 1200×630.
- Aspect: `--aspect 16:9`.
- Size: `--size 2K` (produce 2752×1536 aprox — base para el crop).
- **Crop obligatorio post-generación a 1200×630 exacto** (OG estándar Beehiiv/Twitter/LinkedIn) con Pillow. Receta canónica: `assets/branding/nano-banana-prompt-base.md § Dimensiones obligatorias`.
- **Verificación pre-output:** abrir los 3 `.webp` con Pillow y comprobar `img.size == (1200, 630)`. Si alguno no lo cumple → regenerar. No entregar borrador con heros cuadrados o ratios equivocados.

**Antes de lanzar cualquier prompt:** leer `assets/branding/nano-banana-prompt-base.md`. Contiene el **decision tree** (qué composición usar según escena — 1 robot vs varios, home vs warehouse, etc.) y el **suffix compilado anti-neones** que DEBE concatenarse al prompt específico. Con eso se reduce de 7-9 iteraciones a 2-3 por hero.

Secundariamente, `assets/branding/asset-catalog.md` para prompts exactos por tipo de artículo. El script genera `.webp` automáticamente al guardar el PNG — subir WebP a Beehiiv (mantener PNG + WebP en repo).

### 7. Descargar imágenes inline de fuentes (OBLIGATORIO — EJECUTAR EN EL MISMO TURNO)

Cada artículo necesita imágenes inline de las fuentes originales (fabricantes, prensa, eventos). NO generar estas imágenes — usar fotos reales.

> **🚫 Prohibido diferir a manual.** No se admite marcar imágenes como "⚠️ descarga manual pendiente" ni dejar `[rellenar]` en la tabla de PASOS.md. El tooling cubre el flujo end-to-end y descargarlas es parte del entregable del skill. Si el paso falla (HTTP 404 tras 2 intentos, paywall, geobloqueo), documentar en PASOS.md con URL intentada + motivo del fallo — solo entonces queda como TODO. Regla con incidente de origen: `feedback_content_draft_inline_images.md` (memoria auto-memory), Rafael 2026-04-18 en `mejor-robot-aspirador-2026`.

**Proceso ejecutable (secuencia obligatoria, mismo turno que el borrador):**

1. **Identificar** 2-4 productos/eventos/marcas que aparecen en `<img>` del borrador y necesitan foto real.
2. **Buscar la fuente oficial** con `WebSearch` en paralelo (una query por imagen): `"<marca> <modelo> official product image"` u `"<evento> press photo"`.
3. **Extraer la URL del asset** con `WebFetch` sobre la página oficial del primer resultado, prompt literal: *"Return the full URL of the main product hero image. Return only the URL, no other text."*
4. **Descargar** con `curl -fsSL -o content/articulos/<slug>/assets/<figure-NN-slug>.<ext> "<url>"` (escapar `$` en URLs con `\$` en bash).
5. **Comprimir** con Pillow: abrir imagen, resize si width >1400 px (ratio preservado, Image.LANCZOS), `.save(dst, 'JPEG', quality=82, optimize=True)`. Borrar el original si el formato cambia (PNG/WebP → JPG) para no dejar duplicados.
6. **Validar peso**: objetivo <300 KB/imagen web, <200 KB/imagen email. Total del artículo <800 KB. Si tras comprimir sigue alto, reducir quality a 75 o width a 1200.
7. **Registrar en PASOS.md** tabla de inline images con: archivo · sección · URL de origen · peso final · status ✅ descargada. Nunca dejar `[rellenar]` ni `⚠️ descargar`.

**Nombrado:** descriptivo y numerado por orden de aparición: `figure-01-roborock-qrevo-curv-2.jpg`, `figure-02-dreame-x50-ultra.jpg`, etc.

**Criterio de cantidad:** ~1 imagen cada 300-400 palabras. Para un artículo de 1.200 palabras → 3-5 imágenes inline. Productos/robots que el lector no conoce NECESITAN foto — sin foto, un precio no dice nada.

**Dónde colocar imágenes (NUNCA debajo del H2):**
- Colocar DESPUÉS del párrafo que justifica la imagen, no debajo del título
- La imagen debe reforzar un dato concreto que el lector acaba de leer
- Secciones de opinión pura (veredicto, "lo que no te cuentan") van SIN imagen — el texto es el protagonista

**Integridad imagen ↔ caption — OBLIGATORIO (regla `@rules/design.md § Integridad imagen ↔ caption`).** Toda pareja `<img>` + `<p class="fig-caption">` va precedida por un comentario HTML identificador en línea única, inmediatamente antes del `<img>`:

```html
<!-- FIG N: <marca + modelo + detalle clave> -->
<img class="inline" src="assets/figure-NN-slug.jpg" alt="...">
<p class="fig-caption">Imagen: ... Fuente: ...</p>
```

- `N` es el índice secuencial empezando por 0 (hero = FIG 0).
- El "detalle clave" describe la característica que justifica esa imagen concreta ("fregado por rodillo", "patas extensibles 6 cm", "rodillo antienredos"). Al reordenar secciones del borrador, el marcador evita que un caption quede emparejado con una imagen distinta a la que describe. Regla surge de incidente 2026-04-19 (Rafael pegó un caption que se refería a otra figura).
- El comentario es HTML comment — no aparece al copiar a Beehiiv.

Verificación pre-output: contar `<img class="inline">` y `<!-- FIG ` en el borrador. Deben coincidir 1:1. Si falta alguno, completar antes de entregar.

**Control de peso:** Artículos web → <300 KB/imagen razonable. Newsletter email → <200 KB/imagen, <800 KB total. Reportar siempre peso en PASOS.md.

**Imágenes candidatas no-inline — bloque visible OBLIGATORIO (OPTIONAL-IMAGE pattern):**

Si descargas un asset pero decides NO meterlo inline por defecto (exceso de imágenes, sección de opinión pura, duda editorial), **NO dejarlo solo listado en PASOS.md** — eso fuerza a Rafael a redactar el pie de foto desde cero si luego decide usarlo. En su lugar, insertar en la sección correspondiente del HTML un bloque `<div class="image-optional">` con:

1. Nota ámbar visible explicando que es opcional y cómo activarla/borrarla
2. `<img>` con `src` + `alt` apuntando al asset real
3. `<p class="fig-caption">` con pie de foto ya redactado siguiendo la voz editorial del artículo

```html
<div class="image-optional" style="border:2px dashed #F5A623; padding:12px; margin:16px 0; background:#FFF9EF; border-radius:6px;">
  <p style="font-size:12px; color:#6B7280; font-style:italic; margin:0 0 8px;">⚠️ IMAGEN OPCIONAL — asset ya descargado y pie listo. Borra este bloque entero si NO la quieres, o borra solo este <code>&lt;div class="image-optional"&gt;</code> wrapper si SÍ la quieres (dejando img + caption).</p>
  <img class="inline" src="assets/figure-<slug>.<ext>" alt="<descripción concreta>">
  <p class="fig-caption">Imagen: <1-2 frases voz editorial + dato ancla>. Fuente: <fuente>.</p>
</div>
```

**Regla:** por cada asset descargado a `content/articulos/<slug>/assets/` debe existir una de dos cosas en el borrador HTML: (a) bloque `<img>+<p class="fig-caption">` inline activo, o (b) bloque `<div class="image-optional">` con pie de foto listo. Nunca un asset huérfano sin pie redactado.

**Validación:** antes de cerrar el borrador, listar los assets de la carpeta y verificar que cada uno aparece referenciado en el HTML (inline o como image-optional). `/post-publish` comprueba que no queden bloques `image-optional` antes de publicar.

### 8. Generar PASOS.md + mapa visual (OBLIGATORIO)

**Usar el generador automático** para evitar rehacer el 60% repetido cada vez:

```bash
uv run python utilities/generate_pasos.py <slug> <numero-articulo>
```

El script lee el frontmatter YAML del borrador (dentro del `<!-- -->` inicial del HTML) y genera `PASOS.md` pre-rellenado con:
- SEO metadata + char counts (validación automática de límites Beehiiv)
- Tags formateados con backticks
- Publish to (Web only por defecto en fase pre-audiencia)
- Content Gate off (default evergreen)
- Checklist estándar de publicación

Luego rellenar a mano los bloques marcados `[rellenar: ...]`:
- **Conceptos de hero v1/v2/v3** + recomendación del agente
- **Tabla de imágenes inline** (archivo → sección → fuente)
- **Mapa visual ASCII** — diagrama con H1 → secciones → imágenes → CTAs. Este mapa es la guía principal de Rafael para montar en Beehiiv
- **Datos a validar** (precios, fechas que puedan haber cambiado desde research)
- **Fuentes del artículo** (tabla dato/fuente/verificación)
- **Notas editoriales** (tono, ángulo, decisiones)

**Bloque OBLIGATORIO "Decisiones editoriales" — activo 2026-04-22** (alimenta la anti-repetición del § 1 bis + § 3 + § 3 bis del próximo artículo). Insertar al principio del PASOS.md, antes del bloque SEO:

```markdown
## Decisiones editoriales (variedad)
- **Ángulo 4A:** [Analytical | Aspirational | Anthropological | Actionable] — razón: …
- **Headline template:** [List | Story | Opinion | Question | Framework]
- **Subtítulo variante:** [cifra+tangible | pregunta-gancho | afirmación-provocadora]
- **Longitud bucket:** [flash | medio | largo | pillar] — palabras objetivo: …
- **Template estructural:** [problem-solution | mistakes | how-to]
- **Tangible:** [checklist | decision-tree | dossier-3-datos | cuadro-si-no | tabla-standalone]
- **Cierre:** [checklist-CTA | veredicto | pregunta | manifiesto | tabla-resumen | minimo-banner]
- **Métodos de expansión por sección:**

  | # | H2 | Método |
  |---|---|---|
  | 1 | … | Reasons |
  | 2 | … | Mistakes |
  | … | … | … |

### Diff vs últimos 3 artículos
| Dimensión | N-1 | N-2 | N-3 | Este | ¿Distinto? |
|---|---|---|---|---|---|
| Template H1 | … | … | … | … | ✅/❌ |
| 4A | … | … | … | … | ✅/❌ |
| Subtítulo variante | … | … | … | … | ✅/❌ |
| Longitud bucket | … | … | … | … | ✅/❌ |
| Tangible | … | … | … | … | ✅/❌ |
| Cierre | … | … | … | … | ✅/❌ |
```

Control de calidad: si la tabla diff muestra ≥2 `❌` (repeticiones), reconsiderar la decisión antes de entregar el borrador — una dimensión que colisiona con los últimos 3 rompe la regla anti-repetición del § 1 bis. Los bloques son el único gate: si no están rellenados, el paso 8 no se cierra.

Template origen: `content/templates/PASOS-template.md`. Script: `utilities/generate_pasos.py`.

### 8.4 bis. Cero referencias fantasma — OBLIGATORIO antes de entregar borrador

Regla de integridad editorial: **toda promesa interna del texto debe tener referente real en el mismo artículo**. Si el subtítulo dice "la tabla de abajo", debe existir `<table>`. Si un callout dice "hay que leer lo mismo desde otra tabla", esa tabla tiene que estar. Si el cuerpo promete "la checklist al final", la checklist tiene que existir.

Regla completa + incidente origen (artículo #8 maratón humanoide, 2026-04-20): memoria [`feedback_robohogar_no_phantom_references.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_no_phantom_references.md) + `@rules/editorial.md § Cero referencias fantasma`.

**Grep obligatorio pre-entrega:**

```bash
# Detectar promesas de elementos internos
grep -nE "(tabla|gráfico|infografía|diagrama|imagen|sección|checklist|cuadro|bloque) (de abajo|abajo|arriba|que (te mostramos|verás|ves)|a continuación|más adelante|al final|al principio|al cierre)" content/articulos/<slug>/borrador.html
```

Para cada match: verificar manualmente que el referente existe en el HTML (`<table>`, `<img>`, `<div class="checklist">`, H2 con nombre correspondiente, etc.). Si no existe: **reescribir la frase** (no eliminar el bloque entero si la frase es recuperable) o **eliminar la promesa** y dejar solo prosa informativa.

**Referencias cruzadas a otros artículos ROBOHOGAR:** la URL debe existir en `content/registro-articulos.md`. Si el artículo enlazado aún no está publicado → eliminar el link o dejarlo pendiente para futura actualización post-publish. Nunca linkear a URL especulativa.

**Regla de decisión:** ≥1 referencia fantasma → rechazar output y reescribir frases · 0 referencias fantasma → proceder al paso 8.4 ter.

### 8.4 ter. Datos con fuente rastreable — OBLIGATORIO antes de entregar borrador

Regla hermana de 8.4 bis: **cada cifra o afirmación categórica del cuerpo debe llevar fuente rastreable en la misma frase/párrafo O framing que la marque como claim no verificado**. Regla completa con las 9 categorías + ejemplos: `@rules/editorial.md § Datos con fuente rastreable`.

**Grep obligatorio pre-entrega:**

```bash
# (a) Cifras con unidades sin hipertexto cercano
grep -nE '[0-9]+([.,][0-9]+)?\s*(%|€|\$|millones?|mil|unidades|valoraciones|hogares|kPa|kg|puntos|estrellas|/5)' content/articulos/<slug>/borrador.html | grep -v 'href='

# (b) Afirmaciones categóricas de exclusividad/primacía
grep -niE '\b(el único|la única|únic[oa] que|el primer[oa]?|la primera|el mejor|la mejor|jamás|nunca antes|récord absoluto)\b' content/articulos/<slug>/borrador.html

# (c) Claims del fabricante sin framing "según X"
grep -niE '(tests? internos|según la marca|según el fabricante|la marca afirma|la compañía dice)' content/articulos/<slug>/borrador.html
```

**Para cada match del grep (a):** ¿hay `<a href>` en la misma frase o párrafo? ¿O está cualificado con "según / aproximadamente / estimamos / el orden de"? Si no → añadir link O reescribir sin cifra.

**Para cada match del grep (b):** ¿hay fuente que lo respalde? Si no → suavizar (*"uno de los únicos"*, *"de los primeros"*) o eliminar.

**Para cada match del grep (c):** ¿la frase deja claro que es claim del fabricante? Ej: *"mata el 99,99%"* ❌ · *"Samsung afirma que mata el 99,99%"* ✅.

**Datos catalogados:** toda cifra debe tener fuente verificable en `references/fuentes-por-categoria.md` para esa categoría. Si no está catalogada → añadirla antes de entregar o descartar el dato.

**Regla de decisión:** ≥1 match sin arreglar → rechazar output · 0 matches sin arreglar → proceder al 8.4 quater.

### 8.4 quater. Honestidad de primera persona — OBLIGATORIO antes de entregar borrador

Regla dura activada 2026-04-21. Aplica `@rules/editorial.md § Honestidad de primera persona — cero verbos de acción no realizada`. ROBOHOGAR NO prueba robots en mano, NO desmonta unidades, NO mide dB ni tiempos con cronómetro propio. Cualquier verbo que implique eso es mentira editorial inmediata.

**Grep obligatorio pre-entrega** (`borrador.html`):

```bash
# (a) Verbos de test físico con voz plural/pasado
grep -niE "\b(probad[oa]s?|probamos|hemos probado|testad[oa]s?|hemos testad|medid[oa]s?|hemos medido|desmontad[oa]s?|hemos desmontado|hemos usado|hemos visto en acción|en nuestro test|en nuestras pruebas|en mano|lo hemos oído|lo hemos tenido|hemos comprobado|hemos cronometrado)\b" content/articulos/<slug>/borrador.html

# (b) Afirmaciones de "uso real" que implican experimentación propia
grep -niE "(uso real en (jardines|pisos|hogares|casas)|en pruebas reales|probados en|testados en|en nuestras manos|nuestra experiencia con el producto)" content/articulos/<slug>/borrador.html

# (c) Claims sensoriales o de medición sin framing de fuente
grep -niE "(literal(es|mente) [0-9]|cronometrados? en|medimos |medid[ao] (por nosotros|en nuestro)|hemos (escuchado|oído|percibido|visto por dentro))" content/articulos/<slug>/borrador.html

# (d) "6 modelos probados" / "Probados X robots" en subtítulos/headers
grep -niE "(probad[oa]s? [0-9]+ (modelos?|robots?|aspiradores?|cortacésped|humanoides))" content/articulos/<slug>/borrador.html

# (e) Cifras de ahorro/ventaja inventadas en subtítulos/CTAs/meta (patrón "te ahorra X €")
grep -niE "(te ahorra[s]? [0-9]+(\.[0-9]+)?\s*(€|EUR|euros)|ahorr[ao] [0-9]+(\.[0-9]+)?\s*€|ahorran [0-9]+(\.[0-9]+)?\s*€|diferencia de [0-9]+(\.[0-9]+)?\s*€|se ahorran? [0-9]+(\.[0-9]+)?\s*€)" content/articulos/<slug>/borrador.html
```

**Para cada match:** reescribir con un sustituto honesto de la tabla de `@rules/editorial.md § Honestidad de primera persona`. Ej:
- *"6 modelos probados"* → *"6 modelos comparados sobre fichas oficiales y reviews internacionales"*
- *"filtro de uso real en jardines españoles"* → *"filtro que cruza ficha oficial + reviews internacionales + distribución ES"*
- *"instalación en 30 minutos literales"* → *"instalación declarada de 30 minutos por el fabricante"*
- *"57 dB de ruido medido"* → *"57 dB declarados por [marca]"*
- *"en primeros meses aún pisa alguna flor"* → *"reviews internacionales del primer año señalan confusiones con flores pequeñas"*
- *"checklist que te ahorra 800 € antes de comprar"* → *"checklist para no equivocarte al comprar"* / *"checklist para no comprar de más"* / *"checklist de 5 cosas que verificar antes de darle al botón"*
- *"te ahorra 80-120 € si ya tienes X"* → *"te ahorra algo de dinero si ya tienes X"* o eliminar la cifra
- Resta aritmética directa SÍ permitida: *"el NERA te saca 900 € por encima del Worx"* cuando ambos precios están citados con fuente en el mismo artículo (2.099 − 1.199 = 900)

**Verbos ✅ permitidos en voz plural ROBOHOGAR:** "hemos comparado", "hemos analizado", "hemos leído", "hemos seleccionado", "hemos descartado", "hemos cruzado", "hemos contrastado", "hemos verificado en [fuente]", "nos ha sorprendido la ficha", "nos parece", "recomendamos", "descartamos". Lo que ROBOHOGAR hace de verdad es análisis editorial sobre información pública — eso basta.

**Regla de decisión:** ≥1 match sin justificación explícita en la misma frase (framing "según el fabricante" / "según reviews de [medio]" / "declarado por [marca]") → **rechazar output y reescribir**. Nunca entregar un borrador con un solo verbo mentiroso — la voz entera del artículo se cae con él.

**Incidente origen + detalle operativo:** memoria [`feedback_robohogar_no_fake_testing_claims.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_no_fake_testing_claims.md). Regla completa: `@rules/editorial.md § Honestidad de primera persona`.

Proceder al 8.5 solo con 0 matches (o todos los matches justificados con framing de fuente).

### 8.5. Anti-IA checklist §1 Universal — OBLIGATORIO antes de entregar borrador

Cargar [`@references/anti-ia-checklist.md`](../../references/anti-ia-checklist.md) **§1 Universal completo** (§1.1 lista negra de palabras, §1.2 tricolon/em-dashes/contrast, §1.3 clichés sensoriales, §1.4 voz plural) y correrlo sobre el `borrador.html`. La §2 Ficción NO aplica aquí — solo relatos.

**Regla de decisión:** ≥3 flags → rechazar output y reescribir · 1-2 flags → reescribir líneas ofensivas y re-correr · 0 flags → proceder al paso 8.5 bis.

Complementa (no sustituye) las prohibiciones de `@rules/editorial.md` (autoridad propia, primera persona plural, filtro ES).

### 8.5 bis. Prosa editorial ES — OBLIGATORIO antes de entregar borrador

Cargar [`@references/editorial-es/01-articulos-y-columnas.md`](../../references/editorial-es/01-articulos-y-columnas.md) **completo** (§1 periodismo tech ES, §2 columnistas ES+LATAM, §3 7 patrones de apertura editorial, §4 calcos EN→ES en transiciones, §5 cierre de artículo, §6 transfusión del toque personal al artículo) y correr la **checklist §7** sobre `borrador.html`.

Esta checklist complementa (no sustituye) la anti-IA universal del paso 8.5. La anti-IA filtra tics LLM genéricos; el KB editorial-es aplica los patrones concretos de los 13 referentes ES+LATAM auditados (Pastor, Eva R. de Luis, Lacort, Peirano, Ortiz, Vázquez, Paniagua, Carrión, Salazar, Caparrós, entre otros).

**Verificaciones §7 OBLIGATORIAS:**
- [ ] **§7.1 Flags automáticos (grep)**: 0 matches en conectores anglo vacíos, cierres cliché, superlativos genéricos sin matiz, narrar proceso de investigación
- [ ] **§7.2 Hook**: primera frase cae en uno de los 7 patrones del §3 (apertura oblicua / hook en dos tiempos / dato concreto + año + lugar / subordinada + pero / hook en negativo concreto / apertura escénica en presente / pregunta propia obsesiva). Si cae en *"La inteligencia artificial es…"* o similar → reescribir
- [ ] **§7.3 Voz personal** (≥3 de 4 en artículos ≥1.000 palabras): apertura con anécdota/persona/momento + humildad epistémica en veredicto + pregunta genuina (si editorial reflexivo) + reclamo humano (1 de cada 3 artículos)
- [ ] **§7.4 Recursos ES positivos** (≥3 de 7): aposición explicativa + dos puntos como pivote + frase corta encadenada + autoexención voluntaria + perífrasis de reencuadre + plural impersonal inclusivo + puente oral ES (*"en honor a la verdad"*, *"tenemos claro que"*, *"letra pequeña"*)

**Regla de decisión:** ≥3 flags automáticos O hook genérico O <3 recursos voz personal (§7.3) O <3 recursos ES positivos (§7.4) → reescribir apertura y cierre como mínimo · 1-2 flags → reescribir frases señaladas · 0 flags + hook ok + recursos presentes → proceder al paso 8.5 ter.

Referentes canónicos del nicho aspirador ROBOHOGAR: **Eva R. de Luis (Xataka)** para reviews — hook con subordinada + pero, veredicto segmentado por perfil, puentes orales ES. **Antonio Ortiz (Error500)** para editoriales — humildad epistémica y analogía estructural.

### 8.5 ter. Calcos léxicos EN→ES — OBLIGATORIO antes de entregar borrador

Capa adicional de validación ES activada 2026-04-21. Motivo: el LLM sigue introduciendo calcos sintácticos/léxicos específicos (*"no compres de más"*, *"dale al botón de comprar"*, *"centro de llamadas"*) que no filtran ni el §8.5 anti-IA ni el §8.5 bis editorial-es. Replica el enfoque que ya aplica `/ficcion-draft § 8.3` en narrativa, adaptado a no-ficción.

**Cargar** (lectura obligatoria si no están en contexto):
- [`@references/editorial-es/01-articulos-y-columnas.md § 4.1`](../../references/editorial-es/01-articulos-y-columnas.md) — tabla de calcos anglo en transiciones y marketing-copy (10 entradas).
- [`@references/ficciones/castellano-literario-es.md § 8.1`](../../references/ficciones/castellano-literario-es.md) — los 21 calcos canónicos (aplicar los relevantes a no-ficción: 1 posesivos con partes del cuerpo · 3 "de repente" · 4 adverbios -mente · 7 conectores anglo · 13 "centro de X" · 15 voz técnica · 17 microcopy UI anglo · 19 "Es decir, X, y Y" · 20 inciso em-dash · 21 dativos de persona errados; NO aplicar los específicos de narrativa: 5 voz pasiva en narrador · 14 "en boca de").

**Grep obligatorio pre-entrega** sobre `borrador.html`:

```bash
# (a) Calcos de marketing-copy anglo (editorial-es §4.1 #9 y #10)
grep -niE "(no (compres|pagues?) de más|comprar de más|pagar de más|ahorrarte comprar|dale al botón de (comprar|pagar|finalizar))" content/articulos/<slug>/borrador.html

# (b) Conectores anglo en transiciones (editorial-es §4.1 #1-#8)
grep -niE "(por otro lado|en este sentido|dicho esto|es importante destacar|cabe destacar|adicionalmente|en conclusión,|en definitiva,|es por ello que|es por esto que|a la hora de|de cara a)" content/articulos/<slug>/borrador.html

# (c) "Centro de X" traducido de "X center" (calco #13 ficciones)
grep -niE "(centro de (demostración|demostracion|llamadas|datos|servicio|atención|atencion|operaciones)|call center|data center)" content/articulos/<slug>/borrador.html

# (d) Voz técnica anglo en narrador editorial (calco #15 ficciones)
grep -niE "\b(configuré|configuró|configuro|configura|configurado|registra|registró|registrado|activó|activado|ejecutó|ejecuta|módulo|input|output|backend|cruzó con (los |las |el |la )?(datos|fotos|archivos|registros|imágenes|imagenes|perfiles|contactos|campos))\b" content/articulos/<slug>/borrador.html

# (e) Microcopy UI anglo traducido (calco #17 ficciones)
grep -niE "(No, gracias|¿Estás seguro|¿Estas seguro|Enviar feedback|Aprender más|Aprender mas|Configuraciones|[Gg]ot it)" content/articulos/<slug>/borrador.html

# (f) Adverbios -mente en cascada (calco #4 ficciones, aplica a artículos)
COUNT=$(grep -oE "[a-záéíóúñ]+mente\b" content/articulos/<slug>/borrador.html | wc -l)
echo "Adverbios -mente: $COUNT (objetivo ≤8 en guía de compra ≥2.500 palabras · ≤4 en artículo <1.200 palabras)"

# (g) "Es decir, X, y Y" — inciso con coordinación anglo (calco #19 ficciones)
grep -niE "\bEs decir, [^.,]{1,40}, y [a-z]" content/articulos/<slug>/borrador.html
```

**Regla de decisión:**
- ≥1 match en (a), (c), (d), (e), (g) → **reescribir antes de entregar** (son calcos duros sin contexto válido en artículo).
- Matches en (b) → revisar caso a caso; algunos pueden tener uso válido (*"por otro lado"* como transición limpia entre dos tesis contrapuestas ≠ relleno anglo).
- Count (f) fuera de objetivo → reescribir frases con -mente de más a perífrasis (*"absolutamente"* → *"del todo"*, *"rápidamente"* → *"rápido"*).

**Read-aloud test — último filtro (heredado de ficciones § 8.1):** si algún match es ambiguo (típicamente (d) y (g) por contexto), LEER LA FRASE EN VOZ ALTA. Si el oído peninsular tropieza — si suena a doblaje de serie, a voz de Google Translate, o a manual técnico traducido — reescribir. Los greps son el primer filtro; la oreja es el segundo y definitivo.

**Origen e incidente 2026-04-21:** artículo #9 cortacésped. El subtítulo entregado decía *"checklist de 7 preguntas para que no compres de más al darle al botón"* — calco literal de *"don't overbuy at checkout"*. Rafael lo detectó al leer: *"'comprar de más' en ES significa 'he comprado 20 aspiradores sin querer, no sea caso'; la forma ES es 'pagar más de la cuenta'"*. Las reglas previas (§ 8.5 anti-IA + § 8.5 bis editorial-es) no incluían este calco específico. Este paso 8.5 ter cierra el agujero.

**Regla de decisión final:** proceder al 8.5 quater solo con 0 matches en (a), (c), (d), (e), (g) + count (f) dentro de objetivo + cualquier match ambiguo resuelto por read-aloud test.

### 8.5 quater. Second reader externo · `/validate-prose-es` — OBLIGATORIO antes de entregar borrador (añadido 2026-04-23)

Los greps de 8.5 ter cogen calcos sintácticos documentados (21 patterns ES) + los específicos de marketing-copy del § 4.1 de editorial-es. Pero NO cogen: colocaciones ambiguas no documentadas aún, registros mezclados, frases que requieren releer, ritmo incoherente, verosimilitud de diálogo. Para eso existe `/validate-prose-es` — un segundo lector sin contexto del proceso de generación que hace challenge por capas (grep deterministic + Agent LLM complementario).

**Invocación obligatoria y autónoma:** tras pasar 8.5 ter con 0 fallos, invocar `/validate-prose-es content/articulos/<slug>/borrador.html` (o la ruta al `.md` si el borrador vive como markdown). **El skill se ejecuta sin pedir autorización a Rafael** — es paso del pipeline, no decisión editorial. Rafael recibe el reporte como parte del output del draft.

El skill devuelve uno de 3 veredictos:

- **READY** — proceder al paso 8.6.
- **PENDING_FIXES** — aplicar los fixes de la tabla al `borrador.html` en pasada atómica. Re-invocar `/validate-prose-es` una vez más. Si sigue PENDING tras 2 pases, mostrar el reporte a Rafael antes de continuar.
- **MAJOR_REWRITE** — BLOQUEAR output. Volver al paso 6 (prosa) con el reporte del validador.

**Log permanente** en `content/articulos/<slug>/validator-reports/YYYY-MM-DD-report.md` (trazabilidad editorial).

**Por qué ojo fresco y no auto-auditoría:** el generador tiene sesgo estructural hacia las decisiones que ya tomó. El validador externo no comparte ese sesgo porque no ve el prompt, no ve `PASOS.md`, no ve el razonamiento. Lección del incidente 2026-04-20 (origen de `/validate-prose-es`): el relato `el-que-viene-a-tomar-cafe` v2 pasó 25 validaciones del skill generador pero Rafael detectó 10+ frases sin sentido al leer. El second reader es la defensa sistémica contra ese sesgo.

Aplica a: reviews, comparativas, guías de compra, editoriales, tutoriales, newsletters publicables, cheatsheets. Cualquier prosa visible al lector ROBOHOGAR.

### 8.6. Formato técnico Beehiiv — OBLIGATORIO antes de entregar borrador

Verificar contra `@rules/editorial.md § Formato técnico (Beehiiv)`. Aplica a TODO tipo de contenido (review, comparativa, editorial, guía, cheatsheet, newsletter).

**Negritas — checklist dura (regla editorial.md § Política de negritas):**
- [ ] Ningún `<strong>`, `<b>` ni `**...**` dentro de `<h1>`, `<h2>`, `<h3>`, `<h4>` (ni en Markdown `## **...**`). Verificación: `grep -nE '<h[1-4][^>]*>[^<]{0,80}<(strong|b)\b' borrador.html` → 0 matches.
- [ ] Ningún `<strong>`/`<b>` dentro de `<thead>`. En `<tbody>` solo la columna 1 (`<td>` de etiqueta de fila) puede ir en `<strong>`; columnas 2+ siempre regular.
- [ ] Ningún `<strong>`/`<b>` dentro de `<div class="checklist">` u otro callout con fondo crema `#FFF9EF` / borde `#F5A623`.
- [ ] **Usar SIEMPRE `<strong>` — NUNCA `<span class="bold">` ni `style="font-weight"` inline.** Razón: `<span class="bold">` arrastra el CSS computado al clipboard y Beehiiv aplica su bold encima (doble peso visible). `<strong>` es HTML semántico que los editores WYSIWYG mapean 1:1 sin problema. Verificación: `grep -c 'class="bold"' borrador.html` → 0. Si el borrador tiene residuales: `sed -i -E 's|<span class="bold">([^<]*)</span>|<strong>\1</strong>|g' borrador.html`.
- [ ] El `<style>` del borrador NO contiene la regla `.bold { font-weight: bold; }`. Si aparece, eliminar. Incidente origen 2026-04-19 (Rafael).
- [ ] SÍ permitido: negrita dentro de párrafos de texto corrido (`<p>...<strong>...</strong>...</p>`), callouts simples y bullets fuera de `.checklist`.

**Tablas (mobile-first):**
- [ ] `<thead><tr>` tiene **≤4 `<th>`**. Si son >4, recortar a las 4 más críticas para la tesis del artículo (el resto va en prosa del cuerpo) o partir en 2 tablas temáticas
- [ ] Cada `<td>` contiene texto corto, **≤25 caracteres orientativo**. Paréntesis largos y disclaimers fuera (al caption o al cuerpo)
- [ ] Nombres de producto reducidos a marca + modelo corto (ej. "Ecovacs X8 Pro Omni", no "Ecovacs Deebot X8 Pro Omni")
- [ ] Unidades pegadas sin espacio cuando se pueda ("100°C", "1.399€") para evitar wrap feo en 375px

Si hay violaciones → limpiar antes de entregar. No es opcional ni se pregunta al usuario: es parte del output estándar.

### 8.7. Tangible mínimo obligatorio + promoción en subtítulo — OBLIGATORIO

Aplicar [`@rules/tangibles.md § Reglas operativas`](../../.claude/rules/tangibles.md). Todo borrador DEBE contener:

- [ ] **Checklist accionable** (3-7 ítems concretos) antes del veredicto/cierre, etiquetada visualmente como callout crema `#FFF9EF` + borde `#F5A623` (`<div class="checklist">`). H2 del bloque empieza por `Checklist —` para que el lector lo reconozca como producto (ej: `<h2>Checklist — 5 preguntas antes de comprar</h2>`). Si el tema no admite checklist natural, sustituir por decision tree mini, dossier "3 datos clave" o cuadro "qué hacer / qué no hacer" — pero NUNCA omitir el bloque accionable.
- [ ] **Subtítulo del artículo** (el `<p class="subtitle">` bajo el H1) menciona el tangible con cifra o promesa concreta. Fórmula: `<qué entrega el artículo> + <tangible con número>`. Ejemplos válidos: *"6 modelos, 3 perfiles y una checklist de 5 preguntas que te ahorra 600 € antes de comprar"*, *"Review + checklist de 5 cosas que verificar en cualquier aspirador con vapor"*. Prohibido subtítulo genérico sin cifra ni tangible (*"la guía honesta, sin hype"* ❌).
- [ ] **`meta_description`** del frontmatter (≤155 chars) también menciona el tangible concreto — es lo que Google muestra en SERP y Beehiiv replica en OG card. Reutilizar la misma promesa que el subtítulo pero reformulada para SEO.
- [ ] **`title`/`seo_title`** puede (opcional) incorporar `+ checklist` si la keyword principal deja margen de caracteres: *"Mejor robot aspirador 2026: 6 finalistas + checklist"* (52 chars). Sin forzar si rompe el límite de 55-60 chars.

**Rechazo automático:** si el borrador sale sin checklist/tangible accionable O con subtítulo/meta_description genéricos sin cifra → bloquear y reescribir. No entregar "pendiente de añadir checklist" en PASOS.md.

### 8.8. Banner lead magnet — INSERCIÓN AUTOMÁTICA (paso ejecutable)

**Activado como paso ejecutable desde 2026-04-19.** `/content-draft` debe emitir el `borrador.html` con el banner YA insertado en las posiciones correctas. No diferir a Rafael. No "recordar pegar". El HTML que sale del skill es el HTML final listo para Beehiiv.

**Antes de componer el copy del banner** (eyebrow, título, subtítulo, CTA, trust-line): cargar [`@references/editorial-es/03-microcopy-ctas-meta.md`](../../references/editorial-es/03-microcopy-ctas-meta.md) §5 (*Banners con voz personal*) y §6 (*Checklist pre-output microcopy*). El banner debe incluir AL MENOS 3 de los 6 recursos positivos del §6.2: inversión del imperativo en CTA + dato no redondeado + paréntesis editorial confidencial + autodefinición plural cálido + tripleta coordinada concreta + microcopy post-CTA específico. Trust-line canónica sigue `rules/tangibles.md § Microcopy` (default *"PDF gratis con tu suscripción semanal. Cancela cuando quieras."*).

**Algoritmo (aplicar al generar el borrador):**

1. **Leer `frontmatter.category`** del borrador en generación (ej: `aspirador`, `cortacésped`, `humanoide`, `ficcion`, `editorial`).
2. **Leer word count** estimado del borrador.
3. **Decidir según tabla:**

   | `category` | Banner Hoja de Compra | Posiciones a insertar |
   |---|---|---|
   | `aspirador`, `fregasuelos`, `limpia-cristales` | ✅ Sí | Si words >1.500: **intro + cierre**. Si words ≤1.500: **solo cierre**. |
   | `cortacésped` | ❌ No — ajuste 2026-04-21 | Las 10 preguntas de Hoja de Compra son aspirador-céntricas (m² piso, umbrales, pelo de mascota, ecosistema Matter). Dolor del lector cortacésped es distinto (pendiente, cable perimetral, ruido vecindario, servicio técnico ES). Tangible específico "Hoja de Compra cortacésped" pendiente F2. |
   | `mascota-robot` (Aibo/Loona/LOOI) | ❌ No — ajuste 2026-04-19 | Tangible específico "Mascota-robot: qué esperar" pendiente F2. Intención lector ≠ aspirador. |
   | `asistente-ia-escritorio` (Eilik, asistentes IA de escritorio) | ❌ No — ajuste 2026-04-19 | Tangible específico pendiente F2. |
   | `humanoide` | ❌ No | Tangible "Guía early adopter humanoides" pendiente mes 3-4. |
   | `ficcion` | ❌ No | Canal narrativo, no mezclar con CTA comercial. |
   | `editorial` sin ángulo de compra | ❌ No | — |

   **Regla general (2026-04-21):** un banner solo se pega si el tangible al que apunta **responde las preguntas concretas** del lector de ese artículo. "Categoría consumer dentro de 500-1.500 €" NO es criterio suficiente. Si no hay variante del tangible para la categoría → artículo SIN banner hasta que la haya. Ver `@rules/tangibles.md § Reglas operativas` "Regla general".

4. **Insertar el banner como BLOQUE DE CÓDIGO VISIBLE** (`<div class="snippet-block">`), NO como `<div>` inline renderizado. Regla completa: `@rules/design.md § Bloques de código para snippets HTML inline en borradores`. Razón: Rafael publica haciendo copy-paste desde el borrador al editor Beehiiv vía `/html` → "Custom HTML block", que requiere el HTML como **texto copiable**, no como elemento ya renderizado.
   - **Posición intro:** tras el callout de intro amber, antes del primer `<h2>` de contenido.
   - **Posición cierre:** tras el bloque "Nuestro veredicto", antes del disclaimer.
5. **Estructura del bloque** (plantilla exacta, sustituir `<SLUG>` por `frontmatter.slug`):

   ```html
   <!-- ═══ BANNER HOJA DE COMPRA · POSICIÓN <INTRO|CIERRE> (bloque de código para Beehiiv) ═══ -->
   <div class="snippet-block">
     <p class="snippet-header">📋 Snippet N · Banner Hoja de Compra · posición <intro|cierre></p>
     <p class="snippet-hint">En Beehiiv: escribe <code>/html</code> → selecciona "Custom HTML block" → pega el código de abajo.</p>
     <pre><code>&lt;div style="..."&gt;...&lt;/div&gt;</code></pre>
   </div>
   ```

   El HTML dentro de `<pre><code>` va **escapado**: `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;` (crítico en los UTM del `href` que llevan `&`).
6. **CSS `.snippet-block`** debe incluirse en el `<style>` del borrador. Plantilla canónica en `@rules/design.md § Bloques de código para snippets HTML`.
7. **UTMs estándar Beehiiv** en el `href` del banner: `?utm_source=<slug>&amp;utm_medium=banner&amp;utm_campaign=hoja-compra`.

**Verificación pre-output:** antes de cerrar el skill, contar bloques `<div class="snippet-block">` que contengan "Banner Hoja de Compra" en el HTML generado. Debe ser:
- **0** si `category ∈ {humanoide, mascota-robot, asistente-ia-escritorio, cortacésped, ficcion, editorial-sin-angulo-compra}`
- **1** si categoría incluida en el scope (`aspirador · fregasuelos · limpia-cristales`) y words ≤1.500
- **2** si categoría incluida en el scope y words >1.500

Si el conteo no coincide → auto-corregir antes de entregar. Además, verificar que el CSS `.snippet-block` esté en el `<style>` del borrador **solo si hay al menos 1 snippet**; si el artículo va sin banner, el CSS `.snippet-block` puede omitirse (no afecta si se queda — es CSS inerte).

**Versionado futuro:** si aparece un nuevo tangible (ej. Guía primer mes aspirador, Glosario ROBOHOGAR), ampliar la tabla de arriba (categoría → tangible → posición) y los snippets en [`banner-lead-magnet-snippets.md`](../../content/templates/banner-lead-magnet-snippets.md). Un artículo puede llevar 2 banners distintos (1 por momento de funnel — ver `@rules/tangibles.md § Mapeo momento del funnel`).

**Microcopy del banner — regla heredada de `@rules/tangibles.md § Microcopy de conversión`.** Si el skill genera una variante del texto del banner para un artículo (p. ej. tangible distinto, copy adaptado a la categoría), la trust-line debajo del CTA debe cumplir el default canónico `PDF gratis con tu suscripción semanal. Cancela cuando quieras.` o una variante que supere las 3 reglas: (a) ≥2 de los 3 elementos obligatorios (formato · salida · transparencia), (b) ninguna promesa prohibida (velocidad de entrega, ausencia futura de publicidad, hype), (c) ≤80 caracteres. Verificación: `grep -iE "15 segundos|llega al email en|instantáneo|sin publicidad|sin promociones|sin letra pequeña"` sobre el `borrador.html` — 0 matches obligatorio antes de entregar.

### 8.8 bis. Snippet CTA suscripción final — INSERCIÓN OBLIGATORIA en todo artículo no-ficción

**Activo desde 2026-04-22.** Todo borrador no-ficción (review, comparativa, editorial, guía, tutorial, newsletter semanal) cierra con un snippet CTA dark al newsletter raíz. Canon y HTML exacto: `@rules/newsletter.md § Snippet canónico · banner CTA suscripción al final de artículo (no-ficción)`. Las ficciones NO llevan este CTA — usan el suyo propio (`§ Snippet canónico · banner suscripción al final de ficción`).

**Posición exacta en el esqueleto:** justo después del bloque `¿Sabías que…?` + su `<div class="separator"></div>`, y antes del bloque `Más en ROBOHOGAR` + disclaimer. Estructura resultante:

```
<h2>💡 ¿Sabías que…?</h2>
<div>... dato + fuente ...</div>
<div class="separator"></div>
<!-- ═══ SNIPPET CTA SUSCRIPCIÓN FINAL (bloque de código para Beehiiv) ═══ -->
<div class="snippet-block">
  <p class="snippet-header">📋 Snippet N · CTA Suscripción final · posición fin-artículo</p>
  <p class="snippet-hint">En Beehiiv: escribe <code>/html</code> → "Custom HTML block" → pega el código de abajo.</p>
  <pre><code>&lt;div style="..."&gt;...&lt;/div&gt;</code></pre>
</div>
<p><strong>Más en ROBOHOGAR:</strong></p>
<ul>...</ul>
<p class="disclaimer">...</p>
```

**Reglas:**

- Insertar como `<div class="snippet-block">` con HTML escapado (`<` → `&lt;`, `>` → `&gt;`) igual que el banner Hoja de Compra. Razón heredada: Rafael copia-pega a Beehiiv vía `/html` → Custom HTML block, que necesita el HTML como texto copiable.
- `href` = `https://robohogar.com` **sin UTM** (regla `@rules/newsletter.md § URL destino de CTAs de suscripción`). Excepción única sigue siendo el banner Hoja de Compra.
- Texto fijo — no variar pregunta, beneficio, botón ni trust-line por artículo. El CTA es un bloque de marca consistente, no copy creativo por post.
- Botón dice `Suscribirse` (infinitivo) — NO `Suscribirme` (eso es solo del banner de ficción).
- El CSS `.snippet-block` ya debe estar en el `<style>` del borrador si el artículo lleva además banner Hoja de Compra; si no, incluirlo igual (es el único bloque snippet del borrador).

**Verificación pre-output:**

```bash
# (a) Exactamente 1 snippet CTA final en el borrador
grep -c "¿Te ha servido este análisis?" <borrador.html>   # debe ser 1

# (b) El CTA NO debe llevar UTM
grep -nE '¿Te ha servido[^<]*</div>.*utm_' <borrador.html>  # debe ser 0

# (c) Posición correcta: después del ¿Sabías que? + separator, antes de Más en ROBOHOGAR
grep -nE 'Sabías que|¿Te ha servido|Más en ROBOHOGAR' <borrador.html>
# el orden de líneas debe ser: Sabías → ¿Te ha servido → Más en ROBOHOGAR
```

Si algún check falla → auto-corregir antes de entregar. No dejar en PASOS.md como "pendiente".

### 8.9. Controles pre-publicación — 12 checks OBLIGATORIO antes de entregar borrador

Última fase de acabado. Regla completa + ejemplos: `@rules/editorial.md § Controles pre-publicación — 12 checks`. Dos bloques independientes:

- **Bloque A — Craft (5 checks):** A1 gancho en el título · A2 blindaje de cifras contrarian · A3 dato-trampolín prohibido · A4 precisión técnica > contundencia fácil · A5 leitmotiv en el cierre.
- **Bloque B — Coherencia interna (7 checks):** B1 recomendación única · B2 paridad cuantitativa promesa↔entrega · B3 nomenclatura única por entidad · B4 criterio declarado=aplicado · B5 paridad de tratamiento visual · B6 verificación cruzada de datos técnicos asociados · B7 claridad de datos comparables.

**Ejecución obligatoria:** responder los 12 checks por escrito en `PASOS.md § Controles pre-publicación` con este formato exacto:

```
## Controles pre-publicación (§ editorial.md — 12 checks)

### Bloque A — Craft
- A1 Gancho en título: [✅/❌] — [leído a la mitad: primera mitad engancha sola]
- A2 Blindaje cifras contrarian: [✅/❌/N/A] — [cifras listadas con parentética, o N/A si no hay contrarian]
- A3 Dato-trampolín: [✅/❌/N/A] — [cada dato asombroso tiene párrafo/frase propia]
- A4 Precisión técnica: [✅/❌] — [rotundas escaneadas y defendibles]
- A5 Leitmotiv en cierre: [✅/❌/N/A] — [verbo/frase repetida atada literal en cierre, o N/A si no hay leitmotiv]

### Bloque B — Coherencia interna
- B1 Recomendación única: [✅/❌/N/A] — [grep cruzado, 1 modelo por etiqueta convergente]
- B2 Paridad cuantitativa: [✅/❌] — [subtítulo promete X → cuerpo entrega X literal y contable]
- B3 Nomenclatura única: [✅/❌] — [cada producto ≥3 menciones usa forma canónica]
- B4 Criterio declarado=aplicado: [✅/❌/N/A] — [incumplimientos justificados en texto del finalista]
- B5 Paridad tratamiento visual: [✅/❌] — [N finalistas = N figures, o excepción en PASOS.md]
- B6 Verificación cruzada datos técnicos: [✅/❌/N/A] — [asociaciones ("hermano", "sucesor") + specs coherentes]
- B7 Claridad datos comparables: [✅/❌/N/A] — [nuevo/refurbed, PVP/promo, UE/import etiquetados]
```

**Regla de decisión:** ≥1 check en ❌ sin arreglar → rechazar output y reescribir. Todos en ✅ o N/A justificado → proceder al § 9 Prohibiciones.

**N/A válido solo cuando el check no aplica por estructura del artículo** (ej: A2 N/A sin cifras contrarian; A5 N/A sin leitmotiv repetido; B1/B2 N/A en ficción o editorial sin comparativa; B6 N/A sin asociaciones narrativas entre productos). Documentar POR QUÉ es N/A en el comentario — no marcar N/A por pereza.

Origen e incidentes completos: memoria [`feedback_robohogar_pre_publish_polish.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_pre_publish_polish.md) (feedback externo sobre maratón humanoide + aspiradores 2026, abril 2026).

### 9. Prohibiciones

Aplicar todas las de `rules/editorial.md` (voz, tono, primera persona plural, prohibiciones de contenido, anti-anglicismos de apertura/cierre).

**Anti-anglicismos ES — OBLIGATORIO pre-output** (regla activa 2026-04-19, ver `@rules/editorial.md § Apertura y cierre del cuerpo del email`):
- [ ] 0 apariciones de `Hola X,` + nombre · `Querido/a lector/a` · `Hey` · `Espero que estés bien` · `¿Qué tal la semana?`
- [ ] 0 cierres `Cheers` · `Best` · `Saludos cordiales` al final del artículo/newsletter.
- [ ] 0 em-dash (`—`) en trust-lines ≤15 palabras (bajo CTA, bajo subtítulo, OG description). En titulares y prosa larga sí permitido.
- [ ] Subject line del artículo (tag Beehiiv) en 20-45 chars, preferencia ≤35 (regla actualizada en `@rules/newsletter.md`).
- [ ] 0 uso de `tangible` como sustantivo visible al lector (banner, subtítulo, OG). Sustituir por "PDF gratis", "guía gratis", "descargable".

**Curse of knowledge — OBLIGATORIO pre-output** (regla activa 2026-04-19, ver `@rules/editorial.md § Curse of knowledge`):
- [ ] Acrónimos expandidos en primera mención: `LiDAR`, `ToF`, `PVP`, `AI Act`, `CE`, `SmartThings`, `Matter`, etc.
- [ ] Nombres de modelo con marca + categoría + año en primera mención: `"el Dreame X50 Ultra, aspirador gama alta 2026"` (no solo `"el X50"`).
- [ ] Jerga en inglés traducida en primera mención: `mopping` → fregado, `auto-wash` → autolavado, `auto-empty` → autovaciado, `edge cleaning` → limpieza de bordes.
- [ ] Conceptos regulatorios/técnicos con 1 línea de contexto: homologación CE, tarifa PVPC, banda 2.4 GHz, etc.
- [ ] Test: un lector 30-55 ES, interesado en tecnología pero no técnico, entiende cada frase al primer pase.

**Prohibición específica — voz de autoridad propia (crítico en hooks):**

NUNCA generar hooks, aperturas, subtítulos o párrafos que narren el proceso de investigación con frases tipo:
- ❌ *"Hemos leído Xataka Home, SamMobile y Vacuum Wars, y…"*
- ❌ *"Contrastado con X, Y, Z newsletters / medios"*
- ❌ *"Nos hemos metido en 10 reviews internacionales…"*
- ❌ *"Hemos recopilado toda la información de…"*
- ❌ *"Esta semana hemos leído tres veces [fuentes externas]…"*

Las fuentes externas se citan de forma PERMITIDA:
- ✅ Como autoridad puntual de un dato concreto: *"Xataka Home lo explica sin rodeos: el vapor va a las mopas, no al suelo"*.
- ✅ Como hipertexto contextual: *"según [Vacuum Wars](url), el brazo acierta la mitad de las veces"*.

La tabla completa de fuentes va en el PASOS.md § Fuentes del artículo, NO en el texto publicado. Si un borrador necesita citar >3 fuentes externas en el cuerpo, revisar si el ángulo editorial es lo bastante fuerte antes de seguir — el problema no es la voz, es que falta tesis propia.

Regla con incidente de origen documentado: `feedback_article_voice_authority.md` (memoria auto-memory) + `@rules/editorial.md § Reglas de contenido`.

## Rules

- Cada artículo es un borrador — Rafael SIEMPRE edita antes de publicar
- Los links de afiliado NUNCA van en emails, solo en artículos web
- Artículos de review/comparativa incluyen disclosure Amazon al final
- Output siempre con frontmatter YAML completo

---

## Templates estructurales (destilados de Write With AI)

> Las tres plantillas maestras de Cole/Bush mapean 1:1 a los tipos ROBOHOGAR. Parámetro opcional `--template=<tipo>` para forzar esqueleto. Prompts literales ejecutables → [`../../references/writewithai/05-prompts-utiles.md`](../../references/writewithai/05-prompts-utiles.md). Estructura visual y diagramas ASCII → [`../../references/writewithai/02-estructura-articulo-visual.md`](../../references/writewithai/02-estructura-articulo-visual.md). **4A Framework (ángulo editorial), 5 Headline Templates (H1), 5 Métodos de Expansión (desarrollo de sección) y reglas de anti-repetición vs últimos 3 artículos → [`../../references/writewithai/10-fundamentals-5-lessons.md`](../../references/writewithai/10-fundamentals-5-lessons.md).**

### Sintaxis sugerida

```
/content-draft [tema] --template=problem-solution|mistakes|how-to
```

Si no se pasa `--template`, inferirlo del tipo del §1:
- `Review/Comparativa` → **problem-solution** (default)
- `Guía de compra` → **mistakes** (errores al comprar)
- `Editorial/Personal` → libre (1/3/1 + hook, sin esqueleto forzado)
- Tutorial técnico → **how-to**

### Template 1 · `problem-solution` (reviews y comparativas)

```
H1: Título con promesa
H3: Subtítulo específico
[HOOK] Escena del problema (1/3/1)
H2: "El problema con [categoría]"   → qué falló, qué intentaste, por qué
H2: "La solución: [producto]"        → qué es, cómo funciona, por qué es diferente
H2: "Cómo aplicarlo paso a paso"     → Paso 1/2/3 con ejemplo concreto
H2: "Veredicto"                      → Para quién sí/no + precio + afiliado + alternativa
[CIERRE] Frase punzante + firma + P.D.
```

### Template 2 · `mistakes` (guías defensivas, editoriales)

```
H1: "X errores al [acción]"
[HOOK] Historia de alguien que cometió los errores (1/3/1)
H2: "Por qué estos errores son tan comunes"
H2: "Error 1: [nombre]"              → descripción · consecuencia · cómo corregirlo
H2: "Error 2..." (repetir 3-5)
H2: "Checklist antes de comprar"     → tabla con 5 puntos accionables
[CIERRE]
```

### Template 3 · `how-to` (tutoriales y setups)

```
H1: "Cómo [resultado] [sin obstáculo]"
H3: Tiempo estimado + prerrequisitos
[HOOK] Estado final deseado en 1 frase
H2: "Lo que necesitas"               → lista de materiales/apps/cuentas
H2: "Paso 1: [acción]"               → instrucción + error común a evitar
H2: "Paso 2..." (3-7 pasos)
H2: "Si algo sale mal"               → troubleshooting rápido
H2: "Siguiente nivel"                → 1-2 pistas para profundizar
[CIERRE]
```

### Pinpoint header obligatorio

Antes de escribir el cuerpo, poner como blockquote al inicio del borrador (se elimina antes de publicar — es disciplina de redactor):

```
> Después de leer este artículo, [lector ROBOHOGAR] sabrá [promesa concreta] para poder [acción].
```

Si no se puede rellenar, el borrador no está listo (regla Pinpoint Writing de Cole).

---

## Hook checklist — los 5 tipos a considerar antes de escribir

La primera frase abre un "loop" — si no provoca leer la segunda, está rota. 5 arquetipos prioritarios para ROBOHOGAR (lista completa de 10 tipos con ejemplos → [`../../references/writewithai/01-voz-y-estructura.md#1-aperturas-hooks-10-tipos-con-ejemplo-robohogar`](../../references/writewithai/01-voz-y-estructura.md)):

- [ ] **First-person plural + acción específica** — *"Esta semana hemos desmontado cinco robots aspiradores."*
- [ ] **Belief destruction** — *"'Los robots solo funcionan en casas grandes' — eso creíamos hasta que probamos uno en 55 m²."*
- [ ] **Escena sensorial** — *"Martes, 7:40. El robot sale de su base sin ruido. El bebé sigue durmiendo."*
- [ ] **Stat impactante** — *"Solo el 14% de los hogares españoles tiene robot aspirador. En Alemania, el doble."*
- [ ] **Reframe violento / anti-cliché** — *"Los listados 'top 10 robots 2026' aburren. Lo que os vamos a contar es qué NO comprar."*

Complemento a nivel H1/subtítulo/meta (no sustituye este hook-checklist): 5 Headline Templates + trípode WHO/WHAT/WHY → [`../../references/writewithai/10-fundamentals-5-lessons.md § Lección 4 + Tabla A`](../../references/writewithai/10-fundamentals-5-lessons.md). El hook abre el cuerpo; el headline abre la OG card. Son 2 decisiones distintas y ambas se declaran en PASOS.md.

### Renderizado OBLIGATORIO de los 3 hooks en el HTML

**NO elegir el hook por Rafael.** Generar 3 hooks de arquetipos distintos y renderizarlos como 3 callouts visibles al inicio del `<body>` (justo después de la byline, donde iría el hook final). Rafael los lee en el preview del navegador, elige uno y borra los otros dos bloques.

**Por qué:** los comentarios `<!-- -->` del `<head>` no se ven en el preview. Rafael trabaja en sesiones espaciadas y necesita comparar los 3 hooks renderizados con el formato real (tipografía, callout ámbar, negritas) antes de elegir.

Formato exacto a emitir:

```html
<!-- ═══════════════════════════════════════════════════════════════════
     HOOKS — ELIGE UNO Y BORRA LOS OTROS 2 BLOQUES hook-option
     v1 = <arquetipo> · v2 = <arquetipo> · v3 = <arquetipo>
     ═══════════════════════════════════════════════════════════════════ -->

<p class="variant-reco" style="font-size:13px; color:#6B7280; font-style:italic; margin:12px 0; padding:8px 12px; border-left:3px solid #F5A623; background:#FFF9EF;">
  💡 <strong>Recomendación IA:</strong> v<N> (<arquetipo>).
  <strong>Motivo:</strong> <explicación breve — 1-2 frases — de por qué esta variante es la más fuerte Y por qué las otras dos quedan por debajo>.
</p>

<div class="callout-amber hook-option" data-hook="v1">
  <p><strong style="color:#F5A623;">[HOOK v1 · <arquetipo>]</strong><br>
  <texto del hook v1>.</p>
</div>

<div class="callout-amber hook-option" data-hook="v2">
  <p><strong style="color:#F5A623;">[HOOK v2 · <arquetipo>]</strong><br>
  <texto del hook v2>.</p>
</div>

<div class="callout-amber hook-option" data-hook="v3">
  <p><strong style="color:#F5A623;">[HOOK v3 · <arquetipo>]</strong><br>
  <texto del hook v3>.</p>
</div>

<!-- ═══════════════════ FIN HOOKS ═══════════════════ -->
```

**Reglas:**
- Los 3 hooks deben ser de arquetipos distintos (no 3 variaciones del mismo tipo) para dar contraste real.
- Cada hook debe ser callout completo y autosuficiente — no depender del contexto de los otros dos.
- El label `[HOOK vN · arquetipo]` y la clase `hook-option` son obligatorios: permiten a Rafael identificarlos y borrarlos sin ambigüedad.
- El comentario frontmatter del `<head>` describe los 3 arquetipos, NO declara "Hook elegido: #N" (la elección la hace Rafael en el HTML).
- `/post-publish` debe validar que solo queda 1 bloque `.hook-option` y fallar si quedan ≥2 (señal de que Rafael no eligió).

**Regla de validación:** si ningún hook provoca "vale, una más" al leerlo en el preview, reescribir los 3 antes de continuar.

---

## Variantes OBLIGATORIAS para "Nuestro veredicto" y "¿Sabías que…?"

Mismo patrón que los hooks. Generar **3 versiones** del banner inicial de cada una de estas dos secciones y renderizarlas como bloques visibles en el HTML. Rafael elige uno en el preview y borra los otros dos.

**Por qué:** el veredicto y el "¿sabías que?" son los dos bloques que más se remixan en newsletter, social posts y llms.txt. Tener 3 ángulos distintos permite a Rafael elegir el que mejor case con el hook escogido y con la campaña social posterior.

### Nuestro veredicto

Solo el **banner inicial** (el callout-amber de apertura de la sección) se triplica. Los párrafos que siguen (desarrollos por perfil de lector, dato que hace pensar, cierre) son únicos.

```html
<h2>🏆 Nuestro veredicto</h2>

<!-- ═══════════════════════════════════════════════════════════════════
     VEREDICTO — ELIGE UNO Y BORRA LOS OTROS 2 BLOQUES veredicto-option
     v1 = <ángulo> · v2 = <ángulo> · v3 = <ángulo>
     ═══════════════════════════════════════════════════════════════════ -->

<p class="variant-reco" style="font-size:13px; color:#6B7280; font-style:italic; margin:12px 0; padding:8px 12px; border-left:3px solid #F5A623; background:#FFF9EF;">
  💡 <strong>Recomendación IA:</strong> v<N> (<ángulo>).
  <strong>Motivo:</strong> <1-2 frases — por qué este ángulo cierra mejor el artículo y qué flojea en las otras dos variantes>.
</p>

<div class="callout-amber veredicto-option" data-variant="v1">
  <p><strong style="color:#F5A623;">[VEREDICTO v1 · <ángulo>]</strong><br>
  <texto veredicto v1>.</p>
</div>

<div class="callout-amber veredicto-option" data-variant="v2">
  <p><strong style="color:#F5A623;">[VEREDICTO v2 · <ángulo>]</strong><br>
  <texto veredicto v2>.</p>
</div>

<div class="callout-amber veredicto-option" data-variant="v3">
  <p><strong style="color:#F5A623;">[VEREDICTO v3 · <ángulo>]</strong><br>
  <texto veredicto v3>.</p>
</div>

<!-- ═══════════════════ FIN VEREDICTO ═══════════════════ -->

<p>[Desarrollo común por perfil de lector, dato que hace pensar, etc. — un solo bloque, no triplicado]</p>
```

Ángulos a cubrir (elegir 3 distintos):
- **Conteo/clasificación** — cuántos reales vs pre-order vs demo
- **Perspectiva temporal** — qué puedes tener hoy / qué esperar 18 meses
- **Perspectiva geográfica** — Europa vs Asia vs EE.UU.
- **Perspectiva de presupuesto** — qué compras por X euros
- **Contrarian / anti-recomendación** — por qué NO comprar

### ¿Sabías que…?

Solo el **párrafo-dato inicial** se triplica (con su fuente). Si hay desarrollo posterior o segunda cita, ese bloque queda único.

```html
<h2>💡 ¿Sabías que…?</h2>

<!-- ═══════════════════════════════════════════════════════════════════
     ¿SABÍAS QUE? — ELIGE UNO Y BORRA LOS OTROS 2 BLOQUES sabias-option
     v1 = <ángulo-dato> · v2 = <ángulo-dato> · v3 = <ángulo-dato>
     ═══════════════════════════════════════════════════════════════════ -->

<p class="variant-reco" style="font-size:13px; color:#6B7280; font-style:italic; margin:12px 0; padding:8px 12px; border-left:3px solid #F5A623; background:#FFF9EF;">
  💡 <strong>Recomendación IA:</strong> v<N> (<ángulo>).
  <strong>Motivo:</strong> <1-2 frases — por qué este dato sorprende más o conecta mejor con la tesis del artículo; qué les falta a las otras dos>.
</p>

<div class="sabias-option" data-variant="v1">
  <p><strong style="color:#F5A623;">[¿SABÍAS QUE v1 · <ángulo>]</strong><br>
  <dato + contexto v1>.</p>
  <p><a href="<url-fuente>">Fuente: <fuente>, <año></a></p>
</div>

<div class="sabias-option" data-variant="v2">
  <p><strong style="color:#F5A623;">[¿SABÍAS QUE v2 · <ángulo>]</strong><br>
  <dato + contexto v2>.</p>
  <p><a href="<url-fuente>">Fuente: <fuente>, <año></a></p>
</div>

<div class="sabias-option" data-variant="v3">
  <p><strong style="color:#F5A623;">[¿SABÍAS QUE v3 · <ángulo>]</strong><br>
  <dato + contexto v3>.</p>
  <p><a href="<url-fuente>">Fuente: <fuente>, <año></a></p>
</div>

<!-- ═══════════════════ FIN ¿SABÍAS QUE? ═══════════════════ -->
```

Cada variante puede usar una fuente distinta (no obligatorio citar todas desde la misma). Si una variante reutiliza la misma fuente que otra, repetirla dentro de su bloque (no factorizar fuera).

### Reglas comunes (hook + veredicto + ¿sabías que?)

- Las 3 variantes deben aportar **ángulos genuinamente distintos**, no reformulaciones léxicas del mismo contenido.
- El label `[SECCIÓN vN · ángulo]` y las clases `hook-option` / `veredicto-option` / `sabias-option` son obligatorias — `/post-publish` las usa como checkpoint.
- Cada variante debe ser **autosuficiente y legible** sin el contexto de las otras dos (por si Rafael lee el preview fuera de orden).
- Los datos numéricos/estadísticos deben ser **reales y verificables**, no inventados entre variantes. Si no tienes dato sólido para una variante, usa un ángulo cualitativo en lugar de inventar cifra.
- **OBLIGATORIO: bloque `<p class="variant-reco">` visible justo antes de las 3 variantes** con la recomendación de la IA (v1/v2/v3) **entre paréntesis** y el motivo **entre paréntesis** (1-2 frases explicando por qué esa es la más fuerte y qué flojea en las otras). Rafael usa este bloque para decidir sin tener que comparar las tres a ciegas; es texto desechable — se borra junto con las 2 variantes no elegidas. No poner la recomendación solo en comentarios HTML: Rafael lee el preview renderizado, no el código fuente.

<!-- added by wwai-integration 2026-04-17 -->
