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

Generar 3 variantes con composiciones distintas → `content/articulos/<slug>/assets/hero-<slug>-v{1,2,3}.png`. Modelo: `flash`, aspect: `landscape`, size: `1K`. Script: `$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py`.

**Antes de lanzar cualquier prompt:** leer `assets/branding/nano-banana-prompt-base.md`. Contiene el **decision tree** (qué composición usar según escena — 1 robot vs varios, home vs warehouse, etc.) y el **suffix compilado anti-neones** que DEBE concatenarse al prompt específico. Con eso se reduce de 7-9 iteraciones a 2-3 por hero.

Secundariamente, `assets/branding/asset-catalog.md` para prompts exactos por tipo de artículo. El script genera `.webp` automáticamente — subir WebP a Beehiiv.

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

Template origen: `content/templates/PASOS-template.md`. Script: `utilities/generate_pasos.py`.

### 8.5. Anti-IA checklist §1 Universal — OBLIGATORIO antes de entregar borrador

Cargar [`@references/anti-ia-checklist.md`](../../references/anti-ia-checklist.md) **§1 Universal completo** (§1.1 lista negra de palabras, §1.2 tricolon/em-dashes/contrast, §1.3 clichés sensoriales, §1.4 voz plural) y correrlo sobre el `borrador.html`. La §2 Ficción NO aplica aquí — solo relatos.

**Regla de decisión:** ≥3 flags → rechazar output y reescribir · 1-2 flags → reescribir líneas ofensivas y re-correr · 0 flags → proceder al paso 9.

Complementa (no sustituye) las prohibiciones de `@rules/editorial.md` (autoridad propia, primera persona plural, filtro ES).

### 8.6. Formato técnico Beehiiv — OBLIGATORIO antes de entregar borrador

Verificar contra `@rules/editorial.md § Formato técnico (Beehiiv)`. Aplica a TODO tipo de contenido (review, comparativa, editorial, guía, cheatsheet, newsletter).

**Negritas:**
- [ ] Ningún `<strong>`, `<b>` ni `**...**` dentro de `<h1>`, `<h2>`, `<h3>` (ni en Markdown `## **...**`)
- [ ] Ningún `<strong>`/`<b>` dentro de `<th>` ni `<td>` (ni `| **celda** |` en Markdown)
- [ ] Ningún `<strong>`/`<b>` dentro de `<div class="checklist">` u otro callout con fondo crema `#FFF9EF` / borde `#F5A623`
- [ ] SÍ permitido: negrita dentro de párrafos de texto corrido (`<p>...<strong>...</strong>...</p>`)

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

**Algoritmo (aplicar al generar el borrador):**

1. **Leer `frontmatter.category`** del borrador en generación (ej: `aspirador`, `cortacésped`, `humanoide`, `ficcion`, `editorial`).
2. **Leer word count** estimado del borrador.
3. **Decidir según tabla:**

   | `category` | Banner | Posiciones a insertar |
   |---|---|---|
   | `aspirador`, `cortacésped`, `mascota-robot`, `fregasuelos`, `limpia-cristales` | ✅ Sí | Si words >1.500: **intro + cierre**. Si words ≤1.500: **solo cierre**. |
   | `humanoide` | ❌ No | — (tangible "Guía early adopter humanoides" pendiente) |
   | `ficcion` | ❌ No | — (canal narrativo, no mezclar con CTA comercial) |
   | `editorial` sin ángulo de compra | ❌ No | — |

4. **Insertar snippet de [`content/templates/banner-lead-magnet.html`](../../content/templates/banner-lead-magnet.html)** en las posiciones marcadas:
   - **Posición intro:** tras el callout de intro amber, antes del primer `<h2>` de contenido.
   - **Posición cierre:** tras el bloque "Nuestro veredicto", antes del CTA gris de suscripción.
5. **Sustituir `<SRC_SLUG>`** por el slug del artículo (`frontmatter.slug`) para tracking UTM → `?lm=hoja-compra&src=<slug>`.
6. **Comentarios HTML pre/post** para localización rápida: `<!-- BANNER LEAD MAGNET · posición intro -->` y `<!-- BANNER LEAD MAGNET · posición cierre -->`.

**Verificación pre-output:** antes de cerrar el skill, contar ocurrencias de `class="banner-lead-magnet"` en el HTML generado. Debe ser:
- 0 si `category ∈ {humanoide, ficcion, editorial}`
- 1 si categoría consumer y words ≤1.500
- 2 si categoría consumer y words >1.500

Si el conteo no coincide con la matriz → auto-corregir antes de entregar.

**Versionado futuro:** si aparece un nuevo tangible (ej. Guía primer mes aspirador, Glosario ROBOHOGAR), ampliar la tabla de arriba (categoría → tangible → posición) y los snippets en [`banner-lead-magnet-snippets.md`](../../content/templates/banner-lead-magnet-snippets.md). Un artículo puede llevar 2 banners distintos (1 por momento de funnel — ver `@rules/tangibles.md § Mapeo momento del funnel`).

**Microcopy del banner — regla heredada de `@rules/tangibles.md § Microcopy de conversión`.** Si el skill genera una variante del texto del banner para un artículo (p. ej. tangible distinto, copy adaptado a la categoría), la trust-line debajo del CTA debe cumplir el default canónico `PDF gratis · newsletter semanal · baja cuando quieras` o una variante que supere las 3 reglas: (a) ≥2 de los 3 elementos obligatorios (formato · salida · transparencia), (b) ninguna promesa prohibida (velocidad de entrega, ausencia futura de publicidad, hype), (c) ≤80 caracteres. Verificación: `grep -iE "15 segundos|llega al email en|instantáneo|sin publicidad|sin promociones|sin letra pequeña"` sobre el `borrador.html` — 0 matches obligatorio antes de entregar.

### 9. Prohibiciones

Aplicar todas las de `rules/editorial.md` (voz, tono, primera persona plural, prohibiciones de contenido).

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

> Las tres plantillas maestras de Cole/Bush mapean 1:1 a los tipos ROBOHOGAR. Parámetro opcional `--template=<tipo>` para forzar esqueleto. Prompts literales ejecutables → [`../../references/writewithai/05-prompts-utiles.md`](../../references/writewithai/05-prompts-utiles.md). Estructura visual y diagramas ASCII → [`../../references/writewithai/02-estructura-articulo-visual.md`](../../references/writewithai/02-estructura-articulo-visual.md).

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
