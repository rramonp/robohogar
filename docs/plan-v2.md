# ROBOHOGAR — Plan v2 (abril 2026)

> Basado en: investigación de mercado (abr 2026), análisis de Newsletter Operator (6 meses de artículos), comparativa Ghost vs Beehiiv vs Substack, y assets existentes en el repo.

**Dominio:** robohogar.com (comprado 2026-04-12)  
**Plataforma:** Beehiiv (**plan Scale activo desde 2026-04-18** — automations, segmentación, welcome flows, digital products)  
**Dedicación:** 3-5 horas/semana  
**Objetivo año 1:** 1.000 suscriptores orgánicos  

---

## 1. Posicionamiento y nicho

### El problema del nicho amplio

"Robótica doméstica" abarca desde aspiradores Roborock hasta humanoides de Tesla. Intentar cubrir todo diluye la identidad y compite con Xataka/Computerhoy que ya cubren gadgets del hogar en español.

### El problema del nicho ultra-estrecho

"Solo robots humanoides" no tiene mercado de consumo todavía. No hay productos a la venta, no hay keywords de compra, no hay afiliación posible. El contenido sería 100% especulativo.

### Solución: posicionamiento en capas 70/30

**Identidad:** ROBOHOGAR es el medio en español sobre los robots que llegan (y llegarán) a tu casa.

**70% contenido práctico monetizable (paga las facturas)**
- Reviews y comparativas de robots que la gente YA compra: aspiradores, friegasuelos, cortacéspedes, robots de cocina, robots de piscina
- Guías de compra con links de afiliado Amazon
- Tutoriales de configuración y mantenimiento
- Keywords SEO de compra: "mejor robot aspirador 2026", "Roborock vs Dreame", "robot cortacésped barato"

**30% contenido editorial diferenciador (construye la marca)**
- Avances en robots humanoides: Figure, Tesla Optimus, Unitree, 1X Neo, Xiaomi CyberOne
- Opinión propia sobre el futuro del hogar robotizado
- Entrevistas/análisis cuando se anuncien productos nuevos
- Filosofía: ¿qué significa convivir con robots?

**Por qué funciona:** El 70% genera tráfico SEO orgánico y revenue desde el día 1. El 30% es lo que hace que la gente se SUSCRIBA — nadie se suscribe a "otro review de aspiradores", pero sí a "la perspectiva de alguien que piensa en el hogar del futuro con robots".

### Pilar experimental — Ficciones Domésticas (~10% del mix)

Dentro del 30% editorial reservamos ~10% del mix total (1 cada 3-4 semanas) a **relatos cortos de ciencia ficción doméstica** (2030-2040) con personajes recurrentes. No es decoración: el relato funciona como **producto editorial diferencial** que NO pueden copiar ni Xataka ni Wirecutter. Skill dedicado `/ficcion-draft`. Reglas en [editorial.md § Narrativa especulativa](../.claude/rules/editorial.md). Cuando se active paid tier (F3), la ficción serializada completa queda disponible como producto coleccionable para paid subscribers (ver §11).

---

## 2. Plataforma: Beehiiv

### Setup inicial (30 min)

1. Crear cuenta en beehiiv.com (plan gratuito)
2. Conectar dominio robohogar.com (DNS: CNAME según instrucciones de Beehiiv)
3. Subir branding: **monograma R** (`assets/branding/master/robohogar-logo-monogram-v11.png`) como logo editorial principal (landing, avatar, OG, favicon). La mascota (`assets/branding/master/robohogar-mascot-*.png`) queda para emails, social cards, CTAs cercanos y 404 — ver [design.md](../.claude/rules/design.md)
4. Configurar colores del design system: ámbar `#F5A623`, negro `#0C0C0C`, blanco `#FFFFFF`
5. Montar landing page con AI website builder usando `docs/website-brief.md` como guía de contenido

### Landing page

**NO construir landing page custom en HTML.** Usar el AI website builder de Beehiiv que genera responsive automático. El `assets/landing.html` del repo pasa a ser referencia visual (colores, estructura, copy) — no deliverable.

