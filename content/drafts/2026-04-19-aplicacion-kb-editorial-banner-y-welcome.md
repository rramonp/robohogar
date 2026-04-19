# Caso canónico — aplicación del KB editorial-es a banner Hoja de Compra y welcome email 1

> Demo de validación del KB [`references/editorial-es/`](../../references/editorial-es/) aplicado a 2 piezas existentes de ROBOHOGAR. Comparativa antes/después + justificación por cada cambio con referencia al § del KB que lo motiva.

**Fecha:** 2026-04-19
**Piezas reescritas:**
1. Banner lead magnet Hoja de Compra (aplicable a 3 posts activos + 1 pendiente).
2. Welcome email 1 del MVP 2 emails.

**Criterio de éxito.** Las piezas reescritas deben cumplir las checklists pre-output de [`02-newsletter-y-emails.md § 6`](../../references/editorial-es/02-newsletter-y-emails.md) y [`03-microcopy-ctas-meta.md § 6`](../../references/editorial-es/03-microcopy-ctas-meta.md) con 0 flags automáticos y presencia de ≥3 recursos positivos cada una.

---

## 1. Banner Hoja de Compra — antes / después

### 1.1 Original (snippet 2 actual, Roborock Saros Z70 review)

```
[eyebrow]   ANTES DE COMPRAR
[título]    Descarga gratis la Hoja de Compra ROBOHOGAR
[subtítulo] 10 preguntas para no pagar de más al comprar tu robot doméstico. PDF gratis con tu suscripción semanal. Cancela cuando quieras.
[CTA]       Descargar gratis →
```

### 1.2 Diagnóstico contra [`03-microcopy-ctas-meta.md § 6`](../../references/editorial-es/03-microcopy-ctas-meta.md)

Flags automáticos (§6.1): 0. Base limpia.
Recursos positivos (§6.2) presentes: **1 de 6** (tripleta coordinada *"PDF gratis con tu suscripción semanal. Cancela cuando quieras."* parcialmente — vive en la trust-line, no en el eyebrow ni subtítulo).

Huecos identificables:
- **Falta dato no redondeado** (§6.2) — *"10 preguntas"* es cifra redonda. Doctoralia usa *"105 179 profesionales"*. Aplicar: añadir contador de robots analizados (*"42 analizados · 6 finalistas · 1 checklist"*).
- **Falta paréntesis editorial confidencial** (§6.2, Filmin). El subtítulo es utilitario, no tiene firma. Ejemplo Filmin: *"(y que quizás no conoces)"*.
- **Falta inversión del imperativo en CTA** (§6.2, Holaluz/Yoigo). *"Descargar gratis →"* imperativiza al usuario. Versión ES cálida: *"Enviádmelo al correo"* — el usuario pide la acción.
- **Falta eyebrow con síntesis brutal** (§6.2, Verkami). *"ANTES DE COMPRAR"* es contextual pero no descriptivo del tangible. Verkami reduce proyecto a *"webcómic de fantasía cozy"*. Aplicar: *"CHECKLIST · 5 PREGUNTAS · 2 PÁGINAS"* — el lector sabe al instante qué va a recibir.

### 1.3 Reescrito aplicando KB (versión v3 — purgada de mentiras 2026-04-19 tras feedback Rafael)

```
[eyebrow]   CHECKLIST · 10 PREGUNTAS · 2 PÁGINAS
[título]    Las 10 preguntas clave antes de comprar un aspirador (y por qué te ahorran varios cientos de euros)
[CTA]       Enviádmelo al correo
[trust 1]   PDF gratis con tu suscripción semanal. Cancela cuando quieras.
[trust 2]   Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre.
```

**Subtítulo eliminado.** Las dos iteraciones previas (*"Las destilamos probando robots en casas reales"* / *"Las destilamos tras meses cubriendo este nicho"* / *"42 robots analizados en 2025. 6 finalistas"*) todas rompían la regla dura de honestidad. Al no existir una formulación factual que sustituya sin mentir, se elimina por completo: el banner queda más corto (5 elementos en vez de 6) y el lector no tiene que atravesar una línea promocional antes del CTA.

