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

### 3. Generar borrador

**Usar el template HTML del tipo de artículo** como base — copiar el HTML y reemplazar el contenido:

| Tipo | HTML base (copiar y modificar) | Estructura documentada |
|---|---|---|
| Review/Comparativa | `content/templates/review-comparativa-beehiiv-export.html` | `content/templates/estructura-templates.md` → Template 1 |
| Editorial/Opinión | `content/templates/editorial-opinion-beehiiv-export.html` | `content/templates/estructura-templates.md` → Template 2 |
| Newsletter | *(pendiente — se creará con el primer newsletter)* | |
| Noticias/Roundup | *(pendiente — se creará con el primer roundup)* | |

**Proceso:** leer el HTML base, reemplazar título/subtítulo/contenido manteniendo la estructura de bloques. Consultar `estructura-templates.md` para saber qué bloques van en cada tipo.

**Tags de Beehiiv disponibles:** Aspiradores, Cortacéspedes, Humanoides, Asistentes IA, Robot Mascotas, Smart Home, Noticias, Opinión, Guías

Para **Review/Comparativa**, seguir la estructura completa del template:
1. Hook (1-2 frases) → Contexto (1 párrafo) → Criterios de selección
2. Producto por producto: qué es, lo bueno, lo malo, para quién, precio + afiliado, opinión personal
3. Los que NO recomiendo → Tabla resumen comparativa → Veredicto final
4. CTA suave + Disclaimer afiliados

Para otros tipos, usar la estructura documentada en `content/templates/estructura-templates.md` (Template 2 para editorial/opinión). Incluir siempre frontmatter YAML con: title, seo_title, meta_description, slug, tags, type, status, created, affiliate.

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

Composición y prompts → `assets/branding/asset-catalog.md`. El script genera `.webp` automáticamente — subir WebP a Beehiiv.

### 7. Descargar imágenes inline de fuentes (OBLIGATORIO)

Cada artículo necesita imágenes inline de las fuentes originales (fabricantes, prensa, eventos). NO generar estas imágenes — usar fotos reales.

**Proceso:**
1. Durante el research, identificar 2-4 imágenes clave de fuentes oficiales/prensa
2. Descargar con `curl` a `content/articulos/<slug>/assets/`
3. Nombrar descriptivamente: `figure-02-bmw-factory.jpg`, `tesla-optimus-gen3.jpg`
4. Colocarlas en el HTML del borrador en la posición óptima (ver reglas abajo)

**Criterio de cantidad:** ~1 imagen cada 300-400 palabras. Para un artículo de 1.200 palabras → 3-5 imágenes inline. Productos/robots que el lector no conoce NECESITAN foto — sin foto, un precio no dice nada.

**Dónde colocar imágenes (NUNCA debajo del H2):**
- Colocar DESPUÉS del párrafo que justifica la imagen, no debajo del título
- La imagen debe reforzar un dato concreto que el lector acaba de leer
- Secciones de opinión pura (veredicto, "lo que no te cuentan") van SIN imagen — el texto es el protagonista

**Control de peso:** Artículos web → <300 KB/imagen razonable. Newsletter email → <200 KB/imagen, <800 KB total. Reportar siempre peso en PASOS.md.

### 8. Generar PASOS.md + mapa visual (OBLIGATORIO)

Cada artículo genera un archivo `PASOS.md` en su carpeta con:
1. SEO metadata (title, description, slug, tags) para copiar a Beehiiv
2. Hero image elegida (o las 3 para elegir)
3. Checklist paso a paso para publicar
4. **Mapa visual del artículo** — diagrama ASCII con la posición exacta de cada imagen (H1 → secciones → imágenes → CTAs). Este mapa es la guía principal de Rafael para montar en Beehiiv.

### 9. Prohibiciones

Aplicar todas las de `rules/editorial.md` (voz, tono, primera persona plural, prohibiciones de contenido).

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

La primera frase abre un "loop" — si no provoca leer la segunda, está rota. Antes de escribir el borrador, generar 3 hooks candidatos y elegir el mejor. 5 arquetipos prioritarios para ROBOHOGAR (lista completa de 10 tipos con ejemplos → [`../../references/writewithai/01-voz-y-estructura.md#1-aperturas-hooks-10-tipos-con-ejemplo-robohogar`](../../references/writewithai/01-voz-y-estructura.md)):

- [ ] **First-person plural + acción específica** — *"Esta semana hemos desmontado cinco robots aspiradores."*
- [ ] **Belief destruction** — *"'Los robots solo funcionan en casas grandes' — eso creíamos hasta que probamos uno en 55 m²."*
- [ ] **Escena sensorial** — *"Martes, 7:40. El robot sale de su base sin ruido. El bebé sigue durmiendo."*
- [ ] **Stat impactante** — *"Solo el 14% de los hogares españoles tiene robot aspirador. En Alemania, el doble."*
- [ ] **Reframe violento / anti-cliché** — *"Los listados 'top 10 robots 2026' aburren. Lo que os vamos a contar es qué NO comprar."*

**Regla de validación:** si la primera frase del borrador no provoca "vale, una más", reescribirla antes de continuar. El 1/3/1 solo funciona si la frase-1 del primer párrafo es un hook verdadero.

<!-- added by wwai-integration 2026-04-17 -->
