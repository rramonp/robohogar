# Editorial Rules

## Voz y Tono

- **Tono:** Cercano, informado, con humor sutil. Como un amigo techie que te explica qué robot merece la pena
- **Persona:** Entusiasta de la tecnología doméstica, no vendedor. Opiniones propias, no comunicados de prensa
- **Audiencia:** Adultos 30-55, España, interesados en tecnología pero no necesariamente técnicos
- **Registro objetivo: prosa llana ES habitual, sin florituras** (regla dura 2026-04-28). La voz ROBOHOGAR es la del periodismo tech ES de andar por casa (Eva R. de Luis Xataka, Antonio Ortiz Error500), NO la del articulista literario. Cero metáforas culturales rebuscadas (*"matemáticas de cuarto de la ESO"*, *"depende de cuánto vale tu sábado"*, *"que no te hace ningún comercial"*), cero em-dashes decorativos como remate ingenioso, cero giros que requieran releer una frase para descodificar. Si un párrafo necesita defenderse con *"es que está bien escrito"* o *"es ingenioso"* → reescribir plano. Test del párrafo bueno (canónico, validado por Rafael 2026-04-28): *"Para saber si te compensa un robot cortacésped solo hacen falta cuatro datos. Lo difícil no es hacer la cuenta, es hacerla en el orden correcto: primero tu situación, después el robot."* — sujeto+verbo+complemento, sin inversiones, cero "trying to be clever". Detalle completo + tabla 10 patrones ❌→✅: [`feedback_robohogar_estilo_llano.md`](../memory/feedback_robohogar_estilo_llano.md). Aplica a no-ficción (review, comparativa, guía, editorial, tutorial, newsletter); ficción tiene reglas distintas (prosa peninsular literaria).

## Estructura de artículos

1. Hook directo (1-2 frases que enganchan)
2. Contexto breve (por qué importa)
3. Desarrollo con opinión propia
4. Cierre con takeaway claro o CTA suave

## Reglas de contenido

- NUNCA copiar/pegar texto de fuentes — siempre reescribir con voz propia
- Citar fuentes cuando se usen datos específicos
- **Voz de autoridad propia — NUNCA narrar el proceso de investigación en el texto publicado.** Formas prohibidas en hooks, aperturas, cuerpo o cierre: *"hemos leído X, Y, Z newsletters"*, *"contrastado con A, B, C medios"*, *"nos hemos metido en 10 reviews internacionales"*, *"hemos recopilado toda la información de…"*. Queda cutre — da la impresión de agregador sin tesis propia. Las fuentes externas se citan SOLO como autoridad puntual de un dato concreto (*"Xataka Home lo confirma: el vapor va a las mopas"*) o como hipertexto contextual en un párrafo (*"según [Vacuum Wars](url), el brazo acierta la mitad de las veces"*). La tabla completa de fuentes vive en `PASOS.md`, no en el artículo publicado. Regla ampliada con incidente de origen: memoria `feedback_article_voice_authority.md`.
- Incluir siempre al menos 1 opinión/valoración personal por artículo
- Evitar superlativos vacíos ("revolucionario", "increíble", "game-changer")
- Usar "tú" (no "usted") — registro informal pero profesional
- Primera persona SIEMPRE en plural: "hemos investigado", "os contamos", "nos parece". NUNCA singular ("he investigado", "te cuento"). La voz de marca es plural (equipo/medio), no personal (blog de un tío). Excepción: la bio de Rafael en "Sobre el autor" puede usar singular
- **Registro de trato prohibido:** *usted* y *vosotros* (2ª persona plural) NUNCA. Validado contra 20 newsletters ES de éxito (Kloshletter, Suma Positiva, Xataka, EOM, elDiario, etc.) — 0 apariciones de ambos. Default ROBOHOGAR: *tú* imperativo al lector + plural editorial ("hemos") al hablar del medio.
- Robots se refiere siempre a robótica DOMÉSTICA (aspiradores, cortacésped, humanoides para hogar)

## Curse of knowledge — check pre-output

Concepto de Steven Pinker (*The Sense of Style*, Harvard): *"the difficulty that we all have in knowing what it's like not to know something that we know"*. El autor que conoce su tema asume contexto que el lector no tiene. Resultado: frases que para el autor son obvias pero el lector no puede seguir.

**Regla ROBOHOGAR.** Antes de cerrar el borrador, releer preguntando: *"¿qué estoy asumiendo que el lector ES 30-55 sabe sin estar en el texto?"*. Prohibido dar por sabido en primera mención:

