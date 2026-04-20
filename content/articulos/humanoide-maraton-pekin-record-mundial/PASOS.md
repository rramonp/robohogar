# Artículo #8: Un humanoide bate el récord mundial de media maratón. Lo importante no es el robot — Pasos para publicar

> Artículo tipo Editorial. Rellenar una frase con la promesa concreta al lector.

## SEO (copiar a Beehiiv)

| Campo | Valor |
|-------|-------|
| **Meta title** | `Humanoide bate récord media maratón — ¿y qué?` (45 chars) |
| **Meta description** | `Unitree H1 corrió la media maratón de Pekín en 50:26, 7 min más rápido que el récord mundial humano. El dato que no entra en el titular + checklist de 5 preguntas.` (163 chars) |
| **Slug** | `humanoide-maraton-pekin-record-mundial` |
| **Tags** | `Humanoides, Opinión, Noticias` |
| **Publish to** | `Web only` (fase pre-audiencia, reserva envío hasta que haya ≥30 subs) |
| **Content Gate** | ❌ NO activar (foco SEO, artículo evergreen) |
| **Evergreen** | ❌ false — Editorial reactivo sobre récord 19-abr-2026; pierde frescura en 3-4 semanas. El dato Stanford Behavior-1K 12% sí es evergreen y se reutiliza. |

> **Evergreen** = ¿este artículo sirve para reutilizar en redes dentro de 3-6 meses cuando haya audiencia? `true` para comparativas, reviews, guías y editoriales de tesis. `false` para editoriales reactivos sobre noticia concreta (deals, lanzamientos) con fecha de caducidad.

## Hero image — elegir 1 de 3 variantes

Nueve variantes generadas (v1-v9). Todas en `assets/` como `.png` (master) + `.webp` (subir a Beehiiv):

| Variante | Concepto visual | Archivo WebP | Estado |
|---|---|---|---|
| v1 | Humanoide cruzando meta con motion blur en primer plano | `hero-humanoide-maraton-pekin-record-mundial-v1.webp` | Archivada (sin humano) |
| v2 | Humanoide agotado sentado en el bordillo tras la carrera | `hero-humanoide-maraton-pekin-record-mundial-v2.webp` | Archivada (sujeto equivocado) |
| v3 | Split composition corre vs cocina doméstica | `hero-humanoide-maraton-pekin-record-mundial-v3.webp` | Archivada (ambigua) |
| v4 | Runner bent-over + humanoide triunfal detrás + multitud + confetti | `hero-humanoide-maraton-pekin-record-mundial-v4.webp` | Archivada (neones auto-inyectados) |
| v5 | Runner sentado junto a valla + humanoide cruzando cinta + público con niños | `hero-humanoide-maraton-pekin-record-mundial-v5.webp` | Archivada (neones auto-inyectados) |
| v6 | Plano bajo: runner tumbada + humanoide triunfal + multitud con móviles + lens flare | `hero-humanoide-maraton-pekin-record-mundial-v6.webp` | Archivada (neones auto-inyectados) |
| v7 | Misma composición v6 sin móviles ni flare | `hero-humanoide-maraton-pekin-record-mundial-v7.webp` | Archivada (seguía con neones residuales) |
| v8 | Composición v6 con override anti-sign-guard + negación explícita paleta cyberpunk | `hero-humanoide-maraton-pekin-record-mundial-v8.webp` | Archivada (limpia pero sin diferencial visual vs v9) |
| **v9 · ELEGIDA** | Composición v8 + humanoide vestido como runner (camiseta, dorsal en blanco, shorts, calcetines técnicos) con pies matte-white mecánicos expuestos | `hero-humanoide-maraton-pekin-record-mundial-v9.webp` | ✅ Final |

**Hero final:** `hero-humanoide-maraton-pekin-record-mundial-v9.webp` (67 KB). Rafael la eligió por el contraste humanista del humanoide "vestido de atleta" con pies robóticos expuestos — refuerza visualmente la tesis del artículo (máquina optimizada para una sola tarea, sin ocultar su naturaleza mecánica).

**Notas de iteración para futuros heros:**
- v4-v7 salieron con neones cyberpunk por el sign-guard auto-injectable del script `/nano-banana` heredado de Neon Tentacle Bar (documentado en memoria `feedback_nano_banana_sign_guard_neon.md`).
- Override aplicado desde v8: prompt empieza con `"no empty signs in scene at all. no blank surfaces with writing."` + negación explícita de paleta neón al final.

Subir el **WebP v9** a Beehiiv como Post Thumbnail. PNG master queda en repo.

## Imágenes inline del artículo

| Archivo | Ubicación en artículo | Fuente | Peso |
|---|---|---|---|
| `figure-01-unitree-h1-carrera-pekin.jpg` | Sección "Lo que sí ha pasado en Pekín" · después del 2º párrafo | TechCentral (cobertura Reuters/France24/China Daily) · https://techcentral.co.za/wp-content/uploads/2026/04/re-running-robot-1500-800.jpg | 194 KB |
| `figure-02-behavior-1k-stanford.jpg` | Sección "El 12% que te tienen que contar" · después del párrafo de la cita textual | Stanford HAI AI Index Report 2026 · https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance | 69 KB |

## Mapa visual del artículo

```
[rellenar: diagrama ASCII del layout del artículo con H1/H2/imágenes/CTAs]
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

- [ ] [rellenar: cada precio, fecha y dato específico que pueda haber cambiado desde el research]

### 4. Crear post en Beehiiv (45-75 min)

- [ ] Duplicar post de `[rellenar: slug del artículo Beehiiv a duplicar — ej mejor-robot-asistente-ia-2026 para comparativas]` como base (mismo tipo)
- [ ] Settings:
  - [ ] **Publish to:** `Web only`
  - [ ] Meta title/description: pegar del SEO de arriba
  - [ ] Post URL: `humanoide-maraton-pekin-record-mundial`
  - [ ] Tags: `Humanoides, Opinión, Noticias`
  - [ ] Content Gate: ❌ NO activar (foco SEO, artículo evergreen)
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
- [ ] URL definitiva: `https://robohogar.com/p/humanoide-maraton-pekin-record-mundial`
- [ ] Verificar OG image en [opengraph.xyz](https://opengraph.xyz)
- [ ] Pedir a Claude: `/post-publish https://robohogar.com/p/humanoide-maraton-pekin-record-mundial`

## Fuentes del artículo

| Dato | Fuente | Cómo verificar |
|---|---|---|
| [rellenar] | [rellenar] | [rellenar] |

## Links internos (verificar antes de publicar)

- [rellenar: URLs de otros artículos del registro que se enlazan en el texto]

## Notas editoriales

- [rellenar: notas de tono, ángulo, decisiones editoriales importantes]

---

<!--
Template origen: content/templates/PASOS-template.md
Generado con: utilities/generate_pasos.py <slug>
Placeholders rellenados desde frontmatter de borrador.html + input manual de secciones específicas
-->
