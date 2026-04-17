# Artículo #{ARTICULO_NUM}: {TITULO} — Pasos para publicar

> {SUBTITULO_O_PROMESA}

## SEO (copiar a Beehiiv)

| Campo | Valor |
|-------|-------|
| **Meta title** | `{META_TITLE}` ({META_TITLE_CHARS} chars) |
| **Meta description** | `{META_DESCRIPTION}` ({META_DESC_CHARS} chars) |
| **Slug** | `{SLUG}` |
| **Tags** | {TAGS} |
| **Publish to** | `{PUBLISH_TO}` {PUBLISH_NOTE} |
| **Content Gate** | {CONTENT_GATE} |
| **Evergreen** | {EVERGREEN} — {EVERGREEN_NOTE} |

> **Evergreen** = ¿este artículo sirve para reutilizar en redes dentro de 3-6 meses cuando haya audiencia? `true` para comparativas, reviews, guías y editoriales de tesis. `false` para editoriales reactivos sobre noticia concreta (deals, lanzamientos) con fecha de caducidad.

## Hero image — elegir 1 de 3 variantes

Las tres están en `assets/` como `.png` (master) + `.webp` (subir a Beehiiv):

| Variante | Concepto visual | Archivo WebP |
|---|---|---|
| **v1** | {HERO_V1_CONCEPTO} | `hero-{SLUG}-v1.webp` |
| **v2** | {HERO_V2_CONCEPTO} | `hero-{SLUG}-v2.webp` |
| **v3** | {HERO_V3_CONCEPTO} | `hero-{SLUG}-v3.webp` |

**Recomendación del agente:** {HERO_RECOMENDACION}

Subir el **WebP** elegido a Beehiiv como Post Thumbnail. PNG master queda en repo.

## Imágenes inline del artículo

{INLINE_IMAGES_TABLE}

## Mapa visual del artículo

```
{MAPA_VISUAL_ASCII}
```

## Pasos para publicar

### 1. Preparación (15 min)

- [ ] Abrir `borrador.html` en navegador para previsualizar
- [ ] **Elegir hook** de los 3 candidatos visibles al inicio del body (bloques `class="hook-option"`) — borrar los 2 que no uses
- [ ] Elegir hero image (v1/v2/v3)

### 2. Editar voz (Rafael, 45-90 min)

- [ ] Aplicar voz plural editorial ("hemos", "os contamos") — revisar contra `docs/brand-voice.md`
- [ ] Añadir 1-2 opiniones personales / humor donde encaje
- [ ] Verificar contra `rules/editorial.md` — sin superlativos vacíos, sin "honesta" / "sin filtro"
- [ ] Headlines ≤40 chars en móvil

### 3. Validar datos específicos (15-20 min)

Confirmar que los datos concretos del artículo siguen vigentes desde el research:

{DATOS_A_VALIDAR}

### 4. Crear post en Beehiiv (45-75 min)

- [ ] Duplicar post de `{TEMPLATE_BASE_SLUG}` como base (mismo tipo)
- [ ] Settings:
  - [ ] **Publish to:** `{PUBLISH_TO}`
  - [ ] Meta title/description: pegar del SEO de arriba
  - [ ] Post URL: `{SLUG}`
  - [ ] Tags: {TAGS}
  - [ ] Content Gate: {CONTENT_GATE}
  - [ ] Comments: Activados
- [ ] Subir hero WebP + activar "Show thumbnail on top"
- [ ] Copiar contenido sección por sección
- [ ] Subir imágenes inline en sus secciones

### 5. Preview + verificar (10 min)

- [ ] Preview móvil (icono 📱 en Design Mode)
- [ ] Verificar tablas/callouts se renderizan bien a 375px
- [ ] Verificar links internos a otros artículos del registro

### 6. Publicar + post-publish

- [ ] Publish desde Beehiiv
- [ ] URL definitiva: `https://robohogar.com/p/{SLUG}`
- [ ] Verificar OG image en [opengraph.xyz](https://opengraph.xyz)
- [ ] Pedir a Claude: `/post-publish https://robohogar.com/p/{SLUG}`

## Fuentes del artículo

{FUENTES_TABLE}

## Links internos (verificar antes de publicar)

{INTERNAL_LINKS}

## Notas editoriales

{NOTAS_EDITORIALES}

---

<!--
Template origen: content/templates/PASOS-template.md
Generado con: utilities/generate_pasos.py <slug>
Placeholders rellenados desde frontmatter de borrador.html + input manual de secciones específicas
-->
