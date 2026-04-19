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

Aplicable a artículos (reviews, comparativas, guías, editoriales) y a la prosa narrativa de ficciones (no al diálogo — un personaje puede hablar con la jerga que le toque). Heredado por `/content-draft § 9 Prohibiciones` y `/ficcion-draft § 8.2`.

## Apertura y cierre del cuerpo del email — anti-anglicismos

Auditoría 2026-04-19 de 20 newsletters ES de éxito detectó 0 uso de estos patterns anglo traducidos. Prohibidos en cualquier email, intro de artículo, post social o copy visible al lector:

- **Aperturas prohibidas:** `"Hola X"` + nombre · `"Hola amigo/a"` · `"Querido/a lector/a"` · `"Hey"` · `"Espero que estés bien"` · `"¿Qué tal la semana?"` · `"Hope you're well"` traducido en cualquier forma.
- **Cierres prohibidos:** `"Cheers"` · `"Best"` · `"Saludos cordiales"` (registro corporativo anglo) · `"Atentamente"` al cierre de newsletter.
- **Default ROBOHOGAR apertura:** entrada directa al tema sin saludo, o `"Buenos días."` + primera frase (patrón Kloshletter/medios ES). En ficción se aplican excepciones de diálogo (ver `/ficcion-draft`).
- **Default ROBOHOGAR cierre:** firma institucional ("ROBOHOGAR") + tagline opcional. `"Un abrazo"` aceptable solo en editoriales/ficciones personales, nunca en newsletter semanal estándar.
- **Em-dash (`—`) en trust-lines ≤15 palabras** (bajo botón, bajo subtítulo, OG description): prohibido. Es tic anglo (`" — "` con espacios). Usar coma, punto o dos puntos. En titulares de artículo y prosa del cuerpo sí está permitido.

Referencia completa: `@references/research-newsletters-es-2026-04-19.md`. Skills que generan copy al lector (`/content-draft`, `/ficcion-draft`, `/social-content`, `/pdf-brand`) aplican esta regla como verificación pre-output. El validator de `/pdf-brand` (`skills/pdf_brand/validators.py`) bloquea los patrones listados con regex.

## Formato técnico (Beehiiv)

- **Tipografía global (config Beehiiv):** headings H1/H2/H3 en **DM Sans Bold**, body en **Inter Regular**. Beehiiv aplica este estilo al renderizar; los borradores generan Markdown/HTML semántico plano (sin forzar fuentes inline).
- **Política de negritas.** SÍ en párrafos de texto corrido (cualquier variante: intro, desarrollo, callout simple, nota). NO en:
  - Headings H1/H2/H3 — el bold inline duplica el global setting
  - Tablas: `<thead>` nunca en bold (Beehiiv ya lo estiliza); en `<tbody>` solo la **columna 1** (etiqueta de fila: modelo, categoría, etc.) puede ir en `<strong>` para anclar la mirada en escaneo móvil. Las columnas 2+ siempre regular.
  - Recuadros checklist (div `.checklist` con fondo crema `#FFF9EF` + borde `#F5A623`) — los items van en peso regular
  - Nunca `## **Título**`, ni `<li><strong>...</strong>` dentro de `.checklist`. Al copiar de fuentes externas, limpiar bold embebido antes de publicar.
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

- **Cliffhanger:** emocional o moral, NUNCA físico primario (incoherente con "robot = instrumento neutro"). Detalle: `@references/ficciones/serialized-newsletter-patterns.md` § 3.4.

Skill: `/ficcion-draft`. Pipeline completo: `@.claude/commands/ficcion-draft.md`.
Bible maestra + canon transversal de series: `@references/ficciones/series-bible-maestra.md`.
Knowledge base: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`.
Patrones serialized newsletter 2025: `@references/ficciones/serialized-newsletter-patterns.md`.
Roadmap ebook: `@references/ficciones/ebook-roadmap.md`.

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
