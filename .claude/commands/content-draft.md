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

Para otros tipos, usar la estructura genérica:

```markdown
---
title: "[Título SEO — max 60 chars, keyword principal incluida]"
meta_description: "[155 chars max, con CTA]"
slug: "[url-corto-descriptivo]"
tags: ["tag1", "tag2"]
type: "[review|comparativa|guia|editorial|personal]"
status: borrador
created: YYYY-MM-DD
affiliate: [true|false]
---

# [H1 — Título con keyword principal]

[Hook: 1-2 frases que enganchan. Dato sorprendente, pregunta, o imagen concreta.]

---

## [H2 — Sección 1]

[Contenido. Párrafos de 3-4 líneas máx. Listas con bullets para datos.]

> [Callout con opinión personal o dato destacado]

## [H2 — Sección 2]

[Más contenido...]

[Si editorial: opinión fuerte, sin hedging]

---

**¿Te está sirviendo?** Publicamos cada semana → [link Beehiiv]

---

**Más en ROBOHOGAR:**
- [[Artículo relacionado 1]]
- [[Artículo relacionado 2]]
```

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

Cada artículo NECESITA su imagen hero antes de publicar. Generar **3 variantes con composiciones distintas** para que Rafael elija.

```bash
uv run "$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py" \
  --prompt "[ver prompt template en asset-catalog.md]" \
  --output "content/articulos/<slug>/assets/hero-<slug>-v1.png" \
  --model flash \
  --aspect landscape \
  --size 1K
# Repetir con -v2.png y -v3.png, cada una con composición diferente
```

**Reglas de composición para newsletter** (de `asset-catalog.md`):
- 1-2 elementos máximo, close-ups, punto focal único (debe funcionar a 300px)
- Interacción humano-robot siempre (mano, dedo, persona cerca)
- Fondo luminoso: jardín, cielo, cocina con luz natural. NUNCA skylines ni neones
- Concepto visual > escena literal (metáfora como "Creación de Adán" > foto de producto)

El script genera automáticamente una copia `.webp` (<500 KB) junto a cada PNG. Subir el WebP a Beehiiv.

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

**Control de peso (verificar antes de entregar):**

Dos reglas distintas según el tipo de publicación:

| Tipo | Publish to | Límite por imagen | Límite total | Motivo |
|------|-----------|-------------------|-------------|--------|
| **Artículo web** | `Web only` | Sin límite estricto (razonable: <300 KB) | Sin límite | El navegador carga con lazy loading |
| **Newsletter email** | `Email and web` | <200 KB | <800 KB total | Clientes de email recortan/bloquean imágenes pesadas |

- Siempre reportar el peso en el PASOS.md para que Rafael tenga visibilidad:
  ```
  ## Peso imágenes inline
  | Imagen | KB |
  |--------|----|
  | ces-2026-collage.jpg | 288 |
  | tesla-optimus.jpg | 98 |
  | **TOTAL** | **386 KB** (web only — sin límite estricto) |
  ```
- Para newsletters email: si el total supera 800 KB, comprimir o eliminar la menos esencial

### 8. Generar PASOS.md + mapa visual (OBLIGATORIO)

Cada artículo genera un archivo `PASOS.md` en su carpeta con:
1. SEO metadata (title, description, slug, tags) para copiar a Beehiiv
2. Hero image elegida (o las 3 para elegir)
3. Checklist paso a paso para publicar
4. **Mapa visual del artículo** — diagrama ASCII mostrando exactamente dónde va cada imagen:

```
HERO IMAGE (v10 — WebP)
H1: Título
  Intro callout (texto)
H2: Sección 1
  Párrafo 1
  📷 IMAGEN-NOMBRE.jpg ← después de qué párrafo y por qué
  Párrafo 2
H2: Sección 2 (solo texto — opinión pura)
  ...
CTA mid-article
H2: Sección N
FOOTER CTA
```

Este mapa es la guía principal de Rafael para montar el artículo en Beehiiv.

### 9. Prohibiciones (de `rules/editorial.md`)

- NUNCA copiar/pegar de fuentes — reescribir con voz propia
- NUNCA superlativos vacíos ("revolucionario", "increíble", "game-changer")
- NUNCA frases de IA ("En el vertiginoso mundo de...", "Es importante destacar...")
- SIEMPRE incluir opinión/valoración personal
- SIEMPRE usar "tú" (no "usted")

## Rules

- Cada artículo es un borrador — Rafael SIEMPRE edita antes de publicar
- Los links de afiliado NUNCA van en emails, solo en artículos web
- Artículos de review/comparativa incluyen disclosure Amazon al final
- Output siempre con frontmatter YAML completo
