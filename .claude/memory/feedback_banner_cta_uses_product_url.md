---
name: Banner lead magnet URL → Beehiiv digital product page
description: ROBOHOGAR banner lead magnet CTAs deben apuntar a la URL del Digital Product de Beehiiv, nunca a /subscribe ni a la home genérica
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
Los banners que promocionan un tangible PDF (ej. Hoja de Compra) dentro de artículos ROBOHOGAR deben apuntar a la URL del **Beehiiv Digital Product** correspondiente, no a `/subscribe` ni a la home `robohogar.com`.

Formato: `https://robohogar.com/products/<slug-producto>?src=<slug-artículo>` (path `/products/` en PLURAL — Beehiiv genera así la Digital Product page; `/product/` en singular da 404, confirmado 2026-04-18).

Ejemplo activo: `https://robohogar.com/products/hoja-de-compra?src=mejor-robot-asistente-ia-2026`.

**Why:** Beehiiv crea una product page dedicada para cada Digital Product con su propio formulario de suscripción vinculado al PDF — quien se suscribe ahí recibe automáticamente el tangible en el Email 1 del welcome flow. Alternativas peores: (1) `/subscribe` no es una página configurada, Beehiiv muestra una pantalla default genérica sin mención del PDF → mismatch con la promesa del banner; (2) la home `robohogar.com` tiene el formulario bonito pero no menciona el PDF → también mismatch y pérdida de conversión. Rafael identificó el problema 2026-04-18 al ver que el link `/subscribe` del primer banner aterrizaba en la pantalla default fea.

**How to apply:** cuando crees o revises un banner lead magnet en un artículo o template, el `<a href>` debe ser la product URL del tangible específico + parámetro `?src=<slug-artículo>` para tracking. La UTM `?lm=...` del esquema anterior deja de ser necesaria — el producto ya está implícito en la URL del path. Aplica al template [`content/templates/banner-lead-magnet.html`](../../robohogar/content/templates/banner-lead-magnet.html), a los snippets pre-personalizados, y a cualquier nuevo tangible que se active (Guía primer mes, Glosario, etc.) — cada uno usa su propia product page de Beehiiv.
