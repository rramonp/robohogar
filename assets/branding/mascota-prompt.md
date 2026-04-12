# ROBOHOGAR — Mascota Oficial (Prompt de Referencia)

## Imagen base
`robohogar-mascot-principal.png` — versión definitiva aislada sin fondo. Taza de café en mano.

## Prompt exacto para reproducir la mascota principal

```
Same character as reference image: cute small domestic robot with round head, 
warm glowing LED eyes, small antenna, wearing a light blue checkered apron 
with a heart, holding a coffee mug. Isolated character only, NO background, 
NO furniture, NO plants, NO floor, NO sofa, NO objects around. Pure white 
background (#FFFFFF). Full body view, centered. Clean illustration style, 
professional brand mascot. No text, no letters, no words.
```

## Parámetros de generación

| Parámetro | Valor |
|---|---|
| Model | flash (draft) / 2 o pro (final) |
| Aspect | square |
| Reference | `robohogar-mascot-referencia.png` (versión con fondo hogar, usada como ancla de estilo) |

## Comando completo (Nano Banana)

```bash
uv run "<REPO_ROOT>/skills/external/nano_banana/scripts/image.py" \
  --prompt "<prompt arriba o prompt base + variación>" \
  --output "<output_path>.png" \
  --model flash \
  --aspect square \
  --reference "<path>/robohogar-mascot-referencia.png"
```

## Descripción del personaje

- **Forma:** Robot pequeño y redondeado, proporciones kawaii (cabeza grande, cuerpo compacto)
- **Cabeza:** Esférica, blanca/gris claro, con visor negro grande tipo pantalla LED
- **Ojos:** Dos óvalos cálidos color naranja/ámbar brillante, expresivos y amigables
- **Boca:** Sonrisa sutil en el visor (pequeña línea o punto)
- **Antenas:** Dos antenas finas con bolitas naranjas en las puntas
- **Lateral cabeza:** Círculo decorativo azul/gris (como un altavoz o sensor)
- **Cuerpo:** Compacto, articulaciones visibles (tornillos/juntas color cobre/naranja)
- **Delantal:** Cuadros azul claro y blanco, con un corazón celeste en el centro, bordes con volantes
- **Brazo derecho:** Sujeta una taza de café blanca con espiral decorativa (en pose principal)
- **Brazo izquierdo:** Relajado al costado (en pose principal)
- **Piernas:** Cortas, con botas/pies blancos redondeados
- **Paleta de colores:** Blanco, gris claro, negro (visor), naranja ámbar (ojos/juntas), azul celeste (delantal), cobre (detalles mecánicos)

---

## Prompt base para TODAS las variaciones

Todas las variaciones usan este prompt base + el texto de variación específico:
```
Same robot character as reference: round head, dark visor, warm orange LED 
eyes, small antennas with orange balls, blue checkered apron with heart. 
[VARIACION AQUI]. Isolated character only, pure white background, no objects, 
no scenery. Clean illustration style. No text, no letters.
```
Siempre con `--reference robohogar-mascot-referencia.png`.

## Reglas para mantener consistencia

Mantener SIEMPRE en todas las variaciones:
- Los ojos naranja LED brillantes
- El delantal de cuadros azules con corazón
- Las antenas con bolitas naranjas
- Las proporciones kawaii (cabeza > cuerpo)
- El estilo de ilustración limpio, sin outlines gruesos

---

## Catálogo completo de poses

### Principal — Con café (`robohogar-mascot-principal.png`)
Pose por defecto. Taza de café en mano derecha. Uso: avatar, og-image, favicon (solo cabeza), redes sociales.

### A — Saludando (`robohogar-mascot-saludando.png`)
Mano derecha levantada saludando. Uso: welcome email, primera newsletter, página "Sobre".
```
Variation: robot is waving hello with right hand raised, left hand on hip. 
Cheerful welcoming pose.
```

### B — Con casita (`robohogar-mascot-casita.png`)
Sostiene icono de casa con las dos manos, mirada de asombro. Uso: sección "Robots para el hogar", landing page hero.
```
Variation: robot holds a small glowing house icon in both hands, looking at 
it with wonder, eyes slightly wider. Gentle warm glow from the house.
```

