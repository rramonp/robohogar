# ROBOHOGAR — Asset Catalog

Catálogo vivo de todos los assets visuales generados. **Actualizar después de cada generación con Nano Banana.**

---

## Mascota — Poses (11/11 completadas)

| Pose | Archivo | master/ (2K) | flash-1K/ (1K) | Uso principal |
|---|---|---|---|---|
| Principal (café) | `robohogar-mascot-principal.png` | ✅ | ✅ | Avatar, og-image, favicon, redes sociales |
| A — Saludando | `robohogar-mascot-saludando.png` | ✅ | ✅ | Welcome email, onboarding, página "Sobre" |
| B — Con casita | `robohogar-mascot-casita.png` | ✅ | ✅ | Landing page hero, sección "Robots para el hogar" |
| C — Leyendo | `robohogar-mascot-leyendo.png` | ✅ | ✅ | Cabecera artículos, blog, roundups |
| E — Thumbs up | `robohogar-mascot-thumbsup.png` | ✅ | ✅ | Confirmación suscripción, CTAs, gracias |
| F — Detective | `robohogar-mascot-detective.png` | ✅ | ✅ | Análisis profundo, deep dives, investigación |
| G — Herramientas | `robohogar-mascot-herramientas.png` | ✅ | ✅ | Domótica, integración, setup, tutoriales |
| H — Megáfono | `robohogar-mascot-megafono.png` | ✅ | ✅ | Noticias, lanzamientos, alertas |
| I — Pensativo | `robohogar-mascot-pensativo.png` | ✅ | ✅ | Opinión, editorial, debates |
| J — Compras | `robohogar-mascot-compras.png` | ✅ | ✅ | Guías de compra, ofertas, afiliados Amazon |
| K — Trofeo | `robohogar-mascot-trofeo.png` | ✅ | ✅ | "Robot del mes", rankings, premios |

## Mascota — En contexto

| Archivo | Carpeta | Descripción |
|---|---|---|
| `robohogar-mascot-referencia.png` | `con-fondo/` | Mascota en contexto hogar — usada como `--reference` para anclar estilo |

## Templates generales

| Archivo | Carpeta | Fecha | Descripción |
|---|---|---|---|
| `hero-landing-mascota-hogar.png` | `images/` | 2026-04-12 | Hero section landing — mascota en salón con robot aspirador. Flash, landscape |
| `newsletter-header.png` | `images/` | 2026-04-13 | Cabecera newsletter — mascota saludando + espacio limpio. Flash, 21:9 |
| `social-card-template-v2.png` | `images/` | 2026-04-13 | Template social card — borde elegante + mascota esquina inferior derecha. Flash, square |

## Heros de artículos

| # | Slug | Fecha | Tipo | Modelo | Descripción |
|---|---|---|---|---|---|
| 1 | `mejor-robot-aspirador-2026` | 2026-04-13 | Review | flash | Aspirador premium iluminado cenital ámbar en salón moderno |
| 2 | `robots-humanoides-casa-2030` | 2026-04-13 | Futuro | flash | Humanoide entrando por puerta, backlit cinematográfico |
| 3 | `experiencia-robots-casa` | 2026-04-13 | Lifestyle | flash | Salón acogedor con aspirador + robot servicio + gato |
| 4 | `mejor-robot-asistente-ia-2026` | 2026-04-13 | Gadget | flash | Robot asistente ojos ámbar en encimera, mano interactuando |

Ruta de cada hero: `content/articulos/<slug>/assets/hero-<slug>[-vN].png`

---

## Estructura de carpetas

| Carpeta | Resolución | Propósito |
|---|---|---|
| `assets/branding/master/` | 2K | Assets definitivos — web, landing, print, social cards |
| `assets/branding/flash-1K/` | 1K | Borradores, previews rápidos, tests |
| `assets/branding/con-fondo/` | Variable | Mascota en escenas/contextos — referencias de estilo |
| `assets/images/` | Variable | Templates generales (newsletter header, social card, OG) |
| `content/articulos/<slug>/assets/` | Variable | Hero + imágenes por artículo |

## Estrategia de imágenes por artículo

| Tipo de imagen | Origen | Dónde va |
|---|---|---|
| **Hero/destacada** (1200x630) | Siempre branded con nano-banana | `content/articulos/<slug>/assets/hero-<slug>.png` |
| **Inline** (dentro del artículo) | Originales de la fuente/fabricante | `content/articulos/<slug>/assets/` |
| **Templates** (newsletter header, social card) | Branded con nano-banana | `assets/images/` (no van por artículo) |

### Estructura de carpetas por artículo

```
content/articulos/
  <slug>/
    borrador.md          ← Draft del artículo
    assets/
      hero-<slug>.png    ← Imagen destacada branded (1200x630)
      *.png/jpg          ← Imágenes inline, capturas, fotos producto
```

El agente de imágenes genera el hero automáticamente como parte del pipeline quincenal, lo guarda en la carpeta del artículo y lo registra en este catálogo.

### Estilo ROBOHOGAR para heros de artículos

**Nombre del estilo:** Product-hero cinematográfico
**Referencia visual:** Thumbnails de YouTube tech + portadas de revistas editoriales

#### Principio #1: GANCHO VISUAL = CLICK

La imagen hero es una **miniatura de YouTube**. Su único trabajo es que la gente haga click.
- El lector ve la imagen en una card de 300px en la landing, en una preview de redes sociales, o en un feed de email
- En menos de 1 segundo tiene que entender DE QUÉ VA el artículo y sentir curiosidad
- Si la imagen no genera "quiero saber más", ha fallado
- Referencia: los mejores canales tech de YouTube (MKBHD, Linus Tech Tips) — sus thumbnails son el 50% del éxito de cada vídeo

