---
name: feedback_ficcion_3_candidatos_composiciones_distintas
description: Cuando el skill de ficción propone 3 hero candidates, las 3 composiciones C-XX son SIEMPRE distintas — nunca 3 variantes de la misma cambiando solo objeto-imposibilidad o pose
type: feedback
---

Regla dura establecida por Rafael 2026-04-28 PM durante la generación del relato Pipo (one-shot Ficciones Domésticas).

**La regla:** cuando el skill `/ficcion-draft § 8.x Hero` (o `/nano-banana` modo ficción) propone los 3 candidatos de hero a Rafael, **las 3 composiciones C-XX deben ser totalmente distintas entre sí**. Prohibido proponer 3 variantes de la misma C-XX cambiando solo el objeto-imposibilidad, la pose del personaje o la luz secundaria.

**Why:** el valor editorial del paso "3 opciones" es **exploratorio**, no confirmatorio. Si el skill ya decidió que una C-XX concreta es la correcta y solo cambia detalles internos, Rafael no decide entre composiciones — solo entre matices de una. Pierde la oportunidad de comparar gramáticas compositivas distintas en thumbnail y de descubrir que una opción inesperada funciona mejor que la "obvia". Las 3 distintas obligan a Rafael a evaluar contraste real entre patrones del frame.

**Cita literal de Rafael (2026-04-28 PM):** *"cuando me das tres opciones, creo que sean tres opciones con composiciones totalmente distintas, no tres opciones prácticamente con composiciones idénticas con pequeñas diferencias muy sutiles"*.

**How to apply:**

- **Verificación pre-output del paso "3 candidatos":** comprobar que `len(set([c1.C, c2.C, c3.C])) == 3`. Si no, resamplear del pool hasta tener 3 C-XX únicos.
- **Ideal complementario** (no obligatorio, pero preferente cuando el pool lo permita): las 3 composiciones vienen además de **familias distintas** del catálogo C-01..C-12 (I Íntima · II Plano arquitectónico · III Frame-in-frame · IV Frontal/OTS · V Atmósfera/color-pop). Si las 3 son de familias distintas, contraste máximo. Si el pool no lo permite (filtros tonal + anti-repetición + banda lo restringen), aceptable que 2 compartan familia siempre que las 3 C-XX sigan siendo distintas.
- **Si el skill cree que una C-XX concreta encaja perfecto** con el relato (ej: C-05 eje simétrico altar para una escena ritual): aun así debe proponer 2 más de C-XX distintas para que Rafael vea el contraste. La C-XX "obvia" puede ser la elegida finalmente, pero la elección sale del comparativo, no del prejuicio del skill.
- Aplica al paradigma personaje-acción-imposibilidad (default desde 2026-04-26 PM) y al paradigma minimalista (cuando aplica). No aplica a series con código visual declarado (Amparo · Ronda 3 · MAIA), que mantienen su composición fija como sello de serie.

**Incidente origen — Pipo (2026-04-27 noche):** durante la generación del relato *Pipo*, el skill propuso 3 candidatos compartiendo todos C-05 (eje simétrico altar) + M5 (amanecer brumoso) + A4 (a través de marco), variando solo el objeto-imposibilidad (manos levitando · chispas escribiendo "Lucas" · hija sin cara extendiendo brazo). Rafael lo identificó al revisar y canonizó la regla de 3 composiciones distintas. Los 2 heros de Pipo que llegaron a generarse antes del feedback (C2 y C3, ambos C-05) quedan archivados como referencia; si Rafael decide regenerar 3 candidatos distintos para Pipo, la versión canónica será la nueva. Si decide quedarse con C-05 para este relato concreto, la regla aplica desde el siguiente.

**Canonización en repo (2026-04-28 PM):**
- `.claude/rules/editorial.md § Composición canon (C-01..C-12)` — bullet "Regla dura — los 3 candidatos son SIEMPRE 3 composiciones C-XX totalmente distintas".
- `.claude/commands/ficcion-draft.md § 6.bis` (paso de selección de composición) y `§ 9` (paso de propuesta a Rafael) — verificación `len(set(candidatos.C)) == 3`.
- `assets/branding/ficcion-hero-composiciones-canon.md § Reglas duras § 3.bis` — misma regla con verificación.