Elementos de la landing (del website-brief.md):
- Hero: headline con beneficio + frecuencia + formulario 1 campo
- Preview de contenido real (1-2 issues de ejemplo)
- Sobre mí: entusiasta que prueba robots en casa
- FAQ: 3-5 preguntas (frecuencia, spam, quién soy)
- CTA final: repetir formulario de suscripción

### Configuración de email

- Welcome email con presentación + link al mejor artículo
- Reminder email (4-6h después): "¿Recibiste todo bien?" + pregunta soft para generar replies
- Email gating activado en artículos-lead-magnet

---

## 3. Contenido: estructura y cadencia

### Frecuencia

**Semanal.** Un newsletter cada semana. Razones:
- Pipeline automatizado (research-digest + content-draft + social-content) reduce la carga manual
- Mayor frecuencia = más puntos de contacto = crece más rápido
- Consistencia semanal construye hábito en el lector

### Estructura del newsletter

Cada issue sigue un formato fijo (framework "Numbered Completeness" de Newsletter Operator):

```
🤖 ROBOHOGAR #XX — [Título del issue]

1. LA NOTICIA — La novedad más relevante de la semana en robótica doméstica
2. EN PRUEBA — Review o experiencia propia con un robot (cuando aplique)
3. EL FUTURO — Un avance en humanoides o robótica avanzada + opinión
4. DATO CURIOSO — Estadística, dato histórico, o curiosidad sobre robots
5. ENLACE DE LA SEMANA — El mejor artículo/vídeo que he leído

[CTA de afiliado o recomendación natural cuando encaje]
```

### Contenido base antes del lanzamiento (3 artículos evergreen)

Publicar en Beehiiv como web posts (indexables por Google) ANTES de anunciar la newsletter:

1. **"¿Qué robot aspirador me compro en 2026? Guía sin rodeos"** — Comparativa honest, 3-4 modelos, links afiliado Amazon. Keyword principal: "mejor robot aspirador 2026"
2. **"Los 5 robots humanoides que llegarán a tu casa antes de 2030"** — Figure, Optimus, Unitree, 1X, Xiaomi. Contenido editorial. Keyword: "robots humanoides para casa"
3. **"Así es convivir con un robot: mi experiencia real"** — Artículo personal sobre robots que ya usas en casa. Autenticidad > autoridad.

### Lead magnets (estrategia "lazy lead magnets" de Newsletter Operator)

Cada newsletter publicada puede convertirse en lead magnet con email gating en Beehiiv. No crear lead magnets dedicados — reutilizar el mejor contenido ya publicado.

Primer lead magnet: **"Guía de compra: Robot aspirador en 5 preguntas"** — versión condensada del artículo 1, con email gate.

Testear un lead magnet nuevo cada mes. Los que no funcionan se abren como contenido libre. Los que funcionan se mantienen gated.

---

## 4. Automatización de contenido

### Pipeline de skills Claude Code

Pipeline actual de ROBOHOGAR (ver tabla completa en [CLAUDE.md § Skills del pipeline](../CLAUDE.md)):

1. **`/research-digest`** — agrega RSS + Firecrawl, categoriza con Claude, genera digest en `content/drafts/research-digest-YYYY-MM-DD.md`. Rafael lo invoca semanalmente o cuando quiera refrescar el backlog.
2. **Revisión manual** (15 min): Rafael selecciona temas del digest o del backlog.
3. **`/content-draft <tema>`** — genera borrador HTML + PASOS.md + 3 hero variants en `content/articulos/<slug>/` + imágenes inline si proceden.
4. **`/nano-banana`** — invocado por content-draft para heros y social cards (manual para branding puntual).
5. **Edición y voz propia** (30-45 min): Rafael edita el borrador, añade opinión personal, humor, experiencia.
6. **Publicación en Beehiiv**: copiar el HTML final, programar envío.
7. **`/post-publish <URL>`** — limpieza post-publicación (14 pasos): backup a `content/published/`, registro, llms.txt, commit.
8. **`/social-content <URL>`** — invocado por post-publish paso 11. Posts LinkedIn/X/IG/WhatsApp listos para Buffer.
9. **`/obsidian-robohogar`** — invocado por post-publish paso 12. Sync del vault (guía, registro, wiki, calendario, plan).

### Automatización de redes sociales

