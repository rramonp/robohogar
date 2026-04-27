# Update 3 publicados al canon § 5.bis YouTube-style + painterly chiaroscuro

**Generado:** 2026-04-27 (Opción B del plan Rafael).

Aplica retroactivamente el canon nuevo (display_title YouTube-style + tag_poetico + hero painterly chiaroscuro) a los 3 relatos ya publicados. Los emails YA enviados no se actualizan; el web post + OG card + landing del archive sí.

---

## ① la-objecion

**Frontmatter actualizado** ([2026-04-23-la-objecion.md](la-objecion/2026-04-23-la-objecion.md)):
- `display_title` G4 / banda D
- `tag_poetico: "Diálogos rotos"`
- `hero_paradigma: personaje-accion-imposibilidad`
- `hero-image: assets/hero-la-objecion-v9.png`

**Hero v9 nuevo** (canon § 5.bis painterly chiaroscuro):
- Local: [`la-objecion/assets/hero-la-objecion-v9.png`](la-objecion/assets/hero-la-objecion-v9.png) (1200×630)
- WebP: [`hero-la-objecion-v9.webp`](la-objecion/assets/hero-la-objecion-v9.webp) (37 KB)

**Cambios en Beehiiv → Settings → Posts → Edit `/p/la-objecion`:**

| Campo Beehiiv | Valor antes | Valor nuevo |
|---|---|---|
| **Title** | La objeción | El humanoide que activó una alarma silenciosa contra el ministro al que sirve la cena |
| **Subtitle** | (existente) | Diálogos rotos · Un humanoide doméstico descubre que el ministro al que sirve filtra un expediente OTAN. Tiene veintitrés días y una alarma silenciosa. |
| **Featured image** | hero-la-objecion-v8 | Subir `hero-la-objecion-v9.png` (1200×630) |
| **SEO title** | La objeción \| Ficciones Domésticas ROBOHOGAR | (mantener) |
| **Meta description** | (mantener actual) | (mantener) |
| **URL slug** | la-objecion | (NO TOCAR) |

> ⚠️ **No tocar el slug.** Los emails enviados, links externos y feed RSS dependen de que `https://robohogar.com/p/la-objecion` siga existiendo. Solo cambiar Title + Subtitle + Featured image.

---

## ② el-operador-nocturno

**Frontmatter actualizado** ([2026-04-19-el-operador-nocturno.md](el-operador-nocturno/2026-04-19-el-operador-nocturno.md)):
- `display_title` G2 / banda A
- `tag_poetico: "Hogar uncanny"`
- `hero_paradigma: personaje-accion-imposibilidad`
- `hero-image: assets/hero-el-operador-nocturno-v7.png`

**Hero v7 nuevo:**
- Local: [`el-operador-nocturno/assets/hero-el-operador-nocturno-v7.png`](el-operador-nocturno/assets/hero-el-operador-nocturno-v7.png) (1200×630)

**Cambios en Beehiiv → Edit `/p/el-operador-nocturno`:**

| Campo Beehiiv | Valor nuevo |
|---|---|
| **Title** | El operador en Manila que afina el ruido del robot para que el niño se despierte |
| **Subtitle** | Hogar uncanny · Madrid 2032, las tres y catorce. Un niño se levanta a beber agua. En la cocina hay alguien. No es el robot. Es el que lo pilota desde Manila — y lleva semanas calibrando el ruido para verlo despierto. |
| **Featured image** | Subir `hero-el-operador-nocturno-v7.png` |
| **URL slug** | el-operador-nocturno (NO TOCAR) |

---

## ③ el-que-viene-a-tomar-cafe

**Frontmatter actualizado** ([2026-04-19-el-que-viene-a-tomar-cafe.md](el-que-viene-a-tomar-cafe/2026-04-19-el-que-viene-a-tomar-cafe.md)):
- `display_title` G4 / banda A
- `tag_poetico: "Memorias prestadas"`
- `hero_paradigma: personaje-accion-imposibilidad`
- `hero-image: assets/hero-el-que-viene-a-tomar-cafe-v6.png`

