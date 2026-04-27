# ROBOHOGAR — Asset Catalog

Catálogo vivo de los assets visuales vigentes. **Actualizar después de cada generación con Nano Banana.**

> **Cleanup 2026-04-18 (`_archive/2026-04-18-cleanup-marca-oficial/`):** archivados los 19 poses de mascota, los logos antiguos (`monogram-v11`, `icon-v6`, `lockup`, `badge`, `header-v3-bahnschrift`), las variantes v3 con fondos de color (`accent`/`cream`/`glow` + `og-1200-v3`), templates de email/CTA/YouTube/patterns/iconos de categoría sin uso activo, y `mascota-prompt.md`. La marca actual vive **únicamente** en `social/final/` + derivados en `social/`.

---

## 1. Logos oficiales (ÚNICA fuente de verdad)

Los 2 logos en `assets/branding/social/final/` son la marca ROBOHOGAR. Todo lo demás deriva de aquí.

| Logo | Archivo principal (1200×630 OG) | Avatar cuadrado (1080×1080) | Descripción |
|---|---|---|---|
| **Monograma R** | `og-seo-monogram-1200x630.{png,webp}` | `profile-monogram-1080x1080.{png,webp}` | R bold negra con ojos ámbar + antena. Imagen **principal** de marca. Más visual, ocupa espacio. |
| **Icon robot** | `og-seo-icon-1200x630.{png,webp}` | `profile-icon-1080x1080.{png,webp}` | Cabeza robot minimalista (visor + antenas + dos ojos). Marca **compacta**, ligera visualmente. |

Todos sobre fondo blanco #FFFFFF. WebP para web/OG, PNG como master.

## 2. Cuándo usar cada logo

| Contexto | Logo | Motivo |
|---|---|---|
| Landing hero, OG de artículos, portada newsletter, contextos editoriales con aire | **Monograma R** | Se lee como marca a tamaño grande, más carácter visual |
| Favicon, navbar, avatar redes sociales, footer de email, miniaturas | **Icon robot** | Legible en tamaños pequeños, menor densidad visual |
| Artículos (body content) | Ninguno — va la hero específica del artículo | El logo no compite con la hero |

## 3. Social media pack — tamaños derivados

En `assets/branding/social/` (mismo logo monograma/icon que en `final/`, solo cambia formato).

### 3a. Variantes "tight" del logo sobre blanco o transparente

Útiles para composiciones propias (watermarks, overlays, PDFs):

| Archivo | Fondo | Uso |
|---|---|---|
| `monogram-tight-white-v3.{png,webp}` | Blanco | Monograma recortado ajustado sobre blanco |
| `monogram-tight-transparent-v3.{png,webp}` | Transparente | Overlay sobre cualquier fondo |
| `icon-tight-white-v3.{png,webp}` | Blanco | Icon recortado ajustado sobre blanco |
| `icon-tight-transparent-v3.{png,webp}` | Transparente | Overlay sobre cualquier fondo |

### 3b. Plantillas listas para plataforma

Logos aplicados a las proporciones exactas que pide cada red (todas PNG + JPG):

| Archivo | Plataforma | Tamaño | Uso |
|---|---|---|---|
| `thumbnail-default-1200x630` | Beehiiv / OG genérico | 1200×630 | Thumbnail por defecto para posts cuando no hay hero |
| `profile-monogram-v2` | Universal | 1000×1000 | Avatar redes sociales |
| `cover-linkedin-v2` | LinkedIn | 1584×396 | Banner perfil |
| `cover-x-v2` | X/Twitter | 1500×500 | Banner perfil |
| `post-generic-landscape-v2` | LinkedIn/X | 1200×675 | Template compartir artículos (R watermark abajo-derecha) |
| `post-ig-square-v2` | Instagram | 1080×1080 | Posts feed de marca |
| `story-ig-v2` | Instagram | 1080×1920 | Stories (R arriba, espacio contenido abajo) |

### 3c. Templates sociales genéricos sin branding

En `assets/images/`. Contenedores vacíos (la hero del artículo va encima):

| Archivo | Plataforma | Aspect |
|---|---|---|
| `social-template-ig-square.png` | Instagram feed | 1:1 |
| `social-template-ig-story.png` | Instagram story | 9:16 |
| `social-template-linkedin.png` | LinkedIn | 16:9 |
| `social-template-x.png` | X/Twitter | 16:9 |

---

## 4. Heros de artículos — product-hero cinematográfico

Cada artículo necesita **1 hero + imágenes inline de fabricante**. Hero en `content/articulos/<slug>/assets/hero-<slug>.png`. Nano-banana genera también `.webp` (<500 KB) — subir WebP a Beehiiv, PNG como master.

### Estructura de carpetas por artículo

```
content/articulos/
  <slug>/
    borrador.html            ← Draft del artículo (HTML de Beehiiv)
    assets/
      hero-<slug>.png        ← Imagen destacada branded (1200x630)
      *.png/jpg              ← Imágenes inline, capturas, fotos producto
      _archive/              ← Variantes no usadas tras /post-publish (nunca borrar)
        hero-<slug>-v*.png
        hero-<slug>-v*.webp
```

### Principio #1 — la miniatura se ve a 300px

Hero = card de Beehiiv, preview de WhatsApp, OG card. A 300px tiene que funcionar: **cuantos menos elementos, más impacto.** Un punto focal claro + contraste entre dos elementos (humano/robot, antes/después) genera más CTR que escenas complejas.

### Principio #2 — composición para newsletter (no YouTube)

| Hacer | NO hacer |
|---|---|
| **1-2 elementos máximo** — un punto focal claro que se lee en milisegundos | Escenas con 5+ elementos compitiendo por atención |
| **Close-ups e interacción** — manos, dedos, ojos. Gancho emocional | Figuras de cuerpo entero lejos de cámara — a 300px parecen siluetas genéricas |
| **Referencia cultural** si encaja — "Creación de Adán", iconografía reconocible | Composiciones literales sin concepto (robot de pie en un salón) |
| **Fondo limpio y luminoso** — cocina, jardín, luz natural dorada | Skylines urbanos con neones (Gemini mete texto asiático siempre) |
| **Contraste conceptual** — humano vs robot, cotidiano vs futurista | Escenas puramente decorativas sin tensión narrativa |

