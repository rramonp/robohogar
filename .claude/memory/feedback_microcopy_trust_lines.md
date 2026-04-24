---
name: Microcopy trust-lines bajo CTA (ROBOHOGAR)
description: Regla certificada para la trust-line que va debajo de cualquier CTA de lead magnet en banners, fichas Beehiiv, welcome flow, P.D. newsletter. Prohibiciones duras + default canónico.
type: feedback
originSessionId: 383a134e-9380-44b2-9a0b-a7aef3bbdef3
---
Todo CTA de lead magnet ROBOHOGAR (banner en artículo, ficha Beehiiv Digital Product, email welcome flow, P.D. newsletter) lleva debajo una **trust-line breve** que resuelve 3 objeciones del lector ES: (a) qué recibo, (b) me van a spamear, (c) cuánto me comprometo.

**Default canónico:** `PDF gratis con tu suscripción semanal. Cancela cuando quieras.`

**Prohibido:**
- Promesas de velocidad de entrega (`15 segundos`, `llega al email en`, `instantáneo`, `al momento`). No controlamos el delivery real de Beehiiv (30-90 s + riesgo filtro Promotions).
- Promesas de ausencia futura de publicidad (`sin publicidad`, `sin promociones`). Inconsistente con modelo (afiliados eventuales).
- Copy vago (`sin letra pequeña`, `sin trucos`). No resuelve objeción concreta.
- Hype anglosajón (`Join N+ readers`, `Don't miss out`, `Apúntate ya`). Incumple CTA no-spammy.

**Obligatorio — ≥2 de 3 elementos:**
1. Formato concreto del tangible (`PDF · 2 páginas`, `Checklist 7 preguntas`).
2. Baja fricción de salida (`te das de baja en un clic`, `baja cuando quieras`).
3. Transparencia del vínculo (`gratis` o `PDF + newsletter semanal`).

**Formato:** inline separado por `·`, minúsculas, sin punto final, ≤80 chars.

**Why:** incidente 2026-04-19 — generé el snippet oficial del banner (`content/templates/banner-lead-magnet.html` línea 36) con "te llega al email en 15 segundos" sin criterio propio ni investigación. Rafael me pidió auditar y rechazó el copy. Razones: (1) promesa incontrolable rompe confianza ANTES de abrir el PDF si Beehiiv tarda 45+ s; (2) suena a copy growth US traducido; (3) incumplí "verification first" del CLAUDE.md. El default canónico elegido (Opción B transparente con newsletter) prioriza deliverability (~0 spam reports en F1), consistencia con brand voice ("amigo techie sin hype") y cumplimiento GDPR/LOPDGDD + CTA no-spammy de Write With AI.

**How to apply:** aplicar SIEMPRE al generar copy para banners de artículo, ficha Beehiiv Digital Product "Qué pasa al descargarlo", emails de welcome flow (CTA al PDF) o P.D. de newsletter que promociona tangible. Validar con grep antes de commit:
```
grep -iE "15 segundos|llega al email en|instantáneo|al momento|sin publicidad|sin promociones|sin letra pequeña|join [0-9]|don.t miss|apúntate ya"
```
Si matchea → reescribir. El validator de `/pdf-brand` (`skills/pdf_brand/validators.py`) aplica la misma regex como bloqueo duro pre-export.

Regla documentada en: `c:\Users\bakal\robohogar\.claude\rules\tangibles.md § Microcopy de conversión`. Referenciada desde `.claude/commands/content-draft.md § 8.8` y `.claude/commands/pdf-brand.md § 6`. Evidencia best practices: `references/writewithai/extractions/ctas.md`, `references/writewithai/04-email-newsletter-patterns.md §§ 58-70`, `references/newsletter/email-marketing-playbook.md §13`.
