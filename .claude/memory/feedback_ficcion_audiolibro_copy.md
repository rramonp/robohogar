---
name: ficcion — copia audiolibro obligatoria en vault
description: Todo relato generado por /ficcion-draft debe producir además una copia TTS-optimizada en 02-Drafts/Ficciones/ del vault, con el texto en bloque de código triple-backtick para activar el botón Copy de Obsidian
type: feedback
originSessionId: 215f8fd4-18e5-4b10-a009-a5542c922b93
---
Todo relato generado por `/ficcion-draft` debe producir, además del original en el repo, una **copia audiolibro** en el vault Obsidian:

```
$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/02-Drafts/Ficciones/<Título del relato> (audiolibro).md
```

**Why:** Rafael escucha los borradores en el móvil antes de publicar (vía ElevenLabs Reader o TTS nativo iOS/Android) para detectar con el oído lo que los checkers no ven: ritmo, frases que tropiezan, diálogo que suena a guion. Confirmado 2026-04-19 tras pedir "que lo pueda escuchar como audiolibro" sobre "El operador nocturno". La copia es parte del entregable del skill, no opcional.

**How to apply:**

- **Bloque de código triple-backtick obligatorio** para la parte de lectura. Obsidian renderiza botón Copy automático en la esquina superior derecha del bloque en Reading view → Rafael lo toca una vez y tiene el texto limpio para pegar en ElevenLabs Reader sin arrastrar metadata. Sin el bloque, seleccionar desde el móvil es frágil.
- **Transformaciones TTS aplicadas al contenido del bloque** (no al original):
  - Números `HH:MM` y `HH:MM:SS` → palabras (*"tres y catorce de la madrugada"*, *"nueve horas, veintitrés minutos y cuarenta y siete segundos"*).
  - Siglas problemáticas: `LED` → *"piloto"* / *"luz"*; `OCR` → *"sistema de reconocimiento óptico"*; `Q1` → *"primer trimestre"*; años con dígitos (`2029`) → palabras.
  - Cursivas `*texto*` → eliminadas (TTS las lee mal o las ignora). Énfasis se reformula si es crítico.
  - Labels UI en inglés con traducción → preferir traducción (*"sesión terminada"* en lugar de *"Session ended"*). Los rótulos diegéticos (carteles en escena) se mantienen.
  - Diálogo en inglés diegético (con traductora en escena) → se mantiene en inglés; refuerza el tono.
  - Palabras extranjeras puntuales (tagalo, etc.) → se mantienen, con pronunciación aproximada explicada en la sección *"Notas para narrarlo"* fuera del bloque.
  - Separadores de escena `## I.` y `---` → sustituir por *"Parte uno. <localización natural>."* como párrafo propio.
  - Frontmatter YAML, blockquote big-lie/left-wall y comentarios HTML → fuera del bloque, nunca dentro.
  - Cierre del bloque con *"Fin."* para pausa natural.
- **Verificación pre-output:** 0 `HH:MM` · 0 `*` · 0 `---` · 0 frontmatter · 0 comentarios HTML dentro del bloque; exactamente 2 triple-backticks (apertura + cierre); última línea del bloque = *"Fin."*.
- **Regeneración:** la copia audiolibro es derivada. Al editar el original, regenerarla. `/post-publish` debe comprobar mtime(audiolibro) ≥ mtime(original) antes de cerrar.
- **Nunca se publica.** Es solo escucha interna de Rafael. No lleva hero, no lleva SEO metadata, no se sincroniza a Beehiiv.

Regla documentada en `.claude/commands/ficcion-draft.md § Copia audiolibro para el vault Obsidian`. Ejemplo canónico: `02-Drafts/Ficciones/El operador nocturno (audiolibro).md` (2026-04-19).
