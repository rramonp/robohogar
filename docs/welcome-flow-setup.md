# Welcome Flow ROBOHOGAR — Setup MVP (2 emails)

> Configuración del flujo de bienvenida para nuevos suscriptores de ROBOHOGAR en Beehiiv Scale. MVP deliberado de 2 emails, no 4: mientras subs <100, el ROI marginal de optimizar retention es bajo frente a optimizar CVR. Ver `feedback_welcome_flow_mvp.md` para contexto.
>
> **Estado:** diseñado 2026-04-18, pendiente de implementación en Beehiiv.

---

## 📌 Frases trigger para retomar

| Qué quiero retomar | Frase exacta |
|---|---|
| Arrancar la configuración en Beehiiv | **"Retomamos welcome-flow — empezamos configuración Beehiiv"** |
| Modificar copy de un email | **"Retomamos welcome-flow — edito email [1/2]"** |
| Ver estado / qué falta | **"¿En qué fase del welcome-flow estamos?"** |
| Expandir de 2 a 4 emails (cuando toque ~200 subs) | **"Retomamos welcome-flow — expandir a 4 emails"** |

Con esas frases Claude debe: (a) leer este documento completo, (b) revisar qué checkboxes del § Checklist están marcados, (c) retomar en el primer paso pendiente.

---

## Objetivo

Cubrir las 3 funciones mínimas del welcome en fase 0-100 subs sin añadir esfuerzo marginal sin retorno:

1. **Entregar el lead magnet prometido** (sin esto, el suscriptor se va a las 48 h y la promesa del banner se rompe).
2. **Capturar la señal "reply"** — Gmail/Outlook lee las respuestas como señal fuerte de engagement y blanquea el dominio para los siguientes emails. Evita caer en Promotions/Spam en la newsletter semanal.
3. **Presentar el ritmo editorial** — 2 artículos evergreen seleccionados para que el suscriptor tenga valor mientras espera el primer martes.

**Fuera de scope MVP:** backstory creator, survey de preferencias, nurture de conversión afiliados. Todo eso entra en la expansión a 4 emails cuando subs ≥200.

---

## Arquitectura Beehiiv Scale

Usamos **Automations / Workflows 2.0** (feature plan Scale), no el Welcome Email único. Razones:

- Permite 2 emails con delay entre ellos (72 h).
- Permite segmentar por tag en el futuro (cuando haya más de un lead magnet) sin rehacer.
- No se dispara hasta que el suscriptor confirma el double opt-in (GDPR ✅).

**Desactivar** el Welcome Email único estándar de Beehiiv (Settings → Emails → Preset Emails → toggle Welcome Email OFF). Si queda activo, el suscriptor recibe 3 emails (welcome nativo + nuestros 2), redundante.

**Nota 2026-04-18:** Rafael ya tenía una automation preexistente llamada "Welcome Email" (trigger "Signed up", 1 email con subject "Bienvenido/a a ROBOHOGAR") con 4 recipients históricos. **Reusarla** en vez de crear una nueva:
1. Renombrar a "Welcome MVP — Hoja de Compra".
2. Reescribir el Email 1 existente (reemplazar completo con el Email 1 de abajo).
3. Añadir Wait 72h + Email 2 como pasos nuevos tras el Email 1.
4. Publish changes.

Así se conservan las métricas históricas (4 recipients, 100% open, 75% CTR sirven de baseline comparativo).

---

## Checklist de setup

- [ ] **Subir el PDF "Hoja de Compra ROBOHOGAR v1"** como Digital Product en Beehiiv (Settings → Digital Products → New → precio 0 €).
- [ ] **Copiar la URL del digital product** (será el link del email 1).
- [ ] **Desactivar Welcome Email único** (Settings → Emails → Welcome Email → OFF).
- [ ] **Habilitar Double Opt-In** (Settings → Subscription Form → Double Opt-In → ON — obligatorio GDPR EU).
- [ ] **Crear Automation "Welcome MVP"** (Automations → New Automation).
- [ ] **Trigger:** `Subscriber confirms subscription` (dispara solo tras double opt-in).
- [ ] **Paso 1 — Email:** pegar copy del § Email 1 de abajo.
- [ ] **Paso 2 — Wait:** 72 hours (3 días).
- [ ] **Paso 3 — Email:** pegar copy del § Email 2 de abajo.
- [ ] **Activar el Automation** (toggle del workflow a ON).
- [ ] **Prueba en cuenta de test:** suscribirse con un email personal, confirmar, verificar que llegan los 2 emails con el timing correcto.
- [ ] **Comprobar tracking:** Beehiiv analytics del workflow muestra open rate + click rate + reply rate del email 1.

---

## Email 1 — Entrega del PDF + pregunta

**Disparo:** inmediato post-confirmación double opt-in.

**Subject line:** `Tu PDF (y una pregunta)`
(22 chars · estilo *Curiosity gap + benefit*, arquetipo §14.1 del playbook.)

