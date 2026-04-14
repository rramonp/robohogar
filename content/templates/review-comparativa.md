# Template: Review / Comparativa

> Uso: artículos que comparan 3-6 productos de una misma categoría con opinión honesta.
> Réplica exacta del template Beehiiv (exportado 2026-04-14).
> HTML original: `content/templates/review-comparativa-beehiiv.html`
> Tono: amigo techie que te cuenta qué merece tu dinero. Opinión clara, sin hype.
> Voz de marca: consultar SIEMPRE `docs/brand-voice.md` antes de redactar.

---

## Frontmatter (metadatos del artículo)

```yaml
---
title: "[Título principal — incluye keyword + gancho]"
seo_title: "[Max 60 chars — keyword principal + diferenciador]"
meta_description: "[Max 155 chars — resumen con CTA implícito]"
slug: "[keyword-principal-año]"
tags: ["[tag principal]", "[tag secundario]"]
date: YYYY-MM-DD
type: review-comparativa
affiliate: true | false
status: draft | published
---
```

---

## Estructura del artículo (réplica del template Beehiiv)

### Cabecera

[Imagen hero — 1200x630, generada con /nano-banana, cinematográfica, sin mascota]

# Placeholder para HOOK (1-2 frases de enganche)

placeholder para CONTEXTO (1 párrafo con dato concreto — subtitle de Beehiiv, usado para preview en email y cards)

---

### Intro (párrafo de orientación)

Párrafo suelto (NO heading) que enmarca la comparativa. 2-3 frases: qué productos se comparan, en qué se ha fijado, y qué encontrará el lector al final.

> Ejemplo: "He comparado los 5 robots aspirador más vendidos en Amazon España. Me he fijado en precio real, si te meten suscripción, y cómo funcionan en pisos normales. Al final, veredicto claro."

---

### Bloque de producto (repetir 3-5 veces)

## 1. Producto — Veredicto Corto

[Imagen del producto — foto del fabricante, NO generada]

Descripción breve del producto. Qué es en 1-2 frases.

**Precio:** ~XXX€ · **Suscripción:** Sí/No · **Lo clave:** [1 frase]

### 👍 Lo bueno

- Comentario bueno 1 (1 línea corta)
- Comentario bueno 2
- Comentario bueno 3 (máximo 3)

### 👎 Lo malo

- Comentario malo 1 (1 línea corta)
- Comentario malo 2
- Comentario malo 3 (máximo 3)

### 🎯 Para quién es

Placeholder — perfil de usuario ideal. 1-2 frases.

> 🤖 *Mi opinión:* placeholder — 2-3 frases con voz propia, en primera persona. Opinión real, no resumen.

**[Consultar en Amazon](link-afiliado)**

---

<!-- CTA MID-ARTICLE: insertar entre producto 2 y producto 3 (o entre 3 y 4 si hay 5 productos) -->

### ¿Te está sirviendo? Publicamos esto cada dos semanas

### [Suscríbete gratis](https://robohogar.com)

---

<!-- Continuar con los bloques de producto restantes -->

---

### Productos descartados

## ❌ ¿Y los que NO recomiendo?

Párrafo introductorio breve (opcional).

### Producto 1 — ~XXX€

1-2 frases: por qué no lo recomiendo. Sin bloque completo, sin imagen.

### Producto 2 — ~XXX€

1-2 frases: por qué no lo recomiendo.

### Producto 3 — ~XXX€

1-2 frases: por qué no lo recomiendo.

---

### Tabla comparativa

## 📊 Comparativa

| Producto | Precio | Lo clave | Nota (1-5) |
|----------|--------|----------|------------|
| 1        |        |          | ⭐⭐⭐⭐⭐   |
| 2        |        |          | ⭐⭐⭐⭐     |
| 3        |        |          | ⭐⭐⭐⭐     |

---

### Veredicto final

## 🏆 Entonces, ¿cuál me compro?

Placeholder para veredicto final. 3-4 frases claras con recomendación directa.

**[Consultar Precio en Amazon](link-afiliado-del-ganador)**

---

### Dato curioso (sección signature ROBOHOGAR)

## 💡 ¿Sabías que...?

Dato curioso relacionado con la temática del artículo. 2-3 frases. Sorprendente, compartible, humano.

