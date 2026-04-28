---
type: reference
tema: cómo escribir diálogo natural en castellano peninsular para Ficciones Domésticas — subtexto, ritmo, acotación, decisión-en-voz-alta. Adaptación de las 4 funciones del diálogo de Robert McKee al ES doméstico ROBOHOGAR
audience: skill /ficcion-draft + Rafael (revisión pre-output)
created: 2026-04-28 PM
incidente-origen: auditoría 2026-04-28 PM de los 5 relatos publicados — el diálogo es escaso en 4 de 5 (la decisión irreversible se ejecuta en silencio interior, no en voz alta). Cuando aparece, los referentes peninsulares (Adón, Mesa, Aramburu) lo hacen bien pero no hay guía extraíble: subtexto, acción ↔ habla, función por línea
---

# Diálogo ES doméstico — toolkit para Ficciones Domésticas

> Esta referencia define cómo se escribe diálogo natural en castellano peninsular dentro del canon ROBOHOGAR. Cubre subtexto, función por línea (McKee), acotación, ritmo, y la regla **decisión-en-voz-alta** que mejora engagement con audiencia transmedial.
>
> Capa relacionada: voz literaria peninsular (`castellano-literario-es.md`), POV y DIL (`pov-y-discurso-indirecto-libre.md`), microtensión sentence-level (`microtension-sentence-level.md`).

---

## §1 Diálogo ES vs anglo — el verbo invisible

**Regla canon:** el verbo de habla por defecto en ES literario peninsular contemporáneo es `dijo` (pretérito) o `dice` (presente histórico). Equivalentes neutros aceptables: `preguntó`, `respondió`, `contestó`. Estos cuatro son **invisibles** al lector — no compiten con el diálogo, lo escolan.

**Anti-pattern canónico ES:** abusar de sinónimos del verbo de habla.

| ❌ Verbo de habla "expresivo" | ✅ Sustitución |
|---|---|
| *musitó · susurró · cuchicheó* | *dijo en voz baja* / acotación gestual / `dijo` a secas |
| *exclamó · profirió · espetó · soltó · vociferó* | `dijo` + acción física que muestre el modo |
| *aulló · bramó · rugió* | reescribir el diálogo o cambiar el contexto |
| *masculló · refunfuñó · gruñó* | `dijo` + acción + acotación corta |
| *aclaró · puntualizó · matizó · sentenció* | `dijo` (matizar es voz del autor irrumpiendo) |
| *prosiguió · agregó · añadió* | sin acotación si el contexto lo deja claro |

**Por qué importa:** los verbos expresivos vienen de doblaje y traducción anglo. En narrativa peninsular literaria contemporánea (Adón, Aramburu, Mesa, Marías) el verbo invisible es la norma. Abusar de sinónimos suena a *Audible pulp* traducido, no a literatura.

**Cuota orientativa:** máximo **2 verbos de habla expresivos por relato** — y solo cuando contextualmente sean inevitables. Si superan 2 → reescribir.

**Verificación pre-output (grep):**

```bash
grep -nE '\b(susurr[óaóéí]|musit[óé]|exclam[óé]|prof[ie]ri[óé]|espet[óé]|aull[óé]|bram[óé]|rugi[óé]|mascull[óé]|refunfu[ñn][óé]|gruñ[óé])\b' <relato.md>
```

Match >2 → reescribir antes de entregar.

---

## §2 Las 4 funciones del diálogo (McKee adaptado)

**Regla dura:** cada línea de diálogo debe cumplir al menos UNA de estas cuatro funciones. Si no cumple ninguna → cortar.

1. **Revelar carácter** — la línea muestra algo del personaje (su léxico, su clase, su jerarquía interna, su contradicción) que el narrador no podría decir tan rápido.
2. **Avanzar conflicto** — la línea cambia el balance de poder, deseo o información entre los personajes presentes.
3. **Sembrar dato real** — la línea introduce un anclaje verificable (regulación, marca ficticia del canon, hecho del mundo) que el lector puede contrastar fuera del relato.
4. **Ejecutar decisión irreversible en voz alta** — la línea es el acto. El personaje no decide en su cabeza y luego habla; **decide al hablar**.