- **Acrónimos sin expandir:** `LiDAR`, `ToF`, `PVP`, `AI Act`, `CE`, `ICAM`, `LDS`, `IA`, `SmartThings`, `Matter`, `ROI`, `RTK`, `EPOS`, `OTA`, `IoT`, `LLM`, `B2B`, `B2C`, `KPI`, `CTR`, `CPM`, `SaaS` → expandir o contextualizar la primera vez. **Aplica con especial dureza a acrónimos anglo de business/finance/marketing** (ROI, KPI, B2B, CPM, CTR, SaaS): el lector ROBOHOGAR (30-55 ES, interesado en robótica doméstica, no necesariamente del mundo finance/marketing) NO los decodifica de oficio, y un texto plagado de ellos canta a "blog corporativo traducido del inglés". **Mejor sustituir** que expandir entre paréntesis: `ROI` → *rentabilidad* / *retorno de la inversión* / *amortización*; `KPI` → *indicador principal*; `B2B` → *de empresa a empresa*; etc. Ejemplos:
  - ❌ *"Usa LiDAR para mapear"* → ✅ *"Usa LiDAR (sensor láser de 360°) para mapear"*.
  - ❌ *"Conforme al AI Act"* → ✅ *"Conforme al AI Act (reglamento europeo de IA, en vigor desde 2024)"*.
  - ❌ *"Calculadora ROI ROBOHOGAR"* / *"La cuenta del ROI no es complicada"* → ✅ *"Calculadora de rentabilidad ROBOHOGAR"* / *"La cuenta de la rentabilidad no es complicada"*. Si el SEO obliga a usar `ROI` en algún sitio (poco probable — la keyword ES dominante es *rentabilidad*), reservar el acrónimo SOLO para frontmatter SEO oculto, jamás en cuerpo visible al lector.
  - ❌ *"El KPI principal es la conversión"* → ✅ *"El indicador principal es la conversión"*.
  - **Regla operativa de descarte:** preguntarse *"¿usaría este acrónimo un fontanero, un profesor de instituto o una madre de 45 años en el chat de WhatsApp del barrio?"*. Si la respuesta es no → traducir o expandir.
  - **Incidente origen 2026-04-28** (artículo *robot-cortacesped-rentabilidad-3-anos* borrador #14): se metieron 5 menciones de "ROI" en cuerpo + subtítulo asumiendo que el lector lo decodifica de oficio. Rafael lo detectó al revisar el subtítulo (*"¿Qué significa ROI ROBOHOGAR?"*). Fix: sustituido en todo el cuerpo por *"calculadora de rentabilidad"* y *"la cuenta de la rentabilidad"*. La keyword SEO `robot cortacésped rentabilidad` y el SEO title del artículo ya usaban *rentabilidad* desde el inicio — el body se desviaba al anglo sin razón.
- **Nombres de modelo sueltos sin categoría:** al presentar un robot por primera vez, dar marca + modelo + categoría + año. Ejemplos:
  - ❌ *"El X50 Ultra es el ganador"* → ✅ *"El Dreame X50 Ultra, aspirador de gama alta 2026, es el ganador"*.
  - ❌ *"Qrevo Curv 2 tiene rodillo nuevo"* → ✅ *"El Roborock Qrevo Curv 2 (top 2026 de la marca) tiene rodillo nuevo"*.
- **Jerga de reviews en inglés sin traducir:** `mopping`, `auto-empty`, `auto-wash`, `multifloor mapping`, `edge cleaning` → usar equivalente ES o traducir entre paréntesis la primera vez.
  - ❌ *"El auto-wash funciona bien"* → ✅ *"El autolavado de mopas funciona bien"*.
  - ❌ *"Hace mopping con vapor"* → ✅ *"Friega con vapor"*.
- **Conceptos regulatorios o técnicos sin contexto:** homologación CE, protocolo Zigbee, banda 2.4 GHz, tarifa PVPC → 1 línea de contexto si el lector no tiene por qué saberlo.

**Verificación.** Si un vecino de 55 años, interesado en tecnología pero no técnico, no entendería una frase al primer pase, reescribir. No es infantilización: es claridad.

**No aplica a segundas menciones.** Una vez expandido en primera mención, el siguiente uso puede ir abreviado. *"El Dreame X50 Ultra (gama alta 2026) es el ganador. El X50 sube umbrales mejor que el Roborock."* — OK. El lector ya lo tiene contextualizado.

**Alcance por tipo de contenido:**
- **Artículos (reviews, comparativas, guías, editoriales):** aplica todo — acrónimos, nombres de modelo con marca + categoría + año, jerga anglo, regulación.
- **Ficción (prosa narrativa del narrador):** aplica solo a acrónimos/jerga/regulación. **NO usar nombres de modelo comerciales reales** — eso es otra regla distinta (`§ Narrativa especulativa — SIN MARCAS COMERCIALES`). Los ejemplos de contextualización para ficción usan categorías genéricas ("el aspirador", "el humanoide") o personajes del canon ROBOHOGAR (Tico, Hugo, Eva, RONDA-3, MAIA).
- **Diálogo de ficción:** se relaja — un personaje puede hablar con la jerga que le toque sin explicar. Es verosimilitud.

Heredado por `/content-draft § 9 Prohibiciones` y `/ficcion-draft § 8.2`.

## Apertura y cierre del cuerpo del email — anti-anglicismos

Auditoría 2026-04-19 de 20 newsletters ES de éxito detectó 0 uso de estos patterns anglo traducidos. Prohibidos en cualquier email, intro de artículo, post social o copy visible al lector:

- **Aperturas prohibidas:** `"Hola X"` + nombre · `"Hola amigo/a"` · `"Querido/a lector/a"` · `"Hey"` · `"Espero que estés bien"` · `"¿Qué tal la semana?"` · `"Hope you're well"` traducido en cualquier forma.
- **Cierres prohibidos:** `"Cheers"` · `"Best"` · `"Saludos cordiales"` (registro corporativo anglo) · `"Atentamente"` al cierre de newsletter.
- **Default ROBOHOGAR apertura:** entrada directa al tema sin saludo, o `"Buenos días."` + primera frase (patrón Kloshletter/medios ES). En ficción se aplican excepciones de diálogo (ver `/ficcion-draft`).
- **Default ROBOHOGAR cierre:** firma institucional ("ROBOHOGAR") + tagline opcional. `"Un abrazo"` aceptable solo en editoriales/ficciones personales, nunca en newsletter semanal estándar.
- **Em-dash (`—`) en trust-lines ≤15 palabras** (bajo botón, bajo subtítulo, OG description): prohibido. Es tic anglo (`" — "` con espacios). Usar coma, punto o dos puntos. En titulares de artículo y prosa del cuerpo sí está permitido.

Referencia completa: `@references/research-newsletters-es-2026-04-19.md`. Skills que generan copy al lector (`/content-draft`, `/ficcion-draft`, `/social-content`, `/pdf-brand`) aplican esta regla como verificación pre-output. El validator de `/pdf-brand` (`skills/pdf_brand/validators.py`) bloquea los patrones listados con regex.

## Formato técnico (Beehiiv)

- **Tipografía global (config Beehiiv → Settings → Theme → Typography):** headings H1/H2/H3/H4 en **DM Sans Semibold (600)**, body en **Inter Regular (400)**. Beehiiv aplica este estilo al renderizar; los borradores generan Markdown/HTML semántico plano (sin forzar fuentes inline). El cambio Bold → Semibold (validado 2026-04-26) reduce la sensación de "headings que gritan" y mantiene jerarquía visual suficiente; el peso del heading sigue prohibiendo `<strong>`/`**` interno (regla siguiente: política de negritas).

- **Política de negritas (DURA — OBLIGATORIA).**

  **✅ Permitido — negrita en párrafos de texto corrido** (intro, desarrollo, callouts `.callout-amber` / `.callout-gray`, notas, bullets fuera de `.checklist`): usar **siempre `<strong>`**, nunca `<span class="bold">` ni `style="font-weight"` inline ni `<b>`. Razón completa en el bullet siguiente.

  **❌ PROHIBIDO — BOLD NUNCA dentro de headings ni tablas ni callouts crema:**
  - **Headings H1/H2/H3/H4** (incluye emojis prefijo tipo `<h2>🏆 Nuestro veredicto</h2>` — el heading entero YA tiene peso semibold (600) por config global Beehiiv → Theme → Typography; cualquier `<strong>`/`<b>`/`**...**` dentro duplica el peso y rompe la sensación visual buscada).
  - **Tablas `<thead>`**: nunca en bold (Beehiiv estiliza el thead con su font-weight). En `<tbody>`: solo la **columna 1** (etiqueta de fila) puede ir en `<strong>` para anclar escaneo móvil; columnas 2+ siempre regular.
  - **Recuadros checklist** (div `.checklist` con fondo crema `#FFF9EF` + borde `#F5A623`): items en peso regular. Nunca `<li><strong>...</strong>` ni `<li>**...**</li>` dentro de `.checklist`.
  - Nunca `## **Título**` en Markdown, nunca `<h2><strong>...</strong></h2>` en HTML. Al copiar de fuentes externas, limpiar bold embebido antes de publicar.

  **Verificación pre-output (OBLIGATORIA antes de cerrar borrador):**

  ```bash
  # (a) Bold dentro de headings → debe ser 0
  grep -nE '<h[1-4][^>]*>[^<]*<(strong|b)\b' <borrador.html>

  # (b) Bold markdown dentro de headings → debe ser 0
  grep -nE '^#{1,4} .*\*\*' <borrador.html>

  # (c) Bold dentro de thead → debe ser 0
  grep -nE '<thead>.*<(strong|b)\b' <borrador.html>

  # (d) Bold dentro de .checklist → debe ser 0
  grep -nE 'class="checklist"[^>]*>.*<(strong|b)\b' <borrador.html>
  ```

  Si alguno devuelve matches → reescribir antes de entregar. Regla heredada por `/content-draft` (paso 8.5) y `/ficcion-draft` (paso 8.5).

- **Negritas en párrafos — usar SIEMPRE `<strong>`, NUNCA `<span class="bold">`.** Regla dura 2026-04-19 tras incidente de Rafael: al hacer copy-paste de `<span class="bold">X</span>` del borrador a Beehiiv, Chrome traduce el CSS computado de la clase `.bold` a un inline `style="font-weight: bold"`. Beehiiv aplica su propio bold encima → **doble peso visible**. Cuando Rafael selecciona el texto en Beehiiv y pulsa B, el editor sustituye por `<strong>` semántico y el peso se normaliza — pero es engorroso tener que hacerlo en cada párrafo.

  **Solución:** los borradores usan `<strong>` directamente. Los editores WYSIWYG mapean `<strong>` 1:1 al Bold nativo sin arrastrar inline styles. Al copy-paste funciona a la primera.

  **Consecuencia en el CSS de los borradores:** NO incluir la regla `.bold { font-weight: bold; }` en el `<style>` del borrador. El `<strong>` nativo del navegador ya se ve bold en preview sin clase adicional.

  **Migración de borradores existentes** (aplicada 2026-04-19 a: master · mejor-robot-aspirador-2026 · humanoides-en-casa-cuanto-falta · roborock-saros-z70-review · samsung-jet-bot-steam-ultra-review): `sed -i -E 's|<span class="bold">([^<]*)</span>|<strong>\1</strong>|g'` + eliminar la línea `.bold { font-weight: bold; }` del `<style>`.

  **Verificación pre-output:** `grep -c 'class="bold"' <borrador.html>` → debe ser 0. Si >0, sustituir por `<strong>` antes de entregar.
- **Separador `---` entre productos en comparativa — OBLIGATORIO** (regla dura 2026-04-26). En artículos de comparativa, guía de compra, review multi-producto o editorial que analice productos concretos uno tras otro, **cada bloque de producto** (`<div class="model-card">` en HTML / `### Marca Modelo — claim` en Markdown) va seguido de un separador horizontal antes del siguiente. En `.md` es `---` en línea propia con líneas vacías arriba y abajo. En `.html` es `<div class="separator"></div>` o `<hr>`. Razón: en mobile, los model-cards consecutivos sin separador se leen como una pared de texto continua y pierdes la pausa visual que indica "este producto cierra, viene el siguiente". Verificación pre-output: en borradores con N model-cards, contar separadores `---` o `<div class="separator">` entre ellos — debe haber al menos N-1. El separador final tras el último producto antes del siguiente H2 también cuenta.

- **Bloque "Más en ROBOHOGAR" / "Keep Reading" — PROHIBIDO incluir manualmente** (regla dura 2026-04-26). Beehiiv inyecta automáticamente bajo cada post un bloque "Keep Reading" con los 3 posts más recientes de la publication. Cualquier `<p><strong>Más en ROBOHOGAR:</strong></p>` + `<ul>` con internal links al final del borrador duplica el bloque automático y ensucia el cierre. **NO incluirlo en borradores nuevos.** Internal linking sigue siendo válido **dentro de la prosa** del artículo (callouts, comparativas, menciones cruzadas) — lo que se elimina es la lista al final. Borradores históricos publicados antes de esta regla quedan como están (no re-editar lo ya pegado en Beehiiv). Verificación pre-output: `grep -niE 'Más en ROBOHOGAR|Keep Reading' <borrador.html>` → debe ser 0.

- **Tablas — mobile-first (≥50% lectores en móvil).**
  - **Máximo 4 columnas.** Si una comparativa pide más, o (a) se recortan a las 4 más críticas y el resto va en prosa del cuerpo, o (b) se parte en 2 tablas temáticas.
  - **Texto corto por celda: ≤25 caracteres orientativo** (2-3 palabras). Nada de paréntesis largos dentro de la celda — ese matiz va al caption o al cuerpo.
  - **Nombres de producto cortos:** marca + modelo en 2-3 palabras ("Ecovacs X8 Pro Omni", no "Ecovacs Deebot X8 Pro Omni"). Año entre paréntesis en `<em>` si es imprescindible, con `<br>` para salto.
  - **Valores con unidad pegada sin espacio** cuando sea posible ("100°C" no "100 °C", "1.399€" no "1.399 €") — ahorra wrap feo.
  - **Sin specs secundarias:** potencias, dimensiones, sensores concretos y parentéticos de disclaimer van en prosa, no en celdas.
  - **Validación obligatoria:** contar `<th>` del `<thead>` antes de entregar — si son >4, recortar. Referencia en vivo: tabla de [`content/articulos/mejor-robot-asistente-ia-2026/borrador.html`](../../content/articulos/mejor-robot-asistente-ia-2026/borrador.html) (4 cols, cells cortas, render OK en 375px).

## Newsletter (semanal)

- 3-5 noticias curadas con comentario editorial
- 1 sección fija rotativa (review, comparativa, tutorial, opinión)
- Máximo ~1500 palabras por issue
- Subject lines: cortas, curiosas, sin clickbait

## Narrativa especulativa — Ficciones Domésticas

Pilar experimental (~10% del content mix). Relatos cortos de ciencia ficción doméstica próxima (2030-2040) con personajes recurrentes. Reglas que RELAJAN explícitamente la voz baseline:

- **Voz (excepción a la regla de primera persona plural):** en ficción se usa narrador omnisciente en 3ª persona O primera persona del personaje POV. El "hemos/os/nos" plural editorial NO aplica dentro del relato
- **Tiempo verbal:** presente (inmediatez) o pasado (reflexión). No mezclar en la misma escena sin justificación narrativa
- **Longitud:** flash 500-800 palabras · episodio-serie 1.200-1.800 · standalone web 2.500-3.500 · mini-serie 6-12 episodios. Actualizado 2026-04-18 al consenso Substack 2025 — ver `@references/ficciones/serialized-newsletter-patterns.md` § 3.1
- **Cadencia:** hasta 1 cada 1-2 semanas, **condicionada a evergreen-first** (ficción solo sale si el evergreen SEO de la semana está entregado). Pivote 2026-04-20 de "distribución activa" a "sprint evergreen SEO": la ficción aporta variedad editorial y diferenciación de marca, no tráfico orgánico; por eso no puede canibalizar el motor de crecimiento. Backlog 22 historias validadas en `content/calendario-editorial.md § Backlog tonal` soporta este ritmo con sobra. Detalle del pivote: memoria `feedback_seo_first_pivote.md`
- **Tag visual:** "Ficciones Domésticas" + hero estilo still cinematográfico (NO product-hero). Referencia: Black Mirror doméstico, After Yang, Her
- **Obligatorio:** anclar cada relato en ≥1 dato real (AI Act, INE, spec técnica de un robot que existe). Sin dato real → fantasía genérica, se rechaza
- **Villano:** el robot NUNCA es el villano. El villano es el problema humano (soledad, burnout, brecha digital) que el robot revela o amplifica
- **Exención:** palabras "prohibidas" de la línea baseline (superlativos) permitidas solo en diálogo irónico de un personaje
- **Composición ES directa — no traducir del inglés** (incidente 2026-04-20): la prosa de ficción se compone en castellano peninsular literario desde el primer token. Prohibido pensar una frase en inglés y traducirla, y prohibido usar plantillas narrativas anglosajonas traducidas. La fuente de verdad del knowledge ES (17 calcos con grep + 12 recursos ES positivos + 10 referentes ES peninsulares + 5 casos canónicos del incidente origen) es [`references/ficciones/castellano-literario-es.md`](../../references/ficciones/castellano-literario-es.md) §§ 3, 3.bis, 4, 8.1. El skill `/ficcion-draft` carga ese knowledge obligatoriamente y corre los 17 greps pre-output (ver `.claude/commands/ficcion-draft.md § 8.3`). Si un grep devuelve match ambiguo (calcos 14, 15 o 17 dependen del contexto), LEER LA FRASE EN VOZ ALTA — el oído peninsular es el filtro definitivo. Memoria del incidente: `feedback_anti_calcos_lexicos_es.md`.
- **SIN MARCAS COMERCIALES REALES de ROBÓTICA DOMÉSTICA en la prosa del narrador.** Rechazado por Rafael 2026-04-19 con palabras literales: *"mezclar Dreame X50 con historias reales = creepy. Quiero buenas novelas cortas con temática inversión de Black Mirror, no una promo glorificada que no me da ningún rédito"*.
  - **Alcance exacto**: categorías de producto que ROBOHOGAR analiza comercialmente en artículos — **aspiradores-robot, humanoides domésticos, cortacéspedes-robot, fregasuelos, limpia-cristales, mascotas robot, drones domésticos, brazos robóticos de cocina**. Marcas concretas vetadas en narrador: `Dreame | Roborock | Ecovacs | Cecotec | Xiaomi | iRobot | Roomba | Mova | Eufy | Dyson | Neato | Samsung (Bespoke Jet Bot) | LG (CordZero) | Philips (Homerun) | Unitree | 1X | Figure | Agility | Apptronik | Neura | Sanctuary | Kawasaki | Tesla Optimus | Loona | LOOI | Aibo`.
  - **NO aplica** a marcas de electrodomésticos no-robóticos ni móviles/TVs que aparecen como **caracterización del personaje** (el móvil viejo de una yaya, la lavadora de siempre, el Roomba que el tío tenía en 2015 antes de la acción). Eso es prosa cotidiana ES, no promo. Validado 2026-04-19 sobre el Samsung A13 de Amparo en `content/ficciones/la-casa-de-amparo/character-bible.md`.
  - ✅ **Permitido en narrador**: robots **genéricos** ("el aspirador doméstico", "el humanoide de cuidados", "el cortacésped del patio"), **ficticios del canon ROBOHOGAR** (Tico aspirador IA, Hugo humanoide, RONDA-3 utility, Eva humanoide, MAIA IA epistolar), **marcas inventadas** canonizadas en la bible de la serie (ej: "el modelo SVA-12" si se ha establecido).
  - ✅ **Excepción en diálogo**: un personaje puede mencionar una marca real de robótica **una sola vez por escena** si es verosímil en su boca (un yayo diciendo "el Roomba de toda la vida"). Nunca en cadena, nunca en el narrador.
  - ✅ **Referencia económica implícita permitida**: *"la Casa de Amparo tiene un humanoide que una familia media no podría pagar"* — contexto socioeconómico sin hacer promo.
  - ❌ **Prohibido** que la prosa del narrador use un modelo comercial real de las categorías de arriba como "personaje", decorado o ficha técnica. Si un relato necesita "cómo de potente es el aspirador", se inventa fisiología ficticia o se usa categoría genérica — nunca número de modelo real.
  - **Verificación pre-output**: grep sobre `content/ficciones/**/*.md` (fuera de bloques entre comillas o guiones largos de diálogo) contra la lista de marcas de arriba → 0 matches. Si matchea, reescribir como genérico o ficticio canon. El Samsung/Apple/LG de móviles/TVs como caracterización del personaje queda exento si aparece como objeto de contexto, no como producto en acción.

- **Nombres propios de robots y asistentes IA: siempre ficticios.** Refuerzo Rafael 2026-04-19: *"si los robots tienen nombres deben ser ficticios, no de productos reales"*. Los protagonistas, secundarios o robots de fondo con nombre propio llevan nombre **inventado para ROBOHOGAR**, nunca marca real.
  - ✅ **Canon activo**: Tico (aspirador IA), Hugo (humanoide La Casa de Amparo), RONDA-3 (utility humanoide), Eva (humanoide familia Cortés), MAIA (IA epistolar Cartas a MAIA). Todos inventados.
  - ✅ **Nombres permitidos en relatos nuevos**: cualquier nombre ficticio que no coincida con asistente IA real ni marca comercial.
  - ❌ **Prohibido como nombre de robot/IA del relato**: `Alexa | Siri | Cortana | Bixby | Google Assistant | ChatGPT | Claude | Gemini | Copilot | Grok | Llama | Mistral | Perplexity | Aibo | Loona | LOOI | Atlas | NAO | Pepper | Ameca | Digit`.
  - **Excepción en diálogo**: un personaje puede decir *"le pregunto a Alexa"* una sola vez por escena para verosimilitud cotidiana. Jamás el robot protagonista SE LLAMA Alexa.
  - **Modelos ficticios canon ROBOHOGAR** (series-bible-maestra): HOGAR-X de Doméstica Ibérica, KIKI de Toyminds Barcelona, SVA-12, etc. Si una serie nueva necesita un nombre/modelo, se canoniza en la bible antes de usarlo.

- **Cliffhanger:** emocional o moral, NUNCA físico primario (incoherente con "robot = instrumento neutro"). Detalle: `@references/ficciones/serialized-newsletter-patterns.md` § 3.4.

- **Intensidad narrativa — DEFAULT CINEMATOGRÁFICO** (regla dura 2026-04-26 PM tarde tras feedback Rafael: *"todos los relatos parecen iguales… aquí no ha ocurrido nada y siempre parece que aquí no ha pasado nada. Necesito que pasen cosas en los relatos. Audionovelas en un newsletter de gente acostumbrada a vídeos de YouTube, etcétera. Por defecto quiero que ocurran más cosas."*). Eje **independiente** de la categoría tonal: un relato puede ser inquietante Y cinematográfico, o inquietante Y atmosférico — son ejes distintos. Catálogo canon en [`@references/ficciones/intensidad-narrativa.md`](../../references/ficciones/intensidad-narrativa.md):
  - 🎬 **Cinematográfico** — **40% del catálogo · DEFAULT** · ≥5 eventos significativos · cierre con cliffhanger fuerte que el lector NECESITA resolver · ritmo alto adaptado a oyente acostumbrado a YouTube/TikTok.
  - ⚡ **Dinámico** — 35% · 3-4 eventos significativos · cliffhanger explícito.
  - 🌫️ **Atmosférico** — 20% · 1-2 eventos significativos · siembra + ambigüedad. (Lo que era el default histórico — limitado al 20%.)
  - 🍵 **Slice of life** — 5% · 0-1 eventos significativos · plano sostenido. Reservado a cierres de saga, despedidas, viñetas evocativas.
  - **Definición de "evento significativo"** + tests operativos: [`intensidad-narrativa.md § 2`](../../references/ficciones/intensidad-narrativa.md). Resumen: ✅ acción que cambia el estado del mundo del relato (alguien gana/pierde, decide, hace algo irreversible, recibe noticia que cambia el escenario, encuentra a alguien). ❌ NO cuenta: descripción atmosférica pura, recuerdo, observación interior, gesto cotidiano repetido.
  - **Frontmatter obligatorio**: campo `intensidad-narrativa: <Cinematográfico|Dinámico|Atmosférico|Slice of life>`. Sin él, el output del skill se bloquea.
  - **Auto-balanceo del catálogo**: el skill `/ficcion-draft § 5.6.tris` lee [`content/registro-ficciones.md`](../../content/registro-ficciones.md) columna `Intensidad`, calcula % real publicado y propone categoría infrarrepresentada. Si Rafael no especifica, default = Cinematográfico.
  - **Voz de referencia para Cinematográfico/Dinámico**: combinar voz peninsular literaria (Adón/Mesa/Urraca/Aramburu del catálogo §1+§1.bis) con **estructura de género** (banco §2.bis.2 ampliado: Pierre Lemaitre · Don Winslow · Daniel Suarez · Eva García Sáenz de Urturi). Ya documentado en [`castellano-literario-es.md § 5`](../../references/ficciones/intensidad-narrativa.md).
  - **Verificación pre-output**: listar eventos significativos del relato terminado en `PASOS.md § Eventos del relato` y validar contra el target de la categoría. Si Cinematográfico declarado y solo hay 3 eventos → reescribir antes de entregar.
  - **Catálogo histórico (9 relatos)**: 0% Cinematográfico · 22% Dinámico · 56% Atmosférico · 22% Slice. Inversión necesaria — próximos relatos rotan agresivamente hacia Cinematográfico hasta restablecer la matriz.

- **Variabilidad inter-relatos — OBLIGATORIO con bloqueo duro** (regla dura 2026-04-26 PM tras incidente *El chaval* — auditoría de los 9 relatos detectó copy-paste literal de párrafo entero entre *El que viene a tomar café* y *El chaval* + 14 tropos saturados + 66% del catálogo en mismo conflicto humano + 77% en mismo POV. Cita literal Rafael: *"No digo la forma o la composición, sino directamente copy-paste. Esto es inviable… Necesitamos un barrido completo… lo que haga falta para que esto no vuelva nunca a ocurrir."*). **Cada relato Ficciones Domésticas debe diversificar, contra los últimos 5 publicados, en CUATRO ejes estructurales** además del hook (regla hermana). Si cualquiera de los 4 ejes se repite sin excepción documentada, el skill `/ficcion-draft § 5.6 Variability gate` BLOQUEA el output antes de generar prosa.
  - **Eje 1 — Perfil POV:** edad±5 + género (M/F/X/humanoide) + relación familiar dominante. No repetir mismo perfil exacto en últimos 5. Ej: si los últimos 3 fueron `55-65 · F · hija-cuidadora-de-madre-demente`, el siguiente NO puede ser ese perfil — fuerza rotación a otro grupo demográfico (adolescente, hombre solo 30-40, pareja joven, inmigrante, niño 8-12 con humanoide compañero, anciano viudo, etc.).
  - **Eje 2 — Setting:** ciudad + momento del día + objeto-testigo central. No repetir mismo triple en últimos 5. Ej: si los últimos 3 fueron `Madrid · mañana · cocina-cafetera`, el siguiente fuerza otra ubicación-hora-objeto (pueblo costero, hospital, vehículo en movimiento, espacio público; tarde-noche-madrugada; objeto-testigo distinto).
  - **Eje 3 — Conflicto humano principal:** uno de N canónicos (`duelo` · `demencia` · `soledad-cuidadora` · `paternidad-ausente` · `brecha-digital-generacional` · `radicalización-política` · `obsolescencia-humana` · `corrupción-institucional` · `resignación-rural` · `outsourcing-vínculo-primario` · `teleoperación-explotación` · etc.). No repetir mismo conflicto principal en últimos 5.
  - **Eje 4 — Cliffhanger tipo:** uno de (`relación-sin-resolver` · `decisión-moral-pendiente` · `acto-irreversible-suspendido` · `revelación-no-vista` · `siembra-humanoide-anómalo` · `silencio-meditativo` · `complicidad-silenciosa` · `objeto-testigo-cargado` · etc.). No repetir mismo tipo en últimos 5.
  - **Tracking** en [`content/registro-ficciones.md`](../../content/registro-ficciones.md): columnas `Perfil POV`, `Setting`, `Conflicto humano`, `Cliffhanger tipo` (backfill de los 9 relatos hecho). El skill consulta esa tabla en `§ 5.6` antes de outline.
  - **Tropos quemados** (figuras retóricas, gestos físicos, símiles, frases-fórmula, setting clichés, nombres propios saturados): registro vivo en [`references/ficciones/tropos-quemados.md`](../../references/ficciones/tropos-quemados.md) — 14 tropos identificados como 🔴 QUEMADOS (≥2 usos) + lista 🟡 VIGILAR. Ventana de enfriamiento 5 relatos. Estado ⚫ JUBILADO permanente para los que pasen ≥4 usos. Cada relato registra al cerrar 5-10 figuras dominantes.
  - **Validación grep cruzada pre-output:** [`utilities/check_self_plagiarism.py`](../../utilities/check_self_plagiarism.py) compara n-gramas ≥6 palabras del nuevo borrador contra los últimos 5 relatos publicados + drafts pre-pub. Match ≥6 palabras consecutivas → bloqueo. Match 4-5 palabras de fórmula reconocible → warning + reescritura recomendada.
  - **Excepción documentada — sello de serie:** una serie activa puede mantener un eje fijo (POV, setting o cliffhanger) si está declarado explícitamente como sello editorial en su `arco-serie.md`. Sin declaración escrita, no aplica la excepción.
  - **Memoria de origen:** [`feedback_ficcion_anti_self_plagio.md`](../../../RRP-DEV/.claude/memory/feedback_ficcion_anti_self_plagio.md). Plan completo de implementación: [`se-han-utilizado-recursos-scalable-duckling.md`](../../../.claude/plans/se-han-utilizado-recursos-scalable-duckling.md).

- **Hook de apertura — OBLIGATORIO + variedad obligatoria** (regla dura 2026-04-26 tras feedback de Rafael: *"quiero que nuestros relatos tengan siempre un gancho inicial […] estilo hook de YouTube o piloto de serie de HBO […] no quiero que siempre se repitan las mismas situaciones, esto es primordial"*). **Todo relato Ficciones Domésticas, sin excepción de longitud o serie**, abre con un gancho fuerte en el primer párrafo (idealmente la primera frase) que provoque al lector la necesidad de seguir hasta el final para saber qué ha pasado, cómo se ha llegado ahí o qué decisión se va a tomar. Equivalente narrativo del cold open de un piloto HBO o del teaser de YouTube — no de la apertura ambiental literaria neutra.
  - **Catálogo canon de hooks** (24 tipos en 6 familias: Evento detonante · Pregunta-enigma · Estructura temporal · Voz-forma · Personaje · Atmósfera-mundo): [`@references/ficciones/hooks-taxonomia.md`](../../references/ficciones/hooks-taxonomia.md). El skill `/ficcion-draft` carga este archivo en el paso de outline (§5.7) antes de escribir prosa.
  - **Regla dura de variedad — no repetir hook concreto en los últimos 5 relatos.** El registro `content/registro-ficciones.md` lleva la columna `Hook` (cf. § "Tabla de relatos publicados") que el skill consulta para sugerir tipos no usados recientemente. Alternancia recomendada: si el relato anterior fue de familia X, el siguiente idealmente de otra familia. Excepción documentada en `arco-serie.md` si una serie tiene un hook recurrente como sello editorial declarado (ej: serie epistolar siempre abre con D1 Apertura epistolar).
  - **Frontmatter obligatorio:** campo `hook_type:` con uno de los 24 valores canon. Sin él, el output del skill se bloquea.
  - **Anti-patterns prohibidos como apertura** (lista cerrada en `hooks-taxonomia.md § 5`): apertura ambiental sin tensión (*"Era una mañana de abril en Madrid"*), resumen biográfico del personaje, filosofía declarativa abstracta, *"Todo empezó cuando…"*, primera frase explicativa del universo, pregunta retórica al lector, presentación de personaje con adjetivos, descripción del robot como decorado.
  - **Verificación pre-output:** la primera frase del relato debe coincidir con el `hook_type` declarado (lectura manual obligatoria por parte del skill, no solo grep). Si la apertura cae en un anti-pattern del catálogo § 5 → reescribir antes de entregar. Si el hook concreto está en los últimos 5 publicados sin excepción documentada → cambiar.

- **Display title declarativo YouTube-style — OBLIGATORIO en one-shots y miniseries futuras** (regla dura 2026-04-26 PM tras feedback Rafael viendo recomendaciones de YouTube anglo de "Domestic Fictions": *"quiero cambiar el formato de los títulos de mis próximos one-shots y miniseries… los títulos como ya hay un hook en ellos"*). Eje **independiente** del `title:` corto interno y del `slug:`. El relato lleva 4 nombres distintos en su frontmatter:
  - `title:` (sin cambios — sustantivo simple 2-6 palabras: *La objeción*, *El operador nocturno*).
  - `slug:` (sin cambios — kebab-case corto, URL pública estable `robohogar.com/p/<slug>`).
  - `display_title:` **nuevo, obligatorio** — formato declarativo paradójico, fórmula `"El/La [rol/oficio] que [acción inusual + objeto-imposibilidad]"`, **10-15 palabras** (ajuste 2026-04-26 PM tarde tras feedback Rafael: rangos previos 8-15 dejaban entrar candidatos de 18-23 palabras al re-componer; el techo dura 15 sin excepción y el suelo sube a 10 para garantizar hook compositivo mínimo). Ejemplos canon ROBOHOGAR: *"La cuidadora que reza para que su humanoide no la sustituya antes del tribunal médico"* (15) · *"El humanoide que cobra de noche por los sueños que no tiene"* (12) · *"La ministra que carga su humanoide en el enchufe vacío del Congreso"* (12).
  - `tag_poetico:` **nuevo, obligatorio** — etiqueta editorial ES de un catálogo cerrado (ver bullet siguiente).
  - **Dónde se renderiza el `display_title`:** subject del newsletter Beehiiv · H1 web del post (Beehiiv title) · OG title de la card en LinkedIn/X/WhatsApp · alt-text de la miniatura · copy de redes generado por `/social-content`. El `title:` corto sigue como nombre interno de carpeta, fichero `.md`, breadcrumb, slug-friendly fallback. La URL pública sigue siendo `slug:` corto.
  - **Familia G de hooks de display title** (catálogo nuevo en [`@references/ficciones/hooks-taxonomia.md`](../../references/ficciones/hooks-taxonomia.md)) — 4 subtipos: G1 *Oficio + acción imposible*, G2 *Acto cotidiano + objeto imposible*, G3 *Sujeto + paradoja temporal*, G4 *Función + sustitución imposible*. **No repetir misma subfamilia G en últimos 5 display titles.** Eje independiente del `hook_type` de prosa (familias A-F): un mismo relato declara ambos en frontmatter (ej: `hook_type: A3 · display_title_family: G1`).
  - **Variedad por banda de personaje:** la familia G1 (oficio + acción imposible) abarca 5 bandas — A oficios domésticos · B trabajadores ES día a día · C funcionarios públicos · D figuras públicas por rol · E cultura pop / mediática. **No repetir banda dominante en últimos 5 display titles.** Detalle de bandas en [`assets/branding/ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad`](../../assets/branding/ficcion-hero-archetypes.md). Convención dura: figuras públicas por rol y atrezzo (*"La ministra que…"*) **sin nombre propio real** y **sin cara reconocible** en miniatura — extensión natural de `§ Narrativa especulativa § Nombres propios de robots y asistentes IA: siempre ficticios`.
  - **Verificación pre-output (bloqueo duro):** falta `display_title:` o `tag_poetico:` en frontmatter → output bloqueado. `display_title` < 10 o > 15 palabras → bloqueado. Subfamilia G repetida en últimos 5 sin excepción documentada → bloqueado. Display title que mencione nombre propio real de figura pública → bloqueado.
  - **Aplicación retroactiva:** ninguna. Los 9 publicados quedan con `title:` corto como hasta ahora; columna `Display title` del registro queda como `—` para esos 9. Aplica desde el siguiente relato (one-shot o miniserie). **Series activas con código visual declarado** (La Casa de Amparo, Crónicas de Ronda 3, Cartas a MAIA) tampoco se retitulan en sus relatos publicados, pero **sí adoptan `display_title:` + `tag_poetico:` desde el siguiente episodio** — la mejora del título YouTube-style aplica a series, lo que no aplica es el cambio de canon visual del hero (esas series mantienen su código).

- **Tag poético tonal — catálogo cerrado, OBLIGATORIO en frontmatter** (regla hermana del display title, canonizada 2026-04-26 PM). Cada relato lleva en frontmatter `tag_poetico:` con UNA de las 10 etiquetas canon, mapeadas a categoría tonal:

  | Categoría tonal canon | Tag poético ES (elegir 1 según eje dominante) |
  |---|---|
  | inquietante (40%) | *Hogar uncanny* (eje técnico-sensorial: rutinas que vibran raro) · *Habitaciones extrañas* (eje espacial: el hogar como territorio extranjero) |
  | radical (15%) | *Cuidados rotos* (eje afecto-cuidado: vínculo primario sustituido o quebrado) · *Diálogos rotos* (eje comunicativo: lo que no se dice o no se puede decir) |
  | ambiguo (25%) | *Memorias prestadas* (eje memoria-identidad: recuerdo mediado por máquina) · *Espacios subconscientes* (eje psíquico: lo que el hogar revela del personaje) |
  | inspirador (10%) | *Cocinas tibias* (eje material-doméstico: cuidados pequeños que sostienen) · *Anatomía emocional* (eje introspectivo: vulnerabilidad luminosa) |
  | mundano (10%) | *Domingos eléctricos* (eje cotidiano: rutina con un detalle desviado) · *Física melancólica* (eje observacional: leyes domésticas que ya no funcionan) |

  - **El skill `/ficcion-draft § 5.7-ter` propone 1 tag** del par correspondiente a la categoría tonal en función del eje dominante del relato (afecto vs ausencia, técnico vs sensorial, espacial vs psíquico). Rafael valida.
  - **Catálogo cerrado:** si llega un eje no cubierto, se amplía la regla en este archivo, **no por relato**. Cero etiquetas ad-hoc en frontmatter individual.
  - **Dónde se renderiza (regla acotada 2026-04-27 tras feedback Rafael: *"solo va en el subtítulo"*):** **únicamente al inicio del subtítulo** (Meta B del `beehiiv-paste.html` → campo "Subtitle" de Beehiiv → reutilizado como Meta description del SEO panel y como description de la OG card). NO se renderiza en: footer del cierre del relato, microtítulo en la wiki Obsidian, tag editorial separado de Beehiiv (ahí va solo el `tags-beehiiv:` de categoría), miniatura/hero del relato, H1/H2 web del post, copy de redes generado por `/social-content`. El uso interno (frontmatter `tag_poetico:` + columna `Tag poético` en `content/registro-ficciones.md`) se mantiene sin cambios — son metadatos de auto-balanceo del catálogo, no copy visible al lector.
  - **Backfill retroactivo de los 9 publicados:** sí (etiqueta inferida de la categoría tonal + eje del relato), columna `Tag poético` del registro de ficciones se rellena en una sola pasada. Diferencia con `display_title:` (que NO se backfillea): el tag poético es una etiqueta editorial inferible de la prosa existente, no requiere reescritura.

- **Hero de one-shots y miniseries — canon `personaje-acción-imposibilidad` para nuevos relatos** (regla dura 2026-04-26 PM, canon visual nuevo paralelo al `portada minimalista · objeto-testigo` existente). Aplica solo a one-shots y miniseries futuras. Las 3 series activas (Amparo, Ronda 3, MAIA) mantienen su código visual sin tocar.
  - **ADN visual ROBOHOGAR fijo (redefinido 2026-04-27 PM tras canonizar modalidades visuales — heredado de `asset-catalog.md § 5` + `ficcion-hero-archetypes.md § Modalidades visuales`):** estilo painterly editorial Penguin Modern Classics + chiaroscuro dramático con **foco lumínico único** (Hopper-meets-Caravaggio) + composición del paradigma vigente (minimalista o personaje-acción-imposibilidad) + tight medium close-up con legibilidad a thumbnail 120px + dimensiones 1200×630 (`--model 2 --aspect 16:9 --size 2K` + crop Pillow) + anti-sign-guard activo (cero neones, cero caracteres asiáticos, cero LEDs/glow, cero texto). **La paleta y el color de la fuente lumínica son variables** según la **modalidad visual declarada** (M1-M6) — la modalidad rota relato a relato con anti-repetición de los últimos 3 heros publicados, transversal a paradigmas. **Cero adopción del estilo oil painting / digital painting anglo** del canal "Domestic Fictions" de YouTube — solo adoptamos su gramática compositiva y la variedad cromática inter-relatos, no su look-and-feel pintado.
  - **Lo nuevo (gramática compositiva):**
    1. **Personaje** identificable por oficio/rol del relato en primer plano (delantal de cocina, bata sanitaria, mono de operario, gafas de leer, herramienta en mano, chaleco fluorescente municipal, chaqueta de pleno, sudadera con anillo de luz de streamer, bota de fútbol, micrófono institucional). Visible torso + cabeza, o silueta lateral con identidad clara. Edad/género coherente con POV del relato (Eje 1 anti-self-plagio).
    2. **Acción concreta visible** ejecutada por el personaje (forjando, ajustando, escribiendo, vigilando, alimentando, midiendo, firmando, cosiendo, hirviendo, llamando). Pose dinámica, no contemplativa.
    3. **Objeto-imposibilidad materializado** físicamente en el frame: humo de color anómalo, líquido luminoso, partículas que escriben, luz que escapa de un objeto cotidiano, humanoide encogido en gesto incoherente con su función. **El objeto-imposibilidad es la traducción visual de la paradoja del `display_title`.**
    4. **Composición regla de tercios:** personaje en una zona del frame, objeto-imposibilidad a contrapunto. Foco lumínico ámbar cae diagonal sobre la unión.
    5. **Test legibilidad 120px** (Beehiiv landing) sigue obligatorio: silueta + foco deben distinguirse a thumbnail.
  - **Catálogo de archetypes nuevo en [`assets/branding/ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad`](../../assets/branding/ficcion-hero-archetypes.md)** con 5 bandas (A-E como arriba) y 25+ archetypes iniciales. Anti-repetición acotada al grupo: nunca mismo archetype concreto en últimos 5 heros del paradigma personaje. Adicional: **rotar entre bandas** — no encadenar 3 relatos seguidos en la misma banda salvo excepción documentada en `arco-serie.md`.
  - **Convención de identidad de figuras públicas (banda D):** **identidad por rol y atrezzo solamente**, nunca por cara reconocible ni nombre real. Si Gemini genera una cara que recuerda a figura pública concreta → regenerar. En el `display_title` correspondiente, rol genérico sin nombre propio: ✅ *"La ministra que…"* · ❌ *"La ministra Yolanda Díaz que…"*. Excepción permitida en diálogo del relato (no en título ni hero): un personaje puede mencionar figura pública real una vez para verosimilitud cotidiana. Misma estructura que la excepción para Alexa / Roomba en diálogo.
  - **Compatibilidad con paradigma minimalista:** los dos canon (`personaje-acción-imposibilidad` nuevo · `portada minimalista · objeto-testigo` existente) **conviven** para one-shots/miniseries. Default desde 2026-04-26 = personaje-acción-imposibilidad. El paradigma minimalista queda como opción declarativa cuando el relato lo pida explícitamente (relato cuyo objeto-testigo aislado es más fuerte que cualquier personaje en frame, ej: *La objeción* tela ceremonial). El skill `/ficcion-draft § 8.x Hero` pregunta a Rafael si hay duda; default sin pregunta = nuevo paradigma.

  - **Modalidad visual (M1-M6) — eje cromático ortogonal a ambos paradigmas** (regla dura 2026-04-27 PM tras feedback Rafael: los 4 heros más recientes compartían exactamente la misma paleta azul-noche+ámbar, ángulo eye-level y luz lateral cálida — la galería `/Ficciones` se leía como "el mismo hero con personajes distintos"). Catálogo cerrado en [`assets/branding/ficcion-hero-archetypes.md § Modalidades visuales (M1-M6)`](../../assets/branding/ficcion-hero-archetypes.md): **M1** Ámbar nocturno (default heredado) · **M2** Cobalto tormenta · **M3** Diurno plomizo · **M4** Atardecer magenta-naranja · **M5** Amanecer brumoso · **M6** Fluorescente clínico-institucional. Cada modalidad fija paleta + color de la fuente única + atmósfera; el resto del ADN (painterly + chiaroscuro + composición + thumbnail 120px + anti-sign-guard) no se toca.
    - **Frontmatter `modalidad_visual: M1|M2|M3|M4|M5|M6` OBLIGATORIO.** Sin él, output del skill bloqueado.
    - **Anti-repetición dura:** no repetir misma modalidad en últimos **3 heros** publicados (transversal a paradigma — un hero minimalista M1 cuenta contra un hero personaje M1). Skill consulta columna `Modalidad visual` de `content/registro-ficciones.md` antes de proponer.
    - **Ángulo de cámara A1-A5** queda como eje ortogonal con anti-repetición propia (últimos 3 heros). Refuerzo de la regla del paradigma minimalista que estaba documentada pero no se cumplía.
    - **Mapeo tonalidad → modalidades preferentes** (no exclusivo): inquietante → M1·M2·M6 · radical → M2·M6 · ambiguo → M3·M4·M5 · inspirador → M4·M5 · mundano → M1·M3.
    - **Meta de cobertura inicial:** en los próximos 10 heros publicados desde 2026-04-27, deben aparecer al menos 5 de las 6 modalidades. Si una nunca apareció tras 10, el skill bloquea las otras hasta que toque la faltante.
    - **Aplicación retroactiva:** ninguna. Los 9 publicados se backfillean con `Modalidad visual = M1` + `Ángulo = A1` en `registro-ficciones.md` y no se regeneran sus heros (decisión Rafael 2026-04-27).
    - **Series activas con código declarado** (Amparo, Ronda 3, MAIA) **NO usan el sistema M1-M6** — mantienen su código visual fijo. Igual que el paradigma personaje-acción-imposibilidad: aplica solo a one-shots y miniseries futuras.

  - **Composición canon (C-01..C-19) — eje compositivo macro ortogonal a los demás** (regla dura 2026-04-28 tras feedback Rafael: las 9 miniaturas test M2-M6 salieron correctas en estilo painterly y modalidad cromática, pero las 3 composiciones de los 3 relatos test eran demasiado parecidas en gramática del frame — la variabilidad no llegaba al nivel del canal "Domestic Fictions" anglo que Rafael usa como referente). Catálogo en [`assets/branding/ficcion-hero-composiciones-canon.md`](../../assets/branding/ficcion-hero-composiciones-canon.md): **19 patrones compositivos** organizados en 5 familias — I Íntima emocional (C-01 two-shot · C-02 close-up emocional · C-03 detalle manos · **C-13 three-shot teatral horizontal** · **C-18 detalle de manos con altar simétrico**), II Plano arquitectónico monumental (C-04 espacio institucional · C-05 eje simétrico altar · **C-14 contrapicado escala asimétrica** · **C-15 bóveda con reunión circular**), III Frame dentro de frame (C-06 pantalla/holograma · C-07 ventana/umbral · **C-19 cabina cerrada + ventana exterior radical**), IV Frontal teatral / over-the-shoulder (C-08 frontal teatral · C-09 over-the-shoulder voyeur · **C-16 foco lumínico cenital extremo quirúrgico**), V Atmósfera ambiental + color-pop (C-10 exterior nocturno · C-11 decadencia/caos · C-12 color-pop saturado · **C-17 ritual outdoor con horizonte desolado/apocalíptico**). Las 7 nuevas (C-13..C-19) canonizadas 2026-04-28 tras estudio de capturas adicionales del canal Domestic Fictions enviadas por Rafael — añaden gramáticas ausentes (three-shot, contrapicado de escala, bóveda circular, cenital extremo, ritual outdoor, hands+altar híbrido, cabina cósmica).
    - **Frontmatter `composicion_canon: C-01..C-19` OBLIGATORIO** desde 2026-04-28. Sin él, output del skill bloqueado.
    - **Anti-repetición dura:** no repetir misma composición en los **últimos 5 heros** publicados (transversal a paradigma). Si las **últimas 3** son de la misma familia (I-V), bloqueo de la familia entera para la siguiente.
    - **Selección aleatoria con filtro tonal:** el skill `/ficcion-draft § 8.x Hero` filtra el pool por compatibilidad con `categoria-tonal`, excluye las 5 últimas, aplica bloqueo de familia, y propone **3 candidatos aleatorios** del pool resultante. Rafael valida o pide rotación.
    - **Regla dura — los 3 candidatos son SIEMPRE 3 composiciones C-XX totalmente distintas** (canonizado 2026-04-28 PM tras feedback de Rafael en la generación de Pipo: *"cuando me das tres opciones, quiero tres opciones con composiciones totalmente distintas, no tres prácticamente idénticas con pequeñas diferencias muy sutiles"*). **Prohibido** proponer 3 variantes de la misma C-XX cambiando solo el objeto-imposibilidad / la pose del personaje / la luz secundaria. Si el skill cree que una C-XX concreta encaja perfecto con el relato, igualmente debe proponer 2 más de C-XX distintas para que Rafael vea contraste — el valor del paso es exploratorio, no confirmatorio. **Ideal:** las 3 distintas vienen además de **familias diferentes** (I Íntima · II Plano arquitectónico · III Frame-in-frame · IV Frontal/OTS · V Atmósfera/color-pop) cuando el pool lo permite, para maximizar contraste compositivo macro. **Verificación pre-output del paso:** si los 3 candidatos comparten C-XX → regenerar la propuesta antes de mostrarla. Si comparten familia → aceptable pero solo si el pool no permite alternativa, y declarar el motivo. **Regla universal — aplica también a `/content-draft` (heros de artículos no-ficción) y a cualquier invocación de `/nano-banana` que pida 3 candidatos**: las 3 deben ser composiciones / planos / encuadres / ideas claramente distintas, no 3 variantes sutiles del mismo plano (canonizado 2026-04-28 PM tarde tras feedback Rafael ampliando el alcance al observar el mismo problema en heros de artículo). Detalle universal: [`feedback_3_candidatos_composiciones_distintas.md`](../../.claude/memory/feedback_ficcion_3_candidatos_composiciones_distintas.md).
    - **Meta de cobertura inicial:** en los próximos 19 heros publicados desde 2026-04-28, deben aparecer al menos 12 de las 19 composiciones. Si una nunca apareció tras 19, el skill bloquea las otras hasta que toque la faltante.
    - **Compatibilidad con bandas (paradigma personaje):** mapeo en el catálogo § Compatibilidades especiales — banda A mejor con C-01/C-03/C-07/C-08/C-12/C-13/C-16/C-18 · banda D figuras públicas mejor con C-04/C-05/C-08/C-15/C-16 · etc. No es exclusivo: composiciones cross-banda (C-09/C-10/C-11/C-14/C-17/C-19) son comodín cuando una banda lleva 2 relatos consecutivos en misma composición.
    - **Backfill retroactivo:** los 6 publicados con hero existente se backfillean con la composición que mejor describe su frame (best-fit aproximado, no implica rerender). Tabla en el catálogo. Las 7 composiciones nuevas (C-13..C-19) NO se aplican retroactivamente — son default desde el siguiente relato.
    - **ADN visual (painterly book cover + chiaroscuro + foco único + anti-sign-guard) + regla "cotidiano + sci-fi mezclados" se mantienen en todas las composiciones** — la composición es solo el patrón gramatical macro del frame, no toca el rendering.

- **Composición canon del audiolibro — frontispicio sonoro obligatorio** (regla dura 2026-04-28 PM tras feedback Rafael reproduciendo `el-cristalero.mp3` v1: el bumper Luis cerraba con *"Una Ficción Doméstica de ROBOHOGAR"* y el cuerpo Gabo arrancaba directamente con *"Treinta y un turnos. Mauricio le dio la hoja…"* sin anclar la pieza con su propio nombre — sensación de "te cuento una historia cualquiera" en lugar de "abre el libro X y léelo"). Aplica a TODO audiolibro generado por `/audiobook-generate` para Ficciones Domésticas — one-shots, miniseries, episodios de serie, sin excepción. La composición canónica del MP3 es:

  | Pieza | Voz | Duración típica | Función |
  |---|---|---|---|
  | Bumper intro | Luis | ~2.5s | tarjeta de marca *"Ficciones de ROBO, OGAR"* |
  | Silencio | — | 2s | respiro entre marca y libro |
  | **Anuncio del título** | **Gabo** | **~1-2s** | **frontispicio sonoro, equivalente al Snippet 2.5 HTML** |
  | Silencio | — | 2s | respiro entre frontispicio y cuerpo |
  | Cuerpo del relato | Gabo | minutos | narración íntima |
  | Silencio | — | 3s | respiro emocional pre-cierre de marca |
  | Bumper outro | Luis | ~12s | CTA final de marca |

  - **Texto leído como anuncio:** el `title:` corto del frontmatter del relato (ej: *"El cristalero"*), idéntico letra por letra al frontispicio HTML del Snippet 2.5 que Rafael pega en Beehiiv. **Nunca el `display_title:`** declarativo largo — eso es para subject de email + H1 web + OG card, no para audio (15 palabras leídas como tarjeta de título suenan a sinopsis, no a frontispicio). El skill añade automáticamente punto final si el frontmatter no lo trae (idempotente).

  - **Voz Gabo** (mismo locutor del cuerpo). Razón: el narrador del libro lee su propio frontispicio — es el patrón Penguin / Anagrama del audiolibro impreso. Luis se mantiene exclusivamente como bumper de marca (intro + outro). Cambiar de Gabo a Luis para el título rompería la metáfora "abro el libro y empiezo a leer".

  - **Parámetros prosódicos especiales del TTS** (críticos: con defaults, frases ≤3 palabras se leen como inicio de oración incompleta):
    - `previous_text="Una Ficción Doméstica de ROBO, OGAR."` (cierre simulado del bumper Luis canónico). Sin esto, Multilingual v2 no sabe que viene tras una sentencia cerrada y aplica entonación de continuación.
    - `voice_settings.style = 0.5` (cuerpo: 0.0). Da expresividad de presentación, no de narración íntima.
    - `voice_settings.stability = 0.4` (cuerpo: 0.5). Suficiente variación para que el cierre del título caiga en pitch como final declarativo.
    - `next_text` ausente (no se pasa). Evita que el modelo encadene con el cuerpo sin pausa.

  - **`utilities/generate_audio.py § synthesize_title_announce`** implementa esto. CLI: `python utilities/generate_audio.py <audiolibro.txt> <slug> "<title corto>"` (3er arg obligatorio desde 2026-04-28 PM). Sin él, el script aborta con mensaje claro.

  - **`chunks-index.json` schema_version = 3** desde 2026-04-28 PM: añade `title_text`, `title_duration_seconds`, `silence_after_title_seconds`. Los `chapters[].start_seconds` se calculan con offset = intro + sil_after_intro + título + sil_after_title (la narración empieza tras el frontispicio, no tras el silencio post-intro). Implicación downstream: los timestamps de capítulos del MP4 YouTube + chapters de descripción RSS se desplazan ~3-4s respecto al canon previo.

  - **MP4 YouTube hereda automáticamente.** `/audiobook-distribute` compone el MP4 con el MP3 final como pista de audio + waveform/chyrons. El título leído ya está horneado en el MP3 → aparece en el MP4 sin trabajo extra. Los chapters de la descripción YouTube usan los offsets nuevos del `chunks-index.json` (schema v3).

  - **Aplicación retroactiva:** los 5 audiolibros publicados pre-2026-04-28 PM (`el-que-viene-a-tomar-cafe`, `la-canguro`, `la-objecion`, `papa-desde-singapur`, `pipo`) **NO se regeneran** — el coste TTS de regenerar 5 cuerpos enteros es ~60K créditos (50% cuota mensual Creator). Aplica desde el siguiente relato (`el-cristalero` ya en R2 con título intercalado vía one-shot `intercalate_title_*` 2026-04-28). Si en el futuro un relato pre-canon necesita re-mastering por otro motivo (ej: texto editado, voz cambiada), el título se inyecta en esa pasada — no antes.

  - **Coste por relato:** ~10-20 chars adicionales TTS por título (~10-20 créditos ElevenLabs, despreciable frente a los 12-15K del cuerpo medio).

  - **Verificación pre-output del skill `/audiobook-generate`:** el `title:` corto del frontmatter del relato debe existir y no estar vacío. Si falta, abort. La regla canon del frontispicio HTML (Snippet 2.5) ya garantizaba que el `title:` corto existe en todos los relatos desde 2026-04-26 — esta regla solo añade que también vive como anuncio sonoro.

  Detalle e incidente origen: memoria `feedback_audiolibro_titulo_obligatorio.md`.

Skill: `/ficcion-draft`. Pipeline completo: `@.claude/commands/ficcion-draft.md`.
Bible maestra + canon transversal de series: `@references/ficciones/series-bible-maestra.md`.
Knowledge base: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`.
Patrones serialized newsletter 2025: `@references/ficciones/serialized-newsletter-patterns.md`.
Catálogo canon de hooks de apertura: `@references/ficciones/hooks-taxonomia.md`.
Tropos quemados (registro vivo de figuras/gestos/imágenes/fórmulas saturados): `@references/ficciones/tropos-quemados.md`.
Tracking estructural de variabilidad inter-relatos (POV/Setting/Conflicto/Cliffhanger): `@content/registro-ficciones.md` columnas correspondientes.
Validación grep cruzada anti-auto-plagio: `@utilities/check_self_plagiarism.py`.
Matriz canon de intensidad narrativa (Cinematográfico/Dinámico/Atmosférico/Slice + default Cinematográfico): `@references/ficciones/intensidad-narrativa.md`.
Roadmap ebook: `@references/ficciones/ebook-roadmap.md`.

## Cero referencias fantasma — integridad editorial

Regla estricta: **toda promesa interna del texto debe tener referente real en el mismo artículo**. Prohibido prometer al lector tablas, gráficos, infografías, diagramas, imágenes, secciones, checklists o bloques que no existen literalmente en el post publicado.

Formas prohibidas específicas:
- *"La noticia real está una tabla de [X] abajo"* · *"hay que leer lo mismo desde otra tabla"* → si no hay `<table>`.
- *"como verás en el gráfico de [X]"* · *"la infografía más adelante"* → si no se inserta ningún `<img>`/figura correspondiente.
- *"el análisis completo abajo"* · *"la sección al final"* → si no hay H2/H3 subsiguiente con ese contenido.
- Links a artículos ROBOHOGAR que aún no están publicados — la URL debe existir en `content/registro-articulos.md`.
- Cifras concretas ("12% éxito", "€98.000") sin fuente verificable en `references/fuentes-por-categoria.md` para esa categoría.

**Razón e incidente origen:** artículo #8 *"Humanoide bate récord media maratón"* (2026-04-20): el subtítulo y un callout prometían "la tabla de Stanford abajo" pero el artículo solo citaba el informe en prosa + un gráfico Behavior-1K, no había tabla ninguna. Rafael tuvo que reescribir el subtítulo y eliminar el callout entero tras publicar. Regla ampliada y grep pre-output: memoria [`feedback_robohogar_no_phantom_references.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_no_phantom_references.md).

