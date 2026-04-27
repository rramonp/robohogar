# Pipo · Hero prompts (3 candidatos · v2 · composiciones distintas)

**Canon aplicada:** regla dura `editorial.md § Composición canon · 3 candidatos = 3 C-XX distintas`. Esta v2 reemplaza la v1 (los 3 candidatos compartían C-05) tras feedback de Rafael 2026-04-28 PM. Los renders pre-canon (C2 y C3 v1, ambos C-05) están archivados en `assets/_archive/hero-pipo-c{2,3}-v1-pre-3-distintas-canon-2026-04-28.{png,webp}`.

**Frontmatter declarado:**
- `hero_paradigma: personaje-accion-imposibilidad`
- `modalidad_visual: M5` (amanecer brumoso · niebla lechosa + crema + acento ámbar tenue del soldador) — fija para los 3 candidatos
- `angulo_camara: A4` (a través de marco — siempre con ramas de pino enmarcando) — fija para los 3 candidatos
- `display_title_family: G1` band `B` (trabajadores ES día a día — cazador rural)
- **Archetype propuesto:** B-08 *Cazador en pinar con humanoide soldando un descendiente de chatarra* (canonizable tras este hero — ningún B catalogado encaja con cazador rural).

## Tres candidatos con composiciones C-XX totalmente distintas

Cada candidato es una **composición distinta + familia distinta**. Lo que comparten: M5 + A4 + paradigma personaje-acción-imposibilidad + banda B + Pipo + Manuel + altar de chatarra.

| # | Composición | Familia | Lectura macro del frame |
|---|---|---|---|
| **C1** | C-05 Eje simétrico altar | II Plano arquitectónico monumental | Altar centrado y ritual, sacralidad mecánica, lectura de mapa |
| **C2** | C-09 Over-the-shoulder voyeur | IV Frontal teatral / OTS | Cámara detrás del hombro de Manuel — sentimos descubrir la escena con él |
| **C3** | C-07 Ventana / umbral | III Frame-in-frame | Vemos la escena entre dos troncos de pino — matryoshka espacial, espiar |

3 composiciones, 3 familias distintas. Ideal cumplido.

---

### Candidato 1 · C-05 Eje simétrico altar (familia II Plano arquitectónico monumental)

**Razón:** la lectura más obvia del relato — el altar centrado y simétrico funciona como sacralidad mecánica. El robot es sacerdote; las piezas, ofrenda. Manuel rompe la simetría desde el lado, presencia fuera del eje.

```
[ver /tmp/pipo_v2_c1.txt o el bloque ensamblado más abajo]
```

---

### Candidato 2 · C-09 Over-the-shoulder voyeur (familia IV Frontal/OTS)

**Razón:** lectura más cinematográfica — la cámara se mete detrás del hombro de Manuel y nos hace cómplices del descubrimiento. La cara de Manuel no se ve (regla OTS); leemos su shock por la línea del hombro tenso. Pipo está en foco, ajeno al hunter, absorbido por su tarea.

```
[ver /tmp/pipo_v2_c2.txt]
```

---

### Candidato 3 · C-07 Ventana / umbral (familia III Frame-in-frame)

**Razón:** lectura más íntima y voyeur — el frame se construye entre dos troncos de pino que actúan como portal natural. Tres distancias de testigo: viewer fuera del marco, Manuel apenas dentro del borde, Pipo en el centro lejos del clearing interior. Matryoshka espacial.

```
[ver /tmp/pipo_v2_c3.txt]
```

---

## Verificación pre-output

| Check | C1 | C2 | C3 |
|---|---|---|---|
| `len(set([c1.C, c2.C, c3.C])) == 3` | ✅ C-05 | ✅ C-09 | ✅ C-07 |
| `len(set([c1.fam, c2.fam, c3.fam])) == 3` | ✅ II | ✅ IV | ✅ III |
| Personaje identificable por rol (cazador) | ✅ | ✅ (silueta hombro) | ✅ (silueta umbral) |
| Acción visible coherente con verbo display title | ✅ entrar | ✅ descubrir | ✅ asomarse |
| Objeto-imposibilidad presente | partículas levitando | mano que repta sola | vapor dorado escapando del pecho |
| Modalidad M5 declarada y consistente | ✅ | ✅ | ✅ |
| Ángulo A4 (through-frame) | ✅ ramas pine | ✅ ramas + OTS | ✅ troncos como portal |
| Foco lumínico único | milky backlight | milky backlight | milky backlight desde profundidad |
| Cero LEDs / glow / neón / asiático / texto | ✅ | ✅ | ✅ |
| Test 120px legibilidad | alta | media-alta | alta |
| Riesgo regen Gemini | bajo | medio (puede meter cara hunter) | bajo |

## Recomendación

Los 3 son válidos. Mi voto:
1. **C2 (OTS)** — más cinematográfico y peninsular literario, encaja con la voz Marta Sanz/Mesa y con el peso moral del relato.
2. **C3 (umbral)** — más sutil y atmosférico, gran a thumbnail.
3. **C1 (altar)** — más legible inmediatamente, lectura de mapa.

Rafael decide.

## Comando de ejecución

```bash
# Desde el repo raíz, con GEMINI_API_KEY exportado:
cd c:/Users/cri-c/robohogar
python utilities/nano_banana_image.py --prompt "$(cat /tmp/pipo_v2_c1.txt)" --output content/ficciones/_one-shots/pipo/assets/hero-pipo-v2-c1-altar-C05.png --model 2 --aspect 16:9 --size 2K
python utilities/nano_banana_image.py --prompt "$(cat /tmp/pipo_v2_c2.txt)" --output content/ficciones/_one-shots/pipo/assets/hero-pipo-v2-c2-OTS-C09.png --model 2 --aspect 16:9 --size 2K
python utilities/nano_banana_image.py --prompt "$(cat /tmp/pipo_v2_c3.txt)" --output content/ficciones/_one-shots/pipo/assets/hero-pipo-v2-c3-umbral-C07.png --model 2 --aspect 16:9 --size 2K
```

Tras la elección de Rafael, mover candidatos no usados a `assets/_archive/hero-pipo-v2-c{X}-{nombre}-no-elegido-2026-04-28.png` (regla `feedback_robohogar_archive_heroes`).