De cada newsletter publicado, extraer:
- 1 Reel/Short de Instagram (15-30s, texto animado sobre la noticia principal)
- 1 post de LinkedIn (resumen + CTA a suscribirse)
- 1 hilo de X/Twitter (3-5 tweets con el contenido del issue)

**Herramientas:** Canva para Reels (templates reutilizables con la mascota), programación con Buffer (free plan).

### Automatización de SEO

Cada artículo publicado en Beehiiv se indexa automáticamente. Adicionalmente:
- Configurar Google Search Console para robohogar.com
- Monitorizar keywords con Google Search Console (gratis) — no necesitas herramientas de pago al principio
- Los artículos evergreen (reviews, comparativas) se actualizan cada 6 meses con nuevos modelos/precios. **Primer ciclo completo de refresh: a partir de 2026-10-18** (6 meses desde arranque real del proyecto) — cuando leas esa fecha o posterior, revisar backlog de artículos evergreen marcados con `evergreen_note` en `content/registro-articulos.md` y priorizar los que tengan fecha de revisión vencida.

---

## 5. Crecimiento (basado en Newsletter Operator)

### Fase 1: 0 → 100 subs (mes 1-2)

**Objetivo:** Validar que hay interés real.

- Publicar 3 artículos evergreen antes del "lanzamiento"
- Compartir en círculos cercanos (WhatsApp, LinkedIn personal)
- 1 post de LinkedIn por semana sobre robótica doméstica (S-Tier según Newsletter Operator para B2B/prosumer)
- Activar email gating en el artículo más práctico (guía de compra)

### Fase 2: 100 → 500 subs (mes 3-6)

**Objetivo:** Establecer cadencia y empezar a generar tráfico orgánico.

- Newsletter semanal sin fallar
- Instagram Reels 2-3x/semana (S-Tier para cualquier nicho): clips de robots, unboxings, demos cortas. Usar las 11 poses de la mascota como identidad visual.
- SEO: los artículos de reviews empiezan a posicionar en Google (3-6 meses para resultados)
- Lead magnets: testear 1 nuevo por mes (lazy lead magnets — reutilizar newsletters)
- Cross-promotions con 2-3 newsletters de tecnología en español (Zetatesters, Rastreator tech, etc.)

### Fase 3: 500 → 1.000 subs (mes 6-12)

**Objetivo:** Alcanzar masa crítica para monetización inicial.

- Mantener cadencia + calidad
- YouTube: 1 vídeo quincenal (B-roll sin cámara + voz en off). Cada vídeo tiene un lead magnet custom en la descripción.
- ManyChat para Instagram: "comment to get" giveaways (meta actual según Newsletter Operator)
- Evaluar primeros sponsors directos cuando el tráfico supere 3.000 visitas/mes

### Canales descartados (basado en datos reales de Newsletter Operator)

- **Paid recommendations / Boosts:** Matt McGarry confirma con datos propios: "Not a single subscriber from boosts bought anything." Solo sirven para inflar números, no para revenue. No usar.
- **TikTok:** Difícil convertir a email, no puedes DM a followers. Instagram Reels es mejor.
- **X/Twitter:** Era S-Tier, ahora C-Tier. Algoritmo penaliza links. Bajo alcance orgánico. Si ya tienes presencia OK, pero no invertir como canal primario.
- **Referral programs:** Solo funcionan con audiencias muy grandes y contenido muy compartible. Prematuro para <1.000 subs.

---

## 6. Monetización

### Principio rector: The Overlap Effect

(Newsletter Operator, marzo 2026)

Los productos de una sola categoría están muriendo. La IA commoditiza el contenido puro. Para sobrevivir hay que combinar: Content + Implementation + Community + Experience. Para Robohogar:

| Categoría | Qué es para Robohogar | Cuándo |
|---|---|---|
| Content | Newsletter semanal + artículos SEO | Desde día 1 |
| Implementation | Guías de compra comparativas, calculadoras de precio, templates de configuración | Desde día 1 (como lead magnets) |
| Community | Canal de WhatsApp/Telegram de early adopters de robots en España | Cuando haya 300+ subs |
| Experience | — (futuro: meetups, unboxing events) | Cuando haya 2.000+ subs |