**Aplicación operativa:**
- `content-draft.md` § 8.4 bis — grep pre-output de promesas internas + verificación de cada match.
- `post-publish.md` § 1 — grep de referencias fantasma contra el HTML publicado. **Triaje obligatorio:**
  - **Fantasma evidente + fix obvio** (≤1 frase tocada, sentido preservado, sin cambio de tesis) → arreglar directamente en `borrador.html` + `published/YYYY-MM-DD-<slug>.html` y reportar en el resumen. NO preguntar.
  - **Fantasma ambiguo** (reescritura >1 frase, estructura del bloque afectada, o dato sin fuente que podría ser correcto) → PARAR y avisar a Rafael con la lista + propuesta de fix por cada una.
- `ficcion-draft.md` — aplica parcialmente: en ficción la prosa puede insinuar elementos fuera de escena (Chekhov), pero NO prometer al lector secciones del relato que no existen. Los datos anclados (dato-real) sí tienen que existir y ser verificables.

Voz de autoridad propia (§ editorial anterior) + cero referencias fantasma = contrato básico con el lector de ROBOHOGAR.

## Honestidad de primera persona — cero verbos de acción no realizada

Regla dura hermana de "Voz de autoridad propia" y "Cero referencias fantasma". Aplica a todo contenido publicable (artículo, review, comparativa, editorial, guía, newsletter, ficha tangible).

