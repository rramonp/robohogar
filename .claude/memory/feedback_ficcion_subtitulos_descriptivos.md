---
name: Subtítulos descriptivos en cada sección de Ficciones Domésticas (no romanos pelados)
description: Toda Ficción Doméstica ROBOHOGAR usa "## I. Título sobrio" en lugar de "## I" pelado. Aplica a los 3 formatos consistentemente: markdown fuente · HTML Beehiiv · audiolibro TTS. Regla permanente desde 2026-04-24.
type: feedback
originSessionId: 01128ef3-6a5c-4511-814e-f5225d861642
---
Toda Ficción Doméstica publicada en ROBOHOGAR estructura sus secciones con **número romano + título descriptivo corto**, no con romanos pelados.

Formato canónico:

```markdown
## I. El botón
## II. Octubre del treinta y cuatro
## III. Hernán
## IV. La diapositiva
## V. La cláusula
```

**Why:** la audiencia ROBOHOGAR es mainstream Beehiiv (lectura en móvil/email, escaneo con el pulgar, sesiones cortas). Los romanos pelados (`## I` sin texto) son canon literario peninsular contemporáneo (Bolaño, Sara Mesa, Pilar Adón, Bolaño) pero asumen un lector que se sienta a leer 20 minutos en silencio. Para newsletter mainstream:

- Los romanos pelados se sienten fríos o desorientadores en pantalla.
- Hacen que el relato parezca "un muro de texto con números".
- Rompen la posibilidad de retomar tras pausa (¿"VII" qué era?).
- Suenan pretenciosos para el lector medio.

Los subtítulos descriptivos cortos resuelven esto sin sacrificar nada literario: son sobrios (no Wattpad), ES peninsular, no spoilean.

**How to apply:**

- **Plantilla canónica para elegir el subtítulo:** la primera línea narrativa de la escena O el objeto-testigo / personaje / momento clave de esa sección. 1-4 palabras.
  - ✅ *"El botón"*, *"Hernán"*, *"La diapositiva"*, *"Managua"*, *"La una y dieciséis"*.
  - ❌ *"En el que VELA-9 descubre el secreto del ministro"* (demasiado largo + spoiler).
  - ❌ *"💥 ¡La revelación!"* (Wattpad/clickbait).
- **Tres formatos consistentes:** el `.md` fuente, el HTML Beehiiv y el TXT audiolibro comparten **exactamente los mismos subtítulos**. En audiolibro `## I. El botón` → `Parte uno. El botón.` (mismo título, formato narrado).
- **Aplica a todos los modos** del skill `/ficcion-draft`: one-shot, episodio-serie, episode-0, piloto, tie-in.
- **Si un relato existente tiene romanos pelados** (ficciones publicadas antes de 2026-04-24): se queda como está, no se backfilla retroactivamente.

**Origen:** Rafael 2026-04-24 sobre *La objeción*. Detectó que el audiolibro tenía subtítulos descriptivos ("Parte cuatro. La diapositiva.") pero el `.md` y el HTML Beehiiv tenían solo romanos pelados (`## IV`). Preguntó si los romanos pelados eran convención real o invención. Confirmé que sí son convención literaria peninsular (Bolaño, Mesa, Adón) pero argumenté que para el contexto Beehiiv newsletter mainstream los subtítulos descriptivos funcionan mejor. Rafael aprobó: *"Ok, adelante. Y a partir de ahora, siempre así."*.

**Aplicación operativa:**
- `.claude/commands/ficcion-draft.md § Output → estructura obligatoria`: bullet "Subtítulos descriptivos OBLIGATORIOS" añadido 2026-04-24.
- `.claude/commands/ficcion-draft.md § Copia audiolibro paso 9`: los subtítulos del audiolibro replican los del `.md` fuente (no inventar nuevos).
