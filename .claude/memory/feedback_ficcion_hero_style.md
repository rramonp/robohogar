---
name: ROBOHOGAR — sistema visual por serie para heros de ficción + 2 estilos reservados
description: Cada serie (y one-shot) de Ficciones Domésticas tiene un código visual propio y consistente, para que el lector las reconozca de un vistazo. 3 códigos activos (Amparo domestic warm, RONDA-3 documental social, MAIA epistolar literario dual Cáceres/Berlín). 2 reservados (Asimov oil painting = ebook; Black Mirror frío = relatos inversos). Regla universal: siempre humano + robot/tech en el mismo frame.
type: feedback
originSessionId: b7cd7662-3738-46e0-8b2b-47e9a986d811
---
## Principio rector (pipeline)

**Toda serie de Ficciones Domésticas — y todo one-shot — debe tener un código visual propio, consistente a lo largo de sus episodios.** La diferenciación visual es parte del producto editorial: el lector debe reconocer "esto es un Amparo", "esto es un RONDA-3", "esto es un MAIA" de un vistazo en el feed de Beehiiv y en redes. Validado por Rafael el 2026-04-18.

**Cómo se aplica:**
- Al crear una nueva serie: definir código visual en `arco-serie.md` § 9 "Notas de producción" → "Hero image recurrente" (framing, paleta, referencias, elementos constantes) ANTES del primer episodio.
- Al crear un one-shot: definir código visual en el frontmatter del relato o en un `PASOS.md` — no reutilizar sin pensar el código de otra serie.
- Al generar hero con `/nano-banana`: leer primero esta memoria + el § "Hero image recurrente" del arco-serie. Mantener los elementos constantes (robot/tech del universo + paleta + referencias) y variar escena/humano según el episodio.
- El skill `/ficcion-draft` paso de generación de hero debe consultar esta memoria.

## Regla universal (los 3 códigos activos + 2 reservados la cumplen)

**Todo hero de ficción incluye humano + robot o dispositivo tecnológico visible en el mismo frame.** Sin mezcla humano+tech, pierde el "toque ROBOHOGAR". El "dispositivo" puede ser humanoide, utility robot pequeño, laptop-IA, altavoz inteligente o panel doméstico — nunca un hero sin tecnología presente.

## Códigos activos por serie

### 1. La Casa de Amparo → "domestic warm"

- **Robot constante:** Hugo humanoide 170cm cream matte, diseño minimalista, sin LEDs
- **Humano principal:** Amparo (mujer 78, gris recogido, housecoat, butaca floral). Ocasional: Vicky (nieta), Mercedes (hija)
- **Espacio constante:** un piso antiguo de Lavapiés Madrid — butaca floral + crucifijo + sideboard con fotos + taza Manzanares + persianas venecianas + alfombra persa
- **Framing:** plano frontal medio, Hugo + humano enteros en el frame
- **Luz:** una única fuente cálida (lámpara tulipán ámbar ocre), resto en penumbra cálida
- **Paleta:** ámbar ocre cálido saturado
- **Referencias cinematográficas:** After Yang + Amor sin escalas (cocina íntima)
- **Precedente canónico:** `content/ficciones/la-casa-de-amparo/assets/hero-ep0-llegada-v2.png`

### 2. Crónicas de Ronda 3 → "documental social"

- **Robot constante:** RONDA-3 utility pequeño 55cm, pálido matte municipal-grey, cubo con ruedas, un solo ojo cámara, sin LEDs (estética Real Humans 2012)
- **Humano:** distinto cada episodio (Manola, Awa, Álex, Pilar, Don Emilio, Raquel/Mario, Karim, Laura, Doña Mari…). Cara siempre visible.
- **Espacio:** distinto cada episodio (piso VPO diferente del bloque de 18) — pero todos son VPO español clase trabajadora 2033
- **Framing:** plano medio, robot + humano ambos visibles enteros, ángulo ligeramente bajo (no extremo POV 55cm, sí un poco más bajo que Amparo)
- **Luz:** práctica realista — fluorescente cocina, lámpara IKEA barata, ventana con persiana sin artificio cinematográfico
- **Paleta:** ocre sucio ligeramente verdoso, desaturación superior al resto, grano denso
- **Referencias cinematográficas:** Perfect Days (Wenders 2023) + Real Humans
- **Código de continuidad:** el robot es ancla constante; el humano y el interior cambian cada episodio