👉 [Leer más en FUENTE](link-fuente)

---

### Cierre

## ¿Te ha servido?

## Cada dos semanas más como esto en tu bandeja

[Banner ROBOHOGAR con mascota]

## [Suscríbete gratis](https://robohogar.com)

---

### Artículos relacionados

## 📚 Más en ROBOHOGAR

<!-- Rellenar con artículos publicados reales (títulos + URLs de robohogar.com) -->
<!-- Si no hay artículos publicados todavía, OMITIR esta sección -->

👉 [Título del artículo 1](URL real robohogar.com)
👉 [Título del artículo 2](URL real robohogar.com)

---

Algunos links son de afiliado — si compras a través de ellos, nos ayudas a mantener ROBOHOGAR sin coste extra para ti

<!-- Share buttons (Facebook, Threads, X, LinkedIn) — automático -->
<!-- Footer (© 2026 ROBOHOGAR, Darse de baja, beehiiv) — automático -->

---

## Mapa de emojis por sección

| Emoji | Sección | Función |
|-------|---------|---------|
| 👍    | Lo bueno | Pros del producto |
| 👎    | Lo malo | Contras del producto |
| 🎯    | Para quién es | Perfil de usuario ideal |
| 🤖    | Mi opinión | Veredicto personal (blockquote) |
| ❌    | No recomiendo | Productos descartados |
| 📊    | Comparativa | Tabla resumen |
| 🏆    | ¿Cuál me compro? | Veredicto final |
| 💡    | ¿Sabías que...? | Dato curioso (sección signature) |
| 📚    | Más en ROBOHOGAR | Artículos relacionados |

---

## Bloques en Beehiiv (Design Mode)

| Orden | Tipo de bloque | Contenido |
|-------|---------------|-----------|
| 1 | Image | Hero 1200x630 |
| 2 | Heading H1 | HOOK (1-2 frases) |
| 3 | Paragraph (subtitle) | CONTEXTO (1 frase — preview email/cards) |
| 4 | Paragraph | Intro orientación (2-3 frases, sin heading) |
| 5 | Divider | --- |
| 6 | Heading H2 | 1. Producto — Veredicto Corto |
| 7 | Image | Foto del producto (fabricante) |
| 8 | Paragraph | Descripción breve |
| 9 | Paragraph (bold) | Precio · Suscripción · Lo clave |
| 10 | Heading H3 | 👍 Lo bueno |
| 11 | Bullet list | 2-3 pros (1 línea cada uno) |
| 12 | Heading H3 | 👎 Lo malo |
| 13 | Bullet list | 2-3 contras (1 línea cada uno) |
| 14 | Heading H3 | 🎯 Para quién es |
| 15 | Paragraph | Perfil de usuario (1-2 frases) |
| 16 | Blockquote | 🤖 Mi opinión: 2-3 frases con voz propia |
| 17 | Button | Consultar en Amazon (link afiliado) |
| 18 | Divider | --- |
| — | *(repetir 6-18 por cada producto)* | |
| 19 | CTA mid-article | ¿Te está sirviendo? + Suscríbete (entre producto 2 y 3) |
| 20 | Divider | --- |
| — | *(productos restantes)* | |
| 21 | Heading H2 | ❌ ¿Y los que NO recomiendo? |
| 22 | Heading H3 + Paragraph | Producto descartado 1 (nombre + precio + 1-2 frases) |
| 23 | Heading H3 + Paragraph | Producto descartado 2 |
| 24 | Heading H3 + Paragraph | Producto descartado 3 |
| 25 | Heading H2 | 📊 Comparativa |
| 26 | Table | Producto / Precio / Lo clave / Nota (1-5) ⭐ |
| 27 | Heading H2 | 🏆 Entonces, ¿cuál me compro? |
| 28 | Paragraph | Veredicto final (3-4 frases) |
| 29 | Button | Consultar Precio en Amazon (ganador) |
| 30 | Divider | --- |
| 31 | Heading H2 | 💡 ¿Sabías que...? |
| 32 | Paragraph | Dato curioso (2-3 frases) |
| 33 | Paragraph (link) | 👉 Leer más en FUENTE |
| 34 | Divider | --- |
| 35 | Heading H2 | ¿Te ha servido? |
| 36 | Heading H2 | Cada dos semanas más como esto en tu bandeja |
| 37 | Image | Banner ROBOHOGAR (mascota) |
| 38 | Heading H2 | Suscríbete gratis (link) |
| 39 | Heading H2 | 📚 Más en ROBOHOGAR |
| 40 | Links | 2-3 artículos publicados con título + URL real. Omitir si no hay |
| 41 | Paragraph | Disclaimer afiliados |
| 42 | Share | Facebook, Threads, X, LinkedIn — automático |
| 43 | Footer | © 2026, Darse de baja, beehiiv — automático |