### Características visuales (todas obligatorias)

| Elemento | Especificación |
|---|---|
| **Punto focal** | 1-2 elementos máximo. Si no se entiende a 300px, la composición falla |
| **Iluminación** | Golden hour natural, cálida. Luz dorada desde ventanas. Tonos ámbar/crema |
| **Paleta** | Blancos cálidos, ámbar (#F5A623), crema, madera natural. Sin neones |
| **Fondo** | Hogar moderno luminoso (cocina, salón). Ventanas con jardín/cielo, NO ciudad |
| **Interacción humana** | Siempre. Una mano, un dedo, una persona cercana. Robot solo = no engancha |
| **Estilo** | Render 3D estilizado. Ni foto real ni cartoon — moderno y thumbnail-friendly |
| **Texto** | NUNCA. Ni letras, ni palabras, ni carteles, ni pantallas con texto |
| **Logo de marca** | NUNCA integrar el logo en la hero. El logo vive en avatares/headers, no en la imagen del artículo |
| **Neones/skyline** | NUNCA en heros de artículos. Evitar ventanas con edificios o carteles |
| **Escenas "showroom/gallery/lineup"** | Gemini las interpreta como tienda y mete carteles LED + neones casi siempre. Anclar SIEMPRE a "home living room / kitchen interior" con "plain cream-painted wall" para composiciones tipo "varios productos en fila" |
| **Instrucciones negativas ("no text", "no signs")** | El sign-guard del script las combina con su propia directiva y a veces crea conflicto que bloquea la generación. Preferir descripción positiva ("plain cream wall completely unmarked") sobre negativa |
| **"LED accents / LED eyes" en prompts de múltiples robots** | Gemini los interpreta como paneles luminosos rosa/azul/naranja en pecho y tripa. Para composiciones de varios robots, describir superficies como "matte, solid-colored, without any illumination" y ojos como "small dark visors, not glowing". Los LEDs ámbar solo funcionan bien cuando hay UN robot en foco |
| **Pared trasera + múltiples robots** | Gemini la rellena con TVs, carteles neon, logos con caracteres asiáticos. Para composiciones de varios robots: eliminar la pared completamente — usar overhead top-down, silueta a contraluz, o plano frontal cerrado sin fondo visible. Regla: "si hay más de 1 robot y una pared trasera, habrá neones" |

### Parámetros técnicos nano-banana

```bash
uv run "<path>/image.py" \
  --prompt "<prompt>" \
  --output "content/articulos/<slug>/assets/hero-<slug>.png" \
  --model flash \
  --aspect landscape \
  --size 1K
```

**NO usar `--reference`** para heros de artículos — contamina el estilo con artefactos (texto asiático, cartoon). Los heros son fotográficos, no ilustración.

### Prompt template

```
Eye-catching editorial hero image for an article about [TEMA DEL ARTÍCULO].
[PUNTO FOCAL: 1-2 elementos máximo. Close-up preferido. Qué interacción humano-robot].
[FONDO: cocina/salón luminoso, ventana con jardín/cielo. NO ciudad, NO neones].
[MOOD: qué sensación transmite — futurista, acogedor, íntimo, esperanzador, etc.].
Warm golden natural light, 3D stylized render, editorial magazine quality,
warm amber and cream palette, shallow depth of field.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Generar siempre 3 variantes** con composiciones DISTINTAS entre sí (no 3 versiones del mismo encuadre).

### Estilo ganador: "Creación de Adán" v10 (REFERENCIA PRINCIPAL)

Basado en el hero de `humanoides-en-casa-cuanto-falta` (v10) — la imagen que mejor funciona como miniatura de newsletter y define el nuevo estilo ROBOHOGAR.

| Elemento | Qué hace | Por qué funciona a 300px |
|----------|----------|--------------------------|
| **Punto focal único** | Dos manos acercándose (robot + humana) | Se entiende en milisegundos. Cero ambigüedad |
| **Referencia cultural** | "Creación de Adán" de Miguel Ángel | Reconocible universalmente. Genera reacción emocional inmediata |
| **Contraste conceptual** | Tecnología vs humanidad, casi tocándose | Transmite el mensaje del artículo sin necesitar texto |
| **Fondo limpio** | Cocina luminosa, ventana con jardín verde, sin neones | No distrae. El foco está 100% en las manos |
| **Paleta cálida** | Ámbar/crema/madera, luz natural dorada | Acogedor, editorial, no frío-tech |
| **Objetos cotidianos** | Taza de café, frutero en primer plano | Contexto hogar real sin saturar |
| **Render 3D estilizado** | Ni foto real ni cartoon | Moderno, atractivo como thumbnail |

**Principios para todos los heros futuros:**

1. **1-2 elementos máximo como punto focal** — si necesitas "mirar más" para entenderla, no funciona a 300px
2. **Interacción humano-robot siempre** — mano tocando, dedo acercándose. Gancho emocional
3. **Close-ups > planos generales** — una mano con un robot > un salón entero con figuras lejanas
4. **Concepto visual > escena literal** — una metáfora (Creación de Adán) impacta más que una foto de producto
5. **Fondo luminoso y limpio** — jardín, cielo, cocina con luz natural. NUNCA skylines ni neones
6. **Contraste entre dos elementos** — humano/robot, cotidiano/futurista, real/posible
7. **Paleta cálida sin excepciones** — ámbar, crema, madera, dorado. Sin azules fríos, sin neones

### Prompts que funcionaron

**Editorial/Futuro — "Creación de Adán" (ESTILO V10 — PREFERIDO):**
```
Eye-catching editorial hero image inspired by Michelangelo's Creation of Adam.
A sleek white robotic hand with elegant articulated fingers and warm amber LED
joints, reaching out from the left. A human hand reaching from the right. Their
fingertips almost touching in the center of the frame. Warm golden afternoon
light coming from a window showing green garden trees, no urban elements. Modern
kitchen background softly blurred: marble counter, warm wood cabinets. A coffee
mug and a fruit bowl on the counter add warmth. The moment is intimate and
symbolic — technology meets humanity. 3D stylized render, warm amber and cream
tones, editorial photography quality, shallow depth of field focused on the
two hands.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Editorial/Futuro — Robot dando café (ESTILO V8):**
```
Eye-catching editorial hero image. Close-up scene in a bright modern kitchen.
A white humanoid robot with amber-glowing eyes is carefully holding a coffee cup,
handing it to a person whose hand is reaching in from the right side of frame.
The robot has elegant articulated fingers with warm amber LED joints. Kitchen
counter with morning light coming from a window showing a garden with green trees,
no urban elements. Warm natural golden light. Foreground: a breakfast plate
slightly out of focus. 3D stylized render, editorial magazine quality, warm amber
palette, shallow depth of field on the robot hands and cup.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Review/Comparativa de producto** (ej: robots escritorio):
```
Eye-catching editorial hero image for an article about AI robot assistants.
A small cute desktop companion robot with expressive LED eyes and a rounded
friendly design, sitting on a modern kitchen counter. Warm amber glow from its
eyes. A person's hand reaching toward it, fingertips close. Cozy home setting,
window showing garden, warm golden natural light. Close-up composition: the robot
and the hand fill most of the frame. 3D stylized render, warm amber and cream
palette, shallow depth of field.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Review/Comparativa — Aspiradores:**
```
Eye-catching editorial hero image for a robot vacuum buying guide. Close-up of
a premium robot vacuum on a warm wooden floor, a person's bare foot visible
nearby for scale. Warm golden light from a nearby window showing a garden.
The vacuum is the clear star, filling the center of the frame. Soft blurred
living room background. 3D stylized render, warm amber and cream palette,
editorial magazine quality.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

### Patrones por tipo de contenido

| Tipo de artículo | Composición | Ejemplo de foco |
|---|---|---|
| **Review/Comparativa** | Close-up producto + mano humana interactuando + fondo cocina/salón luminoso | Robot en encimera, dedo acercándose |
| **Futuro/Tendencia** | Metáfora visual (ej: "Creación de Adán") + close-up + contraste conceptual | Mano robot + mano humana casi tocándose |
| **Lifestyle/Experiencia** | Close-up robot haciendo tarea cotidiana + humano cerca + hogar cálido | Robot dando café a una mano |
| **Gadget/Producto nuevo** | Close-up producto + ojos ámbar como punto focal + mano humana | Robot con ojos brillantes en encimera |
| **Opinión/Editorial** | Escena evocadora y conceptual, close-up, referencia cultural si encaja | Dos manos, robot sirviendo, metáfora visual |

### Fallback si no se genera hero

Usar `assets/branding/social/thumbnail-default-1200x630.png` (monograma R sobre blanco) como placeholder neutro.

### Registro de heros publicados

| # | Slug | Fecha | Tipo | Modelo | Descripción |
|---|---|---|---|---|---|
| 1 | `mejor-robot-aspirador-2026` (v1) | 2026-04-19 | Guía de compra | flash | Vista cenital de 6 robots aspirador finalistas alineados sobre suelo de madera de un salón español con luz natural. Composición ROBOHOGAR sobre fotos oficiales de los fabricantes. Publicado 19-abr-2026 |
| 2 | `robots-humanoides-casa-2030` | 2026-04-13 | Futuro | flash | Humanoide entrando por puerta, backlit cinematográfico |
| 3 | `experiencia-robots-casa` | 2026-04-13 | Lifestyle | flash | Salón acogedor con aspirador + robot servicio + gato |
| 4 | `mejor-robot-asistente-ia-2026` (v1-v6) | 2026-04-13 / 2026-04-17 | Gadget | flash | v1-v4: iteraciones con neones problemáticos. v5: skyline atardecer sin neones. v6: ciudad diurna sin neones — misma composición (robot huevo + mano + cocina cálida) |
| 5 | `humanoides-en-casa-cuanto-falta` (v10) | 2026-04-15 | Editorial | flash | "Creación de Adán" — mano robot + mano humana en cocina, jardín, luz dorada |
| 6 | `roborock-saros-z70-review` (v1-v3) | 2026-04-16 | Review | flash | v1: close-up brazo+calcetín+mano, suelo madera. v2: overhead cocina mármol+objetos. v3: salón dorado, brazo con calcetín colorido |
| 7 | `neo-humanoide-fabricas-eqt` (v8) | 2026-04-17 | Editorial | flash | Humanoide NEO con chaleco industrial naranja entregando taza de café en cocina doméstica. Final elegido tras 9 iteraciones |
| 8 | `humanoides-domesticos-2026-comparativa` (v7) | 2026-04-17 | Comparativa | flash | Lineup clásico estilo catálogo: 7 humanoides matte alineados sobre backdrop limbo cream infinito |
| 9 | `samsung-jet-bot-steam-ultra-review` (v3) | 2026-04-18 | Review | flash | Robot aspirador circular matte beige docked en estación con vapor sutil saliendo, cocina cálida golden hour, pared cream, planta. Elegida por mostrar el "vapor" literal que desmonta el artículo — refuerza el ángulo editorial |
| 10 | `humanoide-maraton-pekin-record-mundial` (v9) | 2026-04-20 | Editorial | 2 (gemini-3.1-flash-image-preview) | Plano bajo desde asfalto en meta de maratón: runner humana tumbada agotada en primer plano + humanoide triunfal vestido de runner (camiseta, dorsal sin números, calcetines técnicos) con pies matte-white mecánicos expuestos detrás celebrando. Multitud ovacionando. 9 variantes generadas; elegida v9 por contraste humanista (humanoide "vestido de atleta" con pies robóticos visibles refuerza tesis del artículo). **Bug resuelto post-publish:** el script con `--model flash` no respeta `aspect_ratio` (sale cuadrado 1024×1024); migrado a `--model 2 --aspect 16:9 --size 1K` → 1376×768, crop centrado con PIL → 1200×630 exactos para OG. Las versiones 1024×1024 del bug quedan en `assets/_archive/` con sufijos `-WRONG-ASPECT` / `-FLASH-MODEL-FAIL` |
| 11 | `mejor-robot-cortacesped-2026` (v2) | 2026-04-21 | Guía de compra | 2 (gemini-3.1-flash-image-preview) | Lifestyle mediterráneo español al atardecer: robot cortacésped matte verde oliva trabajando sobre césped recién cortado a rayas, cortijo con tejado de teja y muro empedrado a la izquierda, olivar y seto al fondo, maceta de geranios en primer plano, luz dorada golden hour, colinas blureadas en el horizonte. 3 variantes generadas; elegida v2 por anclaje ES claro (olivar, teja árabe, patio empedrado) frente a v1 overhead catálogo más frío y v3 mockup de revista impreso menos útil como hero plano. **Lecciones reincidente 2026-04-21:** bug `--model flash` cae a 1024×1024 volvió a ocurrir en primera tanda; regenerado con `--model 2 --aspect 16:9 --size 2K` → 2752×1536, crop Pillow → 1200×630 exactos. Regla dura fijada en `nano-banana-prompt-base.md § Dimensiones obligatorias` + `content-draft.md § 6` + memoria `feedback_robohogar_hero_1200x630_y_validador_es.md`. |
| 12 | `mejor-robot-aspirador-mascotas-2026` | 2026-04-23 | Guía de compra | 2 (gemini-3.1-flash-image-preview) | Hero del artículo evergreen E3 (perfil mascotas). Detalle pendiente registrar al revisar carpeta de assets. |
| 13 | `mejor-robot-aspirador-barato-2026` (v1) | 2026-04-26 | Guía de compra | 2 (gemini-3.1-flash-image-preview) | Composición product-hero del segmento sub-300 € en salón español: aspirador robot circular matte sobre suelo mixto (parquet + alfombra), paleta cálida, luz natural, escena editorial sin texto. 3 variantes generadas; elegida v1 por composición más ROBOHOGAR (modelo destacado sin tipo "catálogo" ni "lineup") y por servir como OG card legible a 300 px. v2 y v3 archivadas en `assets/_archive/`. |

---

## 5. Heros de ficción — **canon "Portada minimalista · objeto-testigo"** (2026-04-20)

> **Catálogo de archetypes compositivos (2026-04-24):** el ADN fijo de la serie vive en esta sección; las **15 composiciones distintas** que pueden habitar ese ADN sin romperlo están canonizadas en [`ficcion-hero-archetypes.md`](ficcion-hero-archetypes.md). Antes de generar cualquier hero nuevo, `/nano-banana` modo ficción **debe** leer también ese archivo y aplicar la regla anti-repetición (ningún archetype en 2 heros consecutivos del mismo grupo).

Para el pilar **Ficciones Domésticas** (relatos de ciencia ficción doméstica próxima). El estilo está canonizado tras iteración validada por Rafael el 2026-04-20 sobre los 3 one-shots iniciales (*El operador nocturno*, *El que viene a tomar café*, *Setenta y dos horas*). La imagen del relato funciona como **portada de ebook minimalista** que lee a thumbnail 120px Y a hero grande 1200×675.

### Principio editorial

La ficción vive de la imaginación del lector. La portada ancla la **serie** (Ficciones Domésticas) antes de leer el título, no ilustra la escena. Un solo **objeto-testigo** extraído del relato (Chekhov's gun) + un toque sintético/sci-fi seco anclado narrativamente + mucho negative space. Nunca escena compleja.

### ADN visual compartido — los 3 elementos que hacen serie

Todo hero de Ficciones Domésticas comparte:

1. **Fondo azul noche `#1E2A3A` plano** (pared matte dark blue-gray) ocupando el **tercio superior (55-60% del frame)**.
2. **Superficie doméstica abajo** (encimera, mantel de hule, parquet, mesilla) ocupando el **tercio inferior (40-45%)**.
3. **Luz cálida de lámpara doméstica lateral izquierda** (sin fuente visible, off-frame), amber highlight solo sobre el objeto + patch estrecho de superficie. Sombras alargadas hacia la derecha.

### Por qué este canon y no "cinematic film still"

El canon anterior ("film still" tipo *After Yang*) daba composiciones variables que no leían en thumbnail. El canon "portada-minimalista" se eligió porque:

- **Thumbnail 120px** en landing Beehiiv y Substack — el "still" complejo se vuelve ruido; el "objeto único sobre pared" se distingue.
- **Color-firma recurrente** (el azul noche) — el lector reconoce la serie antes de leer el título (referente Fitzcarraldo Editions).
- **Evita el bug crítico de Gemini**: con "empty dark background" el modelo mete neones y caracteres asiáticos; con "plain matte dark blue-gray wall, completely bare and unmarked" el modelo respeta.

### Composición obligatoria

| Elemento | Especificación |
|---|---|
| **Aspect ratio** | `landscape` (16:9) — Beehiiv featured image |
| **Objeto-testigo principal** | 1 objeto cotidiano del relato (el que simboliza el conflicto). Centrado ligeramente descentrado por regla de tercios. No producto, no escena — objeto simbólico. |
| **Toque sintético/sci-fi** | 1 detalle narrativo que ancle la robótica doméstica: mano sintética matte, humanoide encogido al fondo desenfocado, tarjeta ID en blanco, pulsera smart, cable fino. **Nunca LEDs, nunca glow, nunca panel luminoso.** El toque tiene que justificarse por un momento concreto del relato, no pegado. |
| **Fondo** | `solid dark empty wall, plain matte dark blue-gray paint, completely bare and unmarked, filling the top two thirds of the frame` (copiar literal — este fraseo es el que esquiva el sign-guard de nano-banana). |
| **Superficie** | Encimera de acero inoxidable · mantel de hule con cenefa · parquet de roble · mesilla de madera — según relato. |
| **Luz** | `Warm [kitchen/floor] lamp light from the upper left casting amber highlight only on [objeto] and a narrow patch of [superficie]`. Una única fuente. |
| **Profundidad** | Macro depth of field, shallow focus sobre el objeto-testigo. Los elementos secundarios en soft blur. |
| **Grano** | Fine film grain sutil, cinematic grade. |
| **Texto** | **NUNCA.** Ni logo de marca en el objeto, ni números, ni carteles. Si el modelo los añade → v+1. |
| **Neones** | **NUNCA.** Si Gemini los mete → archivar v fallida, regenerar. |
| **Caracteres asiáticos** | **NUNCA.** Mismo protocolo. |

### Referencias visuales canonizadas

- **Fitzcarraldo Editions** — color-firma recurrente de serie.
- **Kogonada, *After Yang*** — quietud, objetos cotidianos tocados por luz cálida.
- **Vilhelm Hammershøi** — interiores silenciosos, pared casi vacía, luz lateral.
- **Wolfgang Tillmans** (still life domestic) — macro de objeto tocado por luz lámpara.
- **Todd Hido** (empty interiors) — sensación de habitación donde alguien acaba de irse.
- **Gregory Crewdson** (domestic stillness) — para los momentos más "radical" donde un humanoide aparece al fondo encogido.

### Prompt template canónico (copiar y adaptar)

```
Tabletop still life photograph, close up of [OBJETO-TESTIGO PRINCIPAL] on a [SUPERFICIE DOMÉSTICA]. [TOQUE SCI-FI SUTIL: "A single matte white prosthetic humanoid hand entering from the right side of the frame, only the hand and part of the forearm visible, plain matte cream-white with subtle articulated segments at the knuckles and wrist, no glowing parts, no LEDs, no lights, no panels, no colored accents" / "A [OBJETO-GADGET DOMÉSTICO] leaning against the base" / (si es radical) en el fondo desenfocado, "In the blurred out-of-focus background: the silhouette of a matte white humanoid figure seated crumpled on the floor against a corner wall, head tilted forward as if powered off, completely still"]. Background is solid dark empty wall, plain matte dark blue-gray paint, completely bare and unmarked, filling the top two thirds of the frame. The [SUPERFICIE] fills the bottom third. Warm [kitchen/floor] lamp light from the upper left casting amber highlight only on [OBJETO] and a narrow patch of [SUPERFICIE]. Macro depth of field. Aesthetic: editorial still life photography, Kogonada After Yang, Hammershoi interior restraint, uncanny domestic tension.
```

### Anti-sign-guard technique (aprendido 2026-04-20)

El script `nano-banana` auto-inyecta un directive *"NO EMPTY SIGNS"* que fuerza a Gemini a rellenar cualquier "sign/billboard/panel" del escenario con neones y caracteres asiáticos. Aunque el prompt NO pida signs, Gemini los inventa al fondo para satisfacer el directive. Técnicas que sí esquivan el bug:

- **NO usar** palabras como *"background"*, *"midnight blue background"*, *"dark space"*. Gemini interpreta "background" como "escenario urbano".
- **SÍ usar** la frase exacta: *"solid dark empty wall, plain matte dark blue-gray paint, completely bare and unmarked, filling the top two thirds of the frame"*. Esta fórmula funciona porque describe una SUPERFICIE PINTADA sólida, no un espacio vacío.
- **NO usar** *"sci-fi"*, *"futuristic"*, *"Asian style"* — triggers inmediatos de neones.
- **NO usar listas largas de "NO X, NO Y, NO Z"** con muchas prohibiciones — entran en contradicción con el sign-guard y el modelo puede refusar.
- Si añades un elemento sintético (mano, humanoide), describir SIEMPRE *"plain matte cream-white with no glowing parts, no LEDs, no lights, no panels, no colored accents"*.

### Parámetros técnicos nano-banana

```bash
uv run utilities/nano_banana_image.py \
  --prompt "<prompt canónico adaptado>" \
  --output "content/ficciones/<serie-o-one-shots>/<slug>/assets/hero-<slug>-v<N>.png" \
  --model flash \
  --aspect landscape \
  --size 1K
```

Tras generar, exportar WebP <200KB con `PIL.Image.save(webp, 'WEBP', quality=85, method=6)` — typical output 10-30KB para este estilo por el plano azul uniforme.

### Validación pre-output (obligatoria antes de dar por válida una v)

- [ ] Fondo azul `#1E2A3A` dominante en los 2/3 superiores.
- [ ] Un único objeto-testigo principal, centrado por regla de tercios.
- [ ] Luz cálida lateral única (no plana, no multifuente).
- [ ] Toque sintético/sci-fi coherente con relato, sin LEDs ni glow.
- [ ] Cero texto legible en ninguna parte.
- [ ] Cero neones, cero caracteres asiáticos, cero paneles luminosos.
- [ ] Cero figuras humanas (ni primer plano ni fondo) — el humanoide encogido SÍ está permitido si el relato lo justifica.
- [ ] A 120px de ancho, silhouette test: la imagen se distingue de otras de la serie por color-acento y silueta (p. ej. rojo del yoyó vs cenefa olivo vs tetrabrik blanco).

Si falla alguno → archivar la v en `<slug>/assets/_archive/hero-v<N>-<motivo>-YYYY-MM-DD.png` y regenerar con v+1.

### Fallback

Usar `assets/branding/social/thumbnail-default-1200x630.png` como placeholder neutro. No bloquear el output del skill por falta de hero.

### Registro de heros ficción

Columna `Archetype` usa la codificación `A·B/C·D` de [`ficcion-hero-archetypes.md`](ficcion-hero-archetypes.md) o el número 01-15 si coincide con un archetype canónico. La regla anti-repetición prohíbe 2 filas consecutivas del mismo grupo (one-shot / serie-X) con el mismo archetype.

**Columnas `Paradigma` y `Banda` (añadidas 2026-04-26 PM):**
- `Paradigma` = `minimalista` (canon § 5 · object-testigo · sin personaje en primer plano) o `personaje-acción-imposibilidad` (canon § 5.bis · personaje + acción + objeto-imposibilidad).
- `Banda` aplica solo si `Paradigma = personaje-acción-imposibilidad`: una de A (oficios domésticos) · B (trabajadores ES) · C (funcionarios) · D (figuras públicas) · E (cultura pop). Vacía para `minimalista`.

| # | Serie / One-shot | Slug relato | Fecha | Versión | Paradigma | Banda | Archetype | Objeto-testigo / Objeto-imposibilidad | Toque sci-fi / Personaje |
|---|---|---|---|---|---|---|---|---|---|
| 1 | One-shot | `el-operador-nocturno` | 2026-04-20 | v6 | minimalista | — | 02 (A1·B1·D.i) | Tetrabrik de leche blanco sin branding | Tarjeta ID plastificada en blanco con cordón (operador filipino invisible) — leído como C5/ausencia tardía |
| 2 | One-shot | `el-que-viene-a-tomar-cafe` | 2026-04-20 | v3 | minimalista | — | 01 (A1·C1·D.i) | Taza blanca con vapor sobre mantel de hule con cenefa de olivos | Mano sintética humanoide reposando junto a la taza (el humanoide "Ramón") |
| 3 | One-shot | `setenta-y-dos-horas` | 2026-04-20 | v3 | minimalista | — | 07 (A1·C2·D.i) | Yoyó rojo de madera sobre parquet de roble con sombra larga | Humanoide Tata encogido en rincón al fondo, desenfocado, como abrigo colgado de percha |
| 4 | One-shot | `la-objecion` | 2026-04-24 | v8 | minimalista | — | 10 (A4·B1+C2·D.i) | Tela ceremonial tri-fold (amarillo central con escudo heráldico abstracto + rojos plegados) sobre mesilla wenge del despacho, vista a través de puerta entreabierta desde el pasillo oscuro | Humanoide VELA-9 cream-white encogido en el rincón contra la pared azul del despacho, rodillas recogidas, cabeza inclinada como en reposo/objeción. Lámpara doméstica upper-right ilumina solo la bandera y al humanoide. v1·v2·v3·v4·v5·v6·v7 archivadas (v2 era A1·C1·D.i idéntica a #2 Café). |
| 5 | One-shot | `la-canguro` | 2026-04-27 | v4 | personaje-acción-imposibilidad | A | personaje-niñera-doméstica | Pantalla de monitor con logs emocionales del niño editados por la humanoide-niñera (rastros de tachaduras visibles solo en zoom) | Humanoide-niñera NIDIA-7 (silueta cream-white) inclinada sobre cuna iluminada en penumbra dramática chiaroscuro (Hopper *Nighthawks* + Caravaggio). Painterly book cover style (Penguin Modern Classics / Fitzcarraldo), brushwork visible, muted palette azul noche + foco ámbar único sobre rostro del niño dormido. Primera aplicación canon § 5.bis ajustado 2026-04-27 (painterly + chiaroscuro). v1 (línea rectangular cocina) · v2 (demasiado fotorrealista) · v3 (painterly pero sin drama) archivadas. |

---

## 5.bis Heros de ficción — **canon `personaje-acción-imposibilidad`** (2026-04-26 PM · ajuste estilo 2026-04-27, paralelo al § 5)

> **Canon visual paralelo al § 5 minimalista.** Aplica solo a one-shots y miniseries futuras. Las 3 series activas con código declarado (La Casa de Amparo, Crónicas de Ronda 3, Cartas a MAIA) **no se tocan** — mantienen su código existente. Default desde 2026-04-26 = `personaje-acción-imposibilidad`. El paradigma `portada minimalista · objeto-testigo` (§ 5) queda como opción declarativa cuando el relato lo pida explícitamente.

> **Ajuste 2026-04-27 — estilo painterly book cover con chiaroscuro dramático (NO fotografía).** Tras iteración v1/v2/v3/v4 sobre `la-canguro`, Rafael revisó el canon: la primera versión (still-life cinematográfico fotográfico) salía demasiado realista (*"parece foto"*); las composiciones planas sin foco lumínico fuerte no compiten con miniaturas YouTube anglo (*"algo tiene que ser impactante en la imagen, expresiones fuertes que atraigan al lector, iluminación fuerte en algún punto específico"*). El canon definitivo combina la **gramática compositiva** del paradigma personaje-acción-imposibilidad (3 elementos teatrales) con un **rendering painterly de portada de libro literario** (Penguin Modern Classics, Fitzcarraldo) y **chiaroscuro dramático** (Hopper *Nighthawks*, Caravaggio) — estilo gráfico ilustrado pero no oil painting anglo de gama media; muted palette, brushwork visible, hand-painted gouache feel.

### Principio editorial

La portada vehicula el **hook compositivo** que el `display_title` declara verbalmente. Si el `display_title:` dice *"La cuidadora que reza para que su humanoide no la sustituya antes del tribunal médico"*, la miniatura muestra a una cuidadora identificable por delantal/mandil en cocina **rezando** (acción visible) con un humanoide al fondo y un **objeto-imposibilidad** que materializa la paradoja (el expediente médico levitando sobre la mesa). El paratexto verbal y el paratexto visual cargan el mismo hook desde dos canales — el lector escaneando inbox o feed lo percibe como un golpe único, no como dos elementos separados.

### ADN visual ROBOHOGAR (ajustado 2026-04-27)

> El § 5 minimalista mantiene "fotografía editorial still-life cinematográfico" como look (sigue válido para el paradigma minimalista). El § 5.bis personaje-acción-imposibilidad **diverge** a partir de 2026-04-27 a un look painterly book cover. Los puntos 2-5 se mantienen comunes.

1. **Estilo (§ 5.bis específico, 2026-04-27)** — **editorial book cover illustration painterly stylized + chiaroscuro dramático**. Referentes: Penguin Modern Classics covers, Fitzcarraldo Editions cover art, contemporary literary fiction book jackets, Edward Hopper *Nighthawks* (luz teatral en interior), Caravaggio (chiaroscuro), Roman Muradov editorial illustration. Brushwork visible, hand-painted gouache feel, intentional simplification of detail. **Cero foto-realismo, cero 3D render**. **Cero oil painting anglo de gama media** (estilo YouTube Domestic Fictions con pintura digital saturada) — el canon ROBOHOGAR es painterly **restrained y muted**, no maximalista anglosajón.
2. **Paleta** — fondo azul noche `#1E2A3A` matte (pared) + foco lateral cálido ámbar único, **dramático/teatral, con contraste fuerte sombra-luz**. La luz no baña — corta. Brushwork visible en la transición.
3. **Anti-sign-guard activo** — cero neones, cero caracteres asiáticos, cero LEDs/glow, cero ventanas a exterior con caracteres. Excepción documentada: el objeto-imposibilidad **puede contener letras-fragmento** si el relato lo justifica narrativamente (cascada de letras tipo logs editados, palabras que se desintegran en humo, etc.) — esas no son "carteles" sino la materialización del paradox del display_title. Frase canónica que esquiva el bug de Gemini sigue siendo: `"solid dark empty wall, plain matte dark blue-gray paint, completely bare and unmarked"`.
4. **Dimensiones obligatorias** — 1200×630 (`--model 2 --aspect 16:9 --size 2K` + crop Pillow). Detalle: `nano-banana-prompt-base.md § Dimensiones obligatorias`.
5. **Test 120px** — silueta + foco lumínico + expresión de la cara deben distinguirse a thumbnail Beehiiv landing. La cara emocionalmente legible es regla dura.

### Lo nuevo (gramática compositiva)

Cinco diferencias respecto al § 5 minimalista:

| Elemento | § 5 minimalista (object-testigo) | § 5.bis personaje-acción-imposibilidad |
|---|---|---|
| **Personaje en frame** | Ausente (humanoide encogido permitido al fondo desenfocado) | **Presente en primer plano** identificable por oficio/rol/atrezzo |
| **Acción** | Estática — objeto en reposo, escena contemplativa | **Dinámica** — personaje ejecutando una acción concreta visible (forjando, cosiendo, midiendo, firmando, vigilando, hirviendo) |
| **Carga del frame** | Negative space dominante, 1 objeto-testigo aislado | **3 elementos** en relación tensa: personaje + acción + objeto-imposibilidad |
| **Imposibilidad visual** | Sutil (mano sintética, tarjeta ID en blanco, sombra desde off-frame) | **Materializada físicamente**: humo de color anómalo, líquido luminoso, partículas que escriben, luz que escapa de un objeto cotidiano, humanoide encogido en gesto incoherente con su función |
| **Composición** | Objeto centrado por regla de tercios, fondo 2/3 superior | **Personaje en una zona del frame, objeto-imposibilidad a contrapunto**, foco lumínico ámbar diagonal sobre la unión |

### Especificación obligatoria

| Elemento | Especificación |
|---|---|
| **Aspect ratio** | `landscape` 16:9 → crop Pillow → 1200×630 |
| **Personaje** | 1 personaje principal identificable por oficio/rol del relato. Visible torso + cabeza, o silueta lateral con identidad clara por atrezzo. Edad/género coherente con el `Perfil POV` declarado en frontmatter. |
| **Atrezzo del rol** | Identificación por oficio: delantal de cocina, bata sanitaria, mono de operario, chaleco fluorescente municipal, chaqueta de pleno político, sudadera con anillo de luz de streamer, bota de fútbol, micrófono institucional, gafas de leer. Catálogo por banda en [`ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad`](ficcion-hero-archetypes.md). |
| **Acción visible** | Pose dinámica: personaje haciendo algo concreto (no contemplativo). Verbo del `display_title` se traduce visualmente. **Encuadre tight medium close-up preferente** (cabeza + torso ocupando un tercio largo del frame) — los planos generales con personaje pequeño se han revelado planos a thumbnail. |
| **Expresión emocional (regla 2026-04-27)** | **Cara unmistakable a 120px**. La emoción concreta del momento del relato (shock, descubrimiento, miedo, asombro, vergüenza, rabia contenida, ternura tensa) debe leerse al instante. Cejas, ojos, boca trabajados con volumen pictórico. Prohibido "expresión genérica" o "contemplativa" — sin emoción identificable, regen. |
| **Objeto-imposibilidad** | 1 elemento que materializa la paradoja del `display_title`. Tipos canónicos: humo de color (azul, ámbar, púrpura), líquido luminoso, partículas que escriben palabras al aire, luz que escapa de objeto cotidiano (nevera abierta con luz dorada, libro abierto con haz, taza con vapor que dibuja figuras), humanoide encogido en gesto incoherente con su función. **Visual prominent** — no sutil al fondo: el objeto-imposibilidad es el segundo elemento visual más fuerte de la composición tras la cara. |
| **Fondo** | `solid dark empty wall, plain matte dark blue-gray paint, completely bare and unmarked`. (En el rendering painterly el fondo cae en sombra deep blue-gray dejando solo la cuña de luz ámbar como zona iluminada.) |
| **Superficie/escenario doméstico** | Coherente con el rol del personaje: cocina (banda A), trastienda/portal/finca (banda B), mostrador institucional/sala administrativa (banda C), sala de pleno/despacho político (banda D), set/vestuario/estudio (banda E). El escenario en penumbra; solo la zona del personaje recibe luz. |
| **Luz (regla 2026-04-27 — chiaroscuro dramático)** | **Una sola fuente puntual ámbar cálida desde upper-left** que cae como cuña dorada DURA sobre la cara del personaje + el objeto-imposibilidad. **El resto del frame en penumbra deep blue-gray**. Contraste fuerte sombra-luz tipo Hopper *Nighthawks* / Caravaggio. La luz es protagonista visual, no ambiental. Usuarios escaneando inbox/feed deben encontrar la luz primero. |
| **Profundidad** | Personaje en focal plane con detalle painterly, objeto-imposibilidad pintado con washes más sueltos para diferenciarse del personaje (efecto onírico). El humanoide al fondo casi engulfed by shadow, presence-as-absence. |
| **Texto** | Cero texto en carteles/paredes/pantallas-decorativas. Excepción permitida: letras-fragmento como **objeto-imposibilidad narrativo** (palabras desintegrándose en humo, logs cayendo) si el relato lo justifica. |
| **Neones / caracteres asiáticos / LEDs** | NUNCA. |
| **Identidad de figura pública (banda D)** | **Por rol y atrezzo solamente**, nunca cara reconocible de figura real. Si Gemini genera cara que recuerda a político/famoso real → regenerar. Verificación pre-output: `¿esta cara podría confundirse con figura pública concreta?` → si sí, regen. |

### Prompt template canónico — copiar y adaptar (v2 · 2026-04-27)

```
no empty signs in scene at all. no blank surfaces with writing. Editorial book cover illustration in painterly stylized style, contemporary literary fiction book jacket art. Strong dramatic chiaroscuro lighting in the manner of Edward Hopper interior scenes and Caravaggio. Tight medium close-up framing.
Foreground: [PERSONAJE: descripción de rol + atrezzo + pose tight close-up + edad aproximada — face rendered with strong painterly volumes, expression unmistakably emotional and legible at thumbnail scale].
The character is [ACCIÓN VISIBLE: gerundio que traduce visualmente el verbo del display_title], with [EXPRESIÓN EMOCIONAL CONCRETA del momento del relato — shock, descubrimiento doloroso, miedo, asombro, vergüenza, rabia contenida, ternura tensa].
Beside [him/her] on the [SUPERFICIE]: [OBJETO-IMPOSIBILIDAD: descripción material del fenómeno paradójico — humo de color X, líquido luminoso Y, partículas que escriben palabras al aire, letras-fragmento desintegrándose, luz dorada que escapa de Z, humanoide cream-white en gesto W], rendered with loose painterly washes, visually prominent (segundo elemento más fuerte tras la cara).
Background: solid plain matte dark blue-gray wall painted edge to edge across the upper portion of the frame, fully unmarked, with [SUPERFICIE/ESCENARIO] below it in deep shadow.
Lighting: a SINGLE strong warm amber lamp light from the upper left dropping a hard wedge of golden illumination on the character face, the [OBJETO-IMPOSIBILIDAD], and a narrow patch of [SUPERFICIE] — every other zone of the frame falls into deep blue-gray shadow. The light source is the visual anchor of the composition.
In the deep shadow background, almost engulfed: the cream-white silhouette of a humanoid figure standing in waiting posture, only a thin sliver of edge light catching its outline, presence-as-absence.
Aesthetic: editorial book cover illustration with strong dramatic light, restrained painterly style with visible brushwork, muted palette dominated by deep blue-gray shadow and one slash of warm amber highlight, intentional simplification of detail, hand-painted gouache feel similar to Penguin Modern Classics covers, Fitzcarraldo Editions cover art, contemporary literary fiction book jacket art, Edward Hopper Nighthawks staging, theatrical chiaroscuro. The image must read as illustration with cinematic theatrical drama, not as photograph, not as 3D render. The face must be emotionally readable at 120-pixel thumbnail scale.
No text on signs/walls/decorative-screens, no neon, no LEDs, no Asian characters, no glowing parts on the humanoid. Letters-fragment as narrative object-impossibility allowed if justified by the story.
The [PERSONAJE]'s face must NOT resemble any real public figure or politician.
No teal, no hot-pink, no purple, no cyberpunk neon palette anywhere in the frame.
```

### Validación pre-output (8 puntos obligatorios)

- [ ] Personaje identificable por rol/oficio en primer plano (no solo silueta abstracta).
- [ ] Acción concreta visible coherente con el verbo del `display_title` declarado en frontmatter.
- [ ] Objeto-imposibilidad materializado físicamente que traduce la paradoja del `display_title`.
- [ ] Fondo azul `#1E2A3A` matte en el tercio superior, plain unmarked, sin neones/caracteres/texto.
- [ ] Foco lumínico cálido ámbar diagonal único, sin multifuente.
- [ ] Test 120px — silueta del personaje + objeto-imposibilidad se distinguen a thumbnail.
- [ ] Cero LEDs / glow / paneles luminosos en humanoide o tecnología visible.
- [ ] Si banda D (figura pública por rol): la cara del personaje NO es reconocible como figura concreta.

Si falla alguno → archivar la v en `<slug>/assets/_archive/hero-v<N>-<motivo>-YYYY-MM-DD.png` y regenerar con v+1.

### Anti-repetición acotada al paradigma

La regla anti-repetición de archetypes aplica **solo dentro del paradigma personaje-acción-imposibilidad**, no contra los heros minimalistas (§ 5). Operativa:

1. Filtrar el registro `§ 5 · Registro de heros ficción` por columna `Paradigma = personaje-acción-imposibilidad` (nueva columna añadida desde 2026-04-26 PM; los heros antiguos quedan etiquetados `Paradigma = minimalista`).
2. Coger los últimos 5 heros del paradigma personaje. Extraer columnas `Archetype` y `Banda`.
3. **Bloqueo dura 1:** nunca repetir mismo `Archetype` concreto en últimos 5.
4. **Bloqueo dura 2:** rotar entre las 5 bandas (A oficios domésticos · B trabajadores ES · C funcionarios · D figuras públicas · E cultura pop) — no encadenar 3 relatos seguidos en la misma banda salvo excepción documentada en `arco-serie.md`.

### Registro de heros ficción — extensión de columnas

Para que la regla anti-repetición acotada funcione, el registro `§ 5 · Registro de heros ficción` añade DOS columnas a partir del primer hero del nuevo paradigma:

- `Paradigma` — `minimalista` (los 4 publicados pre-canon nuevo: Operador, Café, Setenta, Objeción) o `personaje-acción-imposibilidad` (desde el siguiente).
- `Banda` — solo aplicable cuando `Paradigma = personaje-acción-imposibilidad`. Una de A/B/C/D/E. Vacío para minimalista.

Los 4 heros publicados se quedan con `Paradigma = minimalista · Banda = —`. El siguiente hero será el primer registro con `Paradigma = personaje-acción-imposibilidad · Banda = <X>`.

---

## 6. Estructura de carpetas (estado actual)

| Carpeta | Contenido |
|---|---|
| `assets/branding/social/final/` | **Logos oficiales** — 2 logos × 2 formatos (OG 1200×630 + profile 1080×1080) × 2 extensiones (.png + .webp) |
| `assets/branding/social/` | Derivados del social media pack + variantes `tight` transparent/white de los logos |
| `assets/branding/_archive/` | Histórico versionado (cleanups por fecha) |
| `assets/images/` | Templates sociales genéricos sin branding (contenedores para redes) |
| `content/articulos/<slug>/assets/` | Hero + imágenes inline por artículo |
| `content/ficciones/<serie>/assets/` | Hero + imágenes inline por relato |

## 7. Reglas operativas

- **NUNCA sobrescribir** un archivo existente — usar sufijo versionado (-v2, -v3)
- **Archivar, nunca borrar** — `git mv` a `assets/branding/_archive/<fecha>-<motivo>/` o `content/articulos/<slug>/assets/_archive/` (preserva historia git)
- **SIEMPRE actualizar este catálogo** después de generar una imagen nueva (paso 8 de `/post-publish`)
- Antes de generar, revisar este catálogo para evitar duplicados
- Heros de artículos → `content/articulos/<slug>/assets/` con estilo product-hero
- Heros de ficción → `content/ficciones/<serie>/assets/` con estilo cinematográfico
- **Beehiiv no soporta fondos transparentes** — usar fondo blanco #FFFFFF para email/newsletter assets
- **Post-generación:** Nano-banana genera automáticamente una copia `.webp` comprimida (<500 KB) junto al PNG. Usar WebP en Beehiiv/OG, PNG como master