**Aplicación operativa:** al cerrar el borrador, marcar cada línea de diálogo con su función. Si una línea no cumple ninguna, cortar (la prosa narrativa puede absorberla mejor). Si una escena tiene 12 líneas y solo cumplen función 8, recortar a esas 8 + reescribir las 4 sobrantes como narración o gesto.

### §2.1 La regla de la decisión-en-voz-alta — refuerzo engagement

Cuando la categoría declarada es **Cinematográfico** o **Dinámico** (75% del catálogo target), al menos **una decisión irreversible del relato debe ejecutarse en diálogo, no en silencio interior**. Es la diferencia entre:

- ❌ *"Andrés cerró el feed sin contestar."* (decisión silenciosa interior)
- ✅ *"— Apaga el feed."* (decisión en voz alta — testigo + irrevocable + escuchable en audiolibro)

**Por qué importa para audiencia transmedial:** un oyente de audiolibro / audionovela necesita escuchar el momento clave. Las decisiones silenciosas interiores se las pierde. Las decisiones en voz alta funcionan como bisagras audibles del relato.

**Excepción:** Atmosférico y Slice of life pueden cerrar con decisión silenciosa (ese es su sello). Cinematográfico/Dinámico no.

---

## §3 Subtexto — 6 técnicas para que los personajes no digan lo que piensan

**Regla canon:** en presencia de un robot, un observador, un superior jerárquico, o un sistema de cuidado-mediado-por-algoritmo, el personaje **nunca dice lo que piensa**. Lo dice oblicuo. El subtexto es la diferencia entre diálogo plano y diálogo que pesa.

### §3.1 Interrupción

El personaje empieza una frase y la corta antes del verbo principal. Lo que iba a decir es lo importante.

**Ejemplo canónico** — *La canguro*: Joel quiere preguntarle a NIDIA-7 si Hugo está bien. Lo intenta y lo corta:
> *— ¿Hugo… ?*
> *NIDIA inclinó tres grados la cabeza. Esperó.*
> *— Nada. Que se duerma.*

La pregunta truncada lleva más peso que cualquier formulación completa.

### §3.2 Eufemismo doméstico ES

Usar el eufemismo cotidiano peninsular en vez del nombre directo. Lo doméstico ES está lleno: *"el chisme"* (objeto importante), *"la cosa esa"* (problema serio), *"el bicho"* (humanoide), *"el trasto"* (tecnología), *"el armatoste"*, *"la historia esa"*.

**Aplicación:** cuando un personaje habla de algo que le da miedo, vergüenza o duelo, sustituye el sustantivo directo por eufemismo. Funciona en boca de yayos, padres precarios, cuidadoras, obreros — cualquier registro popular peninsular.

### §3.3 Pregunta lateral

El personaje pregunta una cosa para preguntar otra. Lo que pregunta no es lo que quiere saber.

**Ejemplo canónico** — *Papá desde Singapur*: Mateo le pregunta a Andrés *"¿Estás tú?"* en vez de *"¿estás tú o el humanoide?"*. La pregunta lateral revela que Mateo ya sabe la respuesta. La pregunta es acusación, no consulta.

### §3.4 Silencio acotado

El personaje no responde y la acotación nombra el silencio. El silencio acotado pesa más que cualquier frase.

**Forma canónica:**
> *— ¿Te quedas o te vas?*
> *Manuel no respondió.*

NO:
> *— ¿Te quedas o te vas?*
> *Manuel guardó silencio dramáticamente.*

El silencio se nombra en una frase corta sin adverbio. El lector reconstruye su peso.

### §3.5 Repetición vacía

El personaje repite literalmente lo que el otro acaba de decir. La repetición señala que ha escuchado pero no acepta.