---

## Estilos del template (extraídos del HTML)

| Elemento | Fuente | Peso | Tamaño | Color |
|----------|--------|------|--------|-------|
| H1 | DM Sans | 600 | 80px | #0C0C0C |
| H2 | DM Sans | 600 | 24px | #0C0C0C |
| H3 | DM Sans | 700 | 18px | #535252 |
| Body (p) | Inter | 400 | 16px | #0C0C0C |
| Links | Inter | bold | 16px | #F5A623 |
| Botones | Inter | — | — | bg #F5A623, text #FFFFFF |
| Listas (ul/ol) | Inter | 400 | 16px | #0C0C0C |
| Footer bg | — | — | — | #283642 |
| Footer text | — | — | 12px | #FFFFFF |

---

## Reglas de estilo

- **Longitud**: 1.000-1.800 palabras
- **Tono**: "tú", informal, con humor sutil (ver `docs/brand-voice.md`)
- **Opinión**: OBLIGATORIA en cada producto (bloque 🤖)
- **Lo malo**: OBLIGATORIO — un review sin contras es un anuncio
- **Specs rápidas**: línea Precio/Suscripción/Lo clave antes de Lo bueno
- **Bullets**: máximo 3 por Lo bueno/Lo malo, 1 línea cada uno
- **Afiliados**: botón "Consultar en Amazon" DESPUÉS de Mi opinión
- **CTA mid-article**: entre producto 2 y 3 (o 3 y 4 si hay 5 productos)
- **CTA final**: ¿Te ha servido? + banner mascota + Suscríbete
- **💡 ¿Sabías que...?**: SIEMPRE presente, entre veredicto y CTA final
- **Más en ROBOHOGAR**: bloque nativo Recent Posts, imagen clicable + título, sin "Acceder"
- **Disclaimer**: siempre al final, texto pequeño/gris
- **Emojis de sección**: fijos, consistentes (ver mapa arriba)
- **Productos descartados**: nombre + precio + 1-2 frases. Sin imagen, sin bloque completo

---

## Checklist pre-publicación

- [ ] ¿El H1 incluye keyword principal + hook?
- [ ] ¿La meta description tiene < 155 chars y CTA implícito?
- [ ] ¿Párrafo de orientación (intro) presente bajo el subtitle?
- [ ] ¿Cada producto tiene imagen del fabricante?
- [ ] ¿Cada producto tiene specs rápidas (Precio/Suscripción/Lo clave)?
- [ ] ¿Cada producto tiene 👎 Lo malo (máx 3 bullets)?
- [ ] ¿Cada producto tiene 🤖 Mi opinión?
- [ ] ¿Botón Amazon DESPUÉS de Mi opinión?
- [ ] ¿CTA mid-article entre productos (no al final)?
- [ ] ¿Sección ❌ No recomiendo con formato ligero?
- [ ] ¿Tabla 📊 comparativa con 4 columnas (Producto/Precio/Lo clave/Nota)?
- [ ] ¿El veredicto 🏆 da recomendación clara?
- [ ] ¿Sección 💡 ¿Sabías que...? presente?
- [ ] ¿CTA final (¿Te ha servido? + banner + Suscríbete)?
- [ ] ¿Más en ROBOHOGAR con 3 artículos (sin botón "Acceder")?
- [ ] ¿Imagen hero generada (1200x630)?
- [ ] ¿Disclaimer de afiliados al pie?
- [ ] ¿Mínimo 1.000 palabras?
- [ ] ¿Al menos 2 internal links?
- [ ] ¿Slug configurado en Settings → URL?
- [ ] ¿SEO Title + Meta Description en Settings → SEO?
