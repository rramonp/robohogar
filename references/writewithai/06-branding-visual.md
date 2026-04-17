# 06 — Branding visual (comparativa WriteWithAI ↔ ROBOHOGAR)

> Observaciones visuales extraídas de hero images, paletas y componentes del site writewithai.substack.com. Contraste con el sistema ROBOHOGAR ya definido en `.claude/rules/design.md`. Cross-refs: [estructura](02-estructura-articulo-visual.md) · [emails](04-email-newsletter-patterns.md).

## TL;DR

- WriteWithAI usa una paleta **verde menta (#8AE1A2) + gris oscuro (#363737)** sobre fondo blanco. ROBOHOGAR usa **ámbar (#F5A623) + negro (#0C0C0C)**. Los dos funcionan: acento saturado + neutro fuerte + blanco.
- Su hero es **screenshot-realista tipográfico (1260 × 900)**. El nuestro es **cinematográfico producto-hero (1200 × 630)**. Son dos filosofías distintas — la suya prioriza escaneo, la nuestra prioriza autoridad.
- Componentes a robar: **logo 40×40 en header, footer con poll embebido ❤️/👍/🫤/💢, PS con upsell en footer, subject line repetido como H1**.
- ROBOHOGAR ya tiene sistema más cohesivo que WWAI (monograma R + mascota + templates). Lo que falta: **componentes de interacción en el email** (poll, forward-friendly) y **patrón de logo en header**.

---

## Comparativa de paletas

| Rol | WriteWithAI | ROBOHOGAR | Observación |
|---|---|---|---|
| Primario / acento | `#8AE1A2` menta | `#F5A623` ámbar | Ambos cálidos/saturados sobre blanco. El nuestro es más visible en thumbnails oscuros. |
| Texto principal | `#363737` carbón | `#0C0C0C` negro | Ellos usan "casi-negro" para suavizar. Podemos probar variante `#171717` para textos largos. |
| Fondo | `#FFFFFF` | `#FFFFFF` | Igual. Minimal-editorial. |
| Secundario / UI | gris medio | `#6B7280` + `#F2F2F2` | Equivalentes. |
| CTA | menta con border oscuro | ámbar | Ambos con `border-radius: 8px` aprox. |

**Veredicto:** nuestra paleta es más diferenciable del resto de newsletters tech (verde es saturado pero común en SaaS; ámbar destaca más en un feed Gmail). No cambiar.

## Tipografía

| Uso | WriteWithAI | ROBOHOGAR |
|---|---|---|
| Títulos | **SF Pro Display** (system semibold) | **Jost** regular 400 |
| Cuerpo | **Spectral** serif | **DM Sans** sans |
| Labels / UI | SF Pro Text | DM Sans Medium/SemiBold |

**Observación interesante:** WWAI mezcla **serif en cuerpo + sans en título**. Nosotros usamos **solo sans**. La mezcla serif/sans da aire editorial a artículos largos y en dispositivos con buen rendering (macOS, iPad). A considerar como experimento: probar serif para cuerpo en una review larga. Pero Jost + DM Sans tiene coherencia fuerte y la mascota + monograma refuerzan identidad, así que no es urgente.

## Componentes observados en WriteWithAI

### 1. Logo 40 × 40 en header

WWAI coloca su logotipo redondo (robot verde) en esquina superior izquierda, 40px. Consistente en web + email + hero images.

**ROBOHOGAR actual:** el monograma R está en header del newsletter pero variable en tamaño. Propuesta: **estandarizar 40 × 40 con padding 12 px** en todos los templates.

### 2. Botón CTA primario con shadow inset

Ejemplo de estilo WWAI aplicado a Beehiiv:

```css
.cta-primary {
  background: #F5A623;           /* acento ROBOHOGAR */
  color: #0C0C0C;
  border: 1.5px solid #0C0C0C;
  border-radius: 8px;
  padding: 12px 24px;
  font-weight: 600;
  box-shadow: inset 0 -3px 0 rgba(12,12,12,0.12);  /* truco sutil de "profundidad" */
}
```

El `inset shadow` inferior es lo que diferencia el botón de Substack/Beehiiv estándar. Da sensación de "pressable" sin sombras externas pesadas.

### 3. Hero screenshot-realista 1260 × 900

Cole/Bush usan hero con texto grande + collage visual (ejemplo: bolsa Ruffles + tipografía "1 Chip Rule"). Son composiciones sin producto real, más bien "tarjeta visual del título".

**ROBOHOGAR usa** hero **cinematográfico product-hero 1200 × 630** (la regla del `asset-catalog.md`) — más serio, más autoritativo. **Decisión: mantener.** Es diferenciador en un ecosistema donde todos los newsletters usan collages tipográficos. El product-hero transmite "aquí se prueba el producto de verdad".

**Pero** vale la pena copiar una cosa: **variant de hero para editoriales 30% futuros**. Para artículos no-review (opinión, futuro), un hero más editorial-abstracto encaja mejor que un product-shot. Añadir a `asset-catalog.md` la variante `editorial-1200x630`.

### 4. Footer con poll embebido (❤️ / 👍 / 🫤 / 💢)

WWAI incrusta un mini poll en el pie de cada email:

```
¿Qué te ha parecido esta edición?
[❤️ me encantó]  [👍 bien]  [🫤 regular]  [💢 nop]
```

Beehiiv soporta esto nativamente con su widget de "Post Feedback". **Recomendación: activarlo.** Es feedback cuantitativo semanal sin esfuerzo, y reemplaza la métrica de NPS informal.

### 5. PS con upsell en footer

Cole/Bush colocan después de la firma un "P.S." que es siempre una oferta sutil ("If you want the full prompt library, we cover it in Premium GhostWriting Academy.").

**ROBOHOGAR adapta** esto con **PS editorial** (no comercial):

> P.D. ¿Conoces a alguien mirando robots? Reenvíale este email — así crece ROBOHOGAR sin algoritmos.

Convierte PS de Cole en táctica de *forward-to-a-friend* en lugar de venta. Ajusta al posicionamiento hobby/editorial actual.

### 6. Subject line repetido como H1

WWAI repite textualmente el subject line del email como H1 del post en la web. Coherencia visual + SEO. ROBOHOGAR ya lo hace en parte. **Revisar que sea sistemático.**

---

## Contraste con sistema ROBOHOGAR actual

Lo que ROBOHOGAR ya hace mejor que WWAI:

- **Monograma R + mascota con roles diferenciados** (marca editorial vs tono cercano). Más sofisticado que el logo único de WWAI.
- **Flash-1K variantes de mascota** por contexto (casita, compras, detective, herramientas...) — WWAI no tiene este nivel.
- **Paleta más distintiva** en un ecosistema saturado de verdes SaaS.
- **Cinematic product-hero** para reviews → más autoridad que collage tipográfico.

Lo que ROBOHOGAR puede adoptar de WWAI:

- Logo 40 × 40 estandarizado (header consistente).
- Botón primario con `inset shadow` sutil.
- Poll embebido en footer de newsletter.
- Variante `editorial-1200x630` para artículos no-review.
- PS como táctica de forward-to-a-friend.
- Serif en cuerpo de artículos largos (experimento controlado, no sistema).

---

## 3 ideas visuales concretas a probar en robohogar.com

### Idea 1 · Bloque "Why it matters" visual (Axios-style)

Para cada noticia en la newsletter, componer un bloque visual con:
- Icono de mascota en variante `megafono` (ya existe).
- Titular en **Jost bold 18 px**.
- Sub-línea gris `#6B7280` "Por qué importa:" seguida de 1 frase.
- 3 bullets azul-negros.
- Link único al final (color ámbar `#F5A623`).

Bajo coste, alto escaneado, refuerza identidad editorial.

### Idea 2 · Hero "editorial" para piezas 30%

Generar con `/nano-banana` una serie de 10 hero abstractos-editoriales (1200 × 630) para cubrir temas de futuro: hogar robotizado, humanoides, privacidad, automatización, ciudades. Estilo: **composiciones minimalistas con el monograma R flotando** sobre fondos gradiente oscuros. Guardar en `assets/branding/heroes-editoriales/`.

### Idea 3 · Footer widget "ROBOHOGAR en redes + poll"

Rediseñar el footer del newsletter con:
- Fila 1: poll ❤️ / 👍 / 🫤 / 💢 (widget nativo Beehiiv).
- Fila 2: PS de forward-a-friend con copy editorial.
- Fila 3: iconos mínimos (LinkedIn + Instagram + web) en gris `#6B7280`.
- Fila 4: unsubscribe discreto.

Total altura ≈ 180 px, no invasivo, maximiza datos útiles sin hacer ruido.

---

## Aplicabilidad ROBOHOGAR concreta

**Acciones priorizadas:**
1. **Esta semana:** activar el widget de poll nativo Beehiiv en pie de newsletter. Coste: 5 min.
2. **Próximas 2 semanas:** estandarizar logo 40 × 40 en todos los templates (web, email, social). Actualizar `assets/branding/master/README.md` con dimensiones.
3. **Mes 1:** generar batch de 5 heroes editoriales con `/nano-banana` para cubrir backlog de artículos 30%.
4. **Mes 2:** experimento A/B — una review larga con cuerpo en serif (probar **Spectral** o **Source Serif**) vs la estándar en DM Sans. Medir tiempo medio de lectura. Decidir sistema en función de resultado.
5. **Cualquier momento:** añadir PS de forward-a-friend al template newsletter. Coste: 5 min. Potencial viral bajo pero real.

**No tocar:**
- Paleta (ámbar ya es más diferenciadora que menta).
- Monograma + mascota (sistema superior al de WWAI).
- Cinematic product-hero para reviews (autoridad diferencial).
