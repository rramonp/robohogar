# Newsletter Rules

Mecánicas de email (entrega, diseño, optimización). Voz/tono → `editorial.md`. Playbook detallado con subject lines, arquetipos y welcome sequence → `references/newsletter/email-marketing-playbook.md` + `references/writewithai/04-email-newsletter-patterns.md`.

## Tipos de publicación en Beehiiv

Beehiiv envía cada post por email UNA sola vez. Publicar con 0 subs "quema" el envío y el artículo ya no podrá reenviarse cuando haya audiencia. Default por fase:

| Fase | Artículo | Newsletter semanal |
|---|---|---|
| **Pre-audiencia (<20-30 subs, hoy)** | `Web only` — reserva el envío | `Email only` — se envía aunque sean 0-5 subs |
| **Con audiencia (≥20-30 subs)** | `Email and web` — landing + email | `Email only` |

Al llegar a 20-30 subs: enviar "digest de bienvenida" manual con los artículos top ya publicados.

## Subject Lines (asuntos)

**20-45 chars · preferencia ≤35.** Límite ajustado 2026-04-19 tras research de newsletters ES (Kloshletter 41 chars, Cincominutos 37, EOM 22-30). La regla original ≤25 chars venía de Nicolas Cole (US, inglés monosilábico); el castellano es morfológicamente más largo y apretar a 25 fuerza copy forzado. Regla dura: **≤45 chars**, target ≤35.

Fitea uno de 5 arquetipos: curiosity gap · fear/warning · benefit · authority · story. Sin clickbait, sin ALL CAPS, sin spam triggers. **Máximo 1 emoji** como icono de marca (patrón Cincominutos `⭕️`), nunca decorativo ni en cascada (`🔥🚀✨`). Tabla de ejemplos ROBOHOGAR y openers → `references/writewithai/04-email-newsletter-patterns.md`. Aperturas y cierres del body: `@rules/editorial.md § Apertura y cierre del cuerpo del email`.

## Palabra nuclear del producto

"Newsletter" es la palabra dominante en el 83% del ecosistema ES Substack/Beehiiv auditado (research 2026-04-19, 20 newsletters). ROBOHOGAR la adopta. "**Boletín**" se permite como sinónimo puntual en prosa editorial (tradición periodística ES), nunca como nombre del producto ni en botón CTA. "**Correo**" solo como vector de entrega ("recibe en tu correo"), nunca como nombre del producto. "**Suscripción**" como sustantivo standalone (0% de uso en ES) — evitar; usar `suscríbete` como verbo o `newsletter` como nombre.

## Estructura & CTAs

- Estándar **1-3-1**: 1 gancho + 3 puntos + 1 CTA (párrafo y email global)
- CTA único por email, botón > enlace. Above fold + final en emails largos

## URL destino de CTAs de suscripción — SIEMPRE landing

Todo banner / botón / link de **suscripción al newsletter** ROBOHOGAR apunta siempre a `https://robohogar.com` (landing raíz). Nunca a `/subscribe`, `/signup`, `/newsletter` ni a ninguna ruta interna. Aplica a: banner al final de artículo, banner al final de ficción, CTA de cierre de email, P.D. con enlace, footer de PDF tangible, link en social copy, link en wiki del vault.

**Por qué:** la landing contiene propuesta de valor completa + preview + social proof; `/subscribe` deja al lector en un formulario pelado, peor conversión. Regla dura establecida por Rafael 2026-04-20.

**Excepción única:** el banner del tangible **Hoja de Compra** mantiene `https://robohogar.com/products/hoja-de-compra?utm_source=<slug>&utm_medium=banner&utm_campaign=hoja-compra` porque apunta al Beehiiv Digital Product page específico, no al newsletter genérico (ver `rules/tangibles.md` y memoria `feedback_banner_cta_uses_product_url.md`).

**Verificación pre-output** en cualquier HTML generado por skills (`/content-draft`, `/social-content`, `/pdf-brand`, borradores manuales):

```bash
grep -nE 'href="https?://robohogar\.com/(subscribe|signup|newsletter)[/"?]' <archivo>
```

Debe devolver 0 matches. Si aparece, sustituir por `https://robohogar.com`.

## Snippet canónico · banner CTA suscripción al final de artículo (no-ficción)

Dark-themed, centrado, 4 elementos (pregunta + beneficio + botón + trust-line). Obligatorio como **snippet final** de todo artículo no-ficción (review, comparativa, editorial, guía, tutorial, newsletter). Se pega en Beehiiv vía `/html` → Custom HTML block.

**Posición en el esqueleto del borrador:** justo después del bloque `¿Sabías que…?` + su `<div class="separator"></div>`, y antes del bloque `Más en ROBOHOGAR` (internal linking) + disclaimer. Razón: el CTA principal se presenta antes del jumpoff a otros artículos — si el lector va a convertir, lo hace aquí; si no, sigue leyendo por los links de abajo.

**Relación con el banner Hoja de Compra:** son bloques distintos y compatibles. Hoja de Compra (si aplica por categoría) va en posición intro o cierre-tras-veredicto como tangible específico. Este CTA va al **final absoluto del contenido editorial** como invitación al newsletter raíz, sin UTM (regla `§ URL destino de CTAs de suscripción — SIEMPRE landing`).

