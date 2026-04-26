---
name: Display title YouTube-style + canon hero personaje-acción-imposibilidad para Ficciones
description: Regla dura 2026-04-26 PM — relatos one-shot/miniserie llevan display_title declarativo (familia G) + tag poético del catálogo cerrado + hero compositivo personaje-acción-imposibilidad. No retroactivo.
type: feedback
---

Regla dura establecida por Rafael 2026-04-26 PM tras ver recomendaciones de YouTube anglo de un canal de "Domestic Fictions". Cita literal: *"quiero cambiar el formato de los títulos de mis próximos one-shots y miniseries y miniaturas a algo similar a lo que me recomienda YouTube, fíjate los títulos como ya hay un hook en ellos y las miniaturas que también tienen un hook mucho más fuerte que los nuestros que son simplemente una imagen representando el relato de forma pasiva"* + *"las miniaturas no quiero copiar estilo pero composición y general idea de montaje"*.

Tres reglas duras simultáneas:

**1. `display_title:` declarativo paradójico (frontmatter obligatorio).** Formato `"El/La [rol/oficio] que [acción inusual + objeto-imposibilidad]"`, 8-15 palabras. Vive **paralelo** al `title:` corto (sustantivo simple 2-6 palabras que sigue siendo nombre de fichero, breadcrumb y URL slug-friendly). El `display_title` se renderiza en: subject del newsletter Beehiiv · H1 web del post · OG title de cards · alt-text de miniatura · copy de redes generado por `/social-content`. La URL pública sigue siendo `slug:` corto.

Catálogo de subfamilias G en `references/ficciones/hooks-taxonomia.md § Familia G` (canon nuevo paralelo a A-F):
- **G1** — Oficio + acción imposible (*"La cerrajera que forja llaves para puertas que solo aparecen en pesadillas"*).
- **G2** — Acto cotidiano + objeto imposible (*"El padre que graba audios para una hija que aún no ha decidido nacer"*).
- **G3** — Sujeto + paradoja temporal (*"La mujer que envía mensajes al móvil que tiró al mar en 2018"*).
- **G4** — Función + sustitución imposible (*"El humanoide que cobra de noche por los sueños que no tiene"*).

Anti-repetición: no repetir misma subfamilia G en últimos 5 display titles del registro. Si family = G1, banda de personaje (A-E) no encadenada 3 veces seguidas.

**2. `tag_poetico:` ES de catálogo cerrado (frontmatter obligatorio).** Una de 10 etiquetas mapeadas a categoría tonal:
- inquietante: *Hogar uncanny* / *Habitaciones extrañas*
- radical: *Cuidados rotos* / *Diálogos rotos*
- ambiguo: *Memorias prestadas* / *Espacios subconscientes*
- inspirador: *Cocinas tibias* / *Anatomía emocional*
- mundano: *Domingos eléctricos* / *Física melancólica*

Catálogo cerrado. Si llega un eje no cubierto, se amplía la regla en `editorial.md`, **no por relato**. Backfill retroactivo a los 9 publicados aplicado en `content/registro-ficciones.md`.

**3. Hero canon `personaje-acción-imposibilidad` (default desde 2026-04-26 PM).** Composición teatral con 3 elementos en frame:
- Personaje identificable por oficio/rol/atrezzo en primer plano.
- Acción concreta visible (verbo del display_title traducido visualmente).
- Objeto-imposibilidad materializado físicamente (humo de color, líquido luminoso, partículas que escriben, humanoide en gesto incoherente con su función).

Estilo visual: still-life cinematográfico ROBOHOGAR (After Yang / Hammershoi / Wenders). **NO** oil painting / digital painting anglo. Mantiene paleta azul `#1E2A3A` + foco lateral cálido ámbar único + dimensiones 1200×630 + anti-sign-guard.

Catálogo de archetypes en 5 bandas (en `assets/branding/ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad`):
- **Banda A** — Oficios domésticos / familia / cotidiano (cuidador/a, niño/a, anciano/a, yaya/o).
- **Banda B** — Trabajadores reconocibles del día a día ES (cajera, rider, conserje, profesora, operario, teleoperador, técnica del SAS).
- **Banda C** — Funcionarios y oficios públicos (interventora, agente SS, técnica de Hacienda, subinspectora SEPE, registradora civil, trabajador municipal).
- **Banda D** — Figuras públicas por rol (ministra/o, alcalde/sa, sindicalista, juez/a, embajador/a). **Convención dura: identidad por rol y atrezzo solamente, nunca cara reconocible de figura pública real.** Regen si Gemini la mete.
- **Banda E** — Cultura pop / mediática (influencer streamer, futbolista, presentadora tertulia, podcaster, cantante, periodista de pie de calle). Equipación deportiva sin colores ni escudo de equipo real.

