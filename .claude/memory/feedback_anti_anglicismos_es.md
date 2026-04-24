---
name: Anti-anglicismos ES en copy ROBOHOGAR
description: Reglas validadas por research sobre 20 newsletters ES (2026-04-19) para evitar traducciones literales US que no encajan en ES editorial. Aplica a banners, trust-lines, emails, subjects, social, ficción.
type: feedback
originSessionId: 383a134e-9380-44b2-9a0b-a7aef3bbdef3
---
Research realizado 2026-04-19 sobre 20 newsletters ES de éxito (Kloshletter, Suma Positiva, Xataka, Genbeta, EOM, elDiario, Marketing4eCommerce, Newtral, Cincominutos, Ecotechers, Tendenci@s, Escribe, IA en Español, etc.). Detectó divergencias claras entre patterns US (Nicolas Cole / Write With AI) y patterns ES reales que saturan el knowledge base del repo ROBOHOGAR.

**Reglas duras resultantes (aplican a TODO copy visible al lector):**

1. **Saludos anglo prohibidos** (0/20 newsletters ES los usa): `Hola X,` + nombre · `Querido/a lector/a` · `Hey` · `Espero que estés bien` · `¿Qué tal la semana?`. Default ROBOHOGAR: entrada directa al tema o `Buenos días.` + primera frase.

2. **Cierres anglo prohibidos**: `Cheers` · `Best` · `Atentamente` como cierre de newsletter · `Saludos cordiales` (corporativo anglo traducido). `Un abrazo` aceptable solo en editorial/ficción personal, nunca en newsletter semanal.

3. **Persona gramatical**: `tú` imperativo al lector + plural editorial ("hemos", "os contamos", "nos parece") al hablar del medio. `vosotros` y `usted` vetados (0/20 apariciones).

4. **Subject line**: 20-45 chars, preferencia ≤35. La regla Cole ≤25 chars es US/EN monosilábico; fuerza copy raro en castellano. Rango ES real medido: Cincominutos 37 chars, Kloshletter 41, EOM 22-30.

5. **Verbo CTA**: `Suscríbete` / `Suscribirse` (61%) o `Apúntate` / `Apúntame` (28%). Prohibidos como botón principal: `Me apunto`, `Quiero recibir`, `Únete`, `Sign me up` — no aparecen en ningún landing ES serio.

6. **Microcopy trust-line**: punto final y frase > middots `·` (patrón ES > tech/SaaS US). Em-dash ` — ` con espacios en trust-lines ≤15 palabras prohibido (tic anglo). En titulares y prosa larga sí permitido.

7. **Palabra nuclear del producto**: `newsletter` (83%) > `boletín` (17% en medios tradicionales). `suscripción` como sustantivo standalone → 0% uso, evitar. `correo` solo como vector de entrega.

8. **"Tangible"**: jerga interna del pipeline ROBOHOGAR; nunca en copy visible al lector. Sustituir por "PDF gratis", "guía gratis", "descargable" o formato concreto ("checklist"). Excepciones permitidas: comentarios HTML internos, docs del repo, nombres de marca real (`TangibleFuture`).

**Why:** el knowledge base ROBOHOGAR está dominado por Write With AI (Nicolas Cole, US). Cada frase que acaba en un banner/email/tangible arrastra patterns US traducidos que el lector ES identifica como "esto huele a IA / marketer / blog americano". Research empírico confirma 0 apariciones de los anti-patterns listados en el 100% de los newsletters ES serios auditados.

**How to apply:**
- Skills que generan copy al lector aplican las 8 reglas como verificación pre-output: `/content-draft` § 9, `/ficcion-draft` § 8.2 (con excepción de diálogo de personaje), `/social-content` § Anti-anglicismos, `/pdf-brand` pre-export.
- Validator `skills/pdf_brand/validators.py` bloquea regex automáticamente: saludo_anglo_hola_nombre, saludo_anglo_espero_bien, saludo_anglo_querido_lector, saludo_anglo_hey, jerga_tangible_al_lector (15 patterns totales).
- Al consultar `references/writewithai/*.md` hay disclaimer README.md con tabla de divergencias US↔ES y pointer a `references/research-newsletters-es-2026-04-19.md`.

**Evidencia:** reporte completo en `c:\Users\bakal\robohogar\references\research-newsletters-es-2026-04-19.md` (20 filas · tabla cruzada de 6 touchpoints · glosario ES↔EN de 16 términos · propuestas de revisión validadas por Rafael 2026-04-19).
