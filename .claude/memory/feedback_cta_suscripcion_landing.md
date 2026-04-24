---
name: CTA de suscripción al newsletter apunta siempre a la landing
description: Todo banner/botón de suscripción al newsletter ROBOHOGAR lleva a robohogar.com (home), nunca a /subscribe ni a ninguna ruta interna
type: feedback
originSessionId: e9873eca-e420-4e4a-8520-aa5fe0ef3c72
---
Todo CTA de suscripción al newsletter ROBOHOGAR — banner al final de artículo, banner al final de ficción, botón en email, enlace en social copy, footer de PDF tangible, link en wiki del vault — apunta a `https://robohogar.com` (la landing page raíz), no a `/subscribe` ni a ninguna ruta interna.

**Why:** Rafael estableció la regla explícitamente 2026-04-20 tras ver un snippet que proponía `/subscribe`. La landing page es el embudo canonizado de captación — tiene el copy completo (propuesta de valor + social proof + preview de ficciones) y el formulario de suscripción. Mandar al lector a `/subscribe` lo deja en un formulario pelado sin contexto, peor conversión. Además Beehiiv resuelve la home como la landing configurada — redirigir funciona igual técnicamente, pero perdemos el hit de analytics del landing principal.

**How to apply:** cualquier banner/botón/link de suscripción generado por skills (`/content-draft`, `/social-content`, `/pdf-brand`, borradores de newsletter, snippets de templates) usa `href="https://robohogar.com"`. Sin path, sin query string salvo UTMs por canal. Excepción única: el banner del tangible **Hoja de Compra** mantiene `robohogar.com/products/hoja-de-compra?utm_...` porque apunta al Beehiiv Digital Product page, no al newsletter en sí (regla en memoria `feedback_banner_cta_uses_product_url.md`).

Verificación pre-output en cualquier HTML generado:
```
grep -nE "href=\"https?://robohogar\.com/(subscribe|signup|newsletter)" <archivo>
```
Debe devolver 0 matches. Si aparece, sustituir por `https://robohogar.com` manteniendo UTMs si los había.

Regla persistida en [`.claude/rules/newsletter.md § URL destino de CTAs de suscripción`](../../../robohogar/.claude/rules/newsletter.md).