Anti-repetición acotada al paradigma personaje-acción-imposibilidad (no contra heros minimalistas existentes): no repetir mismo archetype concreto en últimos 5 + rotar entre bandas (no encadenar 3 relatos seguidos en misma banda) + forzado de cobertura (las 5 bandas deben aparecer en los primeros 10 heros del paradigma).

**Why:** YouTube recommendation surface, Apple Mail / Gmail inbox preview, OG cards en LinkedIn/X/WhatsApp y miniaturas de Beehiiv landing premian (a) títulos con paradoja embebida en el propio título, (b) miniaturas con composición teatral fuerte (personaje + acción + objeto-imposibilidad). El formato sustantivo-simple ROBOHOGAR (*La objeción*, *El operador nocturno*) y el canon "portada minimalista · objeto-testigo" no compiten ahí. Adoptamos la gramática de hook anglo SIN copiar su estilo visual pintado — mantenemos still-life ROBOHOGAR.

**How to apply:**
- **Aplica desde el siguiente relato** (one-shot o miniserie). Cero retroactivo en `display_title` o regeneración de heros publicados.
- **Series activas con código declarado** (La Casa de Amparo, Crónicas de Ronda 3, Cartas a MAIA): tampoco se retitulan publicados, **pero sí adoptan `display_title:` + `tag_poetico:` desde el siguiente episodio**. La mejora del título YouTube-style aplica a series; lo que NO aplica es el cambio de canon visual del hero (esas series mantienen su código).
- **Bloqueo duro en `/ficcion-draft § 9`** si falta `display_title:`, `display_title_family:`, `tag_poetico:` en frontmatter, o si el display title contiene nombre propio real de figura pública, o si excede rango 8-15 palabras, o si subfamilia G repetida sin excepción documentada.
- **Compatibilidad con paradigma minimalista:** los dos canon (personaje-acción-imposibilidad nuevo · portada minimalista existente) **conviven** para one-shots. Default = personaje-acción-imposibilidad. Minimalista declarativo cuando objeto-testigo aislado del relato es más fuerte que cualquier personaje en frame (ej: tela ceremonial de *La objeción*).

**Archivos canon afectados:**
- `.claude/rules/editorial.md § Display title declarativo + Tag poético tonal + Hero personaje-acción-imposibilidad` — fuente de verdad de las 3 reglas.
- `references/ficciones/hooks-taxonomia.md § Familia G` — catálogo G1-G4 + anti-patterns + verificación pre-output.
- `assets/branding/asset-catalog.md § 5.bis` — canon visual nuevo paralelo al § 5 minimalista.
- `assets/branding/ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad` — 5 bandas + 25+ archetypes + prompt fragments por banda.
- `content/registro-ficciones.md` — columnas `Display title`, `D-T fam.`, `D-T band`, `Tag poético`, `Hero parad.` añadidas. Backfill: tag poético inferido para los 9 publicados; `Hero parad. = minimalista` para los 4 con hero registrado; resto en `—`.
- `.claude/commands/ficcion-draft.md § 5.7-bis Display title YouTube-style` + `§ 5.7-ter Tag poético tonal` + frontmatter ampliado + sección "Hero image" bifurcada en 3 paradigmas + § 9 validaciones nuevas.
- `.claude/commands/post-publish.md § 1` — verificación de display_title vs `<h1>` del post publicado.
- `.claude/commands/social-content.md § 1` — extracción de display_title como apertura de copy social.
- `.claude/rules/design.md § beehiiv-paste.html` — Meta A lee display_title (no title corto).

**Aplicación inversa:** los 9 publicados pre-2026-04-26 PM no se reescriben ni regeneran. Sus `beehiiv-paste.html` históricos (`la-objecion`, `el-operador-nocturno`) quedan como están. Apple/Amazon Music congelan metadata RSS, así que no tiene sentido reescribir feeds.

**Plan completo de implementación:** `c:\Users\bakal\.claude\plans\quiero-cambiar-el-formato-partitioned-allen.md`.
