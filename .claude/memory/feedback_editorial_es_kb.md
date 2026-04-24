---
name: Editorial ES KB — voz personal no-ficción cargada antes de generar copy
description: /content-draft y /social-content cargan references/editorial-es/ (4 archivos temáticos) antes de producir artículos, newsletter, banner, email, social. KB construido 2026-04-19 con 76 citas literales verificables de 28 referentes ES+LATAM peninsular dosificado 80/20. Eje central la voz personal de newsletters ES de éxito.
type: feedback
originSessionId: 202c8d1a-ac9b-4116-ac19-11c0c1a75e0e
---
**Regla.** Todo copy editorial no-ficción ROBOHOGAR (artículos largos, newsletter semanal, welcome emails, banners de lead magnet, CTAs, subjects, meta descriptions, social posts) debe pasar por el KB `references/editorial-es/` antes de entregarse — aplica los patrones de los referentes ES+LATAM auditados y la checklist pre-output §7 (artículos), §6 (newsletter y microcopy), §4 (social).

**Why.** Rafael reportó 2026-04-19 que los emails automatizados, banners y artículos ROBOHOGAR *"no tienen el toque personal que tienen los newsletters"* ES de éxito. El research en 15 newsletters + 7 columnistas + 13 periodistas/marcas ES extrajo 76 citas textuales verificables (URL pública) y canonizó 7 recursos de intimidad en [`references/editorial-es/02-newsletter-y-emails.md § 2`](../../robohogar/references/editorial-es/02-newsletter-y-emails.md): apertura por anécdota concreta con nombre propio (Suma Positiva) · humildad epistémica explícita (Error500) · cierre con nombre + cadencia (Kloshletter) · callback + numeración del issue (Kaizen, Causas y Azares) · pregunta propia obsesiva (Kaizen) · tagline-identidad recurrente (Suma Positiva) · reclamo humano *"escrito por personas, no por un algoritmo"* (Al día elDiario). La ausencia de estos recursos es lo que hace que el copy suene a LLM traducido del inglés — presencia de ≥4 en newsletter y ≥3 en artículo es el diferencial operativo.

**How to apply.**

1. **Skills que cargan el KB automáticamente** (hooks ya integrados 2026-04-19):
   - `/content-draft` paso 8.5 bis → [`01-articulos-y-columnas.md`](../../robohogar/references/editorial-es/01-articulos-y-columnas.md) + checklist §7. Paso 8.8 → [`03-microcopy-ctas-meta.md`](../../robohogar/references/editorial-es/03-microcopy-ctas-meta.md) §5 para copy del banner.
   - `/social-content` paso 2 → [`04-social-posts.md`](../../robohogar/references/editorial-es/04-social-posts.md) + §2 de `02-newsletter-y-emails.md`.

2. **Piezas manuales fuera de skills** (welcome flow, newsletter semanal escrito a mano): cargar [`02-newsletter-y-emails.md`](../../robohogar/references/editorial-es/02-newsletter-y-emails.md) explícitamente antes de redactar. Checklist §6 obligatoria pre-envío.

3. **Referentes canónicos del nicho aspirador ROBOHOGAR**:
   - **Eva R. de Luis (Xataka)** para reviews — hook con subordinada + pero, veredicto segmentado por perfil (*"sería el modelo que recomendaríamos a [perfil de hogar + mobiliario + suelo]"*), puentes orales ES (*"en honor a la verdad"*, *"letra pequeña"*).
   - **Antonio Ortiz (Error500, Causas y Azares)** para editoriales — *"sospechamos"* como humildad epistémica, callback *"Empezamos con lo más leído de la edición anterior"*.
   - **Holaluz / Doctoralia** para microcopy — inversión del imperativo (*"Enviádmelo al correo"* > *"Descargar gratis"*) + datos no redondeados (*"42 robots analizados · 6 finalistas"*) + microcopy post-CTA específico.
   - **Kloshletter** para cierre newsletter — *"Te escribo mañana. Carlos"* adaptado al plural: *"Te escribimos el martes que viene. — ROBOHOGAR"*.

4. **Cuando detectes prosa propia que suena "plana" o LLM-like**: recurrir al KB primero, no reescribir de memoria. Los patrones son específicos y contextuales — aplicar §2.1 apertura por anécdota en un welcome email es distinto a aplicarla en un subject de 30 chars.

5. **Correcciones de autoría documentadas en el research (evitar errores en futuras menciones)**: Suma Positiva = Samuel Gil (NO David Bonilla, que firma *Bonilista*). Causas y Azares = Antonio Ortiz (NO Ramón González Férriz). Kloshletter = Charo Marcos + Carlos Molina (NO Cris Carrasco).

