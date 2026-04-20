# Editorial Rules

## Voz y Tono

- **Tono:** Cercano, informado, con humor sutil. Como un amigo techie que te explica qué robot merece la pena
- **Persona:** Entusiasta de la tecnología doméstica, no vendedor. Opiniones propias, no comunicados de prensa
- **Audiencia:** Adultos 30-55, España, interesados en tecnología pero no necesariamente técnicos

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

- **Acrónimos sin expandir:** `LiDAR`, `ToF`, `PVP`, `AI Act`, `CE`, `ICAM`, `LDS`, `IA`, `SmartThings`, `Matter` → expandir o contextualizar la primera vez. Ejemplos:
  - ❌ *"Usa LiDAR para mapear"* → ✅ *"Usa LiDAR (sensor láser de 360°) para mapear"*.
  - ❌ *"Conforme al AI Act"* → ✅ *"Conforme al AI Act (reglamento europeo de IA, en vigor desde 2024)"*.
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

- **Tipografía global (config Beehiiv):** headings H1/H2/H3/H4 en **DM Sans Bold**, body en **Inter Regular**. Beehiiv aplica este estilo al renderizar; los borradores generan Markdown/HTML semántico plano (sin forzar fuentes inline).

- **Política de negritas (DURA — OBLIGATORIA).**

  **✅ Permitido — negrita en párrafos de texto corrido** (intro, desarrollo, callouts `.callout-amber` / `.callout-gray`, notas, bullets fuera de `.checklist`): usar **siempre `<strong>`**, nunca `<span class="bold">` ni `style="font-weight"` inline ni `<b>`. Razón completa en el bullet siguiente.

  **❌ PROHIBIDO — BOLD NUNCA dentro de headings ni tablas ni callouts crema:**
  - **Headings H1/H2/H3/H4** (incluye emojis prefijo tipo `<h2>🏆 Nuestro veredicto</h2>` — el heading entero YA es bold por config global Beehiiv; cualquier `<strong>`/`<b>`/`**...**` dentro duplica el peso).
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
- **Cadencia:** máximo 1 cada 3-4 semanas — la ficción se cansa antes que el análisis
- **Tag visual:** "Ficciones Domésticas" + hero estilo still cinematográfico (NO product-hero). Referencia: Black Mirror doméstico, After Yang, Her
- **Obligatorio:** anclar cada relato en ≥1 dato real (AI Act, INE, spec técnica de un robot que existe). Sin dato real → fantasía genérica, se rechaza
- **Villano:** el robot NUNCA es el villano. El villano es el problema humano (soledad, burnout, brecha digital) que el robot revela o amplifica
- **Exención:** palabras "prohibidas" de la línea baseline (superlativos) permitidas solo en diálogo irónico de un personaje
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

Skill: `/ficcion-draft`. Pipeline completo: `@.claude/commands/ficcion-draft.md`.
Bible maestra + canon transversal de series: `@references/ficciones/series-bible-maestra.md`.
Knowledge base: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`.
Patrones serialized newsletter 2025: `@references/ficciones/serialized-newsletter-patterns.md`.
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

Todo contenido publicado (artículo, review, comparativa, editorial, guía, newsletter Y ficción) DEBE pasar [`@references/anti-ia-checklist.md`](../../references/anti-ia-checklist.md) antes del output final.

- **§1 Universal** aplica a todos: artículos, reviews, comparativas, editoriales, guías, newsletters.
- **§2 Ficción** aplica ADEMÁS a relatos (Palahniuk cero thought verbs, subtexto > texto, especificidad Chiang).

Skills que generan prosa publicable integran esta regla como paso pre-output obligatorio (ver `ficcion-draft.md` paso 8, `content-draft.md` paso 8.5). Cualquier nuevo skill que genere prosa publicable debe heredar esta regla.

Razón: la IA tiene tics (palabras como *tapiz/entramado/intrincado/matizado*, tricolon mecánico, em-dashes en cascada, clichés sensoriales) que el lector humano identifica sin saber nombrarlos — y en un newsletter con voz personal destruyen confianza. La checklist es la lista negra + reglas positivas que evita esto.

## Filtro mercado ES/LATAM

ROBOHOGAR se dirige a **España primario + LATAM secundario** (menor poder adquisitivo). No traducir viralidad anglosajona — validar salida real ES antes de aceptar un tema.

**Antes de recomendar o escribir un tema, validar 3 criterios:**

1. **Distribución ES.** ¿La marca/producto se vende en Amazon.es, MediaMarkt, Leroy Merlin, El Corte Inglés o Carrefour? Si no aparece en ninguno → probablemente viralidad US/China sin salida ES.
2. **Keyword ES medible.** ¿Google Trends España muestra búsquedas consistentes? ¿Existe la palabra clave en castellano con volumen >500/mes (orientativo)?
3. **Cobertura ES.** ¿Al menos 2 fuentes ES lo cubren — o cubren su categoría — en las últimas 4 semanas? Universo ampliado en `@references/fuentes-es-master.md` (Tier 1: Xataka, Xataka Home, El Androide Libre, Omicrono, Genbeta, Hipertextual, Menéame, Google Trends ES, El País Tech, 20minutos Tech, IA en Español 42K, EvolupedIA 40K, Topes de Gama, FayerWayer).

**Regla de decisión:** si 2 de 3 son "no" → descartar o downgrade a "contexto internacional", no artículo prioritario.

**Excepción:** editoriales mainstream (Apple, Tesla, Google, Samsung, Xiaomi) siempre aplican por reconocimiento de marca — no requieren validar los 3 criterios.

Aplicación operativa: `@.claude/commands/research-digest.md` (criterio ⭐ ES en priorización) + `@.claude/commands/content-draft.md` (check pre-borrador).
