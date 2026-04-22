# PASOS · Papá desde Singapur

Ficción one-shot standalone. Inspiración: *Beyond the Sea* (Black Mirror S6E3) adaptada a paternidad desplazada ES 2032.

## SEO metadata (copiar a Beehiiv)

| Campo | Valor |
|---|---|
| **Title tag** | Papá desde Singapur — Ficciones Domésticas |
| **Meta description** | Andrés se desplaza tres meses por trabajo y contrata un humanoide-avatar para seguir en casa. Cuando vuelve, su hijo de seis años compara. |
| **Slug** | `papa-desde-singapur` |
| **Tag Beehiiv** | Opinión (+ tag interno: Ficciones Domésticas) |
| **Fecha borrador** | 2026-04-22 |
| **Longitud** | standalone · 2.650 palabras aprox |

## Resumen de la ficha editorial

- **POV:** tercera cercana Andrés, presente (con flashback breve al acto II en pasado narrativo, marcado con bisagra *"Tres meses antes"*).
- **Categoría tonal:** `inquietante` (matiz triste/ambiguo · cierre con elisión — nadie dice lo que ha pasado).
- **Framework:** Pixar Story Spine 8 frases + MRUs durante prosa.
- **Villano humano (Paint The Villain):** *"La presencia mediada que se cobra en silencio"* — la cultura comercial que vende estar presente como servicio y, al entregar una versión optimizada del padre, revela lo que el padre real ya no tenía. Andrés es víctima doble: pierde a la familia por haber intentado no perderla. El humanoide es instrumento neutro, no antagonista.
- **Left-wall:** teleoperación humanoide con latencia <300 ms ya es industrial en 2026 (1X NEO, Figure, Unitree); telepresencia corporativa embrionaria (Ava, Double Robotics); gap Stanford 89,4 % lab vs 12 % real documentado; AI Act art. 50 en vigor pleno desde 2-ago-2026 exige revelar presencia de agente IA.
- **Big-lie (1, la única):** servicio comercial de proxy corpóreo doméstico con humanoide-avatar pilotable a distancia y modo auto autónomo (más paciente que el piloto) cuando el usuario se desconecta.
- **Dato real ancla** (pegar en *Lo real detrás del relato* al publicar):
  1. 1X anunció el 12-abr-2026 acuerdo con EQT para desplegar 10.000 unidades NEO teleoperadas por operadores remotos en Filipinas para clientes industriales europeos.
  2. Stanford AI Index 2026 documenta en el benchmark Behavior-1K un gap 89,4 % éxito en laboratorio vs 12 % en tareas domésticas reales — el humanoide autónomo en casa aún falla sin piloto humano detrás.
  3. AI Act art. 50 (en vigor pleno 2-ago-2026) obliga a revelar al interlocutor humano la presencia de un agente de IA.

## Alternativas villano humano (5 candidatos evaluados · Paint The Villain)

1. *El fantasma del padre optimizado* — el espejismo de que la versión mejor administrada de uno mismo puede sustituir al original.
2. *La culpa corporativa* — la carrera laboral que obliga a delegar la paternidad y vende "soluciones" culposas.
3. *El matrimonio gestionado* — Paloma lleva la carga mental + cede encantada a que otro la asuma.
4. *La infancia eficiente* — cultura de crianza que valora al adulto "paciente" por encima del "presente imperfecto".
5. **ELEGIDO · La presencia mediada que se cobra en silencio** — el servicio comercial que promete estar presente; lo que amplifica es lo que ya estaba (Andrés llevaba dos años "medio ausente" aunque físicamente presente).

## Hero image

Pendiente. Rafael decide si genera hero o publica sin hero (Ficciones en fase 1 admite publicar sin hero si no hay presupuesto de atención). Si se genera, código visual sugerido: **Black Mirror frío** (subcategoría "Relatos inversos de Black Mirror" en `rules/editorial.md § Narrativa especulativa` — queda reservado para ficciones inquietantes donde el sistema humano es la amenaza y el robot es neutro, exactamente este caso).

Prompt base sugerido (adaptar en `/nano-banana` si se activa):

```
Medium close-up interior shot, 2032 Madrid upper-middle-class apartment at 23:10 local time,
corner of the living room. A humanoid robot (matte gray polymer shell, no LEDs, no visible
branding, proportions like 1X NEO but grayer and more utilitarian) kneeling next to a
child's bed, holding a small white teddy bear. Six-year-old boy in pajamas sitting up,
finger on lips. The humanoid's free hand mirrors the gesture.
Warm bedside lamp as only light source, amber glow. The parents' bedroom door ajar
across the hallway, darker. Spanish domestic details: Lego shelf half-visible,
a plastic rocket lamp off on the nightstand. Desaturated palette: cold grays in the
humanoid and the walls, warm amber only in the lamp spill.
Still cinematographic frame, shallow depth of field, no faces fully lit.
No text, no letters, no Asian characters, no windows to exterior, no LEDs, no neon.
References: Black Mirror S6 "Beyond the Sea" interior lighting, "After Yang" tonal warmth.
```