**Principio:** la voz plural editorial ("hemos") solo puede atribuirse a acciones que ROBOHOGAR realmente ha realizado. El equipo editorial de ROBOHOGAR trabaja con fichas oficiales, reviews internacionales, datos públicos de mercado y criterio editorial. **No tiene laboratorio, no tiene los robots en mano, no desmonta unidades, no mide ruido ni duración de batería, no prueba en jardines ni en pisos**. Cualquier verbo que implique acción experimental física que no hemos hecho es mentira — y una sola mentira rompe el contrato con el lector para todo el resto del artículo.

**Verbos prohibidos en voz ROBOHOGAR salvo que describa algo literalmente ejecutado:**

| Verbo/frase prohibida | Por qué | Sustitución honesta |
|---|---|---|
| "6 modelos probados" · "hemos probado" · "probamos X" | Implica test físico en mano | "6 modelos comparados" · "hemos analizado" · "contrastamos fichas y reviews" |
| "uso real en pisos/jardines españoles" · "en nuestras pruebas" · "en nuestro test" | Implica experimentación propia | "en reviews internacionales del último año" · "según la ficha oficial" · "contrastando fichas + reviews" |
| "hemos medido X dB" · "ruido medido de 57 dB" | Implica equipo calibrado | "57 dB declarados por [marca]" · "según ficha oficial de [marca]" |
| "hemos desmontado" · "hemos abierto" · "hemos visto por dentro" | Implica unidad de muestra | "según el despiece publicado por [fuente]" · eliminar si no hay fuente |
| "nos ha gustado" · "nos ha convencido al probarlo" · "lo hemos oído" | Implica experiencia sensorial | "según las reviews que cubren el modelo" · "en reviews internacionales" · reescribir sin claim sensorial |
| "Instalación en 30 minutos literales" · "le hemos cronometrado" | Implica medición propia | "Instalación declarada de 30 minutos por el fabricante" |
| "en primeros meses aún pisa alguna flor" · "nos atacó una flor" | Claim de uso propio | "reviews internacionales del primer año señalan confusiones con flores pequeñas" |
| "De 14 modelos probados nos quedamos con 6" | Implica 14 unidades en mano | "De 14 candidatos revisados nos quedamos con 6" · "seleccionados entre 14 candidatos tras cruzar fichas y distribución ES" |

