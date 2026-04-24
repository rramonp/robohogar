---
name: ROBOHOGAR welcome flow MVP = 2 emails hasta ~200 subs, no 4
description: Welcome flow de ROBOHOGAR es deliberadamente 2 emails (no 4-5) mientras subs <200. Email 1 entrega PDF + reply request, Email 2 +72h con ritmo editorial + 2 evergreens.
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
ROBOHOGAR opera con un welcome flow **MVP de 2 emails**, no la secuencia de 4-5 que propone el playbook de email marketing. Se expande a 4 cuando los suscriptores superen ~200 y el open rate del welcome esté estable >50 %.

**Why:** Rafael lo validó 2026-04-18 con pregunta directa: *"este plan de correos tiene sentido teniendo 0 subscriptores? entiendo que si, mi objetivo principal es obtener suscriptores en este momento"*. La intuición es parcialmente correcta: con <100 subs, el ROI marginal de optimizar retention es bajo frente a optimizar CVR del banner. Pero suprimir el welcome entero es error — 3 funciones siguen siendo críticas en fase 0:

1. **Entrega del lead magnet prometido** (sin esto rompes el pacto del banner, unsub en 48 h).
2. **Señal "reply"** para deliverability futura (Gmail lee respuestas como engagement fuerte; sin welcome flow la primera newsletter semanal puede caer en Spam).
3. **Primer contacto editorial con open rate 60-80 %** — es el único slot garantizado de lectura; desperdiciarlo es caro.

Secuencias de 4-5 emails en fase <100 subs son premature optimization: Email 3 (día 7) choca con la newsletter semanal, Email 4 (día 10) "bienvenida al ritmo" es redundante si ya recibió 2. El esfuerzo marginal va mejor a iterar banner/CVR.

**How to apply:**

- **Documento autoritativo:** `docs/welcome-flow-setup.md` — contiene copy completo de los 2 emails (subject ≤25 chars, preheader, cuerpo), configuración Beehiiv Scale step-by-step (Automations 2.0 con trigger on-confirm + delay 72h), y métricas objetivo por email.
- **Arquitectura Beehiiv:** Automations / Workflows 2.0 (plan Scale), NO el Welcome Email único. Desactivar el Welcome Email nativo si el workflow está activo para no duplicar envíos.
- **Trigger del workflow:** `Subscriber confirms subscription` (double opt-in ON obligatorio por GDPR EU).
- **Email 1 (inmediato):** subject `Tu PDF (y una pregunta)` · entrega PDF + pregunta explícita "¿cuál es la zona de tu casa que más te cuesta limpiar?" con reply request.
- **Email 2 (+72h):** subject `Qué esperar (y 2 joyas)` · explica cadencia martes 9:00 + 2 artículos evergreen del archivo (hoy: Samsung Steam Ultra + Saros Z70).
- **Firma en singular ("Rafael"),** excepción a la voz plural editorial (regla `editorial.md` § Voz: firma/bio autorizan singular).
- **Anti-IA checklist §1 Universal aplicada** a los 2 emails — 0 flags.

**Cuándo expandir a 4 emails:**
- Subs ≥ 200.
- Open rate welcome estable >50 % durante 1 mes.
- Archivo de artículos publicados ≥ 10 (para rellenar email 3 con valor real).
- Frase trigger: *"Retomamos welcome-flow — expandir a 4 emails"*.
- Estructura emails 3-4 documentada en `references/newsletter/email-marketing-playbook.md § 12` (hand-pick article + encuesta corta).

**Regla mental operativa:** con <100 subs foco en CVR (conseguir el siguiente suscriptor). Con >500 subs foco en retención (expandir flow, A/B test subjects, personalizar). No mezclar prioridades entre fases.
