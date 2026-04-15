# Artículo 1: Humanoides en casa — Pasos para publicar

## SEO (copiar a Beehiiv)

| Campo | Valor |
|-------|-------|
| **Meta title** | `Humanoides en casa 2026 — ¿Cuánto falta de verdad?` (50 chars) |
| **Meta description** | `Ya puedes comprar un robot humanoide por el precio de un coche usado. El problema: no sabe limpiar tu baño. Investigamos todos los de 2026.` (139 chars) |
| **Slug** | `humanoides-en-casa-cuanto-falta` |
| **Tags** | `Humanoides`, `Opinión` |
| **Publish to** | `Web only` (no email — es artículo web, no newsletter) |

## Hero image elegida

`assets/hero-humanoides-v10.webp` (31 KB) — "Creación de Adán" robot/humano en cocina.

El PNG master está en `assets/hero-humanoides-v10.png` (1.220 KB). Subir el **WebP** a Beehiiv como thumbnail.

## Pasos

### 1. Crear template Editorial en Beehiiv

- [ ] Abrir el artículo de comparativa existente en Beehiiv (Design Mode)
- [ ] Duplicarlo como nuevo template o crear un post nuevo basándote en él
- [ ] Eliminar las secciones de producto (tabla comparativa, pros/contras, precios)
- [ ] Dejar: header, intro callout ámbar, separadores, CTA mid-article, footer CTA, sección "Sabías que"
- [ ] Adaptar las secciones a formato narrativo: H2 + párrafos de opinión (sin H3 de producto)

### 2. Copiar contenido del borrador HTML

- [ ] Abrir `borrador.html` en el navegador (doble clic) para ver el contenido
- [ ] Copiar sección por sección al template de Beehiiv:
  - Intro (callout ámbar): "He investigado a fondo..."
  - H2: La carrera que nadie esperaba
  - H2: Los que más ruido hacen (con H3: Tesla, Figure, Atlas, Xpeng)
  - CTA mid-article: "¿Te está sirviendo?"
  - H2: El que ya puedes comprar (con truco) (H3: 1X NEO, Unitree G1)
  - H2: Lo que las demos no te cuentan (H3: teleoperación, tareas, desorden)
  - H2: Mi veredicto (callout ámbar con opinión)
  - H2: Sabías que (dato CNN)
  - Footer CTA

### 3. Editar con tu voz

- [ ] Añadir opiniones personales, humor, anécdotas tuyas donde encajen
- [ ] Revisar que suena a ROBOHOGAR, no a informe técnico
- [ ] Verificar que cada sección tiene posición clara (editorial = opinión obligatoria)

### 4. Imágenes

- [ ] Subir `hero-humanoides-v10.webp` como Post Thumbnail en Beehiiv
- [ ] Activar "Show thumbnail on top"
- [ ] Imágenes inline (dentro del artículo): buscar fotos de los robots reales (Tesla Optimus, Figure 03, 1X NEO, Unitree G1) de fuentes oficiales/prensa

### 5. Configurar en Beehiiv

- [ ] Settings → Meta title → pegar del SEO de arriba
- [ ] Settings → Meta description → pegar del SEO de arriba
- [ ] Settings → Post URL → `humanoides-en-casa-cuanto-falta`
- [ ] Settings → Advanced email capture → `Content Gate`
- [ ] Settings → Comments → Activados

### 6. Verificar

- [ ] Preview en móvil (icono 📱 en Design Mode)
- [ ] Enviar test email a tu email personal
- [ ] Verificar OG image en opengraph.xyz tras publicar
- [ ] Comprobar que el WebP carga rápido en la preview

### 7. Post-publicación (pedir a Claude Code)

- [ ] `/social-content` — genera posts para LinkedIn, X, Instagram, WhatsApp
- [ ] `/nano-banana` — ya hecho (v10 elegida)
- [ ] Actualizar Welcome Email si quieres añadir este artículo como enlace
- [ ] Sync a Obsidian: `/obsidian-robohogar sync-published`
- [ ] Mover borrador a `content/published/`
- [ ] Commit

## Fuentes del artículo

Los datos vienen de research verificado (abril 2026). Fuentes principales:

- Tesla Optimus: Washington Post, Teslarati
- Figure 03: Figure AI (oficial), BMW partnership
- 1X NEO teleoperado: Wall Street Journal, Fortune
- Unitree G1 precio: Unitree Shop (oficial)
- Boston Dynamics Atlas: Engadget, Robotics 24/7
- Xpeng Iron faceplant: Futurism, Fox News
- Dato CNN (gente grabándose): CNN abril 2026
- Estudio elderly care: Stanford Report abril 2026

Todos los links están en el HTML del borrador y en `references/fuentes-por-categoria.md`.