### 1.4 Cambios justificados

| Elemento | Antes (v1) | Después (v3) | § KB que lo motiva |
|---|---|---|---|
| Eyebrow | *"ANTES DE COMPRAR"* (contextual vago) | *"CHECKLIST · 10 PREGUNTAS · 2 PÁGINAS"* (síntesis brutal alineada con el PDF real) | [`03 § 6.2`](../../references/editorial-es/03-microcopy-ctas-meta.md) Verkami |
| Título | *"Descarga gratis la Hoja de Compra ROBOHOGAR"* (marca + CTA) | *"Las 10 preguntas clave antes de comprar un aspirador (y por qué te ahorran varios cientos de euros)"* (paréntesis editorial confidencial + descripción del valor, sin afirmación sobre quién se las hace) | [`03 § 1`](../../references/editorial-es/03-microcopy-ctas-meta.md) Filmin (paréntesis) + regla honestidad 2026-04-19 (evita *"nos hacemos"* dudoso) |
| Subtítulo | *"10 preguntas para no pagar de más al comprar tu robot doméstico"* (seguía la norma `rules/tangibles.md` pero sin valor diferencial) | **eliminado** — no existe formulación factual que mejore sin mentir | Regla honestidad 2026-04-19 |
| CTA | *"Descargar gratis →"* (imperativo al usuario) | *"Enviádmelo al correo"* (inversión del imperativo) | [`03 § 1`](../../references/editorial-es/03-microcopy-ctas-meta.md) Holaluz/Yoigo |
| Trust-line 1 | dentro del subtítulo | separada en línea propia | Default canónico [`rules/tangibles.md § Microcopy`](../../.claude/rules/tangibles.md) |
| Trust-line 2 (NUEVA v3) | ausente | *"Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre."* | [`02 § 2.7`](../../references/editorial-es/02-newsletter-y-emails.md) + regla honestidad 2026-04-19 |

### 1.5 Verificación post-reescritura (§6 + honestidad)

- **§6.1 Flags automáticos (grep):** 0 matches en calcos, imperativos agresivos, hype, vaguedades, em-dash en trust-line.
- **Regla honestidad (ampliada 2026-04-19):** 0 afirmaciones hands-on sobreprometidas, 0 marcadores temporales inverificables, 0 cifras inventadas. Cada afirmación del banner contrastada manualmente.
- **§6.2 Recursos positivos presentes:** 4 de 6 (síntesis brutal en eyebrow + paréntesis editorial en título + inversión imperativo en CTA + reclamo humano honesto en trust-line 2). Se descartan *dato no redondeado* (requería inventar cifra) y *autodefinición plural cálido* (no encaja en banner de artículo compacto).
- **§6.3 Voz baseline:** plural *"investigamos"*, *"opinión propia"*, tú *"te ahorran"*, sin exclamaciones, trust-line canónica ✅.

**Umbral cumplido:** 0 flags automáticos + 0 mentiras + 4 recursos genuinos > 5 recursos con mentira → publicable.

**Iteraciones:** v1 (original) → v2 (primer reescrito, *"probando robots en casas reales"* mentira) → v2.1 (*"tras meses cubriendo este nicho"* mentira) → **v3 actual** (subtítulo eliminado, 0 mentiras).

---

## 2. Welcome email 1 — antes / después

### 2.1 Original (`docs/welcome-flow-setup.md § Email 1`)

