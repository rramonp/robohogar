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
- Robots se refiere siempre a robótica DOMÉSTICA (aspiradores, cortacésped, humanoides para hogar)

## Newsletter (semanal)

- 3-5 noticias curadas con comentario editorial
- 1 sección fija rotativa (review, comparativa, tutorial, opinión)
- Máximo ~1500 palabras por issue
- Subject lines: cortas, curiosas, sin clickbait

## Narrativa especulativa — Ficciones Domésticas

Pilar experimental (~10% del content mix). Relatos cortos de ciencia ficción doméstica próxima (2030-2040) con personajes recurrentes. Reglas que RELAJAN explícitamente la voz baseline:

- **Voz (excepción a la regla de primera persona plural):** en ficción se usa narrador omnisciente en 3ª persona O primera persona del personaje POV. El "hemos/os/nos" plural editorial NO aplica dentro del relato
- **Tiempo verbal:** presente (inmediatez) o pasado (reflexión). No mezclar en la misma escena sin justificación narrativa
- **Longitud:** flash 500-1.000 palabras · relato corto 1.500-3.000 · mini-serie 6-12 episodios de 1.500-3.000
- **Cadencia:** máximo 1 cada 3-4 semanas — la ficción se cansa antes que el análisis
- **Tag visual:** "Ficciones Domésticas" + hero estilo still cinematográfico (NO product-hero). Referencia: Black Mirror doméstico, After Yang, Her
- **Obligatorio:** anclar cada relato en ≥1 dato real (AI Act, INE, spec técnica de un robot que existe). Sin dato real → fantasía genérica, se rechaza
- **Villano:** el robot NUNCA es el villano. El villano es el problema humano (soledad, burnout, brecha digital) que el robot revela o amplifica
- **Exención:** palabras "prohibidas" de la línea baseline (superlativos) permitidas solo en diálogo irónico de un personaje

Skill: `/ficcion-draft`. Pipeline completo: `@.claude/commands/ficcion-draft.md`.
Knowledge base: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`.

## Filtro mercado ES/LATAM

ROBOHOGAR se dirige a **España primario + LATAM secundario** (menor poder adquisitivo). No traducir viralidad anglosajona — validar salida real ES antes de aceptar un tema.

**Antes de recomendar o escribir un tema, validar 3 criterios:**

1. **Distribución ES.** ¿La marca/producto se vende en Amazon.es, MediaMarkt, Leroy Merlin, El Corte Inglés o Carrefour? Si no aparece en ninguno → probablemente viralidad US/China sin salida ES.
2. **Keyword ES medible.** ¿Google Trends España muestra búsquedas consistentes? ¿Existe la palabra clave en castellano con volumen >500/mes (orientativo)?
3. **Cobertura ES.** ¿Al menos 2 fuentes ES lo cubren — o cubren su categoría — en las últimas 4 semanas? Universo ampliado en `@references/fuentes-es-master.md` (Tier 1: Xataka, Xataka Home, El Androide Libre, Omicrono, Genbeta, Hipertextual, Menéame, Google Trends ES, El País Tech, 20minutos Tech, IA en Español 42K, EvolupedIA 40K, Topes de Gama, FayerWayer).

**Regla de decisión:** si 2 de 3 son "no" → descartar o downgrade a "contexto internacional", no artículo prioritario.

**Excepción:** editoriales mainstream (Apple, Tesla, Google, Samsung, Xiaomi) siempre aplican por reconocimiento de marca — no requieren validar los 3 criterios.

Aplicación operativa: `@.claude/commands/research-digest.md` (criterio ⭐ ES en priorización) + `@.claude/commands/content-draft.md` (check pre-borrador).
