---
name: feedback_3_candidatos_composiciones_distintas (alcance universal)
description: Cuando cualquier skill (/ficcion-draft, /content-draft, /nano-banana, futuros) propone 3 candidatos de imagen, las 3 son SIEMPRE 3 ideas/composiciones/planos/encuadres claramente distintos — nunca 3 variantes sutiles de la misma. Origen 2026-04-28 PM en ficción (Pipo C-05 ×3) → ampliado 2026-04-28 PM tarde a artículos y `/nano-banana` universal.
type: feedback
---

Regla dura establecida por Rafael 2026-04-28 PM durante la generación del relato Pipo (one-shot Ficciones Domésticas) y **ampliada al alcance universal del skill `/nano-banana`** la misma tarde tras observar el mismo problema en heros de artículo.

**La regla universal:** cuando cualquier skill propone **3 candidatos de imagen**, las 3 son SIEMPRE 3 ideas / composiciones / planos / encuadres claramente distintos. Prohibido proponer 3 variantes de la misma idea cambiando solo el objeto-imposibilidad, la pose del personaje, la luz secundaria, el ángulo del producto o la expresión facial.

**Why:** el valor editorial del paso "3 opciones" es **exploratorio**, no confirmatorio. Si el skill ya decidió que una composición concreta es la correcta y solo cambia detalles internos, Rafael no decide entre composiciones — solo entre matices de una. Pierde la oportunidad de comparar gramáticas distintas en thumbnail y de descubrir que una opción inesperada funciona mejor que la "obvia". Las 3 distintas obligan a Rafael a evaluar contraste real entre patrones del frame.

**Cita literal de Rafael (2026-04-28 PM, ficción):** *"cuando me das tres opciones, creo que sean tres opciones con composiciones totalmente distintas, no tres opciones prácticamente con composiciones idénticas con pequeñas diferencias muy sutiles"*.

**Cita literal de Rafael (2026-04-28 PM tarde, ampliación universal):** *"cuando generes miniaturas con nano banana para relatos o artículos te asegures de que las tres versiones que generas tengan composiciones bien distintas, ideas, planos, etc. No que sean prácticamente la misma idea con pequeñas variaciones"*.

**How to apply (por modo del skill):**

### Modo ficción (`/ficcion-draft § 6.bis` + `/nano-banana` modo 2)

- **Verificación pre-output del paso "3 candidatos":** comprobar que `len(set([c1.C, c2.C, c3.C])) == 3` sobre las composiciones canon C-01..C-19. Si no, resamplear del pool hasta tener 3 C-XX únicos.
- **Ideal complementario** (no obligatorio, pero preferente cuando el pool lo permita): las 3 composiciones vienen además de **familias distintas** del catálogo C-01..C-19 (I Íntima · II Plano arquitectónico · III Frame-in-frame · IV Frontal/OTS · V Atmósfera/color-pop). Si las 3 son de familias distintas, contraste máximo. Si el pool no lo permite, aceptable que 2 compartan familia siempre que las 3 C-XX sigan siendo distintas.
- **Si el skill cree que una C-XX concreta encaja perfecto** con el relato: aun así debe proponer 2 más de C-XX distintas para que Rafael vea el contraste. La C-XX "obvia" puede ser la elegida finalmente, pero la elección sale del comparativo, no del prejuicio del skill.
- Aplica al paradigma personaje-acción-imposibilidad (default desde 2026-04-26 PM) y al paradigma minimalista (cuando aplica). No aplica a series con código visual declarado (Amparo · Ronda 3 · MAIA), que mantienen su composición fija como sello de serie.

### Modo artículo (`/content-draft § 6` + `/nano-banana` modo 1)

- **No hay catálogo C-XX para artículos** (es product-hero cinematográfico decision-tree de `nano-banana-prompt-base.md`). En su lugar, las 3 variantes deben jugar con ejes distintos:
  - **Plano** — detalle de producto en mano · plano americano del usuario con producto · plano amplio del entorno doméstico con producto.
  - **Sujeto principal** — el producto · el usuario en acción · el espacio doméstico · el problema que el producto resuelve.
  - **Ambiente / hora** — luz natural diurna · luz artificial nocturna · golden hour · luz dura cenital.
  - **Escala / distancia** — macro detalle · medium close-up · plano general.
  - **Paleta** — cálida ámbar/madera · fría azul/metal · neutra blancos/grises · contrastada (cálido-frío).
  - **Tipo de toma** — product hero estático · escena de uso doméstico · still life de mesa · ambient escena en movimiento.
- **Verificación pre-output:** describir las 3 variantes en `PASOS.md § Hero` con un párrafo cada una declarando gramática del frame distinta. Si las 3 descripciones son intercambiables → regenerar el set antes de invocar el script.

### Modo logos / social cards / banners (`/nano-banana` otros modos)

- Las 3 son 3 conceptos / layouts claramente distintos, no 3 reordenamientos del mismo grid.

**Incidente origen — ficción (Pipo, 2026-04-27 noche):** durante la generación del relato *Pipo*, el skill propuso 3 candidatos compartiendo todos C-05 (eje simétrico altar) + M5 (amanecer brumoso) + A4 (a través de marco), variando solo el objeto-imposibilidad (manos levitando · chispas escribiendo "Lucas" · hija sin cara extendiendo brazo). Rafael lo identificó al revisar y canonizó la regla de 3 composiciones distintas para ficción. Los 2 heros de Pipo que llegaron a generarse antes del feedback (C2 y C3, ambos C-05) quedan archivados como referencia.

**Ampliación a alcance universal (2026-04-28 PM tarde):** Rafael observa el mismo síndrome en heros de artículo y dicta extensión a cualquier invocación de `/nano-banana` que pida 3 candidatos. Pasa de regla canónica de ficción a regla canónica universal del skill base.

**Canonización en repo (2026-04-28 PM tarde):**
- `.claude/rules/editorial.md § Composición canon (C-01..C-19)` — bullet "Regla dura — los 3 candidatos son SIEMPRE 3 composiciones C-XX totalmente distintas" + bullet "Regla universal aplica también a `/content-draft` y a cualquier `/nano-banana` con 3 candidatos".
- `.claude/commands/ficcion-draft.md § 6.bis` y `§ 9` — verificación `len(set(candidatos.C)) == 3`.
- `.claude/commands/content-draft.md § 6` — bloque "REGLA DURA — las 3 variantes son 3 IDEAS / COMPOSICIONES / PLANOS / ENCUADRES claramente distintos" + ejes de variabilidad.
- `.claude/commands/nano-banana.md § Regla universal — 3 candidatos = 3 ideas / composiciones / planos distintos` — bloque al inicio del skill como regla base aplicable a todos los modos.
- `assets/branding/ficcion-hero-composiciones-canon.md § Reglas duras § 3.bis` — misma regla con verificación.