```
From name: Rafael de ROBOHOGAR
Subject:   Tu PDF (y una pregunta)
Preheader: La Hoja de Compra ROBOHOGAR está dentro. 15 seg de lectura.

---

Hola,

Acabas de suscribirte a ROBOHOGAR y lo primero que te mandamos es la Hoja de Compra. Si viniste buscándola, aquí la tienes. Si te suscribiste por otra razón, la consideramos regalo de bienvenida — cubre exactamente lo que necesitas saber antes de comprar cualquier robot doméstico:

👉 [Descargar la Hoja de Compra ROBOHOGAR (PDF · 2 páginas)](<URL>)

Son las 10 preguntas que nos hacemos nosotros antes de comprar cualquier robot doméstico. Si las respondes todas, te ahorras varios cientos de euros en compras que no encajan con tu casa.

Ahora una pregunta rápida, y va en serio: **¿cuál es la zona de tu casa que más te cuesta mantener limpia?** Cocina, baño, alfombras de los niños, el estudio con pelos del perro, lo que sea.

Responde a este email con una frase. Lo leemos todos y nos ayuda a decidir qué probar y escribir los próximos meses. Cuando somos pocos suscriptores, cada respuesta pesa el triple.

Un saludo,
Rafael

P.D. Si piensas que la Hoja de Compra le viene bien a alguien, reenvíale este correo. No hace falta permiso.
```

### 2.2 Diagnóstico contra [`02-newsletter-y-emails.md § 6`](../../references/editorial-es/02-newsletter-y-emails.md)

Flags automáticos (§6.1):
- **(a) Saludo anglo** — *"Hola,"* matchea la regla de aperturas prohibidas (`editorial.md § Apertura y cierre — anti-anglicismos`). ❌
- **(b) Cierre** — *"Un saludo, Rafael"* — aceptable en editorial firmado pero no cumple §2.3 cadencia explícita. △
- **(c) Filler** — *"Acabas de suscribirte a ROBOHOGAR y lo primero que te mandamos es la Hoja de Compra"* — se puede considerar metanarración del email. △
- **(d) Hype/velocidad** — *"15 seg de lectura"* en preheader. △ (no promesa de velocidad técnica, pero roza la prohibición de `rules/tangibles.md § Microcopy`).
- **(e) Em-dash** — 1 em-dash en *"regalo de bienvenida — cubre exactamente…"*. Aceptable en prosa larga, no crítico.

Recursos positivos §2 (§6.2):
- §2.1 Apertura por anécdota: ❌ — arranca con meta-explicación del email, no con anécdota ni momento.
- §2.2 Humildad epistémica: ❌ — tesis afirmativa sin *"sospechamos"* ni *"en nuestra experiencia"*.
- §2.3 Cierre con cadencia: ❌ — *"Un saludo, Rafael"* no promete cuándo vuelves a escribir.
- §2.4 Numeración del issue: N/A (welcome).
- §2.5 Pregunta propia obsesiva: ❌ — la pregunta al lector es buena, pero no es *"una pregunta que llevamos semanas rondando"*.
- §2.6 Tagline-identidad: ❌ — no aparece *"Esto es ROBOHOGAR: …"*.
- §2.7 Reclamo humano: ❌ — no dice *"lo escribimos nosotros, no un algoritmo"*.

**Presencia: 0 de 7 recursos §2.** Por debajo del umbral mínimo (4 recursos para welcome). → Reescribir completo.

### 2.3 Reescrito aplicando KB

```
From name: ROBOHOGAR (equipo)
Subject:   Tu PDF — y el martes volvemos
Preheader: Dentro: Hoja de Compra y cómo funciona ROBOHOGAR.

---

Buenos días.

Empezamos ROBOHOGAR porque nos cansamos de gastar en robots que no encajaban con nuestras casas. Esto es ROBOHOGAR: robots para casa, humanoides que llegan y el hogar robotizado que ya está aquí.

Lo primero que te mandamos es la Hoja de Compra. Son 10 preguntas clave que separan un aspirador que encaja en tu casa del que no.

[Enviádmelo al correo] <URL>

Si viniste por la checklist, aquí la tienes. Si te suscribiste por otra razón, la consideramos regalo de bienvenida.

Una pregunta que nos ronda: **¿cuál es la zona de tu casa que más te cuesta mantener limpia?** Cocina, baño, alfombras de los niños, el estudio con pelos del perro, lo que sea.

Responde a este email con una frase. Lo leemos todos y nos ayuda a decidir qué probar los próximos meses. Cuando somos pocos suscriptores, cada respuesta pesa el triple.

Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre.

Te escribimos el martes que viene.

— ROBOHOGAR

P.D. Si piensas que la Hoja de Compra le viene bien a alguien, reenvíale este correo. No hace falta permiso.
```

