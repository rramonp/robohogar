# Registro de automatizaciones ROBOHOGAR

> **Fuente única de verdad** de todo lo que Beehiiv (u otras plataformas) envía/dispara automáticamente. Cuando toque iterar cualquier copy, aquí está lo que HAY HOY — copy activo (v última) + histórico de versiones.
>
> **Regla operativa.** Antes de proponer o cambiar copy de cualquier automation: (a) leer este archivo completo, (b) identificar qué existe hoy y qué es plan, (c) proponer v+1 con diff explícito, (d) actualizar este archivo + commit tras aplicar en Beehiiv. No preguntar a Rafael por copy que ya está aquí: consultarlo primero.

---

## Estado del proyecto

- **Fase:** F1 (0-50 subs)
- **Subs:** 0
- **Newsletter semanal:** 0 envíos todavía (pendiente primer envío)
- **Plan Beehiiv:** Scale (automations, segmentación, welcome flows disponibles)
- **Última revisión del registro:** 2026-04-19

---

## Tabla master de automations

| # | Nombre | Plataforma | Trigger | Delay | Estado | Versión activa | Archivos del repo |
|---|---|---|---|---|---|---|---|
| 1 | Sign-up + entrega PDF Hoja de Compra | Beehiiv Digital Product + Automation | Confirma DOI tras suscripción | inmediato | ✅ Activo | v3 (2026-04-19) | `content/lead-magnets/hoja-compra/beehiiv-ficha.md` · este registro § 1 |
| 2 | Reminder 72h Hoja de Compra | Beehiiv Automation | Mismo trigger + wait 72h | 72h | ✅ Activo | v3 (2026-04-19) | este registro § 2 |
| 3 | Welcome flow MVP 2 emails | Beehiiv Automation | (pendiente activar) | — | ⏸️ Plan · no implementado | n/a | [`docs/welcome-flow-setup.md`](welcome-flow-setup.md) |
| 4 | Newsletter semanal | Beehiiv Post (manual) | Rafael publica | — | ⏸️ Pendiente primer envío | n/a | — |

**Cuando se cambie el estado de una fila** (p. ej. activar un flow pendiente): actualizar la tabla Y añadir la nueva sección o actualizar la existente con el copy nuevo + historial.

---

## § 1 · Sign-up + entrega PDF Hoja de Compra

### Metadata
- **Plataforma:** Beehiiv Digital Product + Automation manual (Workflows 2.0).
- **Trigger:** lector confirma DOI tras suscribirse y seleccionar el Digital Product Hoja de Compra.
- **Delay:** inmediato tras confirmación.
- **Ficha asociada:** [`content/lead-magnets/hoja-compra/beehiiv-ficha.md`](../content/lead-magnets/hoja-compra/beehiiv-ficha.md) (controla Product name, Description, Product details, CTA, thumbnail).
- **Estado:** ✅ Activo (copy v3 aplicado 2026-04-19).
- **Última revisión:** 2026-04-19.

### Copy v3 · activo

**Subject:** `Tu PDF (y una pregunta)`
**Preheader:** `La Hoja de Compra ROBOHOGAR está dentro.`
**From name:** `Rafael de ROBOHOGAR`

**Cuerpo:**