### Revenue streams por fase

**Fase 1 (0-500 subs): Afiliación Amazon — €0-100/mes**
- Links de afiliado en cada review y guía de compra
- Un solo review bien posicionado de un robot de 400-800€ puede generar más que meses de sponsorship
- Alta conversión porque el contenido está en el punto exacto de decisión de compra
- Coste: €0

**Fase 2 (500-2.500 subs): Sponsors directos — €200-500/mes**
- Sponsors de nicho: marcas de robots (Roborock, Dreame, Ecovacs), tiendas de domótica
- Media kit en Beehiiv (página custom, como hace Newsletter Operator)
- Precio inicial: €50-100 por ad spot (CPM alto porque nicho tech específico)
- Beehiiv Ad Network como fallback para llenar slots no vendidos

**Fase 3 (2.500+ subs): Diversificación**
- Upgrade a Beehiiv Scale ($49/mes) para digital products y monetización avanzada
- Producto digital: "La guía definitiva de robótica doméstica 2027" — €9.99, actualizada anualmente
- Consultoría/servicio: "te configuro tu ecosistema de robots en casa" — €150/sesión
- Partnerships con marcas (no solo ads: reviews patrocinados, unboxings exclusivos)

### Lo que NO hacer (aprendido de Newsletter Operator)

- **No paywall / suscripción de pago** hasta tener 5.000+ subs muy engaged. El contenido es el motor de crecimiento — bloquearlo prematuramente mata el SEO y el growth.
- **No vender cursos** — la IA ha commoditizado el contenido educativo. Un curso de €47 sobre robots no tiene futuro. Mejor templates y herramientas (Implementation > Content).
- **No depender de Boosts** para revenue. Es co-reg, baja calidad, y genera suscriptores que no compran nada.

---

## 7. Assets existentes (listos para usar)

| Asset | Path | Estado |
|---|---|---|
| **Monograma R** (logo editorial, marca principal) | `assets/branding/master/robohogar-logo-monogram-v11.png/jpg` | ✅ Asset principal — landing hero, avatar, OG, favicon |
| Lockup horizontal + badges | `assets/branding/master/robohogar-logo-*.png` | ✅ Variantes para contextos de header/firma |
| Mascota (14+ poses, 2K) | `assets/branding/master/robohogar-mascot-*.png` | ✅ Para emails, social cards, CTAs cercanos, 404 — NO para marca editorial |
| Mascota con fondo | `assets/branding/con-fondo/` | ⚠️ Limitado — 1 archivo de referencia |
| Social cards | `assets/branding/social/` | ✅ Plantillas para redes |
| Landing HTML | `assets/landing.html` | ✅ Baseline aprobado — iteraciones sobre este archivo |
| Website brief | `docs/website-brief.md` | ✅ Vigente |
| Competitive analysis | `docs/competitive-analysis.md` | ✅ Vigente |
| Design system (paleta, tipografía, reglas) | `.claude/rules/design.md` + `assets/branding/asset-catalog.md` | ✅ Vigente — fuente de verdad |

---

## 8. Roadmap accionable

### Semana 1 (ahora)
- [ ] Crear cuenta Beehiiv (free plan)
- [ ] Conectar dominio robohogar.com
- [ ] Subir branding (mascota + colores)
- [ ] Montar landing page con AI builder
- [ ] Configurar Google Search Console
- [ ] Escribir welcome email

### Semana 2-3
- [ ] Escribir y publicar artículo 1: guía de compra robot aspirador (SEO + afiliado)
- [ ] Escribir y publicar artículo 2: robots humanoides que llegarán a tu casa
- [ ] Configurar email gating en artículo 1 (lead magnet)
- [ ] Crear perfil Instagram @robohogar_es
- [ ] Primer post de LinkedIn anunciando el proyecto

### Semana 4
- [ ] Escribir y publicar artículo 3: experiencia personal con robots en casa
- [ ] Enviar newsletter #1 a los primeros suscriptores
- [ ] Primer Reel de Instagram (puede ser un clip de un robot + texto animado)
- [ ] Dar de alta Amazon Afiliados

