# PASOS — La llave inglesa

**Estado:** borrador redactado 2026-04-24. Pendiente hero + audiolibro + publicación Beehiiv.

---

## Entregables generados

- ✅ **Relato md con frontmatter completo:** [`2026-04-24-la-llave-inglesa.md`](2026-04-24-la-llave-inglesa.md) — 2.710 palabras, standalone, categoría tonal radical, POV 3ª cercana presente.
- ✅ **Copia audiolibro TTS-optimizada local:** [`audiolibro.txt`](audiolibro.txt) — bloque corrido, números en palabras, iniciales deletreadas (*jota y pe*), pausas entre escenas marcadas con línea en blanco.
- ✅ **Copia audiolibro en vault Obsidian:** `02-Drafts/Ficciones/La llave inglesa (audiolibro).md` — bloque triple-backtick para botón Copy de Obsidian móvil → pegar en ElevenLabs Reader. Rafael narra con voz ES-neural Mateo o Valentina.
- ✅ **Registro actualizado:** [`content/registro-ficciones.md`](../../../registro-ficciones.md) — fila #2 añadida con metadatos completos y `⏳ pendiente R2` en columna audiolibro.

## Entregables pendientes (invocación manual posterior)

### 1. Hero visual — `/nano-banana`

Estilo canon ficción **portada minimalista · objeto-testigo** (ver `assets/branding/asset-catalog.md § 5` + `assets/branding/ficcion-hero-archetypes.md`). Objeto-testigo: **la llave inglesa con iniciales grabadas J.P. sobre superficie de metal (el transformador de la subestación, desenfocado al fondo)**. Paleta: fondo azul noche #1E2A3A + luz cálida lateral ámbar (la linterna de Martín) incidiendo sobre la herramienta. Cero caracteres chinos/asiáticos, cero neones cyberpunk, cero signos vacíos (anti-sign-guard obligatorio por bug heredado de Neon Tentacle Bar).

**Invocación sugerida:**

```
/nano-banana hero-ficcion la-llave-inglesa "primer plano cenital de una llave inglesa ajustable de treinta centímetros con mango de madera gastada, iniciales J y P grabadas a cincel en el mango, apoyada sobre la base metálica de un transformador eléctrico rural. Luz cálida ámbar lateral (linterna) iluminando las iniciales; fondo azul noche muy oscuro con la silueta desenfocada de equipamiento eléctrico. Objeto-testigo estilo still photo cinematográfico español. No empty signs, no neon, no cyberpunk, no asian characters."
```

Formato 1200×630 (hero artículo) — generar con `--model 2 --aspect 16:9 --size 2K` + crop Pillow. **NUNCA `--model flash`** (ignora aspect y cae a 1024×1024 silenciosamente). Versionar `hero-la-llave-inglesa-v1.png` + `-v1.webp`. Si Rafael rechaza, iterar `-v2`, `-v3` sin sobrescribir.

### 2. Audiolibro MP3 — `/audiobook-generate` (MANUAL-ONLY)

```
/audiobook-generate la-llave-inglesa
```

Consume créditos ElevenLabs Starter. Genera MP3, sube a Cloudflare R2 bucket `robohogar-audio`, devuelve las 4 strings para Beehiiv (título 🎧 + dek + 2 bloques HTML email/web). Duración estimada 18 min a velocidad normal. Voz recomendada: Mateo (narrador masculino ES neural) — mejor ajuste para el POV masculino y el registro castellano parco.

**Importante:** `/audiobook-generate` es MANUAL-ONLY (no encadenado automático) por economía de API. Rafael invoca cuando el texto esté aprobado.

### 3. Publicación en Beehiiv

Pegar el cuerpo del relato (el md sin frontmatter) como **post nuevo** en Beehiiv. Featured image = hero-la-llave-inglesa-v1.webp. Subject del email: a decidir antes de pegar — opciones tentativas:

- *"La llave inglesa"* (puro, 17 chars) · corto y enigmático
- *"Apagón de 48 horas en Ayllón"* (31 chars) · anclaje concreto
- *"Lo que pasó cuando apagaron el pueblo"* (38 chars) · gancho editorial

Recomendación: opción 1 para el título del post + opción 3 como subject del email (el enigma se abre con el clic). Validar contra `@rules/newsletter.md § Subject Lines` (20-45 chars · ≤1 emoji).

### 4. Post-publish

Tras pegar URL definitiva en Beehiiv:

```
/post-publish <URL>
```

Corre los 14 pasos: limpieza published/, registro-articulos (no aplica — es ficción; registro-ficciones ya actualizado arriba), llms.txt, vault sync, archive snippet update (con hero URL Beehiiv), social content, commit.

### 5. Social content — automático desde post-publish paso 11

`/social-content` se invoca desde `/post-publish` paso 11 y genera posts LinkedIn/X/IG/WhatsApp listos para Buffer, con la ficción como contenido destacado.