**Preheader:** `La Hoja de Compra ROBOHOGAR está dentro. 15 seg de lectura.`

**From name:** `Rafael de ROBOHOGAR`

**Cuerpo (pegar en Beehiiv):**

```
Hola,

Acabas de suscribirte a ROBOHOGAR y lo primero que te mandamos es la Hoja de Compra. Si viniste buscándola, aquí la tienes. Si te suscribiste por otra razón, la consideramos regalo de bienvenida — cubre exactamente lo que necesitas saber antes de comprar cualquier robot doméstico:

👉 [Descargar la Hoja de Compra ROBOHOGAR (PDF · 2 páginas)](<URL_DEL_DIGITAL_PRODUCT>)

Son las 10 preguntas que nos hacemos nosotros antes de comprar cualquier robot doméstico. Si las respondes todas, te ahorras varios cientos de euros en compras que no encajan con tu casa.

Ahora una pregunta rápida, y va en serio: **¿cuál es la zona de tu casa que más te cuesta mantener limpia?** Cocina, baño, alfombras de los niños, el estudio con pelos del perro, lo que sea.

Responde a este email con una frase. Lo leemos todos y nos ayuda a decidir qué probar y escribir los próximos meses. Cuando somos pocos suscriptores, cada respuesta pesa el triple.

Un saludo,
Rafael

P.D. Si piensas que la Hoja de Compra le viene bien a alguien, reenvíale este correo. No hace falta permiso.
```

**Formato al pegar en Beehiiv:**
- **Botón CTA nativo** (no link inline): la línea `👉 [Descargar la Hoja de Compra...]` se sustituye por un bloque Button de Beehiiv (texto `Descargar la Hoja de Compra (PDF)` + URL del digital product). Color ámbar si está configurado.
- **Bold:** solo en `¿cuál es la zona de tu casa que más te cuesta mantener limpia?` (seleccionar → B). Ese es el único CTA secundario del email, tiene que saltar visualmente.
- **Cursiva:** ninguna. Email conversacional, no literario.
- **Links inline:** ninguno en este email (solo el botón CTA).
- **Firma** "Rafael" en singular (excepción a voz plural permitida en firma/bio por editorial.md).

**Métricas objetivo (primeros 20 suscriptores):**
- Open rate: 60 %+ (benchmark welcome 2026)
- Click del PDF: 40 %+
- Reply rate: 15 %+ (señal fuerte Gmail)

---

## Email 2 — Qué esperar + 2 artículos evergreen

**Disparo:** 72 h después del email 1.

**Subject line:** `Qué esperar (y 2 joyas)`
(22 chars · *curiosity gap*, arquetipo §14.1 del playbook.)

**Preheader:** `La ruta ROBOHOGAR en 2 minutos + 2 lecturas mientras llega el martes.`

**From name:** `Rafael de ROBOHOGAR`

**Cuerpo (pegar en Beehiiv):**

```
Hola de nuevo,

Hace 3 días descargaste la Hoja de Compra. Si ya la has mirado, gracias. Si no, [aquí sigue disponible](<URL_DEL_DIGITAL_PRODUCT>).

Este correo es corto y no viene con ningún "qué opinas del tono" ni survey largo. Dos cosas:

**1) Qué vas a recibir cada semana.**

Un email los martes a las 9:00. Una review o comparativa, un dato que nos ha llamado la atención y un apunte sobre hacia dónde va esto del hogar robotizado. Unos 4-5 minutos de lectura. Nada de correos diarios ni de urgencias inventadas.

**2) Dos artículos para ir abriendo boca.**

Mientras llega el primer martes, aquí van los dos del archivo que más nos gustan:

- [Samsung Jet Bot Steam Ultra: vapor a 100 °C, pero no donde piensas](https://robohogar.com/p/samsung-jet-bot-steam-ultra-review) · Para entender por qué los titulares de aspiradores mienten casi siempre.

- [Roborock Saros Z70: ¿merece la pena pagar por un brazo mecánico?](https://robohogar.com/p/roborock-saros-z70-review) · La primera vez que un aspirador recoge calcetines del suelo. Spoiler: a medias.

Cualquier duda, responde este email. Escribimos nosotros, no un autoresponder.

Un saludo,
Rafael

P.D. Si estás en LinkedIn o X, publicamos pensamientos sueltos entre artículo y artículo. Pero el valor está aquí, en el correo del martes.
```

**Formato al pegar en Beehiiv:**
- **Bold:** las dos frases `1) Qué vas a recibir cada semana.` y `2) Dos artículos para ir abriendo boca.` → son subheadings de sección, permiten escaneo rápido.
- **Cursiva:** ninguna.
- **Links inline (3):**
  - `aquí sigue disponible` → URL del digital product (mismo link del Email 1).
  - `Samsung Jet Bot Steam Ultra: vapor a 100 °C, pero no donde piensas` → `https://robohogar.com/p/samsung-jet-bot-steam-ultra-review`
  - `Roborock Saros Z70: ¿merece la pena pagar por un brazo mecánico?` → `https://robohogar.com/p/roborock-saros-z70-review`
