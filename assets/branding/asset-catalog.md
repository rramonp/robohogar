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
| 1 | `mejor-robot-aspirador-2026` | 2026-04-13 | Review | flash | Aspirador premium iluminado cenital ámbar en salón moderno |
| 2 | `robots-humanoides-casa-2030` | 2026-04-13 | Futuro | flash | Humanoide entrando por puerta, backlit cinematográfico |
| 3 | `experiencia-robots-casa` | 2026-04-13 | Lifestyle | flash | Salón acogedor con aspirador + robot servicio + gato |
| 4 | `mejor-robot-asistente-ia-2026` (v1-v6) | 2026-04-13 / 2026-04-17 | Gadget | flash | v1-v4: iteraciones con neones problemáticos. v5: skyline atardecer sin neones. v6: ciudad diurna sin neones — misma composición (robot huevo + mano + cocina cálida) |
| 5 | `humanoides-en-casa-cuanto-falta` (v10) | 2026-04-15 | Editorial | flash | "Creación de Adán" — mano robot + mano humana en cocina, jardín, luz dorada |
| 6 | `roborock-saros-z70-review` (v1-v3) | 2026-04-16 | Review | flash | v1: close-up brazo+calcetín+mano, suelo madera. v2: overhead cocina mármol+objetos. v3: salón dorado, brazo con calcetín colorido |
| 7 | `neo-humanoide-fabricas-eqt` (v8) | 2026-04-17 | Editorial | flash | Humanoide NEO con chaleco industrial naranja entregando taza de café en cocina doméstica. Final elegido tras 9 iteraciones |
| 8 | `humanoides-domesticos-2026-comparativa` (v7) | 2026-04-17 | Comparativa | flash | Lineup clásico estilo catálogo: 7 humanoides matte alineados sobre backdrop limbo cream infinito |
| 9 | `samsung-jet-bot-steam-ultra-review` (v3) | 2026-04-18 | Review | flash | Robot aspirador circular matte beige docked en estación con vapor sutil saliendo, cocina cálida golden hour, pared cream, planta. Elegida por mostrar el "vapor" literal que desmonta el artículo — refuerza el ángulo editorial |

---

## 5. Heros de ficción — still cinematográfico

Para el pilar **Ficciones Domésticas** (relatos de ciencia ficción doméstica próxima). Estilo diferente al product-hero de artículos: es un **still de película**, no una miniatura editorial.

### Cuándo usar este estilo

- Cualquier relato generado por `/ficcion-draft` (flash, corto, mini-serie)
- NO usar product-hero (esa paleta ámbar-cocina hogar editorial), es un lenguaje visual distinto

### Referencias visuales

- *Black Mirror* en registro doméstico (no distópico-industrial)
- *Her* (Spike Jonze) — luz cálida suavemente desaturada, composición íntima
- *After Yang* (Kogonada) — quietud, objetos cotidianos, dolor contenido
- *Ex Machina* en registro ligero — tensión sin amenaza

### Parámetros

| Elemento | Especificación |
|---|---|
| **Composición** | Escena narrativa, no producto. Punto focal = momento emocional (una mano, un rostro, una silueta contra ventana) |
| **Iluminación** | Motivada (ventana, lámpara de mesa, pantalla). No golden hour genérico — luz realista de hora concreta del día |
| **Paleta** | Ámbar cálido ligeramente desaturado + azul frío de pantallas/ventanas nocturnas. Más melancólica que los heros de artículos |
| **Grano** | Ligero grano fílmico, sensación anamórfica. Evitar render 3D perfectamente limpio |
| **Texto** | NUNCA |
| **Neones** | NUNCA (regla común con heros editoriales) |

### Prompt base (adaptar por escena)

```
Cinematic film still, 2030s Spanish home interior, [ESCENA CLAVE DEL RELATO —
1-2 elementos focales, momento emocional concreto].
Natural motivated light (from window / lamp / screen), slight desaturation,
soft film grain, anamorphic lens feel, shallow depth of field.
Editorial speculative fiction mood — warm but melancholic, intimate,
quiet tension. Reference: Black Mirror domestic, After Yang, Her.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

### Parámetros técnicos nano-banana

```bash
uv run "<path>/image.py" \
  --prompt "<prompt>" \
  --output "content/ficciones/<serie>/assets/hero-<slug>.png" \
  --model flash \
  --aspect landscape \
  --size 1K
```

### Fallback

Usar `assets/branding/social/thumbnail-default-1200x630.png` como placeholder neutro. No bloquear el output del skill por falta de hero.

### Registro de heros ficción

| # | Serie | Slug relato | Fecha | Descripción |
|---|---|---|---|---|
| — | _(pendiente primer relato publicado)_ | | | |

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