### C — Leyendo (`robohogar-mascot-leyendo.png`)
Sentado en el suelo leyendo tablet/libro. Uso: cabecera de artículos, sección blog, roundups.
```
Variation: robot is sitting cross-legged on the ground reading a tablet or 
book, looking focused and content, slight smile. Cozy reading pose.
```

### E — Thumbs up (`robohogar-mascot-thumbsup.png`)
Pulgar arriba con mano derecha, taza en la izquierda. Uso: confirmación suscripción, CTAs, "gracias por suscribirte".
```
Variation: robot giving a thumbs up with right hand, left hand holds the 
coffee mug. Confident happy expression, eyes slightly squinted in a smile. 
Slight head tilt to the right.
```

### F — Detective (`robohogar-mascot-detective.png`)
Con lupa investigando, ojo ampliado por la lente. Uso: análisis profundo, deep dives, investigación.
```
Variation: robot holds a magnifying glass up to one eye, eye appears bigger 
through the lens, curious detective expression, leaning forward slightly as 
if investigating something closely.
```

### G — Herramientas (`robohogar-mascot-herramientas.png`)
Llave inglesa y destornillador. Uso: domótica, integración, setup, tutoriales técnicos.
```
Variation: robot holds a small wrench in one hand and a screwdriver in the 
other, like a handy repair technician ready to fix or set up something. 
Confident helpful pose.
```

### H — Megáfono (`robohogar-mascot-megafono.png`)
Megáfono en mano anunciando noticias. Uso: noticias, "Lo que se viene", lanzamientos, alertas.
```
Variation: robot holds a small megaphone or bullhorn in one hand raised up, 
other hand cupped near mouth as if shouting exciting news. Energetic excited 
expression, antennas perked up.
```

### I — Pensativo (`robohogar-mascot-pensativo.png`)
Mano en barbilla, mirando hacia arriba. Uso: opinión, "Vida con robots", editorial, debates.
```
Variation: robot in a thinking pose, one hand on chin, looking up 
thoughtfully, eyes slightly narrowed as if pondering a deep question. 
Contemplative philosophical expression.
```

### J — Compras (`robohogar-mascot-compras.png`)
Carrito de compra + etiqueta de precio. Uso: guías de compra, ofertas, comparativas, afiliados Amazon.
```
Variation: robot pushes a small shopping cart with one hand, the other hand 
holds up a price tag. Helpful shopper expression, like a friendly shopping 
assistant.
```

### K — Trofeo (`robohogar-mascot-trofeo.png`)
Trofeo estrella dorada sobre la cabeza, celebrando. Uso: "Robot del mes", rankings, premios, destacados.
```
Variation: robot proudly holds up a golden star trophy or award with both 
hands above its head, celebrating. Eyes wide with excitement, antennas 
glowing brighter. Victorious celebratory pose.
```

---

## Mapa de uso por sección del newsletter

| Sección | Pose | Archivo |
|---|---|---|
| Avatar / og-image / favicon | Principal | `robohogar-mascot-principal.png` |
| Welcome email / onboarding | A — Saludando | `robohogar-mascot-saludando.png` |
| Landing page hero | B — Con casita | `robohogar-mascot-casita.png` |
| Cabecera artículos / roundups | C — Leyendo | `robohogar-mascot-leyendo.png` |
| Confirmación suscripción / CTAs | E — Thumbs up | `robohogar-mascot-thumbsup.png` |
| Análisis profundo / deep dives | F — Detective | `robohogar-mascot-detective.png` |
| Domótica / integración / setup | G — Herramientas | `robohogar-mascot-herramientas.png` |
| Noticias / lanzamientos / alertas | H — Megáfono | `robohogar-mascot-megafono.png` |
| Opinión / "Vida con robots" | I — Pensativo | `robohogar-mascot-pensativo.png` |
| Guías de compra / ofertas | J — Compras | `robohogar-mascot-compras.png` |
| "Robot del mes" / rankings | K — Trofeo | `robohogar-mascot-trofeo.png` |