### 3. Cartas a MAIA → "epistolar literario" (paleta dual Cáceres/Berlín)

- **"Robot":** NO humanoide visible — MAIA vive en el laptop + altavoces inteligentes + lámpara brass del despacho. La tecnología en el frame es siempre hardware sutil, nunca humanoide
- **Humano principal:** Clara (mujer 30-35, Berlín), Fernando aparece solo en fotos enmarcadas (está muerto), Javier vía WhatsApp transcrito, Remedios anciana vecina
- **Espacio dual:** episodios desde Cáceres → estudio del padre (mahogany + crucifijo + libros legal + lámpara brass). Episodios desde Berlín → piso minimalista alemán (madera clara + una planta + invierno por ventana)
- **Framing:** plano frontal medio, humano leyendo/escribiendo, gesto contenido, laptop + lámpara siempre en frame
- **Luz:**
  - Cáceres → ámbar cálido burgundy intenso, una sola lámpara brass
  - Berlín → azul frío desaturado dominante (luz invierno), lámpara brass cálida como único punto ámbar contraste
- **Referencias cinematográficas:** After Yang + 84 Charing Cross Road (ambos) + Her Berlín invierno (para lado Berlín)
- **Código de continuidad:** la dualidad geográfica es el código — el lector reconoce por la paleta si el episodio se escribe desde Cáceres o desde Berlín

## Estilos reservados (NO usar en episodios)

### Asimov retrofuturista oil painting

- **Uso exclusivo:** tapa de ebook recopilatorio de Ficciones Domésticas (planeado ~500 subs — ver `references/ficciones/ebook-roadmap.md`)
- **Formato:** oil on canvas painterly Michael Whelan + John Berkey, brush strokes visibles
- **Robot:** positronico clásico — brass/ivory plated, articulaciones metal pulido, ojos glass-dome glow dorado, proporciones butler Art Deco
- **Espacio:** interior aristocrático enclosed (NO ventana exterior), mahogany, orrery, chimenea, gilt frames, cortinas burgundy
- **Paleta:** brass/amber dorado + burgundy + chiaroscuro cálido
- **Precedente visual:** `assets/branding/ficcion-references/estilo-asimov-ebook.png`

### Black Mirror frío

- **Uso:** para relatos de la sub-línea "Relatos inversos de Black Mirror" — relatos inquietantes donde el robot es neutro y el humano/sistema es la amenaza (coherente con regla editorial "el robot nunca es el villano")
- **Formato:** cinematic hyperreal Netflix prestige, crisp digital, slight bluish tint
- **Robot:** minimalista Scandinavian industrial, matte light-grey, pinpoint azul frío casi imperceptible en ojos
- **Espacio:** interior contemporáneo enclosed (NO ventana, NO pantallas con contenido), concrete-grey walls, pale wood floor
- **Paleta:** pale steel blue + ash grey + bone white, único acento ámbar frío de floor lamp
- **Referencias:** Black Mirror (*Be Right Back*, *Hang the DJ*) + Devs + Ex Machina
- **Precedente visual:** `assets/branding/ficcion-references/estilo-blackmirror-inquietante.png`

## Anti-patterns universales (los 5 estilos)

- NO hero sin humano + tech juntos en el frame
- NO ventana exterior visible con neones/carteles (Gemini mete caracteres asiáticos — ver historial en `assets/branding/nano-banana-prompt-base.md`)
- NO LEDs/neones/glow en robots (excepciones: glow dorado en ojos Asimov; pinpoint azul sutil en Black Mirror)
- NO texto, letras ni caracteres asiáticos en ningún elemento
- NO showroom comercial, NO minimalismo nórdico glossy, NO sci-fi abstracto monumental tipo Dune (probado — borra el personaje humano)
- NO mezclar códigos visuales dentro de una misma serie