#### Características visuales (TODAS obligatorias)

| Elemento | Especificación |
|---|---|
| **Protagonista** | El producto/robot es el centro absoluto de la imagen. Ocupa ~30-50% del frame |
| **Iluminación** | Dramática, cálida. Luz principal desde arriba o detrás (backlit). Tonos ámbar/dorados |
| **Paleta** | Blancos cálidos, ámbar (#F5A623), grises suaves, sombras profundas. Alto contraste |
| **Fondo** | Hogar moderno (salón, cocina, entrada). Siempre desenfocado (shallow depth of field) |
| **Composición** | El robot/producto se entiende al instante — "YouTube thumbnail energy" |
| **Estilo fotográfico** | Editorial, magazine-quality. Realismo con toque cinematográfico |
| **Mascota** | NO incluir la mascota ROBOHOGAR. Reservada para landing, emails, social cards |
| **Texto** | NUNCA. Ni letras, ni palabras, ni carteles, ni pantallas con texto |
| **Ventanas/exterior** | Evitar skylines urbanos (Gemini mete neones con texto asiático) |

#### Parámetros técnicos nano-banana

```bash
uv run "<path>/image.py" \
  --prompt "<prompt>" \
  --output "content/articulos/<slug>/assets/hero-<slug>.png" \
  --model flash \
  --aspect landscape \
  --size 1K
```

**IMPORTANTE:** NO usar `--reference` para heros de artículos. La referencia a la mascota contamina el estilo y genera artefactos (texto asiático, estilo cartoon). Los heros son fotográficos, no ilustración.

#### Prompt template

```
Eye-catching editorial hero image for an article about [TEMA DEL ARTÍCULO].
[DESCRIPCIÓN DEL PRODUCTO/ROBOT: qué es, cómo se ve, dónde está].
[COMPOSICIÓN: ángulo de cámara, qué está en foco, qué en el fondo].
[MOOD: qué sensación transmite — futurista, acogedor, impresionante, etc.].
Warm amber lighting, editorial photography style, high contrast, shallow depth of field.
Absolutely NO text, NO letters, NO words, NO signs, NO writing of any kind.
```

#### Prompts que funcionaron (referencia para futuros artículos)

**Review/Comparativa de producto** (ej: aspiradores):
```
Eye-catching editorial hero image for a robot vacuum buying guide article.
A premium robot vacuum in the center of frame, dramatically lit from above
with warm amber light. Sleek modern living room out of focus in the background.
The vacuum is the star — product-hero photography style like a magazine cover
or YouTube thumbnail. Clean, high contrast, professional. Warm color palette:
whites, amber highlights, soft shadows.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Artículo futurista/tendencia** (ej: humanoides):
```
Eye-catching editorial hero image about humanoid robots entering homes.
A tall sleek humanoid robot standing in a modern living room doorway,
backlit with dramatic warm amber light streaming in. The humanoid is
stepping into the home for the first time. Cinematic framing, shallow
depth of field. The mood is exciting and slightly futuristic but welcoming.
High contrast, warm whites and ambers. YouTube thumbnail energy — instantly
clear this is about humanoid robots at home.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Artículo lifestyle/experiencia** (ej: vivir con robots):
```
Eye-catching editorial hero image about living with robots at home.
A cozy modern living room seen from a wide angle. Multiple domestic robots
visible: a robot vacuum on the floor, a small robot on the kitchen counter,
a smart speaker glowing amber on a shelf. The room is warm, lived-in,
natural light from a big window. The feeling is: this is already happening,
robots are already part of daily life. Editorial photography style, warm
amber tones, shallow depth of field on the closest robot.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Artículo de producto nuevo/gadget** (ej: asistentes IA):
```
Eye-catching editorial hero image for an article about AI robot assistants
to buy in 2026. A small cute desktop companion robot with expressive LED
eyes and a rounded friendly design, sitting on a modern desk or kitchen
counter. Warm amber glow from its eyes. A person's hand reaching toward
it or interacting with it naturally, like talking to a friend. Cozy home
setting, warm natural light. The robot is the clear hero of the image —
product-hero style like a YouTube thumbnail. High contrast, clean composition.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

#### Patrones por tipo de contenido

| Tipo de artículo | Composición | Ejemplo de foco |
|---|---|---|
| **Review/Comparativa** | Producto centrado, luz cenital dramática, fondo salón desenfocado | Robot aspirador iluminado en parquet |
| **Futuro/Tendencia** | Escena cinematográfica, robot en contexto impactante | Humanoide entrando por una puerta |
| **Lifestyle/Experiencia** | Gran angular, hogar acogedor, varios robots visibles | Salón con aspirador + robot + smart speaker |
| **Gadget/Producto nuevo** | Producto en mesa/encimera, mano humana interactuando | Robot asistente con ojos ámbar en cocina |
| **Opinión/Editorial** | Escena evocadora, conceptual, menos literal | (Aquí sí se puede usar mascota pensativa) |

### Cuándo SÍ usar la mascota en heros

- Landing page hero
- Welcome email / reminder email
- Artículos de opinión/editorial personal (mascota pensativa, detective)
- Social cards genéricas de la newsletter
- Páginas "Sobre" / 404
- Newsletter header

## Reglas

- **NUNCA sobrescribir** un archivo existente — usar sufijo versionado (-v2, -v3)
- **SIEMPRE actualizar este catálogo** después de generar una imagen nueva
- Antes de generar, revisar este catálogo para evitar duplicados
- Nuevas poses de mascota → `master/` (modelo 2/pro) + `flash-1K/` (modelo flash)
- Heros de artículos → `content/articulos/<slug>/assets/` con estilo product-hero