**Ejemplo canónico** — *La objeción*: Lourdes pregunta *"¿Notáis las cosas?"*. VELA-9 responde *"Notamos las cosas, ministra."*. La repetición sin afirmación ni negación deja la pregunta abierta. Es ambigüedad calculada del personaje, no del autor.

### §3.6 Frase que se queda a medias

El personaje empieza con seguridad, pierde fuelle, y deja la frase incompleta. Funciona especialmente con yayos, cuidadoras al límite, padres precarios.

**Forma canónica** *(El cristalero, draft 2026-04-28)*:
> *— Yo, lo que pasa es que…*
> *Encogió un hombro. No siguió.*

La acotación gestual cierra la frase mejor que cualquier verbo de habla.

---

## §4 Acción ↔ habla — el gesto simultáneo

**Regla canon:** cada línea de diálogo lleva un gesto físico simultáneo o inmediatamente posterior. El gesto **no es decorativo** — revela la contradicción entre lo que se dice y lo que se siente.

### §4.1 Gesto que contradice

El personaje dice una cosa y el cuerpo dice otra. El lector escucha dos canales.

> *— No me importa.*
> *Marta apretó la taza con las dos manos.*

La negación verbal + el gesto de aferramiento = el lector sabe que sí importa. No hace falta explicarlo.

### §4.2 Gesto que adelanta la decisión

El personaje hace un gesto físico que **anticipa** lo que va a decir cuatro líneas después.

**Ejemplo canónico** — *Pipo*: Manuel apoya el cañón en el muslo dos párrafos antes de decir *"vámonos, Lobo"*. El cañón apoyado adelanta la decisión de no disparar al lector — antes de que el personaje la articule.

### §4.3 Gesto del observador (humanoide / robot)

En POV humano, el humanoide observa. Su gesto físico (inclinar tres grados la cabeza, pausar el LiDAR, retraer un brazo) se acota como **acción simétrica al diálogo humano**, no como decorado mecánico.

**Ejemplo canónico** — *La canguro*: Joel habla, NIDIA-7 *"inclinó tres grados la cabeza"*. El gesto del humanoide pesa lo mismo que una línea de diálogo. El lector lee la pausa.

### §4.4 Gesto-ancla del espacio doméstico

El gesto se ejecuta sobre un objeto del espacio doméstico ES (cafetera, taza, llaves, mando, pomo de la puerta, llave inglesa). El objeto se vuelve trama, no decoración (ver `castellano-literario-es.md § Espacio doméstico activo`).

---

## §5 Acotación ES — convención ROBOHOGAR

### §5.1 Guion largo, no comillas

Diálogo en **raya española (—)**, no comillas latinas «», no comillas inglesas "". Una raya abre la línea, otra cierra el inciso del narrador.

**Forma canónica:**
```
— Apaga el feed —dijo Joel— y vámonos.
```

- Raya inicial pegada a la primera palabra (sin espacio).
- Raya de cierre del inciso pegada a la última palabra del inciso (sin espacio).
- El inciso (`—dijo Joel—`) NO lleva espacios entre las rayas y las palabras.
- Si la línea termina ahí, **no se cierra** la raya final (la línea cierra con punto, no con raya).

**Forma canónica (línea sin inciso):**
```
— Apaga el feed.
```

### §5.2 Posición del inciso ES — antes de la coma de cierre

Convención peninsular: el inciso del narrador va **antes** de la coma final, no en posición anglo (entre comas extrañas). Compara:

| ✅ ES literario peninsular | ❌ Calco anglo |
|---|---|
| *— No me importa —dijo, y se fue.* | *— No me importa, dijo y se fue.* |
| *— Apaga el feed —dijo Joel—, ya.* | *— Apaga el feed, dijo Joel, ya.* |

### §5.3 Cuándo NO acotar

