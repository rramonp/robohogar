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

## Benchmarks, diseño, deliverability

Open >41%, CTR >3.2%, mobile-first 600px, dark mode safe, SPF/DKIM/DMARC activos. Detalle → `references/newsletter/email-marketing-playbook.md`.

## Preset emails (welcome, double opt-in, reminder) — plain-text + minimalismo

Regla dura: los preset emails transaccionales de Beehiiv (Double Opt-In, Welcome nativo, Smart Nudge) van en **plain text, sin logos ni imágenes inline en el cuerpo**. El header/footer global de Beehiiv ya inyecta el branding (logo + nombre publicación + dirección postal + unsubscribe) → duplicar es redundante y perjudica deliverability. Superhuman, Figma y referentes onboarding lo aplican así. Razón técnica: Gmail/Outlook clasifican HTML con imágenes como Promotions; plain text conversacional cae en Primary. Aplicable también al Email 1 del welcome flow MVP (ver `docs/welcome-flow-setup.md`) — salvo el botón CTA al PDF/link, no meter elementos visuales.

## Timing & GDPR

Martes/miércoles 9:00 CET (consistencia > volumen). Audiencia EU: doble opt-in recomendado, one-click unsubscribe obligatorio.
