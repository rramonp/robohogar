# Nano Banana — Prompt base reutilizable (anti-neones)

Destilación ejecutable de las reglas de `asset-catalog.md` para HEROS de artículos. Objetivo: reducir iteraciones por neones de 7-9 a 2-3. Evidencia: tras 5 artículos, Gemini mete neones/pantallas/texto asiático siempre que haya (a) pared trasera visible + múltiples objetos, (b) "LED accents" + varios robots, o (c) escenas tipo "showroom/lineup/gallery".

---

## ⚠️ Dimensiones obligatorias para hero de artículo ROBOHOGAR

**Regla dura 2026-04-21 (reincidente; Rafael lleva tiempo insistiendo):**

- Dimensión final **1200 × 630** (OG estándar Beehiiv / Twitter / LinkedIn card). No 1024×1024. No cuadrado. No otra cosa.
- Aspect ratio de generación: **16:9** (luego crop centrado a 1200×630, ver § Crop abajo).
- Modelo obligatorio: `--model 2` (o `--model pro`). **Nunca `flash`**: el `flash` (gemini-2.5-flash-image) **ignora silenciosamente** el parámetro `--aspect` y genera siempre cuadrado 1024×1024. El `2` (gemini-3.1-flash-image-preview) y `pro` respetan 16:9.
- Tamaño de generación: **`--size 2K`** (produce 2752×1536 aprox). El `1K` en `flash` es lo que causaba los 1024×1024 falsos.

**Comando canónico para hero de artículo ROBOHOGAR:**

```bash
uv run image.py \
  --prompt "<prompt específico> <suffix compilado>" \
  --output "content/articulos/<slug>/assets/hero-<slug>-v<N>.png" \
  --model 2 \
  --aspect 16:9 \
  --size 2K
```

**Crop obligatorio post-generación** a 1200×630 (ratio 1.905, algo más panorámico que 16:9 puro 1.778):

```python
from PIL import Image
TARGET_W, TARGET_H = 1200, 630
TARGET_RATIO = TARGET_W / TARGET_H  # 1.905

img = Image.open(png_path)
w, h = img.size
src_ratio = w / h
if src_ratio > TARGET_RATIO:
    new_w = int(h * TARGET_RATIO); left = (w - new_w) // 2
    img = img.crop((left, 0, left + new_w, h))
else:
    new_h = int(w / TARGET_RATIO); top = (h - new_h) // 2
    img = img.crop((0, top, w, top + new_h))
img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
img.save(png_path, 'PNG', optimize=True)
img.save(png_path.replace('.png', '.webp'), 'WEBP', quality=85, method=6)
```

**Verificación pre-output:** antes de cerrar el artículo, comprobar que los 3 heros tienen `img.size == (1200, 630)` exactos. Si alguno sale a otra dimensión, regenerar. NO ENTREGAR un borrador con heros cuadrados o cualquier otro ratio — es fallo de config, no de gusto del fabricante.

**Incidente origen:** ver § Historial de errores resueltos (entrada 2026-04-21 al final).

---

**Uso:** toda invocación de `/nano-banana` para un hero de artículo DEBE componer el prompt así:

```
<prompt específico del artículo>
+ <suffix de estilo base, copiar literal de § "Suffix compilado" abajo>
```

Si el prompt específico describe >1 robot o contiene "showroom/lineup/row", aplicar primero el **decision tree** para elegir composición segura.

---

## Decision tree — elegir composición según escena

| Escena | Patrón seguro | Patrón que falla (no usar) |
|---|---|---|
| **1 robot + 1 humano** (close-up manos, interacción) | ✅ Cocina cálida, ventana con jardín, plano cerrado | ❌ Pared con cuadros/objetos — Gemini los convierte en pantallas |
| **1 robot solo** (producto destacado) | ✅ Fondo limbo cream infinito O cocina luminosa desenfocada | ❌ Showroom, escenario de tienda, calle urbana |
| **>1 robot alineados** (comparativa, catálogo) | ✅ Limbo cream infinito SIN pared ni arquitectura · overhead top-down · backlit silueta a contraluz | ❌ Sala con pared (neones garantizados) · showroom · gallery |
| **Robot en casa real** (escena lifestyle) | ✅ Salón/cocina con 1-2 elementos cotidianos (taza, planta, libro) | ❌ Interior con >3 elementos decorativos — Gemini los decora con LED |
| **Robot en warehouse/industria** (editorial) | ✅ Pallets de madera simples, luz natural, plano cerrado | ❌ Nave con estanterías + fondo — metacarteles de marcas ficticias |

**Regla de oro:** si el prompt incluye "several robots" o "row of" y hay una pared trasera implícita → **eliminar la pared**. Usar limbo, overhead o silueta backlit.

---

## Suffix compilado (copiar literal al final del prompt)

