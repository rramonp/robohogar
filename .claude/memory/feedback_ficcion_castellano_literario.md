---
name: ficcion — castellano literario peninsular obligatorio
description: La prosa de ficción ROBOHOGAR debe pasar el knowledge base de castellano literario ES (referentes peninsulares + checklist anti-calco EN→ES) cargado por /ficcion-draft paso 6 antes de generar prosa
type: feedback
originSessionId: 215f8fd4-18e5-4b10-a009-a5542c922b93
---
La prosa narrativa de **ficción ROBOHOGAR** (skill `/ficcion-draft`) debe pasar la checklist del knowledge base [`references/ficciones/castellano-literario-es.md`](../../robohogar/references/ficciones/castellano-literario-es.md) — el archivo destila 10 referentes ES peninsulares contemporáneos (Urraca · Amat · Morales · Martínez · de la Cruz · Adón · Barba · Moreno · Mesa · Otero) con muestras textuales reales, 12 calcos EN→ES específicos de prosa narrativa con alternativas literarias, y 12 recursos ES positivos (perífrasis verbales vivas, voz media reflexiva, imperfecto modulador, oraciones nominales en cierre, dativo ético, coloquialismos peninsulares).

**Why:** incidente Rafael 2026-04-19 sobre *El operador nocturno v1* — diagnostica que el castellano "está bastante flojo, como traducido del inglés, poco fluido y aburrido". Diagnóstico técnico confirmó 25-30% de frases con calcos del inglés concretos: orden SVO rígido con pronombre explícito redundante, gerundios y "al + infinitivo" mecánicos, construcciones nominales recursivas, cierres staccato Hemingway sin afecto narrativo, bloques administrativos sin digestión narrativa de la voz del personaje. El gap del repo era ausencia de un knowledge base de prosa narrativa española literaria contemporánea — había frameworks universales (Pixar, MRUs, Paint The Villain) y auditoría ES de copy/UX (anti-anglicismos en saludos, CTAs), pero ningún modelo de cómo suena buena ficción en español peninsular.

**How to apply:**

- **Punto de carga obligatorio:** `/ficcion-draft` paso 6 carga el knowledge base ANTES de generar prosa. El prompt MRU se reformuló en español (no inglés) y declara registros por escena con referentes citados (escena íntima → Urraca/Adón; escena administrativa → Cristina Morales fricción de registros; escena outsider → Lara Moreno *La menuda* + Mesa).
- **Verificación pre-output (paso 8.3 nuevo del skill):** correr 5 grep automáticos sobre el borrador antes de cerrar:
  - `sus (manos|ojos|piernas|brazos|labios|dedos|pies|hombros|rodillas|cabezas?)` → 0 (calco posesivo cuerpo)
  - `de repente` → ≤1
  - `[a-z]+mente` → ≤4 en standalone (≤2 en flash)
  - `(fue|fueron|era|eran) [a-z]+ad[oa]s?` → revisar (pasiva ser+participio)
  - `sin embargo|de hecho|por supuesto|en definitiva` → ≤1 cada uno
- **Recursos ES positivos a preservar/buscar:** ≥1 perífrasis verbal viva (`se quedó mirando`, `lleva sin`), ≥1 voz media reflexiva (`se le cayó`), ≥1 coloquialismo peninsular en diálogo donde aplique al personaje (`qué cuco`, `el cabrón`, `fíjate`, `vamos`, `a ver` — sin saturar, max 1-2 por escena), ≥1 oración nominal sin verbo principal en cierre rítmico.
- **Voz por personaje:** declarar registro (edad + lugar + clase + muletilla recurrente) ANTES de generar diálogo. Test: tapar acotaciones, ¿se distingue quién habla? Si no, reescribir.
- **Tecnología digerida (criterio ROBOHOGAR específico):** el robot debe tener mote afectivo en focalización interior de al menos un personaje (no solo *"el humanoide"* en todas las escenas). Términos técnicos siempre con caracterización del narrador o personaje, nunca neutros tipo glosario.
- **Anclaje genérico técnico — REGLA DEL BALANCE (refinamiento 2026-04-19, `castellano-literario-es.md § 7.1`):** cada escena del relato contiene **≥1 mención del término técnico genérico** correspondiente a la categoría editorial (`humanoide` · `aspirador` · `cortacésped` · `mascota-robot` · `fregasuelos` · `autómata` · `androide`). Esto preserva coherencia con tags Beehiiv, llms.txt y lectores que llegan desde el catálogo. Después del anclaje, **libertad léxica POV** (*aparato*, *bicho*, *cabrón*, *chisme*, *armatoste*) según registro del personaje. Origen del refinamiento: feedback Rafael 2026-04-19 sobre v2 — la voz peninsular era buena pero el término *"humanoide"* desapareció completamente, debilitando el anclaje editorial. Solución: 1 anclaje + libertad. Patrón canónico aplicado en *El operador nocturno v2*: 1×*humanoide* + ~6-10×*aparato* por escena.
- **Jerga sci-fi clásica permitida (`castellano-literario-es.md § 7.2`):** Asimov (*autómata*, *modelo*, *unidad*), Dick (*androide*, *réplica*, *simulacro*), Tchaikovsky (*espécimen*, *terminal*), genérico contemporáneo (*humanoide*, *unidad doméstica*, *asistente robótico*). Bienvenida en escenas corporativas/técnicas y bocas de personajes verosímiles (técnicos, periodistas, vendedores). Evitar en boca de personajes ajenos al sector salvo justificación. Respeta canon ROBOHOGAR (sin marcas comerciales reales en narrador).
- **Regla de decisión:** ≥4 fallos en checklist completa → reescribir el relato; 1-3 fallos → reescribir párrafos concretos.
- **Caso canónico de aplicación:** *El operador nocturno v2* (2026-04-19) — reescritura del v1 aplicando esta convención. Subió de 2.336 → 2.898 palabras (encadenar suele alargar), bajó adverbios -mente de 7+ a 3, eliminó 0 calcos posesivo+cuerpo, transformó bloques administrativos del call center en voz Miguel digerida, reformuló cierre Hemingway *"No es luz dentro. Es un reflejo"* en frase con afecto narrativo *"que algunas cosas parecen que dan luz cuando solo la devuelven"*. Preservados intactos los pasajes que YA funcionaban en v1: *"No es un perro, Martín"*, *"Qué cuco, el cabrón"*, *"Nadie. Nadie importante"*, frase tagalo, detalles culturales (Hacendado, descansillo, cobalto).

**Cross-references obligatorios:**
- Knowledge base canónico: [`references/ficciones/castellano-literario-es.md`](../../robohogar/references/ficciones/castellano-literario-es.md)
- Skill que lo carga: [`.claude/commands/ficcion-draft.md`](../../robohogar/.claude/commands/ficcion-draft.md) pasos 6, 8.3, 9
- Quick check en checklist universal: [`references/anti-ia-checklist.md § 2.9`](../../robohogar/references/anti-ia-checklist.md)
- Convivencia con frameworks universales: el knowledge ES no sustituye a Pixar/MRUs/Paint The Villain — los complementa con la capa de voz literaria peninsular.

**Iteración futura:** si Rafael detecta nuevas frases que suenan a traducción tras aplicar este knowledge, registrar el patrón concreto en `references/ficciones/castellano-literario-es.md § 3` (calcos EN→ES) con cita textual del fallo y alternativa literaria. La checklist evoluciona con cada nuevo incidente editorial.