### Mes 2-3
- [ ] Cadencia semanal establecida (sin fallar)
- [ ] 2-3 Reels/semana en Instagram
- [ ] 1 post/semana en LinkedIn
- [ ] Testear primer lead magnet adicional
- [ ] Activar reminder email automation (4-6h después del signup)

### Mes 4-6
- [ ] Evaluar SEO: ¿están posicionando los artículos?
- [ ] Evaluar: ¿cuántos subs? Si <100, revisar discovery content
- [ ] Empezar YouTube (B-roll + voz, quincenal o semanal según capacidad)
- [ ] Buscar 2-3 cross-promotions con newsletters tech en español
- [ ] Primer intento de sponsor directo si >500 subs

---

## 9. Métricas de éxito

| Métrica | Objetivo mes 3 | Objetivo mes 6 | Objetivo mes 12 |
|---|---|---|---|
| Suscriptores | 100 | 300 | 1.000 |
| Open rate | >50% | >50% | >45% |
| Click-through rate | >10% | >8% | >6% |
| Revenue mensual | €0 | €50 (afiliado) | €200+ (afiliado + sponsor) |
| Artículos publicados | 6 | 12 | 24 |
| Instagram followers | 100 | 500 | 1.500 |

**Criterio de abandono:** Si después de 6 meses con cadencia consistente (24 newsletters sin fallar) hay menos de 100 suscriptores, el nicho no funciona en español y hay que pivotar o abandonar.

---

*Documento vivo. Actualizar después de cada milestone.*
*Fuentes: Newsletter Operator (últimos 6 meses), análisis Ghost vs Beehiiv (abr 2026), website-brief.md, Write With AI (Cole/Bush, 6-step checklist 2026 y Lead Generating Library 2024).*
*Changelog: auditoría 18-abr-2026 — monograma como marca principal, pipeline de skills actualizado, pilar Ficciones Domésticas añadido (§1 y §3), sección §11 sobre paid newsletter blueprint 2026.*

---

## 10. Growth tactics Fase 2-3 (aprendidos de Write With AI)

> Adaptación de las 5 palancas $400K ARR de Cole/Bush al contexto ROBOHOGAR/Beehiiv/hobby. Detalle y tabla priorizada → [`../references/writewithai/03-growth-playbook.md`](../references/writewithai/03-growth-playbook.md).
>
> **Decisión operativa:** todas son F2-F3. En F1 (≤500 subs) la prioridad sigue siendo consistencia + SEO + afiliados. Estas cinco se activan cuando la cadencia está sólida y hay >500 subs engaged.

### 10.1 Digital product drops trimestrales (F2-F3)

**Cole:** un producto digital cada trimestre (~$100K/drop). **ROBOHOGAR:** pieza "de peso" trimestral, no necesariamente de pago hasta F3.

Productos que encajan con audiencia robótica doméstica ES:
- **Q1/Q3 — Guía de compra estacional** (primavera: cortacésped + aspirador; otoño: regalo navideño). PDF 30-40 pág.
- **Q2 — Calculadora de ROI** (interactiva: superficie + horas + precio → break-even en meses).
- **Q4 — Almanaque ROBOHOGAR** (resumen anual + previsiones). Diferencial editorial, vocación evergreen.

| Fase | Modelo | Esfuerzo | ROI esperado | Dependencias |
|---|---|---|---|---|
| F2 (500-5K subs) | Gratis, lead magnet con content gating | 15-20h/drop | Crecimiento lista +20-30%/drop | Plantilla Canva/Figma fija |
| F3 (5K+) | Pago 14,90-24,90 € (PDF premium) | 25-30h/drop | Primer revenue de producto propio | Beehiiv Scale + Stripe |

### 10.2 Founding Member tier — Beehiiv paid tier (F3)

**Cole:** 10% de lista paga acceso premium. **ROBOHOGAR [F3]:** suscripción **ROBOHOGAR+** con:
- Acceso anticipado a reviews (72h antes).
- Comparativas en profundidad con tablas extendidas y datos de prueba propia.
- Recopilatorio mensual de ofertas afiliados con descuentos exclusivos negociados con marcas.
- Canal Discord/WhatsApp privado (<100 miembros → "Founding" con precio bajo de por vida).

