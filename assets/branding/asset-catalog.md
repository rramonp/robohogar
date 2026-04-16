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
| 5 | `humanoides-en-casa-cuanto-falta` (v10) | 2026-04-15 | Editorial | flash | "Creación de Adán" — mano robot + mano humana en cocina, jardín, luz dorada |

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

**Cada artículo necesita 1 imagen hero + imágenes inline de fabricante:**

| Tipo de imagen | Aspect | Uso | Nombre archivo |
|---|---|---|---|
| **Hero** (artículo + thumbnail) | `square` o `landscape` | Imagen del artículo + post thumbnail + OG/SEO + redes | `hero-<slug>.png` |
| **Inline** (producto) | Variable | Fotos dentro del artículo | Originales de fabricante, no generadas |
| **Templates** (newsletter, social) | Variable | Newsletter header, social card | En `assets/images/`, no por artículo |

La hero se usa tanto dentro del artículo como post thumbnail — Beehiiv recorta automáticamente para cards/OG y el resultado es bueno. **Verificar en [opengraph.xyz](https://opengraph.xyz) tras publicar.** Solo si el recorte sale mal, generar una versión 16:9 adicional (`thumbnail-<slug>.png`).

### Estructura de carpetas por artículo

```
content/articulos/
  <slug>/
    borrador.html        ← Draft del artículo (HTML de Beehiiv)
    assets/
      hero-<slug>.png    ← Imagen destacada branded (1200x630)
      *.png/jpg          ← Imágenes inline, capturas, fotos producto
```

El agente de imágenes genera el hero automáticamente como parte del pipeline semanal, lo guarda en la carpeta del artículo y lo registra en este catálogo.

**Post-generación:** Nano-banana genera automáticamente una copia `.webp` comprimida (<500 KB) junto al PNG original. Usar el WebP para OG/thumbnail en Beehiiv y redes. El PNG se mantiene como master de calidad.

### Estilo ROBOHOGAR para heros de artículos

**Nombre del estilo:** Product-hero cinematográfico
**Referencia visual:** Thumbnails de YouTube tech + portadas de revistas editoriales

#### Principio #1: MINIATURA QUE FUNCIONA A 300px

La imagen hero se ve como miniatura en cards de Beehiiv (~300px), previews de WhatsApp, OG cards de redes. A ese tamaño tiene que funcionar.

**Regla de oro:** cuanto menos elementos, más impacto a tamaño pequeño. Un solo punto focal claro + contraste entre dos elementos (humano/robot, antes/después) genera más CTR que escenas complejas.

#### Principio #2: COMPOSICIÓN PARA NEWSLETTER (no YouTube)

| Hacer | NO hacer |
|---|---|
| **1-2 elementos máximo** — un punto focal claro que se lee en milisegundos | Escenas con 5+ elementos compitiendo por atención |
| **Close-ups e interacción** — manos, dedos, ojos. Gancho emocional inmediato | Figuras de cuerpo entero lejos de cámara — a 300px parecen siluetas genéricas |
| **Referencia cultural** si encaja — "Creación de Adán", iconografía reconocible | Composiciones literales sin concepto (robot de pie en un salón) |
| **Fondo limpio y luminoso** — cocina, jardín, luz natural dorada | Skylines urbanos con neones (Gemini mete texto asiático siempre) |
| **Contraste conceptual** — humano vs robot, cotidiano vs futurista | Escenas puramente decorativas sin tensión narrativa |

#### Características visuales (TODAS obligatorias)

| Elemento | Especificación |
|---|---|
| **Punto focal** | 1-2 elementos máximo. Si no se entiende a 300px, la composición falla |
| **Iluminación** | Golden hour natural, cálida. Luz dorada desde ventanas. Tonos ámbar/crema |
| **Paleta** | Blancos cálidos, ámbar (#F5A623), crema, madera natural. Sin neones |
| **Fondo** | Hogar moderno luminoso (cocina, salón). Ventanas con jardín/cielo, NO ciudad |
| **Interacción humana** | Siempre. Una mano, un dedo, una persona cercana. Robot solo = no engancha |
| **Estilo** | Render 3D estilizado. Ni foto real ni cartoon — moderno y thumbnail-friendly |
| **Mascota** | NO incluir la mascota ROBOHOGAR. Reservada para landing, emails, social cards |
| **Texto** | NUNCA. Ni letras, ni palabras, ni carteles, ni pantallas con texto |
| **Neones/skyline** | NUNCA en heros de artículos. Evitar ventanas con edificios o carteles |

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
[PUNTO FOCAL: 1-2 elementos máximo. Close-up preferido. Qué interacción humano-robot].
[FONDO: cocina/salón luminoso, ventana con jardín/cielo. NO ciudad, NO neones].
[MOOD: qué sensación transmite — futurista, acogedor, íntimo, esperanzador, etc.].
Warm golden natural light, 3D stylized render, editorial magazine quality,
warm amber and cream palette, shallow depth of field.
Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

**Generar siempre 3 variantes** con composiciones DISTINTAS entre sí (no 3 versiones del mismo encuadre). Cada variante debe probar un concepto/composición diferente para que Rafael elija.

#### Estilo ganador: "Creación de Adán" v10 (REFERENCIA PRINCIPAL)

Basado en el hero de `humanoides-en-casa-cuanto-falta` (v10) — la imagen que mejor funciona como miniatura de newsletter y define el nuevo estilo ROBOHOGAR.

**Por qué funciona v10:**

| Elemento | Qué hace | Por qué funciona a 300px |
|----------|----------|--------------------------|
| **Punto focal único** | Dos manos acercándose (robot + humana) | Se entiende en milisegundos. Cero ambigüedad |
| **Referencia cultural** | "Creación de Adán" de Miguel Ángel | Reconocible universalmente. Genera reacción emocional inmediata |
| **Contraste conceptual** | Tecnología vs humanidad, casi tocándose | Transmite el mensaje del artículo sin necesitar texto |
| **Fondo limpio** | Cocina luminosa, ventana con jardín verde, sin neones | No distrae. El foco está 100% en las manos |
| **Paleta cálida** | Ámbar/crema/madera, luz natural dorada | Acogedor, editorial, no frío-tech |
| **Objetos cotidianos** | Taza de café, frutero en primer plano | Contexto hogar real sin saturar |
| **Render 3D estilizado** | Ni foto real ni cartoon | Moderno, atractivo como thumbnail |

**Principios para TODOS los heros futuros:**

1. **1-2 elementos máximo como punto focal** — la miniatura se ve a 300px. Si necesitas "mirar más" para entenderla, no funciona
2. **Interacción humano-robot siempre** — mano tocando, dedo acercándose, persona cerca. Gancho emocional
3. **Close-ups > planos generales** — una mano con un robot > un salón entero con figuras lejanas
4. **Concepto visual > escena literal** — una metáfora (Creación de Adán) impacta más que una foto de producto
5. **Fondo luminoso y limpio** — jardín, cielo, cocina con luz natural. NUNCA skylines ni neones
6. **Contraste entre dos elementos** — humano/robot, cotidiano/futurista, real/posible. Genera tensión narrativa
7. **Paleta cálida sin excepciones** — ámbar, crema, madera, dorado. Sin azules fríos, sin neones

> **Nota sobre neones:** Los neones (cian, rosa, morado) son un artefacto de Gemini y del sign guard. Aunque el primer artículo los usó, la línea editorial definitiva es **sin neones**. Fondos limpios con jardín/cielo funcionan mejor para newsletters.

#### Prompts que funcionaron (referencia para futuros artículos)

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

#### Patrones por tipo de contenido

| Tipo de artículo | Composición | Ejemplo de foco |
|---|---|---|
| **Review/Comparativa** | Close-up producto + mano humana interactuando + fondo cocina/salón luminoso | Robot en encimera, dedo acercándose |
| **Futuro/Tendencia** | Metáfora visual (ej: "Creación de Adán") + close-up + contraste conceptual | Mano robot + mano humana casi tocándose |
| **Lifestyle/Experiencia** | Close-up robot haciendo tarea cotidiana + humano cerca + hogar cálido | Robot dando café a una mano |
| **Gadget/Producto nuevo** | Close-up producto + ojos ámbar como punto focal + mano humana | Robot con ojos brillantes en encimera |
| **Opinión/Editorial** | Escena evocadora y conceptual, close-up, referencia cultural si encaja | Dos manos, robot sirviendo, metáfora visual |

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