- **Nada de botones CTA** en este email: 3 links igual de importantes; un botón ámbar dominaría y saturaría. Links inline dejan que el lector elija.
- Si cuando esto se active ya hay >2 artículos top publicados, actualizar los 2 titulares (mantener evergreen, no reactivos).

**Métricas objetivo:**
- Open rate: 45 %+
- Click a artículos: 20 %+ (combinado, no por link)

---

## Anti-IA checklist aplicada a los 2 emails (§1 Universal)

| Check | Email 1 | Email 2 |
|---|---|---|
| Palabras §1.1 (tapiz, entramado, matizado, etc.) | 0 | 0 |
| Tricolon ≤ 2 | 1 ("Cocina, baño, alfombras, el estudio" es lista de 4, no tricolon) | 1 ("Una review, un dato y un apunte") |
| Em-dashes ≤ 3 total | 0 | 0 |
| Contrast framing "no es X, es Y" ≤ 1 | 0 | 0 |
| Clichés sensoriales §1.3 | 0 | 0 |
| Voz plural (salvo firma) | ✅ (nos debemos, hacemos, leemos, somos) | ✅ (ha llamado, nos gustan, escribimos) |

---

## Por qué el welcome flow es universal en F1 (todos los subs reciben el PDF)

En fase F1 (0-100 subs) el welcome flow es **uno solo** y lo reciben todos los suscriptores, vengan o no del banner del PDF. Razones:

1. **Todo el tráfico de suscripción en F1 viene del banner** (o de muy pocos canales más — LinkedIn personal de Rafael, boca a boca). El caso "se suscribe sin contexto del PDF" es marginal.
2. **La Hoja de Compra es temáticamente universal** para ROBOHOGAR (cubre el 70% del mix consumer). Aunque el suscriptor venga por un artículo editorial o newsletter, la Hoja sigue siendo coherente con el tema general.
3. **Simplicidad operativa** > segmentación prematura con 0-30 subs.

**Cuándo segmentar (F2+, ≥2 tangibles activos):**

Cuando se active un segundo tangible (Glosario ROBOHOGAR, Calendario rebajas ES, etc.):

- Usar **tags automáticos** basados en UTM del subscribe form. El banner ya lleva `?lm=hoja-compra&src=<slug>` → configurar Beehiiv para que ese UTM aplique tag `hoja-compra`. Banner del Glosario llevará `?lm=glosario&src=<slug>` → tag `glosario`.
- **Partir la automation** con triggers condicionales: *"IF tag contains 'hoja-compra' THEN Welcome MVP Hoja de Compra"* / *"IF tag contains 'glosario' THEN Welcome MVP Glosario"* / *"IF no tag THEN Welcome genérico (entrega ambos tangibles)"*.
- Actualizar los 2 copies por automation (email 1 menciona el tangible específico que viene, email 2 adapta los 2 artículos recomendados al tema).

Feature disponible en plan Scale con Automations 2.0. No hay que migrar hoy — anotado para cuando toque.

## Roadmap — cuándo expandir a 4 emails

**Trigger de expansión:** subs ≥200 y open rate welcome estable >50 % durante 1 mes.

**Emails 3 y 4 a añadir** (derivados de `references/newsletter/email-marketing-playbook.md § 12`):

- **Email 3 (día 7):** *Empieza por aquí*. Tercer artículo hand-pick del archivo + 3 bullets resumen. Solo tiene sentido cuando el archivo tenga ≥10 artículos publicados.
- **Email 4 (día 10):** *Encuesta corta*. Poll nativo Beehiiv con 3 opciones (más reviews / más tutoriales / más editorial futuro) para afinar backlog editorial. Solo tiene sentido cuando hay suficiente volumen para obtener N estadístico.

Hasta esos hitos, mantener el MVP de 2 emails — el 80/20 en esta fase está en captar más suscriptores, no en refinar la secuencia de los que ya lo son.

---

## Fuentes y referencias

- Benchmarks 2026: [Amra & Elma — Lead Magnet Conversion Statistics 2026](https://www.amraandelma.com/lead-magnet-conversion-statistics/)
- Beehiiv setup: [Welcome email vs welcome automation](https://www.beehiiv.com/support/article/38813477234071-welcome-email-vs-welcome-automation-which-should-you-use) · [Double opt-in & Smart Nudge](https://www.beehiiv.com/support/article/13081072798743-how-to-enable-double-opt-in-and-smart-nudge)
- Playbook editorial: [`references/newsletter/email-marketing-playbook.md § 12 + § 14`](../references/newsletter/email-marketing-playbook.md)
- Voz y anti-IA: [`.claude/rules/editorial.md`](../.claude/rules/editorial.md) · [`references/anti-ia-checklist.md`](../references/anti-ia-checklist.md)
