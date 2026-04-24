---
name: ROBOHOGAR corre en Beehiiv plan Scale (no Free)
description: ROBOHOGAR tiene Beehiiv plan Scale desde 2026-04-18. Automations, segmentación, welcome flows, digital products y secuencias disponibles. No asumir limitaciones del plan Launch/Free.
type: project
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
ROBOHOGAR corre en **Beehiiv plan Scale** (Rafael lo confirmó 2026-04-18). No estar en Launch/Free.

**Why:** Propuesta de lead magnets 2026-04-18 — redacté la arquitectura asumiendo plan Free ("1 tangible maestro universal porque no hay automations") y Rafael corrigió. CLAUDE.md tenía "Beehiiv (free plan, 2.500 subs)" desactualizado — corregido a "plan Scale". Para decisiones de producto y arquitectura de contenido, asumir Scale como premisa a partir de ahora.

**How to apply:**

**Features disponibles en Scale que NO estaban en Free** — usar en propuestas sin caveat de "upgrade first":
- **Automations / Workflows 2.0** — secuencias on-signup, on-tag, on-event. Segmentación por fuente de suscripción (artículo, lead magnet, referral).
- **Digital products** con entrega automática segmentada (distintos PDFs/links según tag o fuente).
- **Welcome sequences** multi-email con trigger por segmento (no solo 1 welcome único como en Launch).
- **Audience segments** por comportamiento (clicks, opens, polls) + tags custom.
- **A/B testing** de subject lines y contenido.
- **Advanced analytics** — cohort tracking, lifetime value estimate.
- **Custom domains** para landing pages de lead magnets (`descargas.robohogar.com`).

**Consecuencias para arquitectura de contenido:**
- **Lead magnets segmentados por categoría** (aspiradores / cortacéspedes / humanoides / ficciones) son viables desde el día 1. No hay que empezar por "1 maestro universal y luego expandir".
- **Welcome sequence diferenciada por fuente**: quien se suscribe desde "Hoja de Compra" recibe nurture distinto del que viene desde "Dossier Ficciones".
- **Content gate block-level** es viable también (es feature de plan free incluso), pero sigue aplicando `feedback_gate_respects_phase.md` (F1 0-50 subs: sin gate aunque tecnológicamente se pueda).

**Coste implícito:** plan Scale ~$39-49/mes según tier y número de subs. Con 0-30 subs hoy es inversión fija; con 200+ subs + afiliados activos, sostenible. Rafael asume el coste como parte del stack editorial.

**Qué NO ha cambiado:**
- Fase F1 sigue siendo 0-50 subs (cadencia actual) → aplica `@rules/tangibles.md` F1 (tangible inline sin paywall). El paywall de F3 sigue siendo ~5K subs.
- Cap de 2.500 subs del plan NO aplica — ese era el límite del free. Scale escala a 10K-100K según tier. Verificar límite exacto en settings Beehiiv cuando sea relevante.
- 3-5 h/semana de Rafael sigue siendo la restricción real. Automations reducen trabajo de entrega pero el contenido de los tangibles hay que producirlo.