- Cuando el contexto deja claro quién habla (alternancia binaria).
- Tres líneas consecutivas del mismo personaje → no repetir `dijo`.
- Cuando el gesto de §4 sustituye al verbo de habla.

### §5.4 Cuándo SÍ acotar

- Cambio de hablante después de 4+ líneas consecutivas (lector pierde el hilo).
- Pregunta o respuesta que se dirige a un personaje específico en escena con 3+ presentes.
- Acotación que añade gesto físico simultáneo (función §4).

---

## §6 Ritmo del diálogo — densidad y reparto

**Regla orientativa:**

| Categoría intensidad | Ratio diálogo / narración | Decisión irreversible en voz alta |
|---|---|---|
| Cinematográfico | 30-45% diálogo | Obligatoria (≥1) |
| Dinámico | 20-35% | Obligatoria (≥1) |
| Atmosférico | 5-20% | Opcional |
| Slice of life | 0-10% | Opcional |

**Anti-pattern:** muros de diálogo (>5 líneas consecutivas sin gesto, narración o pausa). Romper con acotación gestual o párrafo de narración cada 3-4 líneas.

**Anti-pattern complementario:** diálogo invisible (relato Cinematográfico/Dinámico con <10% de diálogo). Si el relato cae aquí → la decisión irreversible está enterrada en interior, reescribir al menos una escena en voz alta.

---

## §7 Auditoría inversa de los 5 relatos publicados

| Relato | Ratio diálogo | Decisión voz alta | Función dominante |
|---|---|---|---|
| Pipo | ~8% | NO (decisión silenciosa) | Subtexto §3.4 silencio acotado bien |
| La objeción | ~28% | Parcial (Lourdes pregunta, VELA-9 ambiguo) | Subtexto §3.5 repetición vacía canónico |
| Papá desde Singapur | ~22% | Parcial (Mateo pregunta lateral §3.3) | Pregunta lateral canónica |
| Setenta y dos horas | ~6% | NO (decisión por teléfono no narrada) | Casi sin diálogo — abusa de silencio |
| La maratonista y su sombra | ~3% | NO (todo silencio) | Flash sin diálogo — coherente con Atmosférico |

**Diagnóstico:** los 5 relatos saben hacer subtexto bien (especialmente §3.3, §3.4, §3.5). Pero la regla **decisión-en-voz-alta §2.1** se incumple en 3 de los 4 categorizados como Cinematográfico o Dinámico. Ahí está el déficit de engagement con audiencia transmedial. El siguiente relato debería ejecutar al menos una decisión irreversible en diálogo audible.

---

## §8 Cómo se aplica al skill `/ficcion-draft`

1. **Carga condicional** en paso 6 — `dialogo-es-domestico.md §§ 1-5` solo si el outline (paso 5) declara ≥1 escena dialogada. Si el relato es flash sin diálogo (Slice/Atmosférico puro), no se carga.
2. **Verificación pre-output** en paso 8.x:
   - Grep §1 verbos de habla expresivos (cuota ≤2).
   - Categoría Cinematográfico/Dinámico → verificar que hay ≥1 línea de diálogo en la escena de decisión irreversible (no decisión silenciosa).
3. **Frontmatter** `dialogo_pct:` (porcentaje aproximado) declarado tras revisión. Auto-balanceo lee esta columna.

---

## §9 Mantenimiento

Archivo vivo. Cuando se identifique una 7ª técnica de subtexto extraída de un relato publicado, añadir a §3.7. Si el grep §1 detecta un verbo expresivo nuevo recurrente, añadir a la tabla. Cuando un relato consigue ratio diálogo >35% sin perder voz literaria, registrar como ejemplo canónico.

**Referentes externos** (consulta opcional):
- Robert McKee — *Story* (1997) cap. "Dialogue", *Dialogue* (2016).
- Sol Stein — *Stein on Writing* (1995) cap. "Dialogue".
- Para ES peninsular: Aramburu (*Patria*), Marías (*Corazón tan blanco*) — manuales del diálogo invisible.
