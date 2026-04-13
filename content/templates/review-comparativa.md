# Template: Review / Comparativa

> Uso: artículos que comparan 3-6 productos de una misma categoría con opinión honesta.
> Ejemplos: "Robots de escritorio con IA", "Mejor robot aspirador 2026", "Cortacéspedes robot".
> Tono: amigo techie que te cuenta qué merece tu dinero. Opinión clara, sin hype.

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

## Estructura del artículo

### HOOK (1-2 frases)

Frase directa que engancha. Nada de "en este artículo vamos a ver...".
Conectar con algo que el lector ya siente o piensa.

```
Ejemplo: "Hay robots de escritorio que te hablan, te reconocen y cuestan
menos que unos AirPods Pro. Otros cuestan 400€ y apenas funcionan.
Vamos a separar el grano de la paja."
```

### CONTEXTO (1 párrafo)

¿Por qué importa este tema AHORA? ¿Qué ha cambiado recientemente?
Dato concreto o tendencia que justifique el artículo.

```
Ejemplo: "En 2026, la integración de ChatGPT en robots domésticos ha
pasado de ser una demo a ser un producto real. Ya hay [X] modelos
a la venta por menos de 500€."
```

### CRITERIOS DE SELECCIÓN (H2)

Explicar brevemente QUÉ criterios usas para evaluar. Esto establece
credibilidad y transparencia.

```
Ejemplo H2: "Cómo he evaluado estos robots"
- Precio vs. lo que realmente hace
- ¿Necesita suscripción mensual?
- ¿Funciona bien en español?
- Opiniones reales de usuarios (no solo reviews patrocinados)
```

### PRODUCTO 1 — EL RECOMENDADO (H2)

```
H2: [Nombre del producto] — [veredicto en 3-5 palabras]
     Ejemplo: "Eilik — el que más merece tu dinero"
```

Estructura por producto:

- **Qué es en una frase** — descripción ultra-breve
- **Lo bueno** — 3-4 bullets concretos (no genéricos)
- **Lo malo** — 2-3 bullets honestos (NUNCA omitir lo malo)
- **Para quién es** — perfil de usuario ideal
- **Precio** — con link de afiliado si aplica
- **Mi opinión** — 2-3 frases con voz propia, en primera persona

> Regla: empezar SIEMPRE por el producto recomendado. El lector impaciente
> se lleva la respuesta en 30 segundos. El curioso sigue leyendo.

### PRODUCTO 2 (H2)

Misma estructura que Producto 1.

### PRODUCTO 3 (H2)

Misma estructura que Producto 1.

### [PRODUCTOS 4-6 si aplica] (H2 cada uno)

Para comparativas con más productos, mantener la misma estructura.
Máximo 6 productos — más de eso diluye la calidad.

### LOS QUE NO RECOMIENDO (H2)

```
H2: "¿Y los que NO recomiendo?"
```

Breve mención (2-3 frases cada uno) de productos populares que has
descartado y POR QUÉ. Esto genera mucha confianza — el lector ve
que no recomiendas todo.

### TABLA RESUMEN (H2)

```
H2: "Comparativa rápida"
```

Tabla markdown con todos los productos lado a lado:

| Producto | Precio | Suscripción | Lo mejor | Lo peor | Veredicto |
|----------|--------|-------------|----------|---------|-----------|
| ...      | ...    | ...         | ...      | ...     | ⭐⭐⭐⭐    |

### VEREDICTO FINAL (H2)

```
H2: "Entonces, ¿cuál me compro?"
```

- 3-4 frases claras tipo: "Si buscas X, ve a por Y. Si tu presupuesto
  es Z, entonces W."
- Cerrar con CTA suave a suscripción: "Si te ha servido, en ROBOHOGAR
  publicamos esto cada 2 semanas."

---

## Reglas de estilo para este template

- **Longitud**: 1.000-1.800 palabras (ni más ni menos)
- **Tono**: "tú", informal, con humor sutil. Como hablarle a un amigo
- **Opinión**: OBLIGATORIA. Si no tienes opinión, no publiques
- **Lo malo**: OBLIGATORIO en cada producto. Un review sin contras es un anuncio
- **Afiliados**: link natural al final de cada producto ("Disponible en Amazon (XX€)")
- **Disclaimer**: al pie del artículo: "Algunos links son de afiliado — si compras a través de ellos, nos ayudas a mantener ROBOHOGAR sin coste extra para ti"
- **Imágenes**: 1 imagen por producto (foto real, no render de marketing si es posible)
- **SEO**: H1 con keyword, H2 con variaciones semánticas, alt text en imágenes

---

## Checklist pre-publicación

- [ ] ¿El título incluye keyword principal?
- [ ] ¿La meta description tiene < 155 caracteres y CTA implícito?
- [ ] ¿Cada producto tiene sección "Lo malo"?
- [ ] ¿Hay al menos 1 opinión personal por producto?
- [ ] ¿Los precios están actualizados?
- [ ] ¿Los links de afiliado funcionan?
- [ ] ¿Hay tabla resumen comparativa?
- [ ] ¿El veredicto final da recomendación clara?
- [ ] ¿Imagen destacada generada (1200x630)?
- [ ] ¿Disclaimer de afiliados al pie?
- [ ] ¿Mínimo 1.000 palabras?
- [ ] ¿Máximo 2 internal links a otros artículos?