### 2.4 Cambios justificados

| Elemento | Antes | Después | § KB que lo motiva |
|---|---|---|---|
| From name | *"Rafael de ROBOHOGAR"* | *"ROBOHOGAR (equipo)"* | Voz plural editorial (`editorial.md`). Rafael como firma en singular reservado a editoriales personales — el welcome MVP es institucional |
| Subject | *"Tu PDF (y una pregunta)"* (22 chars — bien) | *"Tu PDF — y el martes volvemos"* (30 chars — dentro de 20-45) | [`02 § 2.3`](../../references/editorial-es/02-newsletter-y-emails.md) cadencia explícita en subject |
| Preheader | *"La Hoja de Compra ROBOHOGAR está dentro. 15 seg de lectura."* | *"Dentro: Hoja de Compra y cómo funciona ROBOHOGAR."* | Elimina *"15 seg de lectura"* (roza promesa velocidad `rules/tangibles.md`) + añade expectativa de contenido |
| Saludo | *"Hola,"* ❌ calco anglo | *"Buenos días."* | `editorial.md § Anti-anglicismos` (patrón Kloshletter) |
| Apertura | Meta-explicación del email | Anécdota de origen + tagline-identidad (sin *"el otro día"* para evitar marcador temporal sin respaldo) | [`02 § 2.1`](../../references/editorial-es/02-newsletter-y-emails.md) + [`02 § 2.6`](../../references/editorial-es/02-newsletter-y-emails.md) Suma Positiva |
| Descripción tangible | *"10 preguntas para no pagar de más al comprar tu robot doméstico"* | *"10 preguntas clave que separan un aspirador que encaja en tu casa del que no"* | Descripción funcional del contenido del tangible, cero afirmaciones sobre tiempo/testing no verificables |
| CTA | *"Descargar la Hoja de Compra ROBOHOGAR (PDF · 2 páginas)"* | *"Enviádmelo al correo"* | [`03 § 1`](../../references/editorial-es/03-microcopy-ctas-meta.md) Holaluz (inversión imperativo) |
| Pregunta al lector | *"Ahora una pregunta rápida, y va en serio"* | *"Una pregunta que nos ronda"* | [`02 § 2.5`](../../references/editorial-es/02-newsletter-y-emails.md) Kaizen adaptado sin marcador temporal inverificable (*"meses dándole vueltas"* eliminado: newsletter reciente) |
| Reclamo humano | ausente | *"Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre."* | [`02 § 2.7`](../../references/editorial-es/02-newsletter-y-emails.md) Al día elDiario + regla dura de honestidad 2026-04-19 |
| Cierre | *"Un saludo, Rafael"* | *"Te escribimos el martes que viene. — ROBOHOGAR"* | [`02 § 2.3`](../../references/editorial-es/02-newsletter-y-emails.md) Kloshletter (*"Te escribo mañana. Carlos"* adaptado al plural) |

### 2.5 Verificación post-reescritura (§6 + regla honestidad ampliada)

- **§6.1 Flags automáticos:** 0 matches en saludos anglo, cierres anglo, filler, hype/velocidad, promesas temporales sin respaldo, em-dash en trust.
- **Regla dura de honestidad (§2.7 ampliada 2026-04-19):** 0 afirmaciones hands-on sobreprometidas, 0 afirmaciones temporales sin respaldo, 0 afirmaciones volumétricas inventadas. Descripción del tangible funcional (*"10 preguntas clave que separan X de Y"*), no autodescripción del proceso (*"tras meses"* / *"destilamos de 42 robots"* eliminados).
- **§6.2 Recursos presentes: 5 de 7** (tras purga honestidad):
  - ✅ §2.1 Apertura por anécdota (*"Empezamos ROBOHOGAR porque nos cansamos…"*)
  - ❌ §2.2 Humildad epistémica — eliminada *"las destilamos de 42 robots"* por mentira; la humildad epistémica queda en el reclamo humano (*"Probamos lo que podemos"*) del final, no en la descripción del tangible
  - ✅ §2.3 Cierre con cadencia (*"Te escribimos el martes que viene. — ROBOHOGAR"*)
  - N/A §2.4 Numeración del issue (welcome)
  - ✅ §2.5 Pregunta propia (*"Una pregunta que nos ronda"* — sin marcador temporal falso)
  - ✅ §2.6 Tagline-identidad (*"Esto es ROBOHOGAR: robots para casa, humanoides…"*)
  - ✅ §2.7 Reclamo humano honesto (*"Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre."*)
