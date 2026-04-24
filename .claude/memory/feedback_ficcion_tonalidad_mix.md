---
name: ficcion — sistema tonal canon Black Mirror
description: Ficciones Domésticas ROBOHOGAR rige por matriz tonal canon 40/15/25/10/10 (inquietante / radical / ambiguo / inspirador / mundano), sello casa Black Mirror-adjacent 80% del catálogo, criterio anti-triste reforzado para inspirador
type: feedback
originSessionId: 215f8fd4-18e5-4b10-a009-a5542c922b93
---
Las ficciones de ROBOHOGAR (skill `/ficcion-draft`) se rigen por un **sistema tonal canon** definido en [`references/ficciones/tonalidad-y-mix-editorial.md`](../../robohogar/references/ficciones/tonalidad-y-mix-editorial.md). Matriz objetivo del catálogo macro:

- 🩻 **Inquietante** — 40% (sello casa Black Mirror; incluye subcategoría inquietante-heavy)
- 🪤 **Radical** — 15% (territorio extremo: asesinato, manipulación severa, perversión moral)
- 🤔 **Ambiguo moral** — 25% (sin villano claro; el lector duda en votar)
- 💚 **Inspirador** — 10% (positivo de verdad, NO triste)
- 🍵 **Mundano** — 10% (slice of life especulativo, respiro)

**Sello dominante:** Black Mirror-adjacent = 80% (inquietante + radical + ambiguo). Inspirador + mundano = 20% para rango emocional.

**Why:** feedback Rafael 2026-04-19 sobre *El operador nocturno v2* — bien escrito pero "demasiado mundano" (lector dice *"hmm ok"* en lugar de *"joder"*). Rafael quiere que las ficciones sean **inolvidables**, estilo Black Mirror, no slice of life cotidiano. Aceptó pequeño % mundano (10-15%) como respiro pero NO como sello. Validó matriz 40/15/25/10/10 tras revisar 20 historias propuestas + 5 nuevas inquietante-heavy + 1 reescritura.

**How to apply:**

- **Auto-balanceo del catálogo (skill `/ficcion-draft` paso 0.5):** al invocar sin tonal explícito, el skill lee el catálogo histórico (frontmatter `categoria-tonal` de relatos publicados), calcula % real por categoría sobre los últimos 12 relatos, identifica la categoría con mayor déficit en puntos porcentuales respecto a la matriz objetivo, y propone esa como default. Rafael puede sobrescribir con `--tono=X`. Si fuerza misma categoría 3 veces seguidas, skill avisa que el mix se está desviando.
- **Frontmatter del relato:** campo obligatorio `categoria-tonal: inquietante | inquietante-heavy | radical | ambiguo | inspirador | mundano`.
- **Modulación del framework por categoría tonal (skill paso 3):**
  - Inquietante / inquietante-heavy → Pixar Spine + foreshadowing acto 1 + revelación parcial acto 2 + cliffhanger emocional con elisión.
  - Radical → Spine acelerado + apertura cotidiana engañosa + cierre irreversible + alguien sigue como si nada.
  - Ambiguo → Spine bifurcado, dos posiciones igual de defendibles + decisión sin juicio narrativo.
  - Inspirador → Spine suave + descubrimiento gradual + cierre positivo SIN PENA RESIDUAL (criterio anti-#16: inspirador-triste cae en inquietante disfrazado).
  - Mundano → 5-Sentence Story para flash + cierre descriptivo plano sin promesa.
- **Validación pre-output (skill paso 9):** desenlace coherente con `categoria-tonal` declarada. Si inquietante → final con elisión (alguien calla / borra / acepta en silencio); si inquietante-heavy → vuelta de tuerca obligatoria territorio incómodo; si inspirador → prohibido cerrar con muerte/duelo/pérdida.
- **Subcategoría inquietante-heavy:** dentro del 40% inquietante, una porción es heavy (manipulación íntima, voyeurismo coordinado, coerción suave por dark patterns) más cerca de radical sin llegar. Es lo que separa Black Mirror clásico de Black Mirror flojo. Caso canónico aplicado: *El operador nocturno v3* (2026-04-19) — Joel Santos calibra audio sintetizado durante 7 noches para inducir el despertar del niño y verle la cara, sustituye ritual de su hijo perdido Aldwin.
- **Backlog tonal validado:** 22 historias clasificadas por categoría en [`content/calendario-editorial.md § Backlog tonal validado 2026-04-19`](../../robohogar/content/calendario-editorial.md). 5 inquietantes-heavy nuevas + 1 reescritura + 16 validadas en primera ronda. 2 descartadas (#5 humanoide adelgaza, #16 cortacésped huérfano por inspirador-triste).

**Antipatrones documentados:**

- **Inspirador-triste** (criterio anti-#16): cierre con muerte/duelo/pérdida disfrazado de mensaje positivo. Eso NO es inspirador, es inquietante con etiqueta equivocada. Ejemplo descartado: niño huérfano que hereda cortacésped programado por su madre fallecida — cierre triste, NO entra en inspirador.
- **Mundano largo:** mundano funciona en formato flash (500-800 palabras). Un mundano standalone (>1.500) sin gancho es solo flojo.
- **Falsa ambigüedad:** narrador finge equilibrio pero el desenlace deja claro quién tenía razón. Si el ambiguo no genera duda real, no es ambiguo.
- **Inquietante "hmm ok":** situación curiosa pero sin consecuencia emocional para los personajes. Caso original *El operador nocturno v2* — la v3 corrige con vuelta de tuerca.

**Cross-references obligatorios:**
- Documento canon completo: [`references/ficciones/tonalidad-y-mix-editorial.md`](../../robohogar/references/ficciones/tonalidad-y-mix-editorial.md)
- Skill que lo carga: [`.claude/commands/ficcion-draft.md`](../../robohogar/.claude/commands/ficcion-draft.md) pasos 0.5, 3, 9
- Backlog tonal: [`content/calendario-editorial.md § Backlog tonal validado`](../../robohogar/content/calendario-editorial.md)
- Voz literaria peninsular (capa independiente): [`references/ficciones/castellano-literario-es.md`](../../robohogar/references/ficciones/castellano-literario-es.md)
