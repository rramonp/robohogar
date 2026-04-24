---
name: CTA suscripción final Ficciones Domésticas ROBOHOGAR
description: Ficciones cierran con snippet dark 5-elementos (eyebrow ROBOHOGAR · "¿Te ha gustado?" · "La próxima Ficción Doméstica, en tu correo." · botón Suscribirme · trust-line). Canon 2026-04-22.
type: feedback
originSessionId: 749cb54f-081c-4d7c-81a5-0a9108ab2b98
---
Toda Ficción Doméstica de ROBOHOGAR cierra con el snippet canónico CTA dark propio de ficción, distinto del CTA final de artículos no-ficción. HTML exacto y canon en `robohogar/.claude/rules/newsletter.md § Snippet canónico · banner suscripción al final de ficción`.

**Estructura (5 elementos fijos en orden):**
1. Eyebrow `ROBOHOGAR` (ámbar uppercase, letter-spacing, 11px).
2. Pregunta-gancho `¿Te ha gustado?` (20px DM Sans bold).
3. Título-promesa `La próxima Ficción Doméstica, en tu correo.` (20px DM Sans bold, línea propia).
4. Botón `Suscribirme` (1ª persona — distinto del `Suscribirse` infinitivo del CTA de artículo).
5. Trust-line `Newsletter gratis. Un email por semana. Cancela cuando quieras.` (12px, blanco, mismo texto que el CTA de artículo).

Todo centrado (`text-align:center`), fondo `#283642`, acento `#F5A623`, `href=https://robohogar.com` **sin UTM**.

**Diferencias deliberadas respecto al CTA de artículo no-ficción:**
- Ficción lleva eyebrow `ROBOHOGAR` + pregunta-gancho separada; artículo entra directo con la pregunta sin eyebrow.
- Ficción tiene título-promesa propio (`La próxima Ficción Doméstica...`), no "Cada semana...".
- Botón `Suscribirme` (1ª persona) vs `Suscribirse` (infinitivo). No mezclar.
- Trust-line idéntica en ambos (refuerza cadencia + salida fácil como señales de marca).

**Posición en el borrador de la ficción:** como snippet-block para pegar en Beehiiv vía `/html` → Custom HTML block, tras el bloque *"Lo real detrás del relato"*.

**Why:** Rafael 2026-04-22 tras probar visualmente el snippet viejo de ficción (3 elementos: eyebrow + frase + botón). El nuevo añade (a) pregunta-gancho `¿Te ha gustado?` que engancha emocionalmente al lector que acaba de terminar el relato, (b) trust-line al final que resuelve la objeción de spam/compromiso. El tamaño del título principal baja de 24px a 20px para que las dos líneas (pregunta + promesa) quepan visualmente sin romper jerarquía mobile.

**How to apply:**
- Al generar ficción con `/ficcion-draft` (manual o vía skill), insertar este snippet-block tras el bloque "Lo real detrás del relato" en el borrador HTML. No variar texto por relato — es bloque de marca consistente.
- Verificación pre-output: el HTML del banner debe contener las frases literales `¿Te ha gustado?`, `La próxima Ficción Doméstica, en tu correo.`, `Suscribirme`, `Newsletter gratis. Un email por semana. Cancela cuando quieras.` (4 greps).
- El CTA de artículo no-ficción ("¿Te ha servido este análisis?" + `Suscribirse`) **no sustituye** al de ficción. Ambos coexisten; cada canal tiene el suyo.
