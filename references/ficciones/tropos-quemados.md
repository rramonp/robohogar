---
type: reference
tema: registro vivo de tropos / figuras retóricas / gestos / setting clichés ya utilizados en Ficciones Domésticas
audience: skill /ficcion-draft + Rafael (decisión editorial pre-escritura)
created: 2026-04-26
incidente-origen: feedback Rafael 2026-04-26 tras leer "El chaval" — copy-paste literal de párrafo entero (cafetera + geranios + luz que no calienta) entre *El que viene a tomar café* y *El chaval*; gestos calcados; 66% del catálogo en mismo conflicto humano. Diagnóstico completo en plan `se-han-utilizado-recursos-scalable-duckling.md` y memoria `feedback_ficcion_anti_self_plagio.md`.
---

# Tropos quemados — registro vivo de Ficciones Domésticas

> **Source of truth** del repertorio léxico-figurativo de la saga. Cada figura/gesto/imagen/fórmula utilizada en un relato se anota aquí con contador. El skill `/ficcion-draft` consulta este archivo en `§ 5.6 Variability gate` ANTES de empezar a componer prosa, y bloquea el output si el draft cae en cualquier tropo marcado 🔴 QUEMADO.
>
> Sirve a la regla dura **"Variabilidad inter-relatos"** de [`@.claude/rules/editorial.md § Narrativa especulativa`](../../.claude/rules/editorial.md). Hermana operativa de [`hooks-taxonomia.md`](hooks-taxonomia.md) (variedad de aperturas) y [`tonalidad-y-mix-editorial.md`](tonalidad-y-mix-editorial.md) (variedad de tono).

## §1 Estados de un tropo

| Estado | Apariciones | Regla |
|---|---|---|
| 🟢 **LIBRE** | 0 | Disponible. El registro lo añade al primer uso. |
| 🟡 **VIGILAR** | 1 | Disponible pero un segundo uso lo quema. El skill avisa antes de usarlo. |
| 🔴 **QUEMADO** | ≥2 | **Prohibido en próximos 5 relatos** desde el último uso. El skill bloquea el output si lo detecta. |
| ⚫ **JUBILADO** | ≥4 | **Prohibido permanentemente.** Tropo agotado para la saga. |

**Ventana de enfriamiento del 🔴 QUEMADO**: 5 relatos desde el último uso. Cuando hayan pasado 5 relatos sin usarlo, vuelve a 🟡 VIGILAR. Esto permite reciclaje cuidadoso sin recurrencia obvia.

## §2 Lista cerrada inicial — extraída de auditoría 2026-04-26

Los 14 tropos identificados como saturados por la auditoría comparativa de los 9 relatos publicados/draft. Cualquiera que haga match en próximo relato → bloqueo.

### §2.1 Setting clichés

| Tropo | Tipo | Apariciones | Relatos | Estado |
|---|---|---|---|---|
| Cafetera italiana subiendo + gluglú + olerlo sin oírlo | setting cliché | 3 | el-que-viene-a-tomar-cafe (v1, v2), el-chaval | 🔴 QUEMADO |
| Geranios sin florecer en maceta del patio (variantes: jazmín, otra planta sin florecer 3 años) | imagen vegetal | 2 (+1 variante jazmín) | el-que-viene-a-tomar-cafe, el-chaval (+ setenta-y-dos-horas variante) | 🔴 QUEMADO |
| "Luz de [mes] que no calienta" entrando por ventana del patio | imagen lumínica | 2 | el-que-viene-a-tomar-cafe (enero), el-chaval (octubre) | 🔴 QUEMADO |
| Tortilla francesa como cena de personaje solo | objeto-comida | 2 | el-pendiente, el-chaval | 🔴 QUEMADO |
| Mantita verde sobre las rodillas del personaje vulnerable durmiendo | objeto-textil | 1 | el-chaval | 🟡 VIGILAR |
| Patio interior madrileño con ventanas | espacio físico | 4+ | tomar-café, pendiente, chaval, operador-nocturno | 🔴 QUEMADO |

