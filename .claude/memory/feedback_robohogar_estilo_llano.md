---
name: Estilo prosa ROBOHOGAR — llano, sin florituras
description: Voz ROBOHOGAR es ES habitual de andar por casa. No metáforas que intentan sonar guay (matemáticas de cuarto de la ESO, tu sábado, etc), no em-dashes decorativos, no inversiones para estilo. Ejemplo canónico del registro tras incidente 2026-04-28
type: feedback
---

Regla dura establecida por Rafael 2026-04-28 tras 3 iteraciones del primer párrafo de §1 en `robot-cortacesped-rentabilidad-3-anos`. Cita literal: *"que no intente parecer algo súper guay, que suena fatal"* + *"florituras que has intentado hacer, que no tienen ningún sentido en español"*.

**Regla:** la prosa de artículos ROBOHOGAR (no-ficción: review, comparativa, guía, editorial, tutorial) usa ES habitual, llano, de andar por casa. Que se entienda al primer pase y al leerse en voz alta. NO intentar sonar guay, ingenioso o literario. Las florituras anglo-traducidas o las metáforas culturales rebuscadas no encajan en la voz ROBOHOGAR — suenan fatal en castellano normal y distancian al lector.

**Why:** la audiencia ROBOHOGAR es 30-55 ES, interesada en robótica doméstica, no necesariamente del mundo finance/marketing/tech-twitter. Lee el contenido para tomar una decisión de compra de 500-2.500 €. Cualquier giro que requiera releer una frase para entenderla, o que sugiera *"el autor se está esforzando por ser ingenioso"*, rompe la confianza editorial. El registro objetivo es el de una conversación con un amigo techie que sabe del tema y te lo explica claro — NO el de una columna de opinión que busca destacar por estilo.

**How to apply (regla operativa simple):**

**Patrones PROHIBIDOS** (ejemplos del incidente origen 2026-04-28):

| ❌ Floritura | ✅ Plano |
|---|---|
| *"matemáticas de cuarto de la ESO con cuatro datos"* | *"solo hacen falta cuatro datos"* |
| *"depende de cuánto vale tu sábado"* | *"depende de cuántas horas le dedicas hoy"* |
| *"la cuenta a 3 años que no te hace ningún comercial"* | *"la cuenta a 3 años, sin trampas"* |
| *"el robot no se paga solo 'porque es muy moderno'"* | *"el robot no se paga solo por ser moderno"* (sin ironía entrecomillada) |
| *"Aquí los m² te juegan en contra"* | *"Aquí los metros cuadrados no compensan"* |
| *"la cuenta es brutal y a favor del robot"* | *"la diferencia es grande y a favor del robot"* |
| *"salvo masoquismo"* | *"salvo que disfrutes haciéndolo"* |
| *"la mejor decisión que vas a tomar este año"* | *"la decisión más rentable para ese caso"* |
| *"Aquí va al revés"* (eco confuso) | *"Aquí lo hacemos en orden: primero X, después Y"* |
| *"sin descuentos imaginarios"* | *"con precios reales, no promociones"* |

**Patrones permitidos** (lo que SÍ es voz ROBOHOGAR):

- Frases declarativas SVO directas: *"Para saber si te compensa solo hacen falta cuatro datos."*
- Listas explícitas: *"Primero tu situación, después el robot."*
- Comparaciones llanas: *"Si empiezas mirando el robot, terminas justificando una compra que ya habías decidido."*
- Conectores ES neutros: *"y", "pero", "porque", "lo que pasa es que", "la diferencia es", "conviene"*. Cero conectores anglo (*"sin embargo"*, *"de hecho"*, *"por supuesto"*, *"en definitiva"*).
- Em-dashes solo cuando aclaran (inciso) o introducen ejemplo concreto. NO em-dashes como decoración para conectar dos turnos ingeniosos.
- Tecnicismos solo cuando aportan: si una palabra ES neutra hace el mismo trabajo, va la ES neutra.

**Test del párrafo bueno** (Rafael validó este como referencia el 2026-04-28):

> *"Para saber si te compensa un robot cortacésped solo hacen falta cuatro datos. Lo difícil no es hacer la cuenta, es hacerla en el orden correcto: primero tu situación, después el robot. Si empiezas mirando el robot, terminas justificando una compra que ya habías decidido."*

Características que lo hacen bueno y que se buscan reproducir:
- Sujeto + verbo + complemento, sin inversiones.
- Cero metáforas culturales (cuarto de la ESO, tu sábado, etc).
- Cero "trying-to-be-clever" turns.
- Em-dashes ausentes; dos puntos cuando hace falta separar idea de ejemplo.
- El final cierra con observación útil, no con remate ingenioso.

**Aplicación inversa (lo que sigue siendo válido):**

- Hooks pueden tener gancho fuerte (es el cold open), pero el gancho viene de un dato o una contradicción concreta, no de un giro estilístico (*"el robot no se paga solo porque es muy moderno"* ❌ vs *"el robot se paga solo solo si tu jardín pasa de 400 m² y tu sábado vale algo"* ✅).
- Veredictos pueden ser categóricos (*"no compres robot"*, *"el robot es la mejor opción"*) — eso es voz editorial, no floritura.
- Humor sutil del CLAUDE.md sigue permitido: pero "humor sutil" es comentario lateral con gracia natural, no metáfora forzada que requiere descodificarse.
- Ficción Doméstica (relatos cortos) tiene reglas distintas — ahí sí cabe prosa literaria peninsular (Adón, Mesa, Aramburu, etc.). Esta regla aplica solo a no-ficción.

**Aplicación operativa en skills:**

- `/content-draft` paso 8.5 bis carga `references/editorial-es/01-articulos-y-columnas.md` antes de escribir prosa. Esa regla refuerza esto: la voz objetivo es la del periodismo tech ES (Eva R. de Luis Xataka, Antonio Ortiz Error500), no la del articulista literario.
- Verificación pre-output: antes de cerrar el borrador, releer cada párrafo preguntando *"¿estoy intentando sonar guay aquí?"*. Si la respuesta es sí → reescribir plano.

**Incidente origen 2026-04-28:** primer párrafo de §1 en `robot-cortacesped-rentabilidad-3-anos` borrador #14. Tres iteraciones:
- v1 (mía): *"La cuenta del ROI no es complicada — es matemática de cuarto de la ESO con cuatro datos."* + *"Aquí va al revés."* — Rafael preguntó *"¿qué significa ROI?"* (curse-of-knowledge, ya documentado aparte) y declaró que no le sonaba.
- v2 (mía, post-ROI fix): *"La cuenta de la rentabilidad no es complicada — es matemática de cuarto de la ESO con cuatro datos. El error de los anuncios de fabricante es invertir el orden..."* — seguía sin gustar.
- v3 (mía, plana): *"Para saber si te compensa un robot cortacésped solo hacen falta cuatro datos. Lo difícil no es hacer la cuenta, es hacerla en el orden correcto..."* — **validada por Rafael**: *"haz esto la forma habitual, no las florituras"*.

La diferencia entre v2 y v3 NO es información (ambas dicen lo mismo) — es registro. v3 es el registro objetivo. Internalizar.

**Patrón de referencia para futuros artículos:** auditar cada párrafo del cuerpo y de hooks/veredicto/¿sabías que? contra esta regla antes de cerrar el output. Si un párrafo necesita defenderse con *"es que esto está bien escrito"* o *"es ingenioso"*, reescribir plano.