**Verbos ✅ permitidos en voz plural ROBOHOGAR:**

- *"hemos comparado"* · *"hemos analizado"* · *"hemos leído"* · *"hemos seleccionado"* · *"hemos elegido"* · *"hemos descartado"* · *"hemos cruzado"* · *"hemos contrastado"*
- *"hemos decidido"* · *"hemos priorizado"* · *"hemos revisado"* · *"hemos verificado en [fuente externa]"* · *"hemos confirmado en Amazon.es"*
- *"nos ha sorprendido la ficha"* · *"nos ha llamado la atención el precio"* · *"nos parece"* · *"nuestra lectura es"*
- *"recomendamos"* · *"descartamos"* · *"preferimos"*

Lo que ROBOHOGAR hace de verdad es **análisis editorial riguroso sobre información pública**: leer fichas oficiales, cruzar con reviews internacionales de Xataka, T3, PCMag, Wirecutter, CGMagazine, YouTube-reviewers, verificar distribución ES en Amazon.es / Leroy Merlin / tiendas oficiales, y emitir juicio editorial por perfiles. Eso es más que suficiente para una guía de compra honesta y con voz propia — no hace falta mentir con verbos de test que no existen.

**Cifras concretas de ahorro/ventaja/pérdida — prohibido inventar:**