**Hero v6 nuevo:**
- Local: [`el-que-viene-a-tomar-cafe/assets/hero-el-que-viene-a-tomar-cafe-v6.png`](el-que-viene-a-tomar-cafe/assets/hero-el-que-viene-a-tomar-cafe-v6.png) (1200×630)

**Cambios en Beehiiv → Edit `/p/el-que-viene-a-tomar-cafe`:**

| Campo Beehiiv | Valor nuevo |
|---|---|
| **Title** | La hija que cada mañana programa al humanoide para que sea el padre muerto de su madre |
| **Subtitle** | Memorias prestadas · Vallecas, 2032. Una hija cuida a su madre con demencia. Cada mañana enciende al humanoide y le pide que sea su padre muerto. Hasta que la hermana lo descubre. |
| **Featured image** | Subir `hero-el-que-viene-a-tomar-cafe-v6.png` |
| **URL slug** | el-que-viene-a-tomar-cafe (NO TOCAR) |

---

## Archive snippet — actualizado automáticamente

[`content/templates/beehiiv-archive-snippet.html`](../../templates/beehiiv-archive-snippet.html) ya tiene los 3 H3 actualizados con los nuevos display_titles. **Pendiente: re-upload del snippet completo a Beehiiv → Settings → Website → Pages → Archive → Custom HTML block**, tras subir los nuevos heros (las URLs `media.beehiiv.com/...` se generan al hacer el re-upload del featured image).

Una vez los heros estén en Beehiiv, copiar las nuevas URLs del CDN a las cards correspondientes del archive snippet.

---

## Feed RSS podcast — qué se actualiza, qué no

Decisión 2026-04-27 con Rafael: **el `<title>` corto se mantiene en el feed RSS** (Apple/Spotify/Amazon). El display_title largo va al `<itunes:subtitle>`.

| Item RSS | Campo a actualizar | Valor |
|---|---|---|
| la-objecion | `<title>` | (mantener: "La objeción") |
| la-objecion | `<itunes:subtitle>` | El humanoide que activó una alarma silenciosa contra el ministro al que sirve la cena |
| la-objecion | `<itunes:image>` | Re-subir cover podcast 1400×1400 nueva → `feed.robohogar.com/covers/la-objecion-podcast-1400x1400.jpg` |
| el-operador-nocturno | `<title>` | (mantener: "El operador nocturno") |
| el-operador-nocturno | `<itunes:subtitle>` | El operador en Manila que afina el ruido del robot para que el niño se despierte |
| el-operador-nocturno | `<itunes:image>` | Re-subir cover nueva |
| el-que-viene-a-tomar-cafe | `<title>` | (mantener: "El que viene a tomar café") |
| el-que-viene-a-tomar-cafe | `<itunes:subtitle>` | La hija que cada mañana programa al humanoide para que sea el padre muerto de su madre |
| el-que-viene-a-tomar-cafe | `<itunes:image>` | Re-subir cover nueva |

⚠️ **NO cambiar `<guid>`.** Apple Podcasts trata el GUID como inmutable; cambiarlo crea un episodio duplicado.

Los covers podcast 1400×1400 se generaron desde los nuevos heros vía `python utilities/generate_audiobook_covers.py <slug>` cuando se hizo /audiobook-generate de cada uno. Si todavía no se hizo (la-objecion sí, los otros 2 no — solo la-objecion tiene MP3 publicado en RSS), no hay covers que actualizar. Solo aplica para la-objecion.

---

## Archivos archivados (auditoría)

Los heros viejos siguen en local versionados. No se borran porque el canon § 5 minimalista sigue existiendo como opción declarativa:

