---
name: ROBOHOGAR — Cero verbos de acción no realizada + cero cifras de ahorro inventadas (honestidad de primera persona)
description: Regla dura editorial. (1) "Hemos probado", "uso real", "medido", "cronometrado", "desmontado" prohibidos salvo acción literalmente ejecutada. (2) "Te ahorra 800 €" / "600 € antes de comprar" prohibidos salvo resta aritmética directa sobre precios citados con fuente. ROBOHOGAR analiza fichas + reviews, no prueba en mano.
type: feedback
originSessionId: d677cb72-9b8c-47af-bc9a-8d85e34db6f2
---
ROBOHOGAR no tiene laboratorio, no tiene los robots en mano, no desmonta unidades, no mide dB ni cronometra instalaciones. Lo que hace es análisis editorial sobre información pública: fichas oficiales, reviews internacionales (Xataka, T3, PCMag, Wirecutter, CGMagazine, YouTube), distribución ES en Amazon.es / Leroy Merlin / tiendas oficiales. Ese es el contrato con el lector.

**Verbos prohibidos en voz plural ROBOHOGAR salvo acción literalmente ejecutada:**
- `probad[oa]s?` · `probamos` · `hemos probado` · `testado` · `hemos medido` · `hemos cronometrado` · `hemos desmontado` · `hemos usado` · `lo hemos oído` · `en nuestro test` · `en nuestras pruebas` · `en mano` · `uso real en (jardines/pisos)` · `instalación en X minutos literales` · `X dB medidos` · `en los primeros meses aún pisa`

**Verbos ✅ permitidos:**
- `hemos comparado` · `hemos analizado` · `hemos leído` · `hemos seleccionado` · `hemos descartado` · `hemos cruzado` · `hemos contrastado` · `hemos verificado en [fuente]` · `nos ha sorprendido la ficha` · `nos parece` · `recomendamos` · `descartamos`

**Claims sensoriales siempre con framing:** "declarado por [marca]", "según ficha oficial", "según review de [medio]", "según usuarios verificados en [plataforma]". Sin framing → reescribir sin claim o eliminar.

**Cifras concretas de ahorro/ventaja/pérdida en subtítulos, meta descriptions, hooks, callouts o CTAs — prohibido inventar:**

- ❌ *"checklist de 7 preguntas que te ahorra 800 € antes de comprar"* (¿800 € frente a qué?)
- ❌ *"checklist de 5 preguntas que te ahorra 600 € antes de comprar"* (idem, artículo aspirador 2026 — misma mentira heredada)
- ❌ *"te ahorra 80-120 € si ya tienes X en el trastero"* (cifra inventada)
- ❌ *"Gardena Sileno te ahorra 200 €"* (diferencia arit que no corresponde con precios citados)

Sustitución honesta (de más a menos conservadora):
1. **Resta aritmética directa**: si los dos precios están citados con fuente en el mismo artículo, dar la cifra. Ej: *"el NERA te saca 900 € por encima del Worx M800"* (2.099 € − 1.199 € = 900 €, ambos con link oficial) ✅
2. **Generalización cualitativa**: *"cientos de euros"*, *"varias decenas de euros"*, *"una diferencia notable"*, *"el equivalente a una cuota de comunidad"*
3. **Sin cifra, promesa de no-error**: *"checklist para no equivocarte al comprar"*, *"checklist para no comprar de más"*, *"5 cosas que verificar antes de darle al botón"*

La versión 3 es el default cuando no haya resta aritmética defendible. La promesa "no te equivoques" es editorialmente más fuerte que una cifra inventada — el lector ES sabe que las cifras redondas en headlines son marketing.

**Why:** incidente artículo #9 *"Mejor robot cortacésped 2026"* (2026-04-21). Doble ola de mentiras detectadas por Rafael en dos pases separados de 3 segundos cada uno:

**Ola 1 — verbos de test no realizado.** El subtítulo abría con *"6 modelos probados, de 1.099 € a 2.499 €…"*. Rafael: *"cómo es posible que la primera frase del artículo sea algo que tenemos remarcado 200 veces: 'no tienes que poner mentiras'… resulta que la primera frase de todo el artículo es una mentira"*. Además contenía *"filtro de uso real en jardines españoles, no ficha técnica en frío"* (exactamente lo contrario de la realidad), *"instalación en 30 minutos literales"*, *"57 dB medido"*, *"en primeros meses aún pisa alguna flor"*.

**Ola 2 — cifras de ahorro inventadas.** Tras corregir los verbos, el subtítulo quedó con *"checklist de 7 preguntas que te ahorra 800 € antes de darle al botón"*. Rafael volvió a parar: *"has vuelto a poner otra mentira, que con la checklist se ahorran 800 €. Ya lo habías hecho en otro artículo. No tenemos que poner si se han ahorrado 800 €. Basta que pongas que se han ahorrado cientos de euros por el checklist y ya está"*. En el cuerpo también había *"ahorra 80-120 € al usuario que ya tiene algo de Worx"* y *"Gardena te ahorra 200 €"*, ambas cifras inventadas sin base aritmética sobre precios citados.

**Antecedente:** el artículo aspirador 2026 ya tenía las mismas dos mentiras (*"Probados 14 robots en pisos españoles"* + *"checklist de 5 preguntas que te ahorra 600 € antes de comprar"*) y se coló por inercia al usar ese HTML como referencia. El artículo aspirador publicado debe corregirse en post-publish.

**How to apply:**
- `/content-draft` § 8.4 quater — grep obligatorio pre-entrega sobre los verbos prohibidos. ≥1 match sin framing "según [fuente]" → rechazar output.
- `/post-publish` — grep final sobre HTML publicado. Evidente + fix ≤1 frase → auto-fix y reportar. Estructural → parar y consultar.
- Al redactar cualquier frase con "hemos X" o "nos Y", preguntarse: *"¿realmente hemos hecho X/Y?"*. Si no, reescribir con verbo honesto.
- Al copiar estructura de un artículo previo como referencia (ej. `mejor-robot-aspirador-2026` como base de `mejor-robot-cortacesped-2026`), NO heredar el copy del subtítulo/hook/intro por inercia — releer cada frase contra esta regla. Los artículos previos pueden tener mentiras heredadas sin detectar.

**Fuente de verdad:** `@rules/editorial.md § Honestidad de primera persona — cero verbos de acción no realizada`. Complementa "Voz de autoridad propia" (no narrar el proceso de investigación) y "Cero referencias fantasma" (no prometer elementos que no existen).

**Regla de actitud:** ROBOHOGAR no hace marketing, hace análisis editorial riguroso. El escape fácil ("X modelos probados" es marketing clásico) es el que rompe el contrato editorial. Una sola mentira rompe la voz entera del artículo para el resto del texto.