Promesas tipo *"te ahorra 800 €"*, *"te ahorras 600 € antes de comprar"*, *"ahorra 200 € al mes"*, *"diferencia de 450 € frente a X"* que aparezcan en **subtítulos, meta descriptions, hooks, callouts o CTAs** están PROHIBIDAS salvo que la cifra sea aritmética directa sobre precios citados en el mismo artículo con fuente (ej: "el NERA te saca 900 € por encima del Worx" cuando NERA=2.099 € y Worx=1.199 € son precios citados con link → 900 € es resta verificable ✅).

Prohibido por inventadas:
- ❌ *"checklist de 7 preguntas que te ahorra 800 € antes de comprar"* (¿800 € frente a qué alternativa?)
- ❌ *"checklist de 5 preguntas que te ahorra 600 € antes de comprar"* (idem, artículo aspirador 2026)
- ❌ *"te ahorra 80-120 € si ya tienes X en casa"* (cifra inventada sobre accesorios)
- ❌ *"Gardena te ahorra 200 €"* (diferencia aritmética que no corresponde con los precios citados)

Sustitución honesta — opciones ordenadas de menos a más conservadora:
1. **Resta aritmética directa**: cuando los dos precios están citados con fuente, dar la cifra (*"te saca 900 € por encima del Worx M800"*). Si falta uno de los dos precios con fuente, no.
2. **Generalización cualitativa**: *"cientos de euros"*, *"varias decenas de euros"*, *"una diferencia notable"*, *"el equivalente a una cuota de comunidad"*.
3. **Sin cifra, promesa de no-error**: *"checklist de 7 preguntas para no equivocarte al comprar"*, *"checklist de 7 preguntas para que no compres de más"*, *"checklist de 5 cosas que verificar antes de darle al botón"*.

