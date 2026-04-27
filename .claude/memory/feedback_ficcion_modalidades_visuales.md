---
name: Modalidades visuales (M1-M6) — eje cromático ortogonal de heros de Ficciones
description: Catálogo cerrado de 6 paletas/atmósferas que rotan relato a relato para evitar que la galería /Ficciones se vea homogénea. Anti-repetición últimos 3, transversal a paradigma minimalista y personaje-acción.
type: feedback
---

Regla dura establecida por Rafael 2026-04-27 PM tras feedback comparativo con el canal "Domestic Fictions" de YouTube.

**Toda generación de hero de relato Ficciones Domésticas (one-shots y miniseries futuras, paradigmas minimalista § 5 y personaje-acción-imposibilidad § 5.bis) debe declarar `modalidad_visual: M1|M2|M3|M4|M5|M6` y `angulo_camara: A1|A2|A3|A4|A5` en frontmatter, y respetar anti-repetición de los últimos 3 heros publicados (transversal a paradigma) en ambos ejes.**

**Why:** los 4 heros más recientes (la-canguro v4, el-operador-nocturno v7, el-humanoide-ministro v9, la-hija-padre-muerto/el-que-viene-a-tomar-cafe v6) compartían exactamente la misma modalidad — fondo `#1E2A3A` + ámbar lateral cálido + ángulo eye-level + plano medio close-up. Como conjunto en la galería `/Ficciones` de Beehiiv, las 4 cards apiladas se leían como "el mismo hero con personajes distintos". Rafael comparó contra el canal "Domestic Fictions" de YouTube (capturas: tormenta cobalto, atardecer magenta, día gris plomizo, fluorescente clínico, amanecer brumoso) y pidió variedad equivalente, manteniendo identidad de marca: *"Necesito un par de variantes. Para que no sea siempre la misma luz, mismos colores, mismo todo. […] Quiero que tengas una regla para generar variantes y que, con el mismo formato, sean todas muy diferentes. Desde composición a coloreado."*

**Catálogo cerrado** (canon en [`assets/branding/ficcion-hero-archetypes.md § Modalidades visuales (M1-M6)`](../../assets/branding/ficcion-hero-archetypes.md)):

| # | Modalidad | Paleta dominante | Color de fuente única | Tonalidades preferentes |
|---|---|---|---|---|
| **M1** | Ámbar nocturno *(default heredado)* | Azul noche `#1E2A3A` + ámbar `#F5A623` | Lámpara doméstica cálida | inquietante · ambiguo · mundano |
| **M2** | Cobalto tormenta | Cobalto profundo + cian/púrpura + cristal mojado | Backlight tras ventana lluviosa | inquietante · radical |
| **M3** | Diurno plomizo | Gris-azulado pálido + ocre + blancos crudos | Norte difusa neutra | mundano · ambiguo |
| **M4** | Atardecer magenta-naranja | Magenta + naranja sandía + violetas largas | Sunset window horizontal | inspirador · ambiguo |
| **M5** | Amanecer brumoso | Teal-blue helado + crema + ámbar tenue | Milky backlight con vapor | ambiguo · inspirador · mundano |
| **M6** | Fluorescente clínico-institucional | Cyan-verde + blanco-azulado + turquesa | Cenital fluorescente fría | radical · inquietante (institucional) |

**ADN inmutable que conviven todas las modalidades:** estilo painterly editorial Penguin Modern Classics + chiaroscuro dramático con foco lumínico **único** (Hopper-meets-Caravaggio) + composición del paradigma vigente + tight medium close-up legibilidad 120px + anti-sign-guard activo (cero neones, cero caracteres asiáticos, cero LEDs/glow, cero texto) + dimensiones 1200×630.

**How to apply (regla operativa):**

- **Frontmatter obligatorio en relatos nuevos** (one-shots y miniseries futuras): `modalidad_visual: M1..M6` + `angulo_camara: A1..A5`. Sin ambos, el skill `/ficcion-draft § 8.x Hero` bloquea el output.
- **Anti-repetición transversal a paradigma:** ningún `modalidad_visual` ni `angulo_camara` puede repetirse en los **últimos 3 heros publicados**. El skill consulta `content/registro-ficciones.md` columnas `Modal.` y `Áng.` antes de proponer.
- **Mapeo tonalidad → modalidades preferentes:** el skill propone candidatos del subset preferente; Rafael valida o pide alternativa. La regla NO es exclusiva — un relato puede pedir modalidad fuera de su preferente con motivo declarado en `PASOS.md § Hero`.
- **Forzado de cobertura:** en los 10 primeros heros desde 2026-04-27, deben aparecer al menos 5 de las 6 modalidades. Si una nunca apareció tras 10, el skill bloquea las otras hasta que toque la faltante.
- **Series activas con código declarado** (La Casa de Amparo · Crónicas de Ronda 3 · Cartas a MAIA): NO usan M1-M6 ni A1-A5. Mantienen su código visual fijo. Igual scope que el paradigma personaje-acción-imposibilidad.
- **Aplicación retroactiva:** ninguna. Los 9 publicados pre-2026-04-27 se backfillean con `M1` + `A1` en `registro-ficciones.md` y NO se regeneran sus heros (decisión Rafael 2026-04-27 vía AskUserQuestion). La galería `/Ficciones` ganará variedad orgánicamente desde el siguiente relato.
- **Prompt fragments por modalidad** (inglés, listos para Gemini): catálogo en [`ficcion-hero-archetypes.md § Prompt fragments por modalidad`](../../assets/branding/ficcion-hero-archetypes.md). Sustituyen el bloque `[D]` (luz/paleta/atmósfera) del template canónico.

**Riesgos por modalidad** (auditoría visual con cuidado):

- **M2 / M6:** Gemini puede meter neones de tormenta en M2 (escaparates urbanos al fondo, luces de coche borrosas) o pantallas LED de hospital en M6. Si los mete → regen.
- **M3 / M5:** menos contraste cromático que M1 → más arriesgadas en thumbnail 120px. Verificar legibilidad de silueta antes de aprobar.
- **M4:** Gemini puede saturar magenta hasta perder identidad serie. Si la imagen empieza a parecer un fanart anime → bajar saturación o regen.

**Origen completo + plan de implementación:** [`C:\Users\cri-c\.claude\plans\las-nuevas-miniaturas-de-sunny-liskov.md`](../../../.claude/plans/las-nuevas-miniaturas-de-sunny-liskov.md). Decisiones aprobadas vía AskUserQuestion (alcance canon = ampliación a 6 modalidades · retroactividad = solo desde el próximo relato).

**Documentación canónica relacionada:**
- Catálogo + reglas duras + prompt fragments: [`assets/branding/ficcion-hero-archetypes.md § Modalidades visuales (M1-M6)`](../../assets/branding/ficcion-hero-archetypes.md).
- ADN visual amplio (conviven 6 modalidades): [`.claude/rules/editorial.md § Hero de one-shots y miniseries`](../rules/editorial.md).
- Algoritmo del skill (paso 7-10): [`.claude/commands/ficcion-draft.md § Paradigma 2 — Algoritmo de selección`](../commands/ficcion-draft.md).
- Tracking en registro: [`content/registro-ficciones.md`](../../content/registro-ficciones.md) columnas `Modal.` + `Áng.`.