| Slug | Hero antiguo (canon § 5 minimalista, conservar) | Hero nuevo (canon § 5.bis painterly chiaroscuro) |
|---|---|---|
| la-objecion | hero-la-objecion-v8.png (Fitzcarraldo objeto-testigo) | hero-la-objecion-v9.png (humanoide butler + alarma silenciosa) |
| el-operador-nocturno | hero-el-operador-nocturno-v6.png (vaso de agua minimalista) | hero-el-operador-nocturno-v7.png (niño + humanoide + audio fragments) |
| el-que-viene-a-tomar-cafe | hero-el-que-viene-a-tomar-cafe-v5.png (taza minimalista) | hero-el-que-viene-a-tomar-cafe-v6.png (hija programando + overlay padre fantasma) |

---

## Frontispicio interior — añadir Snippet 2.5 a los 3 posts

Canon nuevo 2026-04-27 ([memoria](../../.claude/memory/feedback_ficcion_frontispicio_titulo_corto.md)): tras los snippets de audio (Snippet 2 web-only) y antes del primer H2 del cuerpo, los 3 posts llevan un Custom HTML block con el título corto del relato. Identifica la pieza como obra editorial (patrón Anagrama / Penguin Modern Classics) sin competir con el display_title largo del H1.

**Snippets listos para pegar** (Beehiiv → Edit post → posición entre Snippet 2 audio y "I. ..." → `/html` → Custom HTML block):

#### la-objecion

```html
<div style="margin: 56px 0 40px; padding: 0; text-align: center; font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <div style="color: #F5A623; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">Ficciones Domésticas</div>
  <div style="font-family: 'DM Sans', sans-serif; font-size: 32px; font-weight: 700; color: #0C0C0C; line-height: 1.15; margin: 0; letter-spacing: -0.3px;">La objeción</div>
  <div style="display: inline-block; width: 36px; height: 2px; background: #F5A623; margin: 18px auto 0;"></div>
</div>
```

#### el-operador-nocturno

```html
<div style="margin: 56px 0 40px; padding: 0; text-align: center; font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <div style="color: #F5A623; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">Ficciones Domésticas</div>
  <div style="font-family: 'DM Sans', sans-serif; font-size: 32px; font-weight: 700; color: #0C0C0C; line-height: 1.15; margin: 0; letter-spacing: -0.3px;">El operador nocturno</div>
  <div style="display: inline-block; width: 36px; height: 2px; background: #F5A623; margin: 18px auto 0;"></div>
</div>
```

#### el-que-viene-a-tomar-cafe

```html
<div style="margin: 56px 0 40px; padding: 0; text-align: center; font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <div style="color: #F5A623; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">Ficciones Domésticas</div>
  <div style="font-family: 'DM Sans', sans-serif; font-size: 32px; font-weight: 700; color: #0C0C0C; line-height: 1.15; margin: 0; letter-spacing: -0.3px;">El que viene a tomar café</div>
  <div style="display: inline-block; width: 36px; height: 2px; background: #F5A623; margin: 18px auto 0;"></div>
</div>
```

---

## Checklist Beehiiv update (Rafael)

- [ ] la-objecion: editar post → cambiar Title + Subtitle + Featured image + insertar frontispicio (Snippet 2.5) entre audio y cuerpo + Save
- [ ] el-operador-nocturno: editar post → cambiar Title + Subtitle + Featured image + insertar frontispicio (Snippet 2.5) + Save
- [ ] el-que-viene-a-tomar-cafe: editar post → cambiar Title + Subtitle + Featured image + insertar frontispicio (Snippet 2.5) + Save
- [ ] Archive snippet: copiar URLs CDN nuevas de los 3 heros al archive snippet local + re-pegar en Beehiiv → Settings → Website → Pages → Archive
- [ ] (Solo la-objecion) Feed RSS: re-subir cover podcast 1400×1400 nueva + actualizar `<itunes:subtitle>` + `<itunes:image>` del item
- [ ] Verificar a las 24h en Apple Podcasts que el cover refresca (Spotify/Amazon casi instant)