### §2.2 Gestos físicos

| Tropo | Apariciones | Relatos | Estado |
|---|---|---|---|
| Pelusa/hilacha del codo del humanoide quitada con dos dedos como hilacha de chaqueta | 3 | el-que-viene-a-tomar-cafe (líneas 43, 263), el-chaval (línea 40) | 🔴 QUEMADO |
| Humanoide hace gesto de servirse café aunque no lo bebe (decoración de los ingenieros) | 2 | el-que-viene-a-tomar-cafe, el-chaval | 🔴 QUEMADO |
| Personaje pone dos tazas, la grande descascarillada para el familiar mayor | 2 | el-que-viene-a-tomar-cafe, el-chaval | 🔴 QUEMADO |
| Bata azul abrochada al revés en personaje con demencia | 2 | el-que-viene-a-tomar-cafe (Soledad), el-chaval (Concha) | 🔴 QUEMADO |
| Personaje vulnerable durmiendo en la butaca/silla con manta encima al cierre | 2 | el-chaval, papá-desde-singapur (variante) | 🟡 VIGILAR |

### §2.3 Símiles y metáforas

| Tropo | Apariciones | Relatos | Estado |
|---|---|---|---|
| Símil "humanoide apagado en rincón = abrigo colgado de una percha grande" | 2 | el-que-viene-a-tomar-cafe (línea 293), setenta-y-dos-horas (línea 224) | 🔴 QUEMADO |
| Latido ámbar / luz ámbar en base del cuello del humanoide | 2 | la-objecion, el-chaval | 🟡 VIGILAR |
| Punto azul / verde / ámbar pequeño bajo la garganta como indicador de estado | 3 | el-operador-nocturno (azul), el-chaval (ámbar), la-canguro (verde) | 🔴 QUEMADO — variar a otro código sensorial (sonido del servomotor, calor de la base, parpadeo del techo, sin marcar estado del humanoide con luz visible) |

### §2.4 Frases-fórmula y muletillas del narrador

| Tropo | Apariciones | Relatos | Estado |
|---|---|---|---|
| "Cinco años hace ya" / "Cinco años muerto" como bisagra temporal | 2 | el-que-viene-a-tomar-cafe (*"Cinco años muerto y cada mañana en la cocina"*), el-chaval (*"Cinco años hace ya"*) | 🔴 QUEMADO |
| "Hace tres años que no le hace ya nada" — fórmula de agotamiento por costumbre | 2 | el-que-viene-a-tomar-cafe, el-chaval | 🔴 QUEMADO |
| Tabla de horas precisa al inicio de escena ("A las ocho menos cuarto", "A las siete y cuarenta", "A las nueve y veinte", "A las diez y cuarto") | 6+ | tomar-café, pendiente, chaval, llave-inglesa, operador, objeción | 🔴 QUEMADO — variar con descripción del momento o salto al "ya" sin reloj |

### §2.5 Diálogo y muletillas de personaje

| Tropo | Apariciones | Relatos | Estado |
|---|---|---|---|
| Madre desmemoriada llamando a la hija con nombre incorrecto (de su propia madre o hermana muerta) | 2 | el-que-viene-a-tomar-cafe (Soledad llama "Pepi" o "mamá"), el-chaval (Concha llama "Pepi") | 🔴 QUEMADO |
| Personaje desmemoriado responde "Ah. Ah, sí, sí" repetido en mismo relato | 1 (intra) | el-chaval | 🟡 VIGILAR |
| Vecino del rellano que avisa con tono cortado en escalera ("Llámala. Llámala antes de comer") | 1 | el-chaval (don Marcial) | 🟡 VIGILAR |
| Hija/familiar lejano al teléfono cobrando distancia internacional | 2 | papá-desde-singapur, el-chaval (Beatriz desde Berlín) | 🔴 QUEMADO |

### §2.5.bis Figuras nuevas del relato `la-canguro` (2026-04-26)