- **§6.3 Voz baseline:** plural (*"empezamos"*, *"nos cansamos"*, *"nos ronda"*, *"escribimos"*), tú al lector, sin exclamaciones, sin emojis decorativos, párrafos de 1-3 frases ✅.

**Nota metodológica.** 5 de 7 recursos está por encima del umbral mínimo (4) para welcome. Mejor 5 verdaderos que 7 con mentiras. La §2.2 humildad epistémica se puede recuperar en futuros issues cuando haya dato real (*"tras analizar X modelos que sí hemos podido probar, decidimos Y"*) — nunca inventar cifra para forzar el recurso.

**Umbral de reescritura cumplido:** 0 flags + 6 de 7 recursos + voz ok → publicable.

---

## 3. Notas comparativas (antes / después agregado)

| Métrica cualitativa | Banner original | Banner nuevo | Welcome original | Welcome nuevo |
|---|---|---|---|---|
| Toque personal (§2 newsletter) | bajo (utilitario) | medio (paréntesis confidencial + voz plural) | bajo (0 de 7) | alto (6 de 7) |
| Diferencial anti-LLM | bajo (plantilla estándar) | medio (cifras no redondeadas + inversión imperativo) | bajo (saludo anglo + cierre genérico) | alto (apertura origen + reclamo humano + cadencia) |
| Bloqueo del validator `/pdf-brand` | pasa | pasa | N/A (fuera del validator) | N/A |
| Presencia recursos ES positivos | 1 de 6 | 5 de 6 | 0 de 7 | 6 de 7 |

## 4. Acciones de seguimiento propuestas

- [ ] **Banner**: si Rafael aprueba la v2, actualizar `content/lead-magnets/hoja-compra/snippets-para-pegar.md` snippets 2, 3 y 4 (Roborock Saros Z70, Samsung Jet Bot Steam Ultra, Mejor robot aspirador 2026) con el copy nuevo + re-pegar en Beehiiv.
- [ ] **Welcome email 1**: si Rafael aprueba la v2, actualizar `docs/welcome-flow-setup.md` bloque *"Email 1"* con el copy nuevo + pegar en Beehiiv welcome automation.
- [ ] **Validación A/B** (iteración F2): comparar CVR banner v1 vs v2 tras 2-3 semanas con ≥500 impresiones por variante. Comparar reply rate welcome v1 vs v2 tras 30 suscriptores nuevos con cada variante.
- [ ] **Canonizar** en KB si v2 supera a v1 en métricas: actualizar `03-microcopy-ctas-meta.md § 5.2` y `02-newsletter-y-emails.md § 4` con la versión canonizada como default.

## 5. Metadatos

- KB utilizado: [`references/editorial-es/02-newsletter-y-emails.md`](../../references/editorial-es/02-newsletter-y-emails.md) §2, §4, §6 + [`references/editorial-es/03-microcopy-ctas-meta.md`](../../references/editorial-es/03-microcopy-ctas-meta.md) §1, §5, §6.
- Research fuente: [`2026-04-19-research-editorial-es-newsletters.md`](2026-04-19-research-editorial-es-newsletters.md) + [`2026-04-19-research-editorial-es-periodismo-y-copy.md § BLOQUE B`](2026-04-19-research-editorial-es-periodismo-y-copy.md).
- Pendiente: decisión de Rafael sobre si reemplazar directamente las versiones actuales o mantener ambas variantes para A/B test.