Pegar este bloque al final de cualquier prompt para hero de artículo:

```
Matte solid-colored surfaces without any illumination, without any patterns, without any chest panels, without any printed symbols. Robot eyes are simple small dark circular shapes like camera lenses, not glowing. Plain cream-painted walls completely unmarked. Natural golden hour sunlight only. 3D stylized render, editorial magazine quality, warm amber and cream color palette, cinematic shallow depth of field. Home interior aesthetic, not commercial showroom. Absolutely NO text, NO letters, NO words, NO writing of any kind.
```

Ese suffix resuelve simultáneamente:
- **Cuerpos de robots sin paneles luminosos** (el error de v4 del artículo humanoides-2026)
- **Pared limpia sin decoraciones** (el error de v1/v5)
- **Sin texto/carteles asiáticos** (mencionado positivamente + negativamente)
- **Sin estética de showroom** (fuerza "home interior")

---

## Palabras/frases a evitar en el prompt específico

| Evitar | Porque | Usar en su lugar |
|---|---|---|
| "LED accents", "glowing chest", "illuminated panel" | Gemini añade paneles rosa/morados rosa | "matte solid chest, no illumination" |
| "showroom", "gallery", "display lineup", "exhibition" | Interpreta como tienda con carteles LED | "home living room", "kitchen interior", "studio limbo" |
| "several robots in a row", "seven humanoids lined up" (sin escena) | Gemini completa con pared comercial + decoración neón | Añadir siempre el contexto exacto: "standing on a warm wooden floor in front of a plain cream wall" O "on a seamless cream infinity backdrop" |
| "futuristic interior", "sci-fi apartment" | Trigger para escena con pantallas holográficas y neones | "minimalist home kitchen", "modern warm living room" |
| "Asian style", "Japanese design" | Añade caracteres japoneses/chinos en carteles | No usar — si el artículo es sobre un producto chino, describir el producto sin describir estética asiática |

---

## Validación rápida post-generación

Antes de convertir a webp y usar la imagen, revisar que:

- [ ] **No hay texto legible** en carteles, pantallas o paredes
- [ ] **No hay paneles luminosos** en pecho, tripa o espalda de los robots (magenta, cyan, amarillo, naranja brillante)
- [ ] **No hay pantallas LED** en ninguna superficie del fondo
- [ ] **No hay caracteres asiáticos** (japoneses, chinos, coreanos) en ningún elemento
- [ ] **La escena se lee como hogar/estudio**, no como tienda/feria/centro comercial

Si falla alguno: archivar la variante con `mv <archivo> assets/_archive/` (regla del repo — nunca `rm`), ajustar prompt según tabla de "Palabras a evitar" y regenerar.

---

## Historial de errores resueltos (para no repetirlos)

| Artículo | Versión fallida | Qué puso Gemini | Regla aplicada desde entonces |
|---|---|---|---|
| `mejor-robot-asistente-ia-2026` v1-v4 | Skyline atardecer con neones | Carteles cian/rosa en edificios | "Sin ciudad, sin skyline" |
| `neo-humanoide-fabricas-eqt` v1-v7 | Carteles LED + caracteres asiáticos | Pantallas en pared del fondo | "Cocina con pared crema plana" |
| `humanoides-domesticos-2026-comparativa` v1 | Gallery lineup + neones | Letras decorativas + pantallas | "Limbo cream, sin arquitectura" |
| `humanoides-domesticos-2026-comparativa` v4 | LED accents → paneles rosa/naranja en robots | Chest panels luminosos | "Matte solid, no illumination" |
| `humanoides-domesticos-2026-comparativa` v5 | TV con caracteres asiáticos + círculo morado | Decoración de pared | "Eliminar pared — overhead/limbo/backlit" |
| `la-casa-de-amparo` ep0 v1 | Hero ficción con ventana exterior de barrio Lavapiés | Neones de caracteres asiáticos (morado/cyan/naranja) en escaparates visibles por la ventana del piso | Para heros de ficción en "Lavapiés/Madrid/barrio multicultural": **no usar ventana exterior visible** — mantener escena 100% interior, o usar ventana con persianas cerradas sin exterior a la vista |
| `mejor-robot-cortacesped-2026` v1/v2/v3 | Hero generado con `--model flash --size 1K --aspect landscape` | Devolvió 1024×1024 cuadrado (el modelo `flash` ignora silenciosamente `--aspect`) | Usar SIEMPRE `--model 2` (o `pro`) + `--aspect 16:9` + `--size 2K` + crop Pillow centrado a 1200×630. Ver § "Dimensiones obligatorias" al inicio de este archivo. Regla dura desde 2026-04-21 tras reincidencia (Rafael había avisado antes). |

Cuando ocurra un error nuevo, añadir fila aquí y regla a § "Palabras a evitar".