```
Buenos días.

Acabas de suscribirte a ROBOHOGAR y lo primero que te mandamos es la Hoja de Compra. Si viniste buscándola, aquí la tienes. Si te suscribiste por otra razón, la consideramos regalo de bienvenida: cubre lo que merece la pena saber antes de comprar cualquier robot doméstico.

👉 [Descargar la Hoja de Compra ROBOHOGAR (PDF · 2 páginas)](<URL_DEL_DIGITAL_PRODUCT>)

Son 10 preguntas clave que separan un robot que encaja en tu casa de uno que no. Si las respondes todas, te ahorras varios cientos de euros en compras que no encajan con la tuya.

Una pregunta, y va en serio: ¿cuál es la zona de tu casa que más te cuesta mantener limpia? Cocina, baño, alfombras de los niños, el estudio con pelos del perro, lo que sea.

Responde a este email con una frase. Lo leemos todos y nos ayuda a decidir qué probar y escribir los próximos meses. Cuando somos pocos suscriptores, cada respuesta pesa el triple.

Aquí, más allá del PDF, publicamos análisis y comparativas de lo que ya se vende, editoriales sobre hacia dónde va todo esto y algún relato corto sobre cómo será vivir con robots en 2030. Todo por email, con cadencia semanal.

Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre.

— ROBOHOGAR

P.D. Si piensas que la Hoja de Compra le viene bien a alguien, reenvíale este correo. No hace falta permiso.
```

**Formato al pegar en Beehiiv:**
- **Botón CTA nativo:** la línea `👉 [Descargar la Hoja de Compra...]` se sustituye por un bloque Button de Beehiiv (texto `Descargar la Hoja de Compra (PDF)` + URL del Digital Product, color ámbar).
- **Bold:** solo en *"¿cuál es la zona de tu casa que más te cuesta mantener limpia?"* (seleccionar → B). Es el CTA secundario, tiene que saltar.
- **Cursiva:** ninguna.
- **Links inline:** ninguno (solo el botón CTA).

### Cambios v1 → v3 (aplicados 2026-04-19)

| Elemento | v1 (original) | v3 (activo) | Motivo |
|---|---|---|---|
| Saludo | `Hola,` | `Buenos días.` | Anti-anglicismos (`editorial.md § Anti-anglicismos`) |
| Descripción tangible | *"10 preguntas que nos hacemos nosotros antes de comprar cualquier robot doméstico"* | *"10 preguntas clave que separan un robot que encaja en tu casa de uno que no"* | Regla honestidad — *"nos hacemos nosotros"* sin respaldo. Descripción funcional del valor |
| Bloque nuevo | — | *"Aquí, más allá del PDF, publicamos análisis y comparativas… cadencia semanal."* | Petición Rafael 2026-04-19: el suscriptor debe saber qué recibirá además del PDF |
| Reclamo humano | ausente | *"Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre."* | Fórmula canónica §2.7 KB editorial-es (diferencial defensivo + honestidad) |
| Cierre | `Un saludo, Rafael` | `— ROBOHOGAR` | Plural editorial coherente con cuerpo del email |

### Copy v1 · histórico (ya no activo)

```
Hola,

Acabas de suscribirte a ROBOHOGAR y lo primero que te mandamos es la Hoja de Compra. Si viniste buscándola, aquí la tienes. Si te suscribiste por otra razón, la consideramos regalo de bienvenida — cubre exactamente lo que necesitas saber antes de comprar cualquier robot doméstico:

👉 Descargar la Hoja de Compra ROBOHOGAR (PDF · 2 páginas)

Son las 10 preguntas que nos hacemos nosotros antes de comprar cualquier robot doméstico. Si las respondes todas, te ahorras varios cientos de euros en compras que no encajan con tu casa.

Ahora una pregunta rápida, y va en serio: ¿cuál es la zona de tu casa que más te cuesta mantener limpia? Cocina, baño, alfombras de los niños, el estudio con pelos del perro, lo que sea.

Responde a este email con una frase. Lo leemos todos y nos ayuda a decidir qué probar y escribir los próximos meses. Cuando somos pocos suscriptores, cada respuesta pesa el triple.

Un saludo,
Rafael

P.D. Si piensas que la Hoja de Compra le viene bien a alguien, reenvíale este correo. No hace falta permiso.
```

---

## § 2 · Reminder 72h Hoja de Compra

### Metadata
- **Plataforma:** Beehiiv Automation (workflow manual).
- **Trigger:** mismo que § 1 + wait 72h.
- **Delay:** 72h tras descarga.
- **Estado:** ✅ Activo (copy v3 aplicado 2026-04-19).
- **Última revisión:** 2026-04-19.

