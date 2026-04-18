# Newsletter Rules

Mecánicas de email (entrega, diseño, optimización). Voz/tono → `editorial.md`. Playbook detallado con subject lines, arquetipos y welcome sequence → `references/newsletter/email-marketing-playbook.md` + `references/writewithai/04-email-newsletter-patterns.md`.

## Tipos de publicación en Beehiiv

Beehiiv envía cada post por email UNA sola vez. Publicar con 0 subs "quema" el envío y el artículo ya no podrá reenviarse cuando haya audiencia. Default por fase:

| Fase | Artículo | Newsletter semanal |
|---|---|---|
| **Pre-audiencia (<20-30 subs, hoy)** | `Web only` — reserva el envío | `Email only` — se envía aunque sean 0-5 subs |
| **Con audiencia (≥20-30 subs)** | `Email and web` — landing + email | `Email only` |

Al llegar a 20-30 subs: enviar "digest de bienvenida" manual con los artículos top ya publicados.

## Subject Lines

Max 25 chars. Fitea uno de 5 arquetipos: curiosity gap · fear/warning · benefit · authority · story. Sin clickbait, sin ALL CAPS, sin spam triggers. Tabla de ejemplos ROBOHOGAR y openers → `references/writewithai/04-email-newsletter-patterns.md`.

## Estructura & CTAs

- Estándar **1-3-1**: 1 gancho + 3 puntos + 1 CTA (párrafo y email global)
- CTA único por email, botón > enlace. Above fold + final en emails largos

## Benchmarks, diseño, deliverability

Open >41%, CTR >3.2%, mobile-first 600px, dark mode safe, SPF/DKIM/DMARC activos. Detalle → `references/newsletter/email-marketing-playbook.md`.

## Preset emails (welcome, double opt-in, reminder) — plain-text + minimalismo

Regla dura: los preset emails transaccionales de Beehiiv (Double Opt-In, Welcome nativo, Smart Nudge) van en **plain text, sin logos ni imágenes inline en el cuerpo**. El header/footer global de Beehiiv ya inyecta el branding (logo + nombre publicación + dirección postal + unsubscribe) → duplicar es redundante y perjudica deliverability. Superhuman, Figma y referentes onboarding lo aplican así. Razón técnica: Gmail/Outlook clasifican HTML con imágenes como Promotions; plain text conversacional cae en Primary. Aplicable también al Email 1 del welcome flow MVP (ver `docs/welcome-flow-setup.md`) — salvo el botón CTA al PDF/link, no meter elementos visuales.

## Timing & GDPR

Martes/miércoles 9:00 CET (consistencia > volumen). Audiencia EU: doble opt-in recomendado, one-click unsubscribe obligatorio.