| Target | Esfuerzo | ROI esperado | Dependencias |
|---|---|---|---|
| 3-5% conversión (150-250 pagos con 5K subs) | Medio (4h/mes mantenimiento + 6h setup) | 1.500-5.000 €/año | Beehiiv Scale (49$/mes), 5K+ subs engaged, 6 meses mínimo de track record |

**Descarta F2:** empujar paid antes de 5.000 subs quema lista (confirmado por Newsletter Operator §6).

### 10.3 Master Content Library (F2)

**Cole:** índice centralizado de todos los posts por categoría como producto en sí. **ROBOHOGAR [F2]:** rehacer `robohogar.com/archivo` como **biblioteca navegable multi-eje**:

Ejes de filtrado:
- **Categoría:** aspiradores · cortacésped · humanoides · robot cocina · robot piscina · smart home.
- **Nivel de precio:** <300 € · 300-600 € · 600-1.000 € · >1.000 €.
- **Tipo de hogar:** piso <70 m² · piso >70 m² · casa con jardín · con mascotas · con niños.
- **Tipo de contenido:** review · comparativa · guía · editorial · tutorial.

Cada post tagueado en Beehiiv. SEO orgánico masivo + utilidad de navegación.

| Fase | Esfuerzo | ROI esperado | Dependencias |
|---|---|---|---|
| F2 (30-50 artículos publicados) | Alto setup (10-12h) + bajo mantenimiento | Tráfico SEO +40-60% (long-tail), conversión visitante→sub +2-3x | 30+ artículos publicados, tags Beehiiv definidos, página custom HTML (Beehiiv lo permite en free) |

### 10.4 Welcome email + survey + gift + upsell (F1→F2)

**Cole:** secuencia automática 5-7 emails → encuesta → regalo → upsell. **ROBOHOGAR:** descrito en detalle en [`../references/newsletter/email-marketing-playbook.md#12-welcome-sequence-4-5-emails-colebush-beehiiv`](../references/newsletter/email-marketing-playbook.md) §12 y §15.

**Ruta por fase:**
- **F1 (ahora):** welcome email + reminder (lo que Beehiiv free permite) + Emails 2-5 como broadcasts manuales segmentados a subs de <2 semanas.
- **F2 (Beehiiv Scale):** automation nativa de 5 emails + poll Beehiiv como survey + PDF gated como gift.
- **F3:** añadir upsell real al paid tier (§10.2).

| Fase | Esfuerzo | ROI esperado | Dependencias |
|---|---|---|---|
| F1 (broadcasts manuales) | 4-5h setup inicial + 30 min/mes | Open rate welcome >50%, +15% retención 30d | Nada — disponible ya |
| F2 (automation) | 2h migración | +10% retención adicional, +30% replies | Upgrade Beehiiv Scale (49$/mes) |

### 10.5 Distribución en redes — LinkedIn + Instagram Reels (F2)

**Cole:** Substack Notes para atraer lectores cross-newsletter. **ROBOHOGAR:** Substack Notes no aplica (estamos en Beehiiv). Mapping:

| Canal Cole | Equivalente ROBOHOGAR | Por qué |
|---|---|---|
| Substack Notes (orgánico) | **Instagram Reels** (15-30s) | S-Tier 2026 según Newsletter Operator. Audiencia 30-55 ES vive en IG, no en X |
| Substack cross-recomm. | **Beehiiv Boosts / Cross-Recommendations** | Activar solo cuando >5.000 subs (somos atractivos para otros newsletters tech ES) |
| LinkedIn thought-leader | **LinkedIn personal Rafael** | 1 post/semana, angle "padre techie que investiga robots", no corporate |
| — | **YouTube quincenal (F3)** | B-roll sin cámara + voz; lead magnet custom por vídeo |

**Descartes explícitos:**
- **TikTok:** difícil conversión a email, sin DM a followers. Reels gana.
- **X/Twitter:** pasó de S-Tier a C-Tier, algoritmo penaliza links. Mantener solo si ya hay presencia.
- **Paid recommendations / Boosts comprados:** Matt McGarry confirma "not a single subscriber from boosts bought anything". Inflan números sin revenue.

