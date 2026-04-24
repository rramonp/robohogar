---
name: ROBOHOGAR — Hero 1200×630 obligatorio (modelo 2 + crop) + validador ES de calcos en /content-draft
description: (1) Hero artículos = 1200×630 exacto, generar con --model 2 --aspect 16:9 --size 2K + crop Pillow. NUNCA flash (ignora aspect y genera 1024×1024). (2) /content-draft debe correr validador ES de calcos léxicos como hace /ficcion-draft (paso 8.5 ter) — grep de "no compres de más", "dale al botón de", "centro de X", microcopy UI anglo, voz técnica. Read-aloud test como filtro final.
type: feedback
originSessionId: d677cb72-9b8c-47af-bc9a-8d85e34db6f2
---
**Incidente 2026-04-21:** Rafael revisó el artículo #9 "Mejor robot cortacésped 2026" y detectó tres problemas simultáneos que deberían haber bloqueado la entrega:

1. **Calco léxico "no compres de más"** en el subtítulo — traducción literal de *"don't overbuy"*. En ES peninsular "comprar de más" significa "comprar demasiadas unidades por error" (≠ sobrepagar por una). La forma idiomática ES es *"no pagar más de la cuenta"* / *"no te equivoques al comprar"*. Las reglas previas (anti-IA + editorial-es §4.1) no tenían este calco específico.
2. **Heros en 1024×1024 cuadrado** cuando el estándar ROBOHOGAR es 1200×630 (OG Beehiiv/Twitter/LinkedIn). Rafael literalmente: *"Otra cosa que también hemos hecho un montón de veces mal; supuestamente has puesto reglas, hooks, validadores y toda la puta mierda para que no vuelva a ocurrir, y la siguiente vez vuelve a ocurrir"*. Reincidente.
3. **Validador ES de calcos** no estaba activo en `/content-draft` aunque sí en `/ficcion-draft § 8.3`. La prosa de no-ficción se estaba generando sin la capa de validación que sí tiene la ficción.

---

## (1) Hero dimensions obligatorias 1200×630

**Why:** el estándar OG card de Beehiiv/Twitter/LinkedIn es 1200×630 (ratio 1.905). El modelo `flash` de Gemini (`gemini-2.5-flash-image`) **ignora silenciosamente** el parámetro `--aspect` y cae siempre a 1024×1024 cuadrado. Usar `flash` para heros rompe el estándar visual sin avisar.

**How to apply** (regla dura para cualquier `/content-draft` o `/nano-banana` que genere hero de artículo):

```bash
uv run image.py \
  --prompt "<prompt específico con suffix anti-neones>" \
  --output "content/articulos/<slug>/assets/hero-<slug>-v<N>.png" \
  --model 2 \            # ✅ gemini-3.1-flash-image-preview (rápido + respeta aspect)
                         # Alternativa: --model pro (gemini-3-pro-image-preview, más lento + calidad)
                         # ❌ NUNCA --model flash (genera 1024×1024 siempre)
  --aspect 16:9 \
  --size 2K              # produce ~2752×1536
```

**Crop obligatorio post-generación** con Pillow a 1200×630 exacto (ratio 1.905, ligeramente más panorámico que 16:9 puro 1.778):

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

**Verificación pre-output:** abrir los 3 `.webp` con Pillow y confirmar `img.size == (1200, 630)`. Si no → regenerar. El skill NUNCA entrega un borrador con heros cuadrados.

Documentado en: `assets/branding/nano-banana-prompt-base.md § Dimensiones obligatorias` + `.claude/commands/content-draft.md § 6`.

---

## (2) Validador ES de calcos en /content-draft — paso 8.5 ter

**Why:** `/ficcion-draft` carga obligatoriamente `references/ficciones/castellano-literario-es.md § 8.1` y corre 21 greps de calcos canónicos antes de entregar. `/content-draft` tenía anti-IA (§ 8.5) + editorial-es (§ 8.5 bis) pero NO la capa de calcos léxicos específicos. Resultado: salieron frases sin sentido ES como *"checklist para que no compres de más"* / *"dale al botón de comprar"* (traducciones literales de *"don't overbuy"* / *"hit the buy button"*).

**How to apply** — `/content-draft § 8.5 ter` corre estos greps obligatorios antes de cerrar el borrador:

- (a) **Calcos marketing anglo:** `no (compres|pagues) de más · comprar/pagar de más · ahorrarte comprar · dale al botón de (comprar|pagar|finalizar)`
- (b) **Conectores anglo:** por otro lado · en este sentido · dicho esto · es importante destacar · adicionalmente · en definitiva · es por ello que · a la hora de · de cara a
- (c) **"Centro de X":** centro de (demostración|llamadas|datos|servicio|atención|operaciones) · call center · data center
- (d) **Voz técnica anglo en narrador:** configuró · registra · activó · ejecuta · módulo · input · output · backend · cruzó con (datos|fotos|archivos)
- (e) **Microcopy UI anglo:** No, gracias · ¿Estás seguro · Enviar feedback · Aprender más · Configuraciones (como label UI) · Got it
- (f) **Adverbios -mente count** (≤8 en guía larga, ≤4 en artículo corto)
- (g) **Inciso "Es decir, X, y Y":** coordinación anglo

**Regla de decisión:**
- ≥1 match en (a), (c), (d), (e), (g) → reescribir antes de entregar (calcos duros sin contexto válido).
- Matches en (b) → revisar caso a caso (algunos conectores tienen uso editorial legítimo).
- Count (f) fuera de objetivo → sustituir adverbios por perífrasis (*absolutamente* → *del todo* · *rápidamente* → *rápido*).

**Read-aloud test como filtro final:** si un match es ambiguo (típicamente d y g), leer la frase en voz alta. Si suena a traducción (doblaje, Google Translate, manual técnico), reescribir. Los greps son el primer filtro; la oreja es el definitivo. Mismo principio que `/ficcion-draft § 8.1` ya aplica.

**Nuevos calcos canonizados 2026-04-21** en `references/editorial-es/01-articulos-y-columnas.md § 4.1`:
- #9 *"no compres de más"* / *"no pagues de más"* → *"no pagar más de la cuenta"* / *"no te equivoques al comprar"*
- #10 *"dale al botón de comprar"* → *"antes de pagar"* / *"antes de cerrar la compra"*

Documentado en: `.claude/commands/content-draft.md § 8.5 ter` + `references/editorial-es/01-articulos-y-columnas.md § 4.1 #9-#10` + `§ 7.1 (e)(f)(g)` (greps añadidos).

---

## (3) Regla de actitud

Cuando una regla existe pero el agente la incumple por reincidencia, **la regla no basta — hay que hacerla verificable programáticamente**. Por eso:
- Hero 1200×630 → verificación `img.size == (1200, 630)` obligatoria pre-output, no confianza en el agente para configurar el modelo correcto.
- Calcos ES → grep automático, no confianza en que el agente los detecte por intuición.
- Cifras inventadas → grep automático, no confianza en que el agente recuerde la regla.

La confianza se recupera con validación automática, no con más prosa en las reglas.
