# Pendientes · rebrand tagline «Robótica doméstica de andar por casa»

> Fecha creación: 2026-04-22 · Commit repo: `a79e9ed`
>
> Trabajo de rebrand de la tagline oficial ROBOHOGAR. El repo ya está alineado
> en el commit de arriba. Lo que queda es aplicar los cambios manuales en
> Beehiiv, SEO y redes sociales. Este doc es la checklist activa — marca
> cada tarea con `[x]` según vayas completando. Cuando todo esté `[x]`,
> puedes archivar este archivo en `utilities/_archive/` o borrarlo.

---

## Strings canónicos (copia-pega exacto)

| Pieza | String exacto | Chars |
|---|---|---|
| **Headline / H1 landing** | `Robótica doméstica de andar por casa` | 36 |
| **Subtítulo hero** | `Análisis y Ficciones Domésticas. Cada semana` | 44 |
| **Meta title** (title tag + OG title) | `ROBOHOGAR — Robótica doméstica de andar por casa` | 52 |
| **Meta description** (meta + OG description) | `Análisis, crítica y Ficciones Domésticas sobre robótica doméstica. Cada semana, directo a tu correo.` | 102 |
| **Beehiiv Publication Description** | `ROBOHOGAR — Robótica doméstica de andar por casa. Análisis y Ficciones Domésticas cada semana.` | 95 |
| **CTA banner final de artículo** (standalone) | `De andar por casa. Cada semana.` | 31 |
| **Bio social compacta** (X, IG) | `Robótica doméstica de andar por casa · robohogar.com` | 52 |
| **Bio social larga** (LinkedIn) | `ROBOHOGAR — Robótica doméstica de andar por casa. Análisis y Ficciones Domésticas cada semana.` | 95 |
| **Welcome email opening** | `Soy Rafael, y esto es ROBOHOGAR — robótica doméstica de andar por casa.` | 71 |

### Decisiones cerradas (no dudar al rellenar)

- **"Ficciones Domésticas"** siempre en mayúscula (es nombre propio de la serie).
- **"de andar por casa"** en minúscula dentro de la tagline (locución, no nombre propio).
- **Subtítulo hero: punto intermedio sí, punto final NO**. `Análisis y Ficciones Domésticas. Cada semana` (sin punto tras "semana"). Convención de hero editorial contemporáneo (Apple, Stripe, Morning Brew, Axios, Substack). En prosa corrida (meta description, CTA banner, bio larga) sí se ponen los dos puntos finales normales.
- **CTA banner standalone = opción A** (minimalista, eco del tagline) vs opción B (tagline entera repetida).
- **Meta title NO puede ser solo `ROBOHOGAR`** — desperdicia 40+ chars de SEO. Siempre brand + descriptor.
- **Meta description NO repite "de andar por casa"** — ya está en el title, ahí arriba sería redundante. La description aporta la 2ª capa (pilares editoriales + canal).

---

## 🟥 Beehiiv UI · pendientes manuales

### Publication & SEO

- [ ] **B1.** `Settings → Publication → Publication Description` → `ROBOHOGAR — Robótica doméstica de andar por casa. Análisis y Ficciones Domésticas cada semana.`
- [ ] **B2.** `Website Builder → Hero → Headline` → `Robótica doméstica de andar por casa` *(debería estar ya, verificar en robohogar.com)*
- [x] **B3.** `Website Builder → Hero → Subtítulo` → `Análisis y Ficciones Domésticas. Cada semana` *(ya correcto en la landing viva: punto intermedio sí, punto final no — convención hero)*
- [ ] **B4.** `Website Builder → SEO → Title tag` → `ROBOHOGAR — Robótica doméstica de andar por casa`
- [ ] **B5.** `Website Builder → SEO → Meta description` → `Análisis, crítica y Ficciones Domésticas sobre robótica doméstica. Cada semana, directo a tu correo.`
- [ ] **B6.** `Website Builder → SEO → OG title` → *idéntico a B4*
- [ ] **B7.** `Website Builder → SEO → OG description` → *idéntico a B5*

### Automations & formularios

- [ ] **B8.** `Automations → Welcome Email 1` — verificar si el cuerpo menciona la tagline vieja (*"comparativas, reviews, editoriales y relatos"* o *"Tu dosis de robótica doméstica"*). Si aparece → sustituir por `Análisis y Ficciones Domésticas. Cada semana.`
- [ ] **B9.** `Design → Website → Custom CSS` — pegar el bloque CSS que traduce *"Keep Reading" → "Sigue leyendo"* y *"Read more" → "Leer más"*. CSS completo en la conversación del 2026-04-22 (sección después del screenshot de Playwright).
- [ ] **B10.** Formulario signup del footer de la landing — trust line dice `100% gratis · Sin spam · Cancela cuando quieras`. La regla ROBOHOGAR (`rules/tangibles.md § Microcopy de conversión — trust-lines bajo CTA`) prohíbe *"Sin spam"* como promesa futura frágil. Sustituir por `Gratis · Un email por semana · Cancela cuando quieras`.

### Posts ya publicados

- [ ] **B11.** Post `/p/humanoide-maraton-pekin-record-mundial` — el CTA banner del final dice la tagline intermedia *(«Análisis, crítica y Ficciones Domésticas sobre robots en casa. Cada semana.»)*. Editar en Beehiiv: `Posts → abrir → Edit → localizar el custom HTML block del CTA final → cambiar texto a `De andar por casa. Cada semana.`. Nota: el email ya se envió al lector, este cambio solo afecta a la versión web.

---

## 🟨 Social / bios · pendientes manuales

- [ ] **S1.** X / Twitter bio → `Robótica doméstica de andar por casa · robohogar.com`
- [ ] **S2.** LinkedIn Company Description → `ROBOHOGAR — Robótica doméstica de andar por casa. Análisis y Ficciones Domésticas cada semana.`
- [ ] **S3.** Instagram bio → `Robótica doméstica de andar por casa` + link en bio
- [ ] **S4.** Directorios de newsletters donde estés listado (Substack discovery, Newsletter-ES, etc.) — usar *Bio social larga* (S2) o *Beehiiv Publication Description* (B1)

---

## ✅ Repo · ya hecho (commit `a79e9ed`)

*(Referencia — no requiere acción)*

- `.claude/rules/newsletter.md:58` — CTA banner snippet canónico
- `docs/brand-voice.md:36, 44-46` — tagline oficial + variantes cortas (title tag, meta description, bio social, welcome email)
- `docs/guia-implementacion.md:215, 296-297` — checklist Beehiiv Description + checklist hero headline/subtítulo
- `docs/website-brief.md:132-135, 183-184` — diagrama hero + brief
- `content/templates/articulo-beehiiv-master.html` — master template (todas las ocurrencias)
- `content/articulos/humanoide-maraton-pekin-record-mundial/borrador.html:156` — draft
- `content/published/2026-04-20-humanoide-maraton-pekin-record-mundial.html:156` — backup del publicado

### No tocados (intencional)

- `content/templates/estructura-templates.md:31` — changelog histórico del 2026-04-18 (registro de lo que existía, no se reescribe).
- `assets/branding/_archive/2026-04-18-cleanup-marca-oficial/landing.html` — carpeta `_archive/`, histórico versionado.

---

## Cuando esté todo hecho

1. Marca todas las casillas `[x]`.
2. Commit final opcional: `chore: cerrar pendientes rebrand tagline` con este MD movido a `utilities/_archive/2026-04-22-rebrand-tagline.md`, o bórralo directamente.