---

## Verificaciones pre-publicación ya aplicadas

- ✅ **Castellano peninsular directo.** Composición ES nativa desde el primer token. Cero calcos anglo, cero *"en boca de"* no-verbal, cero voz técnica anglo infiltrada en narrador doméstico.
- ✅ **Anti-IA §§1+2.** Cero *tapiz/entramado/intrincado/matizado*. Em-dashes usados con mesura (solo como inciso narrativo, no decorativo en cascada). Cero *thought verbs* Palahniuk en POV (`Martín sabe`, `Martín mira`, `Martín camina` — descartados `pensó/sintió/se dio cuenta`).
- ✅ **Villano humano doble, ninguno señalable** (Paint The Villain invertido). (a) La política pública de subvenciones que creó la asimetría. (b) La comunidad que aceptó la automatización sin pelearla. El humanoide no aparece en escena ni como presencia narrativa directa — aparece como sustantivo genérico en la exposición inicial y como ausencia durante las 48h.
- ✅ **Cliffhanger estrictamente emocional.** Martín miente al Ministerio con frase preparada + saludo de dos dedos con Alicia. La decisión está tomada pero el peso moral queda con el lector. Cero cliffhanger físico.
- ✅ **Cero marcas comerciales reales de robótica** en narrador. El humanoide es genérico ("humanoide de cuidados subvencionado"). Nombre propio: ninguno (el humanoide no es personaje en esta ficción).
- ✅ **Nombres ES peninsulares canónicos.** Martín Sanchidrián, Alicia Peña, Ramón Cacharro, Juanjo Herrero, Carreras, Mercedes, Doña Esther, Don Emilio, Marta, Eugenia, Juan Peña (padre fallecido de Alicia, inicial J.P. en la llave).
- ✅ **Afiliación política omitida.** Martín es "alcalde independiente por agrupación vecinal". Ni IU ni PP ni Vox ni sigla nacional.
- ✅ **Dato real anclado.** Ejercicios REE post-crisis Ucrania + Ley 39/2006 Dependencia + INE despoblación Castilla y León + arquitectura eléctrica rural + CIS cohesión vecinal post-covid. Bloque "Lo real detrás del relato" al final del md con contexto verificable.
- ✅ **Left-wall + big-lie declarados** en frontmatter. Big-lie marcado como única licencia: la impunidad de 12h del sabotaje.
- ✅ **Triángulo de asimetría dramática.** El lector sabe lo que Martín sabe **más un dato** que Martín ve demasiado tarde (las iniciales J.P. en la llave = Juan Peña, padre de Alicia, ferretero hasta 1991).

## Verificaciones pendientes antes de pegar en Beehiiv

- ⏳ **`/validate-prose-es` sobre el md.** Segunda capa (grep de 22 calcos + LLM reader). Invocación:
  ```
  /validate-prose-es content/ficciones/_one-shots/la-llave-inglesa/2026-04-24-la-llave-inglesa.md
  ```
- ⏳ **Read-aloud final** — leer en voz alta escena 4 (enfrentamiento en el bar) para confirmar que el diálogo suena natural en castellano peninsular parco. Si algo chirría → reescribir.
- ⏳ **Revisión Rafael.** Validar tono, ritmo, cierre. Posibles ajustes:
  - ¿Demasiada evidencia circunstancial en escena 4? Martín identifica a los tres "por evidencia circunstancial" pero la prosa solo muestra la llave + el parentesco. Aceptable si se asume el conocimiento de alcalde-del-pueblo; si resulta flojo, añadir un detalle (la bolsa de herramientas del viernes, las botas que ha visto a los tres calzar).
  - ¿Mercedes (mujer de Martín) tiene presencia suficiente? Aparece tres veces (viernes llegada / madrugada dormida / ausencia implícita al final). Si Rafael quiere más, añadir una línea en escena 5 con Mercedes esperándolo al volver a casa.
  - ¿La frase "En ese momento no los une" al final de la escena 2 funciona como foreshadowing, o es demasiado explícita? Alternativa: cortar la frase. El lector conecta solo.

---

## Triggers para retomar

| Qué quiero retomar | Frase exacta |
|---|---|
| Generar hero | **"Genera hero de La llave inglesa"** o directamente `/nano-banana hero-ficcion la-llave-inglesa ...` |
| Generar audiolibro MP3 | **"Genera audiolibro de La llave inglesa"** o `/audiobook-generate la-llave-inglesa` |
| Validar prosa ES | **"Valida prosa ES de La llave inglesa"** o `/validate-prose-es content/ficciones/_one-shots/la-llave-inglesa/2026-04-24-la-llave-inglesa.md` |
| Post-publish | **`/post-publish <URL-beehiiv>`** tras pegar URL definitiva |
| Ajustar borrador | **"Retocamos La llave inglesa — <qué ajustar>"** |