## Second reader externo — `/validate-prose-es`

**Recomendado pre-publicación.** El skill `/ficcion-draft § 8.4` marca esto como obligatorio cuando se va a publicar. En modo auto one-shot el generador lo deja pendiente para que Rafael decida:

- Si Rafael valida directamente el texto y decide publicar sin second reader: proceder a paso 2 (audiolibro).
- Si Rafael quiere filtro externo de calcos y colocaciones ambiguas: invocar `/validate-prose-es content/ficciones/_one-shots/papa-desde-singapur/2026-04-22-papa-desde-singapur.md` antes del paso 2. El reporte se guardará en `validator-reports/2026-04-22-report.md`.

El generador confía en que 8.3 (25 greps anti-calco EN→ES) han pasado; el read-aloud test interno identificó 2 frases que se reescribieron antes del output (*"en stand-by doméstico, solo se activaba cuando detectaba suciedad o una voz de mando"* → *"estaba inactivo, solo se despertaba si alguien le hablaba o si había que limpiar algo"*; *"No ofreció solución"* → *"No le propuso nada"*).

## Checklist publicación Beehiiv

- [ ] Rafael edita texto final (tipo 1-2 pases de lectura en voz alta)
- [ ] Si procede, corre `/validate-prose-es <path>` y aplica fixes
- [ ] Genera hero con `/nano-banana` (opcional) o publica sin hero
- [ ] Copia el MD a Beehiiv como borrador
- [ ] Pega en *Lo real detrás del relato* los 3 datos ancla de arriba
- [ ] Tag Beehiiv: **Opinión** (+ tag interno Ficciones Domésticas si existe)
- [ ] Publica con `Email and web` (ya hay audiencia suficiente para emitir; si Rafael prefiere reservar el envío, usar `Web only`)
- [ ] Pega URL definitiva al autor del pipeline y ejecuta `/post-publish <URL>` para el cierre

## Snippet CTA final (auto-inserta al migrar a Beehiiv)

Al pasar a Beehiiv, cierra el relato con el snippet canónico **ficción** de `rules/newsletter.md § Snippet canónico · banner suscripción al final de ficción`:

- eyebrow `ROBOHOGAR` (ámbar)
- `¿Te ha gustado?`
- `La próxima Ficción Doméstica, en tu correo.`
- botón `Suscribirme` → `https://robohogar.com` (sin UTM)
- trust-line `Newsletter gratis. Un email por semana. Cancela cuando quieras.`

NO usar el CTA de artículo no-ficción (`¿Te ha servido este análisis?`). Son snippets distintos, no mezclar.

## Hooks para siguiente relato o serie

El relato es one-shot, pero el universo del "proxy corpóreo doméstico" admite expansión si el tema resuena:

- Variante POV Paloma: los tres meses desde la perspectiva de la mujer que recibe al humanoide-avatar — qué gana al tener "al marido presente", qué descubre al comparar. Sería ambiguo, no inquietante.
- Variante POV Mateo (1ª persona niño): peligroso de ejecutar bien; si se hace, flash 500-800 palabras, gran responsabilidad con la voz.
- Tie-in editorial: artículo de no-ficción ROBOHOGAR *"Los humanoides que te pilotan desde otro continente: qué hay ya en 2026 y qué no"* (anclado al deal 1X-EQT + AI Act art. 50 + estado Ava/Double).

No canonizar serie "Presencia Vida" sin validación explícita de Rafael. El one-shot funciona cerrado; abrir serie exigiría bible + arco.

## Registro en `content/registro-ficciones.md`

Al publicar, añadir entrada con `categoria-tonal: inquietante`. Útil para el auto-balanceo del catálogo en `/ficcion-draft § 0.5` (próximas invocaciones).

## Copia audiolibro

Generada en vault Obsidian: `02-Drafts/Ficciones/Papá desde Singapur (audiolibro).md`. Optimizada TTS (sin cursivas, sin dividers, reloj en palabras cuando procede). Lista para copiar a ElevenLabs Reader desde el móvil y escuchar.

Al editar el MD del relato, regenerar la copia audiolibro con *"regenera audiolibro de papa-desde-singapur"*.

## Audiolibro ElevenLabs (paso 2 del pipeline del día)

Tras validación Rafael del texto:

```
/audiobook-generate papa-desde-singapur
```

Invocación MANUAL (regla canon `CLAUDE.md § Skills del pipeline`). Voz Luis `GojDwihhnL1f7RrBuXsJ`. Stats + OK antes de consumir API.