| Fase | Esfuerzo | ROI esperado | Dependencias |
|---|---|---|---|
| F2 (500-5K subs) | Medio (3-4h/semana para Reels + LinkedIn + IG feed) | +30-50% growth sub, awareness de marca | Canva templates con mascota, Buffer free plan |
| F3 (5K+) | Alto (6-8h/semana añadiendo YouTube) | Consolidación multi-canal, primer tráfico directo significativo | YouTube setup + 1 vídeo quincenal sostenible |

<!-- added by wwai-integration 2026-04-17 -->

---

## 11. Paid newsletter blueprint 2026 (Cole/Bush) — diferido a F3

> Destilado del post *My 6-step checklist to build a $100,000+ paid newsletter in 2026* (Cole + Bush, 4-mar-2026). Referencia completa con prompts y adaptación Beehiiv: [`references/writewithai/08-paid-newsletter-blueprint-2026.md`](../references/writewithai/08-paid-newsletter-blueprint-2026.md).
>
> **Cuándo activar:** cuando ROBOHOGAR supere 5.000 subs engaged + 6 meses de track record sostenido + upgrade a Beehiiv Scale ($49/mes). Con 0 subs hoy, este bloque es *knowledge documentado*, no roadmap a 12 meses.

### 11.1 Cadencia dual 1-free + 1-paid

Cuando se active ROBOHOGAR+, reorganizar la cadencia semanal:

| Día | Tipo | Contenido | Audiencia |
|---|---|---|---|
| Martes 9:00 | Gratis (Email and web) | Análisis de la semana + review abierto + hook al paid | Toda la lista |
| Viernes 9:00 | Paid (paywall) | Deep-dive + tangible coleccionable + comparativa premium o episodio de ficción serializada | ROBOHOGAR+ |

Cálculo de tiempo: dobla de 3-5h a 6-10h/semana. Activar solo si Rafael puede sostenerlo o si el revenue ya cubre outsourcing parcial del post-publish.

### 11.2 Tangible = producto, no bonus

Cada artículo (gratis y paid) se diseña con el tangible como **el cliffhanger**: la promesa concreta que justifica la lectura (checklist compra, tabla comparativa, decision tree, dossier 3-datos, heat map de precios de la semana). El copy lleva hasta el tangible — no al revés. Detalle en [`.claude/rules/tangibles.md`](../.claude/rules/tangibles.md). Aplicable desde **F1**, aunque el skill `/pdf-brand` siga pendiente: basta con una tabla inline o un bloque "Descarga" al final.

### 11.3 Paywall patterns (cuando exista paid tier)

- **Paywall preview 20-50%:** toda la free list ve el inicio del post paid. Recordatorio constante sin excluir. Beehiiv Scale soporta esta función nativamente.
- **Paywall at cliffhanger:** el corte ocurre JUSTO antes de entregar el tangible (*"Aquí tienes la tabla comparativa con los 7 modelos y el que compramos nosotros: [PAYWALL]"*). Cole atribuye a este patrón el 90% del crecimiento de Write With AI.

### 11.4 Qué entra en el paid tier ROBOHOGAR+

- **Ficción serializada completa** (Ficciones Domésticas) — las mini-series se entregan por episodios solo a paid. Acaba convirtiéndose en producto coleccionable (e-book, bundle).
- **Evergreen reviews actualizables** — reviews con "lifetime updates" cada 6 meses. El paid asegura seguir recibiendo la versión al día cuando cambien precios o modelos.
- **Comparativas premium** — tabla extendida con datos de testing propio de Rafael, no solo specs de fabricante.
- **Canal Discord/WhatsApp privado** — comunidad founding member cuando haya 100+ pagos (F3 avanzado).
- **Acceso anticipado 72h** — reviews y comparativas salen primero a paid, luego abren a gratis.

### 11.5 Qué descartamos del post original

- **Substack Notes (Paso 6 original):** no aplica — estamos en Beehiiv. El equivalente ya está cubierto por `/social-content` (LinkedIn + X + IG + WhatsApp).
- **Benchmarks $400K ARR de Cole:** son de una audiencia Ship 30 alumni preexistente. Para ROBOHOGAR el target F3 realista son 3-5% de 5K subs = 150-250 pagos (ver §10.2 Founding tier).