### Copy v3 · activo

**Subject:** `¿Ya has mirado la Hoja de Compra?`
**Preheader:** `Por si se quedó en la bandeja · 2 artículos cortos para ir abriendo boca.`
**From name:** `Rafael de ROBOHOGAR`

**Cuerpo:**

```
Buenos días.

Hace unos días descargaste la Hoja de Compra. Si ya la has mirado, genial. Si no, [aquí sigue disponible](<URL_DEL_PDF>).

Este correo es corto. Dos cosas:

**1) Qué recibes a partir de ahora.**
Un email con cadencia semanal. Una review o comparativa, un dato que nos ha llamado la atención, o un apunte sobre hacia dónde va el hogar robotizado. Lectura corta. Sin correos diarios ni urgencias inventadas.

**2) Dos artículos para ir abriendo boca.**
Del archivo, los dos con los que merece la pena empezar:

- [Samsung Jet Bot Steam Ultra: vapor a 100 °C, pero no donde piensas](<URL_ARTÍCULO_1>) — para entender por qué los titulares de aspiradores mienten casi siempre.
- [Roborock Saros Z70: ¿merece la pena pagar por un brazo mecánico?](<URL_ARTÍCULO_2>) — la primera vez que un aspirador recoge calcetines del suelo. Spoiler: a medias.

Cualquier duda, responde este email. Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre.

— ROBOHOGAR

P.D. Si este correo te acaba en Promotions, moverlo a Principal ayuda a que los siguientes no se pierdan.
```

**Formato al pegar en Beehiiv:**
- **Bold:** solo en los dos encabezados numerados *"1) Qué recibes a partir de ahora."* y *"2) Dos artículos para ir abriendo boca."*.
- **Links inline:** sí — el link al PDF en la primera sección + los 2 links de artículos con descripción detrás del em-dash.
- **Ningún botón nativo** en este email (es reminder textual, no CTA fuerte).

### Cambios v1 → v3 (aplicados 2026-04-19)

| Elemento | v1 (original) | v3 (activo) | Motivo |
|---|---|---|---|
| Saludo | `Hola de nuevo,` | `Buenos días.` | Anti-anglicismos |
| Timing del delay | *"Hace 3 días descargaste la Hoja de Compra"* | *"Hace unos días descargaste la Hoja de Compra"* | Honestidad — admite imprecisión del delay (Beehiiv entrega con variación) sin comprometer cifra exacta |
| Cadencia newsletter | *"Un email los martes a las 9:00… Unos 4-5 minutos de lectura"* | *"Un email con cadencia semanal… Lectura corta"* | Regla honestidad — 0 envíos hasta 2026-04-19, no hay histórico que respalde día/hora ni duración exacta |
| Promesa de primer martes | *"Mientras llega el primer martes"* | eliminado | Misma razón |
| Reclamo humano | *"Escribimos nosotros, no un autoresponder"* | *"Probamos lo que podemos. El resto lo investigamos a fondo por ti. Opinión propia, siempre."* | Fórmula canónica §2.7 (más rica + coherente con email 1) |
| Cierre | `Un saludo, Rafael` | `— ROBOHOGAR` | Plural editorial coherente |
| P.D. | *"Si estás en LinkedIn o X, publicamos pensamientos sueltos entre artículo y artículo. Pero el valor está aquí, en el correo del martes."* | *"Si este correo te acaba en Promotions, moverlo a Principal ayuda a que los siguientes no se pierdan."* | (a) Sin afirmación sobre actividad en redes (no verificada hoy). (b) Sin mención al martes. (c) Consejo de deliverability real + útil — ayuda a que los siguientes emails no caigan en Promotions |

### Copy v1 · histórico (ya no activo)