```html
<div style="margin:40px 0 0;padding:28px 24px;background:#283642;border-radius:8px;color:#FFFFFF;text-align:center;font-family:'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;">
  <div style="font-family:'DM Sans',sans-serif;font-size:20px;font-weight:700;color:#FFFFFF;line-height:1.3;margin-bottom:10px;">¿Te ha servido este análisis?</div>
  <p style="margin:8px 0 16px;font-size:15px;color:#FFFFFF;line-height:1.55;">De andar por casa. Cada semana.</p>
  <a href="https://robohogar.com" style="display:inline-block;background:#F5A623;color:#FFFFFF !important;padding:12px 24px;border-radius:6px;font-weight:700;text-decoration:none;font-size:15px;font-family:'DM Sans',sans-serif;">Suscribirse</a>
  <p style="margin:14px 0 0;font-size:12px;color:#FFFFFF;line-height:1.4;">Newsletter gratis. Un email por semana. Cancela cuando quieras.</p>
</div>
```

Texto fijo, no se varía por artículo. El botón dice `Suscribirse` (infinitivo) — el de ficción mantiene `Suscribirme` (primera persona). Trust-line cumple la regla `@rules/tangibles.md § Microcopy de conversión`: 3 elementos (formato "gratis" · cadencia "semanal" · salida "cancela cuando quieras"). `href` apunta a `https://robohogar.com` sin UTM.

**Verificación pre-output:** todo borrador no-ficción debe tener exactamente 1 bloque `<div class="snippet-block">` que contenga el string `¿Te ha servido este análisis?` en la posición descrita. Si 0 → falta; si ≥2 → duplicado.

## Snippet canónico · banner suscripción al final de ficción

Dark-themed, centrado, 5 elementos en orden fijo: eyebrow `ROBOHOGAR` + pregunta-gancho `¿Te ha gustado?` + título-promesa `La próxima Ficción Doméstica, en tu correo.` + botón `Suscribirme` + trust-line. Actualizado 2026-04-22 (añadida pregunta-gancho + trust-line). Para pegar en Beehiiv vía `/html` → Custom HTML block tras el bloque "Lo real detrás del relato" de cada Ficción Doméstica.

```html
<div style="margin:40px 0 24px;padding:32px 24px;background:#283642;border-radius:10px;color:#FFFFFF;font-family:'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;text-align:center;">
  <div style="color:#F5A623;font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;">ROBOHOGAR</div>
  <div style="font-family:'DM Sans',sans-serif;font-size:20px;font-weight:700;color:#FFFFFF;line-height:1.3;margin-bottom:10px;">¿Te ha gustado?</div>
  <div style="font-family:'DM Sans',sans-serif;font-size:20px;font-weight:700;color:#FFFFFF;line-height:1.25;margin-bottom:22px;">La próxima Ficción Doméstica, en tu correo.</div>
  <a href="https://robohogar.com" style="display:inline-block;background:#F5A623;color:#FFFFFF !important;padding:14px 28px;border-radius:8px;font-weight:700;text-decoration:none;font-size:15px;font-family:'DM Sans',sans-serif;">Suscribirme</a>
  <p style="margin:14px 0 0;font-size:12px;color:#FFFFFF;line-height:1.4;">Newsletter gratis. Un email por semana. Cancela cuando quieras.</p>
</div>
```

**Diferencias con el CTA final de artículo no-ficción** (arriba en este mismo archivo):
- Ficción lleva eyebrow `ROBOHOGAR` + pregunta-gancho; artículo entra directo con la pregunta sin eyebrow.
- Ficción mantiene el título-promesa `La próxima Ficción Doméstica, en tu correo.` como línea propia.
- Botón `Suscribirme` (1ª persona) vs `Suscribirse` (infinitivo) en artículos. No mezclar.
- Ambos comparten trust-line, paleta, tamaños de padding y UTM ausente (`href` a `https://robohogar.com` raíz).

Texto fijo — no se varía por relato. La prosa del cierre es el último contacto del lector con la ficción; mantener el CTA consistente refuerza la marca editorial por encima de adornos por relato.

## Benchmarks, diseño, deliverability

Open >41%, CTR >3.2%, mobile-first 600px, dark mode safe, SPF/DKIM/DMARC activos. Detalle → `references/newsletter/email-marketing-playbook.md`.

## Preset emails (welcome, double opt-in, reminder) — plain-text + minimalismo

Regla dura: los preset emails transaccionales de Beehiiv (Double Opt-In, Welcome nativo, Smart Nudge) van en **plain text, sin logos ni imágenes inline en el cuerpo**. El header/footer global de Beehiiv ya inyecta el branding (logo + nombre publicación + dirección postal + unsubscribe) → duplicar es redundante y perjudica deliverability. Superhuman, Figma y referentes onboarding lo aplican así. Razón técnica: Gmail/Outlook clasifican HTML con imágenes como Promotions; plain text conversacional cae en Primary. Aplicable también al Email 1 del welcome flow MVP (ver `docs/welcome-flow-setup.md`) — salvo el botón CTA al PDF/link, no meter elementos visuales.

## Timing & GDPR

Martes/miércoles 9:00 CET (consistencia > volumen). Audiencia EU: doble opt-in recomendado, one-click unsubscribe obligatorio.