| Tropo | Tipo | Apariciones | Relatos | Estado |
|---|---|---|---|---|
| "Postura de espera del catálogo" del humanoide (brazos sueltos, voz neutra calibrada gama Cuidados) | gesto físico humanoide | 1 (3 menciones intra-relato) | la-canguro | 🟡 VIGILAR |
| "Tarda tres décimas" como medida de duda del humanoide al componer respuesta no protocolar | frase-fórmula narrador | 1 (2 menciones intra-relato) | la-canguro | 🟡 VIGILAR |
| Cocina americana abierta al salón VPO con barra pintada en blanco satinado | setting cliché | 1 | la-canguro | 🟡 VIGILAR |
| Dibujo infantil del oficio del padre pegado a la nevera con imán identitario | objeto-testigo cargado | 1 | la-canguro | 🟡 VIGILAR |
| Mecanismo de revelación: protagonista accede al "modo administrador" del humanoide y descubre logs ocultos | estructura narrativa | 1 | la-canguro | 🟡 VIGILAR |
| Logs literales con timestamp + entrada + respuesta protocolar como dispositivo de revelación | estructura narrativa | 1 | la-canguro | 🟡 VIGILAR |
| "Política de minimización de daño emocional doméstico" — vocabulario corporativo del humanoide en boca propia | voz administrativa parodiada | 1 | la-canguro | 🟡 VIGILAR |
| "Respira por la nariz. Se le había olvidado respirar por la nariz." | gesto + frase-fórmula narrador | 1 | la-canguro | 🟡 VIGILAR |
| Cifra de precio mensual del humanoide refurbished citada en cuerpo del relato (79 €/mes) | dato económico ficcional | 1 | la-canguro | 🟢 LIBRE |

### §2.6 Estructura de cierre

| Tropo | Apariciones | Relatos | Estado |
|---|---|---|---|
| Cierre con personaje cerrando los ojos / metiéndose en cama vestida sobre la colcha | 3 | el-operador-nocturno, la-maratonista (durmiendo con pulsómetro), el-chaval | 🔴 QUEMADO |
| Cierre con humanoide haciendo "algo levemente distinto" en última escena (siembra del relato) | 4 | tomar-café, papá-desde-singapur, la-objecion, el-chaval | 🔴 QUEMADO — necesita rotar a otros tipos de cliffhanger |
| Cierre con plano lento sobre objeto-testigo cargado (yoyó, pendiente en platito, vela en patio) | 3 | setenta-y-dos-horas, el-pendiente, el-chaval | 🔴 QUEMADO |

### §2.7 Nombres propios saturados

| Nombre | Tipo | Apariciones | Relatos | Estado |
|---|---|---|---|---|
| **Pilar** | protagonista mujer | 2 | el-que-viene-a-tomar-cafe (Pilar hija cuidadora), el-pendiente (Pilar viuda con aspirador) | 🔴 QUEMADO — no usar como protagonista |
| **HOGAR-X / HOGAR-X5** | modelo humanoide doméstico canon | 4 | tomar-café, papá-singapur (X5), chaval, operador-nocturno (variante NEO) | 🟡 VIGILAR — usar pero con alias afectivo NUEVO en cada relato |
| Madre desmemoriada con nombre corto trisílabo (Soledad / Concha) | personaje secundario | 2 | tomar-café (Soledad), chaval (Concha) | 🟡 VIGILAR — variar registro fonético |

## §3 Estructura de la entrada — formato canónico

Cada tropo nuevo se añade con esta estructura:

```markdown
| <Descripción concreta del tropo, no genérica> | <tipo: setting cliché / gesto físico / símil / fórmula narrador / muletilla diálogo / estructura cierre / nombre> | <N apariciones> | <slug1, slug2, ...> | <estado> |
```

**Reglas de descripción:**
- Específica, no genérica. ❌ "humanoide en rincón" → ✅ "humanoide apagado en rincón en postura de espera del catálogo (torso recto + manos en regazo)".
- Cita la frase literal cuando sea fórmula verbal: ❌ "fórmula temporal" → ✅ *"Cinco años hace ya"* / *"Hace tres años que no le hace ya nada"*.
- Documenta variantes superficiales: una "luz de enero que no calienta" y una "luz de octubre que no calienta" cuentan como mismo tropo (la fórmula es la misma, varía el mes).