```
Hola de nuevo,

Hace 3 días descargaste la Hoja de Compra. Si ya la has mirado, gracias. Si no, [aquí sigue disponible] ← link al PDF.

Este correo es corto y no viene con ningún "qué opinas del tono" ni survey largo. Dos cosas:

1) Qué vas a recibir cada semana.
Un email los martes a las 9:00. Una review o comparativa, un dato que nos ha llamado la atención y un apunte sobre hacia dónde va esto del hogar robotizado. Unos 4-5 minutos de lectura. Nada de correos diarios ni de urgencias inventadas.

2) Dos artículos para ir abriendo boca.
Mientras llega el primer martes, aquí van los dos del archivo que más nos gustan:

- [Samsung Jet Bot Steam Ultra: vapor a 100 °C, pero no donde piensas] ← link · Para entender por qué los titulares de aspiradores mienten casi siempre.
- [Roborock Saros Z70: ¿merece la pena pagar por un brazo mecánico?] ← link · La primera vez que un aspirador recoge calcetines del suelo. Spoiler: a medias.

Cualquier duda, responde este email. Escribimos nosotros, no un autoresponder.

Un saludo,
Rafael

P.D. Si estás en LinkedIn o X, publicamos pensamientos sueltos entre artículo y artículo. Pero el valor está aquí, en el correo del martes.
```

---

## § 3 · Welcome flow MVP 2 emails

**Estado:** ⏸️ Plan · no implementado.
**Archivo plan:** [`docs/welcome-flow-setup.md`](welcome-flow-setup.md) — diseño de 2 emails (Email 1 welcome + Email 2 a 72h con artículos evergreen), trigger *subscriber confirms subscription*, arquitectura Beehiiv Workflows 2.0.
**Razón para no implementar aún:** el flujo actual ya cubre los dos emails básicos (entrega PDF + reminder). Duplicar sería spam. El welcome MVP 2 emails se activará cuando se consolide una cadencia de newsletter real (primer envío + estabilización) y haya algo nuevo que prometer al suscriptor orgánico que NO vino por la Hoja de Compra.
**Cuándo reactivar este plan:** subs ≥ 50 + al menos 3-4 envíos del newsletter estables.

---

## § 4 · Newsletter semanal

**Estado:** ⏸️ Pendiente primer envío (2026-04-19 · 0 subs).
**Trigger:** manual — Rafael publica post en Beehiiv, éste manda email a la lista.
**Cadencia prevista (sin compromiso público todavía):** semanal.
**Día/hora:** sin compromiso hasta que haya histórico estable. Cuando se consolide un patrón (p. ej. 4 envíos en el mismo día/hora), se podrá mencionar en copy externo.
**Archivo plan del arranque:** [`docs/guia-implementacion.md`](guia-implementacion.md) § fases de lanzamiento.

Cuando se envíe el primer issue: actualizar esta sección con subject + estructura del issue + link al post.

---

## Cambios pendientes tras la próxima iteración mayor

- [ ] Al activar § 3 (welcome MVP 2 emails): pasar Email 1 del welcome MVP a esta tabla como § 5 + desactivar el automation actual § 1 o replantear la arquitectura (puede que § 1 se fusione con el welcome MVP Email 1 si la lógica lo permite).
- [ ] Al enviar primer issue del newsletter semanal (§ 4): actualizar estado + mencionar día/hora real si se confirma cadencia.
- [ ] Al alcanzar subs ≥ 200 + open rate welcome >50% estable: expansión a 4 emails welcome (ver memoria `feedback_welcome_flow_mvp.md`).

---

## Regla operativa (recordatorio)

Antes de proponer o cambiar copy de cualquier automation: (a) leer este archivo, (b) identificar estado real, (c) proponer v+1 con diff explícito, (d) actualizar este archivo Y el archivo asociado + commit único tras aplicar en Beehiiv. Si el copy ya está aquí — **no preguntar a Rafael por algo que yo mismo he escrito**.