La promesa de "no equivocarse" o "no comprar de más" es más fuerte editorialmente que una cifra inventada, porque es verdad y porque el lector sabe que las cifras redondas en headlines son marketing. Usar la versión 3 como default cuando no haya resta aritmética defendible.

**Claims sensoriales y técnicos siempre con framing:**

Cualquier afirmación sobre ruido, silencio, fluidez de corte, duración real de batería, capacidad real de pendiente, etc. debe llevar en la **misma frase o párrafo** uno de estos framings:

- *"declarado por [marca]"* · *"según la ficha oficial"*
- *"según las reviews internacionales"* · *"según el review de [medio]"*
- *"según usuarios verificados en [plataforma]"*

Sin framing → reescribir sin claim sensorial o eliminar la frase.

**Incidente origen 2026-04-21:** artículo #9 *"Mejor robot cortacésped 2026"* (guía de compra evergreen). El subtítulo de entrada abría con *"6 modelos probados, de 1.099 € a 2.499 €…"* — mentira flagrante (ningún modelo se había probado, solo se habían analizado fichas + reviews). Además: *"filtro de uso real en jardines españoles, no ficha técnica en frío"* (exactamente lo contrario de la realidad), *"instalación en 30 minutos literales"* (implica cronómetro propio), *"57 dB medido"* (implica equipo propio), *"en los primeros meses pisa alguna flor"* (implica test de campo). Rafael detectó el subtítulo a los 3 segundos de abrir el borrador y paró la entrega. Ampliación: memoria [`feedback_robohogar_no_fake_testing_claims.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_no_fake_testing_claims.md).

**Aplicación operativa:**
- `content-draft.md` § 8.4 quater — grep pre-output obligatorio sobre la lista de verbos prohibidos de arriba. Rechazo automático si hay ≥1 match sin justificación explícita.
- `ficcion-draft.md` — no aplica en narrador omnisciente (la ficción puede inventar acciones del personaje). Sí aplica en el bloque "Lo real detrás del relato" cuando la voz vuelve a ser ROBOHOGAR editorial.
- `post-publish.md` — grep final en el HTML publicado. **Triaje:** mentira evidente + fix ≤1 frase → auto-fix en borrador + published + reportar. Mentira estructural (afecta tesis del artículo) → parar y consultar.

**Regla de actitud:** cuando el agente redacte una frase que contenga "hemos X", debe preguntarse: *"¿realmente hemos hecho X?"*. Si no, reescribir. El escape fácil ("6 modelos probados" es marketing clásico) es el que rompe el contrato editorial. ROBOHOGAR no hace marketing, hace análisis editorial riguroso.

Voz de autoridad propia + cero referencias fantasma + cero verbos de acción no realizada = contrato editorial completo con el lector de ROBOHOGAR.

## Datos con fuente rastreable — cada cifra cita o cualifica

Regla hermana de "Cero referencias fantasma". Aplica a todo contenido publicable (artículo, review, comparativa, editorial, guía, newsletter, ficción con datos anclados).

**Principio:** cada afirmación numérica o categórica del cuerpo debe llevar **fuente rastreable en la misma frase/párrafo** O framing que la marque como claim no verificado. Si no es posible, reescribir en términos aproximativos sin cifra.

**Categorías que OBLIGATORIAMENTE llevan link/cita o framing explícito:**

1. **Cifras de ventas/unidades** ("60.000 Eilik", "1,8M iFlytek") → link a comunicado/fuente primaria.
2. **Ratings/valoraciones** ("4,8/5 con 1.000 reseñas") → plataforma explícita ("en Amazon ES", "en Trustpilot").
3. **Eficacia/estadísticas** ("99,99% bacterias", "17% hogares España", "89,4% éxito simulación") → link al estudio + página/sección si es informe largo.
4. **Inversión/financiación** ("10.000M levantados", "Tesla 20.000M en 2026") → link a Reuters/Bloomberg/TechCrunch o comunicado oficial.
5. **Proyecciones de mercado** ("1,2M humanoides en 2030", "15% a hogares") → link al reporte + distinción explícita si el desglose es inferencia propia (*"nuestra estimación"*, *"extrapolando los datos"*).
6. **Fechas regulatorias** ("AI Act 2 ago 2026") → link al texto normativo oficial (EUR-Lex, BOE).
7. **Datos históricos** ("desde 2003", "primer NaviBot") → link a fuente que lo confirme. Si no se encuentra, cambiar a aproximación (*"desde mediados de los 2000"*) o eliminar.
8. **Tests del fabricante** ("tests internos Samsung", "según la marca") → SIEMPRE cualificar como claim del fabricante, nunca presentar como dato independiente. Ej: ❌ *"mata el 99,99% de bacterias"* · ✅ *"Samsung afirma que mata el 99,99%"*.
9. **"Único / primero / mejor jamás"** → o citar fuente que lo respalda O suavizar (*"uno de los únicos"*, *"de los primeros en…"*). Contradicción detectada en auditoría: dos productos presentados como "primer humanoide doméstico" en el mismo artículo.

**Alternativa sin fuente:** reformular con framing de autoría.
- ❌ *"Tesla invertirá 20.000M en humanoides en 2026"*
- ✅ *"Tesla anuncia inversión masiva en humanoides para 2026"* (sin cifra)
- ✅ *"Tesla apunta a inversiones del orden de decenas de miles de millones [según Reuters](url)"*

**Verificación pre-output (grep):**

```bash
# (a) Cifras con unidades típicas sin hipertexto en la misma línea
grep -nE '[0-9]+([.,][0-9]+)?\s*(%|€|\$|millones?|mil|unidades|valoraciones|hogares|kPa|kg|puntos|estrellas|/5)' <borrador.html> | grep -v 'href='

# (b) Afirmaciones categóricas de exclusividad/primacía
grep -niE '\b(el único|la única|únic[oa] que|el primer[oa]?|la primera|el mejor|la mejor|jamás|nunca antes|récord absoluto)\b' <borrador.html>

# (c) Claims del fabricante sin framing
grep -niE '(tests? internos|según la marca|según el fabricante|la marca afirma|la compañía dice)' <borrador.html>
```

Cada match → revisar manualmente. Si no hay `<a href>` cercano ni framing → arreglar antes de entregar.

**Triaje en `/post-publish` (si aparece publicado):**
- **Evidente + fix obvio** (añadir framing "según X", sustituir una palabra, quitar una cifra sin pilar editorial) → auto-fix en `borrador.html` + `published/` + reportar. NO preguntar.
- **Ambiguo** (reescritura afecta argumento, cifra puede ser correcta pero no sé verificar en sesión) → PARAR y consultar con propuesta.

**Fundamento empírico:** auditoría 2026-04-20 de los 8 artículos publicados detectó 14 claims sin fuente o con framing deficiente (Samsung NaviBot 2003 posiblemente erróneo, Tesla 20.000M sin cita, 99,99% bacterias sin link, "el único compañero inteligente" exagerado, etc.). Lista canónica en [`references/audit-2026-04-20-unsourced-claims.md`](../../references/audit-2026-04-20-unsourced-claims.md) como corpus de referencia + ejemplos canónicos para futuros artículos.

## Anti-IA checklist — OBLIGATORIO para TODO contenido

Regla heredada de [CLAUDE.md § Output Validation](../../CLAUDE.md). Canon único: [`@references/anti-ia-checklist.md`](../../references/anti-ia-checklist.md) — §1 Universal aplica a todo (artículos, reviews, comparativas, editoriales, guías, newsletters), §2 Ficción aplica además a relatos. Skills que generan prosa publicable la integran pre-output (`content-draft § 8.5`, `ficcion-draft § 8`).

