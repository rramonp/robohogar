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

| Tipo | Contenido | Monetización | Ejemplo |
|---|---|---|---|
| **Review/Comparativa** (70%) | Producto real, specs, precios, opinión, veredicto | Links afiliado Amazon | "Roborock S8 vs Dreame X40" |
| **Guía de compra** (70%) | Selección de productos, recomendaciones por presupuesto | Links afiliado Amazon | "Mejor robot aspirador 2026" |
| **Editorial** (30%) | Futuro, opinión, tendencias, humanoides | Sin afiliados — construye marca | "Robots humanoides en 2030" |
| **Personal** (30%) | Experiencia propia, anécdota, reflexión | Sin afiliados — autenticidad | "Mi vida con un aspirador robot" |

### 2. Recopilar input

- Leer el research digest más reciente de `content/drafts/research-digest-*.md`
- Si Rafael da un tema específico, investigar con Firecrawl/WebSearch
- Identificar keyword SEO principal y 2-3 secundarias (consultar `rules/seo.md`)

### 3. Generar borrador

Estructura del artículo (consultar `rules/editorial.md` para tono):

```markdown
---
title: "[Título SEO — max 60 chars, keyword principal incluida]"
meta_description: "[155 chars max, con CTA]"
slug: "[url-corto-descriptivo]"
category: "[Aspiradores|Cortacéspedes|Humanoides|Guías|Opinión]"
tags: ["tag1", "tag2", "tag3"]
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

[Si review: tabla de specs, pros/contras con ✅/❌, veredicto claro]
[Si comparativa: tabla comparativa lado a lado]
[Si editorial: opinión fuerte, sin hedging]

---

**¿Te ha gustado?** Suscríbete para recibir esto cada 2 semanas → [link Beehiiv]

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

- **Carpeta del artículo:** `content/articulos/<slug>/borrador.md`
- **Assets:** `content/articulos/<slug>/assets/`
- **Vault Obsidian:** `C:\Users\bakal\OneDrive - HBX Group\Desktop\DEMAND\Obsidian\RRP\RRP_ONEDRIVE\HBX\05_Personal\05-01_Robotica Newsletter\02-Drafts\YYYY-MM-DD-slug.md`
  (usar template vault: `Templates/Template Article Draft.md`)

### 6. Generar hero image (OBLIGATORIO)

Cada artículo NECESITA su imagen hero (1200x630) antes de publicar. Sin imagen, las cards en la landing y las previews en redes quedan vacías.

**Invocar `/nano-banana` en modo hero de artículo:**

```bash
uv run "<path>/image.py" \
  --prompt "Eye-catching editorial hero image for an article about [TEMA]. [PRODUCTO/ESCENA]. Warm amber lighting, editorial photography style, high contrast. Absolutely NO text, NO letters, NO words, NO signs, NO writing of any kind." \
  --output "content/articulos/<slug>/assets/hero-<slug>.png" \
  --model flash \
  --aspect landscape \
  --size 1K
```

**Estilo:** Product-hero cinematográfico (tipo YouTube thumbnail). Reglas completas en `assets/branding/asset-catalog.md` sección "Estilo ROBOHOGAR para heros de artículos".

**NO usar `--reference`** para heros. NO incluir la mascota. El producto/robot es el protagonista.

### 7. Otros assets

- [ ] Screenshots/imágenes inline → guardar en `content/articulos/<slug>/assets/`
- [ ] Si review: foto del producto (buscar en web del fabricante o pedir a Rafael)

### 8. Prohibiciones (de `rules/editorial.md`)

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