## §4 Protocolo de actualización

**Quién actualiza:** el skill `/ficcion-draft` al cerrar cada relato (paso de Output) actualiza `tropos-quemados.md` añadiendo las 5-10 figuras dominantes del relato nuevo (gesto físico clave, metáfora dominante, objeto-testigo cargado, frase-fórmula recurrente, símil distintivo). Rafael revisa al final como parte del check pre-publish.

**Cuándo se promueve un tropo de 🟡 VIGILAR a 🔴 QUEMADO:** automático en el segundo uso. No hace falta decisión editorial.

**Cuándo se jubila un tropo (⚫):** decisión editorial de Rafael cuando el tropo aparece ≥4 veces y el feedback indica saturación de marca. Una vez ⚫ JUBILADO, el skill lo bloquea para siempre.

**Cuándo un tropo enfría:** el skill calcula automáticamente. Cuando el último uso del tropo está a >5 relatos del último publicado, el tropo vuelve a 🟡 VIGILAR (puede usarse de nuevo con cuidado).

## §5 Anti-tropos canónicos del universo (no lista negra, lista positiva — registro de qué NO se ha hecho aún)

Lista de oportunidades para próximos relatos. NO obligatorio elegir de aquí, pero útil cuando el `§ 5.6 Variability gate` reporta saturación de los 4 ejes y necesitas inspiración nueva.

**POVs aún no explorados o muy poco usados:**
- POV humanoide directo (1 vez en *La objeción*; reservado a Libro 2+ del Gran Reset según setting)
- Adolescente 14-18 años (no usado)
- Pareja joven sin hijos (no usado)
- Hombre solo 30-40 años (no usado)
- Inmigrante / persona racializada (no usado)
- Personal de servicio humano (no usado, distinto al humanoide)
- Trabajador esencial sin humanoide (no usado)
- Animal con humanoide (no usado)
- Niño 8-12 años con humanoide compañero (no usado, 1 variante en El operador nocturno como POV víctima)

**Settings aún no explorados:**
- Pueblo costero · sierra · pueblo agrícola
- Hospital · residencia · hospicio
- Vehículo en movimiento (tren, AVE, autobús, coche)
- Espacio público (parque, plaza, polideportivo, biblioteca)
- Lugar de trabajo (oficina, fábrica, almacén, restaurante)
- Cementerio · iglesia · juzgado
- Madrugada en lugar nocturno comercial activo

**Conflictos humanos no explorados:**
- Migración / desarraigo / vuelta al pueblo
- Trabajo precario y humanoide como amenaza laboral directa
- Adopción / fertilidad / gestación
- Religión / ritual / fe en transición tecnológica
- Adolescencia / iniciación / identidad
- Amistad pura sin familia
- Vínculo entre humanoides distintos (ya en setting Libro 2)
- Cuidado del humanoide enfermo / averiado por el humano

**Cliffhangers no explorados:**
- Decisión política colectiva (votación, asamblea, referéndum)
- Riesgo físico real (no descartado, sin sangre — evolución de "violencia tiene consecuencias físicas reales" del setting)
- Encuentro con extraño en lugar público
- Pérdida material concreta no resuelta (deudas, herencia, vivienda)
- Reconciliación inesperada
- Cambio de planes anunciado
- Lectura conjunta de algo que no se ve

## §6 Memoria del incidente origen

[`feedback_ficcion_anti_self_plagio.md`](../../../RRP-DEV/.claude/memory/feedback_ficcion_anti_self_plagio.md) documenta el detalle completo del incidente 2026-04-26: 9 relatos auditados, 14 tropos saturados detectados, copy-paste literal de párrafo entero entre *El que viene a tomar café* y *El chaval*, decisión de Rafael (reescritura quirúrgica + sistema multinivel + bloqueo duro + 7 referentes ES nuevos).