6. **Caso canónico de aplicación validado**: [`content/drafts/2026-04-19-aplicacion-kb-editorial-banner-y-welcome.md`](../../robohogar/content/drafts/2026-04-19-aplicacion-kb-editorial-banner-y-welcome.md) — banner Hoja de Compra pasó de 1/6 a 5/6 recursos positivos; welcome email 1 pasó de 0/7 a 6/7 recursos §2. Si se aprueba A/B test, canonizar v2 como default.

**Herencia y no duplicación.**
- El KB construye sobre `rules/editorial.md`, `rules/newsletter.md`, `rules/tangibles.md`, `anti-ia-checklist.md §1 Universal` y `docs/brand-voice.md` — NO los sustituye. La anti-IA filtra tics LLM universales; el KB aplica patrones ES concretos con muestras textuales.
- No aplicable a ficción — ficción tiene su propio KB en `references/ficciones/castellano-literario-es.md` + memoria [`feedback_ficcion_castellano_literario.md`](feedback_ficcion_castellano_literario.md). Son capas hermanas, cada una con sus referentes.
- El validator regex de `skills/pdf_brand/validators.py` cubre anti-patterns duros (velocidad, sin publicidad, hype). El KB añade **patrones positivos** (qué SÍ hacer).

**Iteración futura (F2).** Research dedicado a social posts ES con muestras reales (cuentas tech con voz editorial — Xataka, Peirano, Ortiz, Carrión en X/LinkedIn) para canonizar §1 del `04-social-posts.md` con muestras literales en lugar de extrapolaciones actuales.

---

## REGLA DURA DE HONESTIDAD EN COPY — INCIDENTE 2026-04-19 (crítica)

Durante el cierre del KB, al proponer el snippet landing para la Hoja de Compra, propuse dos veces frases que sonaban bien pero eran **falsas verificables**:

1. ❌ *"Probamos los robots, los desmontamos, los comparamos en casa"* — falso para humanoides y aspiradores caros que Rafael no posee.
2. ❌ *"Las destilamos tras meses cubriendo este nicho"* — falso: newsletter reciente con artículos de 1-2 semanas, no hay "meses" verificables.
3. ❌ *"42 robots analizados en 2025. 6 finalistas"* — falso: cifra inventada sin respaldo.

Rafael rechazó las tres literal: *"estoy cansado de que siempre te inventes cosas que son mentiras para quedar bien. Podemos conseguir el mismo efecto diciéndolo de otra manera, sin quedar como mentirosos"*.

**Regla dura permanente (canonizada en `references/editorial-es/02-newsletter-y-emails.md § 2.7`).** Aplica a TODA afirmación factualmente verificable en copy público (trust-line, subtítulo banner, meta description, bio, about, welcome email, newsletter), no solo al reclamo humano:

**Vector 1 — hands-on.** Prohibido afirmar *"probamos"* / *"desmontamos"* / *"en casa"* cuando el catálogo incluye humanoides o robots caros que no se poseen. Fórmula canónica aceptada: *"Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre."*

**Vector 2 — temporal.** Prohibido *"tras X meses"* / *"llevamos años"* / *"desde 20XX"* si la publicación es reciente. Verificación: contrastar fecha real de arranque antes de aprobar cualquier marcador temporal.

**Vector 3 — volumétrico.** Prohibido cifras de suscriptores, modelos analizados, horas probando, sin dato real verificable en backend. Si no hay dato → eliminar cifra, no inventar.

**Verificación pre-output OBLIGATORIA de 3 preguntas por cada línea de copy con afirmación factual:**
1. ¿Es verdad al 100% del alcance implícito? (Si implícitamente aplica a "todos los robots de ROBOHOGAR", ¿cubre humanoides?)
2. ¿El marcador temporal contrasta con la fecha real del proyecto?
3. ¿La cifra corresponde a backend/datos verificables o la invento para que cuadre?

Si cualquier respuesta es "no" → eliminar afirmación o reescribir con humildad del alcance, NUNCA suavizar sin cambiar la sustancia mentirosa.

**Principio.** El copy persuasivo ES de calidad (Filmin, Holaluz, Doctoralia) nunca sobrepromete hands-on ni tiempo acumulado; convierte resolviendo objeciones concretas con datos verificables, no inflando el relato. Al día elDiario (*"escrito por Juanlu Sánchez, subdirector de eldiario.es (no por un algoritmo)"*) es el modelo: verdad literal verificable, cero inflación.

**Instrucción operativa.** Si al escribir copy me sale una frase que "queda bien pero puede sonar a mentira" — detenerme, aplicar las 3 preguntas de verificación, y si alguna falla, reescribir desde cero eliminando la afirmación problemática en vez de suavizarla. Mejor 4 recursos §2 verdaderos que 7 con una mentira.
