---
name: Left wall + Big lie + Triángulo información (ficción ROBOHOGAR)
description: Dos frameworks narrativos de Adrian Tchaikovsky (via How I Write de David Perell 2025-12-31) integrados en el pipeline de ficción ROBOHOGAR 2026-04-19 — arquitectura de plausibilidad (left wall + one big lie) y triángulo autor/personaje/lector.
type: feedback
originSessionId: 383a134e-9380-44b2-9a0b-a7aef3bbdef3
---
Tras análisis del vídeo *How to Write Absurdly Well — Adrian Tchaikovsky* (David Perell, *How I Write*, 2025-12-31, 1h5m) se integraron 2 frameworks al pipeline de ficción ROBOHOGAR. Los otros 6 consejos del vídeo fueron descartados por duplicación con el stack existente o incompatibilidad con formato email-serializado.

## 1. Left wall + One big lie (arquitectura de plausibilidad)

- **`left-wall`**: restricción real/científica/regulatoria **inviolable** del relato. Ejemplos ROBOHOGAR: `"AI Act art. 6 humanoides domésticos alto riesgo"`, `"Aspirador 2033 sin brazos · LiDAR 360° superficies sólidas"`, `"Protocolo SAMUR Madrid real"`.
- **`big-lie`**: **única** licencia creativa mayor que el relato pide al lector (máximo 1 por relato, no negociable). Ejemplos: `"Humanoide refurbished accesible a familia media ES"`, `"Aspirador modela rutinas humanas con precisión de detección de ausencia"`, `"Humanoide de cuidados diagnostica ictus 30s antes"`.
- Regla Tchaikovsky: *"You can get away with one big lie… but in order to support your one big lie, everything else needs to be true."*
- Ambos campos se declaran en el frontmatter YAML del `.md` del relato antes de redactar. `/ficcion-draft` paso 3.5 los pide explícitamente.
- Si el skill detecta 2+ big lies: recortar a 1 o reescribir el concepto. No avanzar con 2 big lies.

## 2. Triángulo de información autor/personaje/lector

- Framework: 3 niveles de info distintos — lo que el AUTOR sabe, lo que el PERSONAJE sabe, lo que el LECTOR sabe.
- Regla: el **lector debe saber algo que el personaje no** (o viceversa según la escena). Si los 3 saben lo mismo → escena plana.
- Ejemplo maestro Tchaikovsky: Rex en *Dogs of War* (perro modificado) cumple órdenes sin el marco moral para reconocerlas como crímenes de guerra. El lector sí lo ve. Asimetría = motor del libro.
- **Encaja directamente con tesis ROBOHOGAR "villano humano / robot neutro":** robots narrador (Tico, RONDA-3) o humanos con info limitada (Amparo con demencia incipiente, Clara vía epistolar) crean asimetría dramática nativa al género doméstico-especulativo.
- Aplicación: `character-bible.md` de cada serie declara para cada POV activo los campos `pov_sabe`, `pov_no_sabe`, `asimetria_dramatica`.

**Why:** Tchaikovsky tiene 60+ libros publicados (*Children of Time* ganó Arthur C. Clarke Award), es voz autorizada en sci-fi. Estos 2 frameworks son gaps reales en el stack ROBOHOGAR — el resto (Paint The Villain, especificidad, cliffhanger, world-first) ya estaba cubierto con más granularidad. El left wall evita la deriva de acumular 3-4 mentiras pequeñas que destruyen plausibilidad juntas. El triángulo de información es el framework más original del vídeo y encaja perfecto con la tesis "Black Mirror invertido" + narradores robot/humanos-limitados.

**How to apply — ORGÁNICO, NO OPCIONAL (refuerzo Rafael 2026-04-19):**

El skill `/ficcion-draft` declara `left-wall` + `big-lie` SIEMPRE, por defecto, sin esperar a que Rafael los pida. Se registran en 3 sitios a la vez:

1. **Frontmatter YAML** del relato (`YYYY-MM-DD-<slug>.md`): campos `left-wall:` y `big-lie:` rellenos antes de la redacción.
2. **Bloque visible inmediatamente debajo del H1** del relato (antes del primer párrafo de prosa), formato callout editorial tipo:

   ```markdown
   # <Título del relato>

   > **Mentira grande:** <big-lie en una frase>.
   > **Muro izquierdo:** <left-wall en una frase>.
   > *Registradas por `/ficcion-draft` · cambiar antes de publicar si no encajan.*
   ```

3. **Reporte al chat** tras generar el borrador: incluir explícitamente "📌 Mentira grande elegida: …" + "🧱 Muro izquierdo: …" al mismo nivel que el resumen del relato + villano + cliffhanger. Rafael puede cambiar la mentira o el muro antes de que el siguiente episodio se genere.

**Regla inviolable**: si paso 3.5 no está completado con ambos campos, `/ficcion-draft` NO avanza al paso 4 (Paint The Villain). Bloqueo duro.

- Personaje con POV robot o humano-limitado → declarar `pov_sabe` / `pov_no_sabe` / `asimetria_dramatica` en `character-bible.md`.
- Revisión de relatos existentes → detectar si hay 2+ big lies acumuladas (señal de deriva).

**Descartado del vídeo (documentado para no reabrir debate):**
- "Don't plan the ending" — contradice la exigencia de cliffhanger intencional de formato newsletter ES.
- "Research down to handful of words" — ya lo cubre Chiang en Anti-IA checklist §2.4.
- "Frameworks con luz grip" — meta-regla genérica; ROBOHOGAR ya es pragmático.
- "Fight scene as character revelation" — no hay fight scenes en ficción doméstica.
- "Character wears a mask" — refuerza MRU existente, no añade.
- "World-first, not plot-first" — solo aplicable a novelas largas; ROBOHOGAR arranca por semilla narrativa.

**Referencias:**
- Vídeo: https://youtu.be/LO0qHnhpkDs (David Perell · How I Write · 322K views)
- Reglas aplicadas: `@references/ficciones/serialized-newsletter-patterns.md § 2.4` · `@.claude/commands/ficcion-draft.md § 3.5` · `@references/writewithai/07-ficcion-y-narrativa-serializada.md § 3.4`