## Controles pre-publicación — 12 checks

Acabado sobre el borrador **ya cerrado** estructuralmente (tras anti-IA, tras editorial-es, tras cero-fantasma, tras datos-rastreables). Dos bloques independientes: **A) Craft** (pulido de escritura) + **B) Coherencia interna** (consistencia del artículo consigo mismo). Si cualquiera de los 12 falla → reescribir antes de entregar.

### Bloque A — Craft (5 checks)

- **A1. Gancho en el título.** Si hay tesis contrarian, va ANTES del dato. Test: leer el H1 cortado a la mitad — si la primera mitad sola no engancha, invertir orden. Patrón *"Tesis: dato"* > *"Dato. Tesis"*. Ej: ❌ *"Un humanoide ha batido el récord humano. Lo importante no es el robot"* → ✅ *"Lo importante no es el robot: un humanoide ha batido el récord humano"*.
- **A2. Blindaje de cifras contrarian.** Toda cifra contrarian citada sin adorno (`12%`, `3 de cada 10`, `0,7 s`) lleva parentética ≤10 palabras que define qué mide y qué implica fallar. Ej: ❌ *"12% en tareas reales"* → ✅ *"12% — es decir, completa la tarea sin romper nada ni a nadie — en tareas reales"*.
- **A3. Dato-trampolín prohibido.** Si un dato merece asombro (salto 2025→2026, cifra sin precedente), o tiene **párrafo corto propio** (2-3 frases: cuántos, tiempo mediano, qué ha cambiado técnicamente), o va en **frase suelta** sin verbos que sugieran escena que no se pinta. Prohibido usarlo como trampolín de paso hacia el argumento siguiente. Ej: ❌ *"cruzaron meta decenas"* en media frase camino del siguiente párrafo → ✅ *"Decenas terminaron autónomamente, frente a ninguno en 2025"* (frase suelta).
- **A4. Precisión técnica > contundencia fácil.** Escanear el borrador en busca de rotundas (*optimizado para una sola tarea*, *incapaz de*, *nunca podrá*, *siempre*, *único*, *el primero en*). Cada una debe ser técnicamente defendible. Si un lector del nicho la desmonta en Reddit en 30 segundos → resta credibilidad. Ej: ❌ *"patas optimizadas para una sola tarea"* (sobre un humanoide general-purpose) → ✅ *"patas mecánicas sin tendones ni calambres, más un equipo pendiente de su batería"*.
- **A5. Leitmotiv en el cierre.** Si el artículo repite un verbo o frase (*"leer titulares despacio"*, *"el dato que no cuentan"*), el cierre debe atarlo **literal**. La repetición remata el ritmo. Si al releer no se identifica un leitmotiv, leer el borrador entero con marcador — suele estar sin verlo. Ej: ❌ cierre que no toca la frase repetida → ✅ *"Leer titulares despacio. Ese es, por cierto, el único trabajo que un humanoide no nos va a quitar en los próximos veinte años"*.

### Bloque B — Coherencia interna (7 checks)

- **B1. Recomendación única.** Un solo "ganador" por criterio. Etiquetas *"mejor global"*, *"mejor compra"*, *"ganador"*, *"el elegido"* convergen en el mismo modelo en H2, fila highlighted de la tabla, caption y veredicto. Si el H2 dice *"mejor global: X"* y la tabla resalta *"mejor compra global: Y"* → contradicción que el 80% de lectores escaneando no descifra. Grep cruzado al cerrar: `grep -niE "mejor (global|compra|elección)|ganador|recomendamos"` — todas apuntan al mismo modelo, O a etiquetas explícitamente distintas (*"lo más nuevo"* ≠ *"mejor global"*).
- **B2. Paridad cuantitativa promesa ↔ entrega.** Toda cifra de cobertura en título/subtítulo/intro (*"6 modelos"*, *"5 preguntas"*, *"3 perfiles"*) se entrega 1:1 y contable en el cuerpo. Grep: `\b\d+\s+(modelos|preguntas|perfiles|puntos|trucos|pasos|razones|finalistas|items)\b` → contar matches en promesa y verificar que el cuerpo entrega ese número exacto en `<h2>` / `<li>` / `<tr>`. Si el subtítulo promete *"3 perfiles"* y el artículo entrega 6 etiquetas sueltas → reescribir subtítulo o construir los 3 perfiles reales. Nunca promesa colgada.
- **B3. Nomenclatura única por entidad.** Cada producto/marca/concepto usa **un solo nombre canónico** (por defecto = el del H2 de su bloque). Al cerrar: para cada producto citado ≥3 veces, listar formas usadas y unificar. Ej: ❌ *"Cecotec Conga 11090 Ultra Genesis"* (H2) + *"Conga 11090 Ultra"* (cuerpo) + *"Cecotec Conga 11090"* (tabla) → ✅ *"Cecotec Conga 11090 Ultra"* en los tres sitios.
- **B4. Criterio declarado = criterio aplicado.** Si el artículo enumera criterios de selección al principio, cada finalista los cumple. Si uno no los cumple, **justificar en el texto del propio finalista** por qué entra igual. Nunca esconder. Ej: ❌ Samsung en comparativa de aspiradores después de declarar *"toallita arrastrada no cuenta"* sin explicación → ✅ *"El Samsung no cumple al 100% el criterio 3 (usa mopa vibratoria, no rodillo ni giratoria), pero el ecosistema SmartThings lo rescata para el perfil objetivo"*.
- **B5. Paridad de tratamiento visual — TODO producto analizado lleva foto inline** (regla dura refuerzo 2026-04-23). En artículos de comparativa, guía de compra, review multi-producto o editorial que analice productos concretos, **cada producto que reciba análisis propio** — H2/H3 con nombre de modelo, bloque `<div class="model-card">` o equivalente con precio + *para quién sí / no* — **DEBE llevar al menos 1 `<img class="inline">` dentro de su sección**, con pie de foto (`<p class="fig-caption">`) y fuente citada. Sin excepciones por "ya sale en otro artículo" ni por "el fabricante no facilita render": el lector que llega por SEO a ESTE artículo concreto espera ver el producto del que le hablas. Si la foto oficial no existe, usar foto de review reputada (Xataka Home, TechRadar, Vacuum Wars, etc.) citada como fuente; si ni eso se encuentra, reconsiderar si el producto merece sección de análisis propia o baja a mención-bullet. Los productos **descartados** (bloque "los que dejamos fuera / descartados") **no requieren foto** — son referencias negativas, no objetos de análisis; un bullet con razón editorial basta. **Verificación pre-output automática** (implementada en `/content-draft § 8.5 cinco`): contar `<div class="model-card">` (y secciones equivalentes con H2/H3 de producto + bloque de precio) y verificar que cada una contenga ≥1 `<img class="inline">`; si el conteo no coincide → bloqueo del output. **Incidente origen 2026-04-23:** borrador #10 *mejor-robot-aspirador-mascotas-2026* v1 entregó 5 modelos analizados con solo 2 fotos (Ecovacs X8 y Dreame X50), argumentando en `PASOS.md` "remisión editorial al artículo #6 contenedor" como justificación para saltar Roborock / Eufy / Cecotec. Rafael rechazó al revisar: *"no puede ser que pongamos artículos y analicemos productos sin poner fotos"*. Las fotos del resto se añadieron manualmente y la regla B5 deja de aceptar asimetrías documentadas: pasa a exigir paridad dura verificada por script.
- **B6. Verificación cruzada de datos técnicos asociados.** Si dos productos se asocian narrativamente (*"chasis hermano"*, *"versión europea de"*, *"sucesor de"*, *"misma gama que"*), sus specs comparables (succión Pa, peso, autonomía, precio base) deben ser coherentes, o llevar nota aclaratoria. Ej: ❌ *"MOVA V70 Ultra (40.000 Pa), chasis hermano del Dreame X50 Ultra (~20.000 Pa)"* sin explicar la diferencia → ✅ corregir cifra o reformular (*"comparte diseño con la gama Dreame, aunque la succión declarada es superior"*). Es el tipo de dato que un lector de Reddit desmonta en 30 segundos.
- **B7. Claridad de datos comparables.** Precios/specs de distinto tipo (nuevo vs reacondicionado, PVP vs promo, distribución UE vs import, con vs sin suscripción) se etiquetan explícitamente. Ej: ❌ *"1.074 € Amazon · 711 € refurbed.es"* → ✅ *"1.074 € nuevo en Amazon · 711 € reacondicionado en refurbed.es"*. Tres palabras que evitan el malentendido.

**Incidentes origen + ejemplos completos:** memoria [`feedback_robohogar_pre_publish_polish.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_pre_publish_polish.md) — Bloque A desde artículo #8 maratón humanoide (2026-04-20); Bloque B desde *"Mejor robot aspirador 2026"* (2026-04-19).

**Aplicación operativa:**
- `/content-draft` § 8.9 — paso obligatorio pre-output: responder los 12 checks por escrito en `PASOS.md § Controles pre-publicación` con formato `[✅/❌/N/A] — [comentario]`. Si alguno falla → reescribir antes de entregar.
- `/post-publish` — auditoría ligera post-publicación: grep de B1 (*"mejor global"* cruzado), B2 (cifras promesa vs estructura entregada), B6 (*"hermano de" / "sucesor de"* + specs cruzadas). Triaje como cero-fantasma: evidente+fix obvio → auto-fix; ambiguo → parar y consultar.
- **Regla iterativa:** la lista irá creciendo. Cada nuevo incidente de feedback externo se evalúa contra los 12 checks; si revela un vicio no cubierto, se añade como A6/A7/B8/etc.

## Filtro mercado ES/LATAM

ROBOHOGAR se dirige a **España primario + LATAM secundario** (menor poder adquisitivo). No traducir viralidad anglosajona — validar salida real ES antes de aceptar un tema.

**Antes de recomendar o escribir un tema, validar 3 criterios:**

1. **Distribución ES.** ¿La marca/producto se vende en Amazon.es, MediaMarkt, Leroy Merlin, El Corte Inglés o Carrefour? Si no aparece en ninguno → probablemente viralidad US/China sin salida ES.
2. **Keyword ES medible.** ¿Google Trends España muestra búsquedas consistentes? ¿Existe la palabra clave en castellano con volumen >500/mes (orientativo)?
3. **Cobertura ES.** ¿Al menos 2 fuentes ES lo cubren — o cubren su categoría — en las últimas 4 semanas? Universo ampliado en `@references/fuentes-es-master.md` (Tier 1: Xataka, Xataka Home, El Androide Libre, Omicrono, Genbeta, Hipertextual, Menéame, Google Trends ES, El País Tech, 20minutos Tech, IA en Español 42K, EvolupedIA 40K, Topes de Gama, FayerWayer).

**Regla de decisión:** si 2 de 3 son "no" → descartar o downgrade a "contexto internacional", no artículo prioritario.

**Excepción:** editoriales mainstream (Apple, Tesla, Google, Samsung, Xiaomi) siempre aplican por reconocimiento de marca — no requieren validar los 3 criterios.

Aplicación operativa: `@.claude/commands/research-digest.md` (criterio ⭐ ES en priorización) + `@.claude/commands/content-draft.md` (check pre-borrador).
