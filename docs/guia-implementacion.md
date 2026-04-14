# ROBOHOGAR — Guía de Implementación (micro-pasos)

> Cada paso es una acción concreta. Si una fase no aplica todavía, sáltala — cada FASE es autocontenida.
> Referencia estratégica: `docs/plan-v2.md` · Referencia visual: `docs/website-brief.md`

---

## Preparación: Clonar el repo (si estás en otro PC)

Si es la primera vez en este PC o no tienes el repo clonado:

```bash
cd $HOME
git clone https://github.com/rramonp/robohogar.git
cd robohogar
```

Si ya lo tienes clonado, actualiza:

```bash
cd $HOME/robohogar
git pull
```

> [!tip]
> Esta guía también está disponible en Obsidian:
> `05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md`
> Si modificas la guía en el repo, copia la versión actualizada al vault de Obsidian.

---

## FASE 0: Beehiiv Setup (30 min)

### Crear cuenta

- [x] Ir a **https://app.beehiiv.com/signup**
- [x] Rellenar: nombre → `Rafael`, email → tu email personal, contraseña
- [x] Publication Name → `ROBOHOGAR`
- [x] Description → `Tu casa se está robotizando y no te has enterado. Te lo cuento cada 2 semanas: gratis, honesto y en español.`
- [x] Category → `Technology`
- [x] Frequency → `Biweekly`

### Subir branding

- [x] Ir a **Settings → Publication → Branding**
- [x] Logo: subir `assets/branding/master/robohogar-mascot-principal.png`
- [x] Favicon: subir la misma imagen (Beehiiv la recorta)
- [x] Accent color → `#F5A623`
- [x] Background → `#FFFFFF`
- [x] Text color → `#0C0C0C`
- [x] Font: Beehiiv no permite Jost/DM Sans custom en free plan — elegir la sans-serif más limpia disponible (Inter o el default)

### Conectar dominio robohogar.com

- [x] En Beehiiv: ir a **Settings → Publication → Domains → Add Custom Domain**
- [x] Escribir `robohogar.com` y pulsar Continue
- [x] Beehiiv muestra los registros DNS necesarios — déjalos abiertos en una pestaña

**En Namecheap (https://ap.www.namecheap.com → Domain List → robohogar.com → Advanced DNS):**

> [!warning]
> Elimina PRIMERO los registros por defecto que Namecheap pone (parking records, URL redirect, etc.) antes de añadir los de Beehiiv. Si no, habrá conflictos.

Registros DNS que Beehiiv típicamente pide (los valores exactos los da Beehiiv en su panel — copia desde allí):

| # | Tipo | Host | Valor (copiar de Beehiiv) | TTL |
|---|---|---|---|---|
| 1 | CNAME | `www` | apuntando a Beehiiv CDN | Auto |
| 2 | A | `@` | IP de Beehiiv | Auto |
| 3 | CNAME | verificación 1 | valor de Beehiiv | Auto |
| 4 | CNAME | verificación 2 | valor de Beehiiv | Auto |
| 5 | TXT | `@` | verificación SPF | Auto |
| 6 | CNAME | DKIM key 1 | valor de Beehiiv | Auto |
| 7 | CNAME | DKIM key 2 | valor de Beehiiv | Auto |
| 8 | CNAME | DKIM key 3 | valor de Beehiiv | Auto |
| 9 | TXT | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:dmarc@robohogar.com` | Auto |
| 10 | MX | `mail` | valor de Beehiiv | Auto |
| 11 | TXT | `mail` | SPF para subdominio mail | Auto |
| 12 | CNAME | `mail` | valor de Beehiiv (si pide CNAME en vez de MX) | Auto |

- [x] Añadir cada registro en Namecheap: botón **Add New Record** → seleccionar tipo → pegar Host y Value
- [x] Volver a Beehiiv y pulsar **Verify Domain**
- [x] Si dice "Pending" — esperar. Propagación DNS: 15 min a 72h (normalmente <2h)

> [!tip]
> Para comprobar propagación: https://dnschecker.org — busca tu dominio y tipo de registro (CNAME, TXT, etc.)

### Configurar email sender

- [x] En Beehiiv: **Settings → Publication → Sending → Sender Email**
- [x] Configurar como `hola@robohogar.com` o `robot@robohogar.com`
- [x] Sender Name → `Rafael de ROBOHOGAR`
- [x] Reply-to → tu email personal (para recibir respuestas directas)

### DMARC

- [x] Verificar que el registro TXT `_dmarc` está activo en Namecheap (paso #9 arriba)
- [x] En Beehiiv, en la sección de Domain, debe aparecer DMARC como ✅ verificado
- [x] Si no aparece tras 24h, revisar que el Host es exactamente `_dmarc` (sin el dominio, Namecheap añade `.robohogar.com` automáticamente)

---

## FASE 1: Landing Page (1 hora)

### AI Website Builder

> [!warning] PASO CRÍTICO
> Abre `docs/website-brief.md` del repo. Ve a la sección **"Prompt para Beehiiv AI Builder"** (línea ~165). Copia el bloque de código ÍNTEGRO (70+ líneas, desde `Build a newsletter landing page...` hasta el cierre de ```). NO uses un resumen — pega TODO.

- [x] En Beehiiv: ir a **Website → AI Website Builder**
- [x] Si no ves AI Builder: ir a **Website → Design Mode** y construir manualmente siguiendo la tabla de secciones de abajo
- [x] Pegar el prompt completo (70+ líneas) del website-brief.md
- [x] Pulsar **Generate** y esperar a que se genere la página completa
- [x] **Verificar:** comparar cada sección generada con la tabla "Ajustar sección por sección" de abajo. El AI no siempre genera exacto — ajustar en Design Mode lo que falte

### Ajustar sección por sección (Design Mode)

**Hero (above the fold):**
- [x] Headline → `Tu casa se esta robotizando y no te has enterado`
- [x] Subtítulo → `Te lo cuento cada 2 semanas: Gratis, honesto y en español`
- [x] Placeholder del input → `tu@email.com`
- [x] Botón → `Suscríbete gratis` con fondo `#F5A623`, texto `#FFFFFF`
- [x] Texto bajo botón → `100% gratis · Sin spam · Cancela cuando quieras`
- [x] Imagen de la mascota principal con café

**Artículos destacados (justo bajo el hero):**
- [x] En Design Mode: añadir bloque **"Recent Posts"** o **"Featured Posts"**
- [x] Configurar para mostrar 2-3 posts con imagen + título + excerpt
- [x] Título de sección → `Lo último en ROBOHOGAR`

> [!warning]
> Esta sección estará vacía hasta que publiques los primeros artículos (FASE 2). Publica al menos 2 posts ANTES de compartir la landing públicamente.

**Qué recibirás:**
- [x] Título → `¿Qué recibirás cada 2 semanas?`
- [x] 4 bullets:
  - `🤖 Lo que ha pasado en robótica doméstica, sin tecnicismos`
  - `🔍 Reviews sin filtro de robots que ya están a la venta`
  - `🚀 Humanoides y el futuro de tu casa robotizada`
  - `💡 Un dato curioso + el mejor enlace que he encontrado`

**Sobre el autor:**
- [x] Imagen: subir `assets/branding/master/robohogar-mascot-leyendo.png` *(sección omitida — decisión editorial)*
- [x] Texto → `Soy Rafael. Pruebo robots en casa, investigo lo que viene y te cuento lo que merece la pena — sin comunicados de prensa ni hype vacío.`

**FAQ:**
- [x] Pregunta 1: `¿Con qué frecuencia llega?` *(sección omitida — decisión editorial)*
- [x] Pregunta 2: `¿Es gratis?`
- [x] Pregunta 3: `¿Quién escribe esto?`

**Footer:**
- [x] Segundo CTA: `¿Te lo vas a perder?` + formulario de email
- [x] Links a redes cuando estén creadas (FASE 5)

### Mobile testing

- [x] En Beehiiv Design Mode: usar el icono de preview móvil (📱)
- [x] Verificar: el formulario de email es visible sin scroll
- [x] Verificar: las cards de artículos se apilan verticalmente
- [x] Verificar: el texto es legible (mínimo 16px body)
- [x] Verificar: el botón CTA es fácil de pulsar con el pulgar (mínimo 44px alto)
- [x] Publicar la landing: **Website → Publish**

### Assets necesarios para la landing (generar con nano-banana)

| Asset | Archivo | Dónde se usa | Prioridad |
|---|---|---|---|
| **Hero mascota** | `hero-landing-beehiiv.png` (1200x800) | Hero section, lado derecho | P1 — sin esto la landing queda vacía |
| **OG image** | `og-image-robohogar.png` (1200x630) | Meta tag, compartir en redes | P1 — necesario antes de compartir links |
| **Favicon** | `favicon-robohogar.png` (512x512) | Pestaña del navegador | P1 — credibilidad básica |
| **About mascota** | Reutilizar `mascot-leyendo.png` del master | Sección "Sobre el autor" | Ya existe |

> [!tip]
> Generar los 3 assets P1 con `/nano-banana` ANTES de montar la landing en Beehiiv. Así al configurar solo hay que subir los archivos.

### Referencia visual: cómo se ven los mejores

| Referente | Qué copiar para la landing |
|---|---|
| **Newsletter Operator** | Hero con social proof ("50K+ founders") + email campo con borde naranja. "Featured" articles como cards justo debajo. 3 CTAs por página (hero, mid, footer). |
| **Morning Brew** | Tagline memorable ("Become smarter in 5 minutes"). Segundo CTA con mockup de móvil. Juegos como engagement (futuro). |
| **The Hustle** | Headlines GRANDES (54px). Separación clara entre "News Briefs" (corto) y "Originals" (largo). Lead magnet mid-page. |
| **TLDR** | Subscribe button después de CADA artículo (agresivo pero efectivo). Social proof "1.6M readers" prominente. Layout ultra-minimal. |
| **Milk Road** | Ticker de datos relevantes al nicho (futuro: "Últimos robots lanzados"). Pill buttons modernos. |

---

## FASE 1B: Estética del Blog (formato de artículos en Beehiiv)

El blog son los artículos publicados como web posts en Beehiiv. Es tan importante como la landing — el visitante que llega por SEO aterrizará en un artículo, NO en la landing.

### Configuración global del blog

- [x] En Beehiiv: **Website → Design → Blog Settings**
- [x] Layout de artículos: elegir layout con imagen destacada grande arriba (como The Hustle Originals)
- [x] Mostrar: autor, fecha, tiempo de lectura, categoría
- [x] Activar compartir en redes (botones share al final del artículo)
- [x] Activar comentarios (genera engagement y reply signals)

### Estética de cada artículo (basada en research)

Cada artículo publicado en Beehiiv debe seguir esta estructura visual:

```
[Imagen destacada — 1200x630, mascota + contexto temático]

CATEGORÍA · 5 min de lectura

# Título SEO optimizado (H1)

Subtítulo con hook (1-2 frases que enganchen)

---

Contenido con H2s para cada sección principal.
Párrafos cortos (3-4 líneas máx).
Listas con bullets para datos concretos.
Imágenes inline donde aporten (screenshots, comparativas).

> Callout con opinión personal o dato destacado

[CTA mid-article: "¿Te está gustando? Suscríbete para recibir esto cada 2 semanas →"]

Más contenido...

[Link de afiliado natural dentro del contexto, no banner]

---

**¿Te ha gustado?** Comparte con alguien que tenga un robot en casa.

[Botones: Compartir en Twitter · LinkedIn · WhatsApp]

---

**Más en ROBOHOGAR:**
[Card artículo relacionado 1] [Card artículo relacionado 2]
```

### Assets necesarios para artículos (generar con nano-banana)

**Templates (generar una vez):**

| Asset | Archivo | Uso | Prioridad |
|---|---|---|---|
| **Header newsletter** | `newsletter-header.png` (600x150) | Cabecera de cada email enviado | P1 |
| **Social card template** | `social-card-template.png` (1080x1080) | Compartir artículos en redes | P2 |

**Imágenes por artículo (genera el agente de imágenes automáticamente):**

Cada artículo necesita 1 imagen destacada (1200x630). El agente de imágenes (`/nano-banana`) la genera automáticamente como parte del pipeline de publicación y la cataloga en `assets/branding/asset-catalog.md`.

### Estrategia de imágenes

| Tipo | Origen | Ejemplo |
|---|---|---|
| **Imagen destacada (hero)** | Siempre branded con nano-banana | Mascota + contexto temático, estilo ROBOHOGAR |
| **Imágenes inline (dentro del artículo)** | Originales de la fuente/fabricante | Fotos de producto, screenshots, renders oficiales |

**Por qué branded para el hero:** Las cards en la landing, el OG al compartir y la preview en redes deben tener identidad visual consistente. Si cada artículo usa una foto distinta (Samsung, iRobot, stock), la landing parece un collage.

**Por qué originales inline:** Dentro del artículo el lector quiere ver el producto real, no ilustraciones. Fotos del fabricante + capturas aportan realismo y credibilidad.

> [!warning]
> Cada artículo NECESITA su imagen destacada branded (1200x630) antes de publicar. Sin imagen, las cards en la landing y las previews en redes quedan vacías y la conversión cae. El agente de imágenes se encarga de esto como paso del pipeline.

### Patrones de formato por tipo de contenido

**Review/Comparativa (70% del contenido):**
- Tabla comparativa specs al inicio
- Pros/Contras con iconos ✅/❌
- Veredicto claro: "¿Lo compraría? Sí/No y por qué"
- Link de afiliado al final de cada review individual
- Reference: Newsletter Operator usa inline CTA mid-article con lead magnet

**Editorial/Futuro (30% del contenido):**
- Hook con dato sorprendente o imagen evocadora
- Opinión personal fuerte (no hedging)
- Dato + especulación + consecuencia para el lector
- Sin links de afiliado (este contenido construye marca, no revenue)
- Reference: The Hustle "Originals" — reportajes largos con titulares creativos

**Newsletter quincenal:**
- Template fijo de 5 secciones (ver FASE 4)
- Máximo 1.500 palabras
- Email gating en el artículo web más valioso de cada issue
- Reference: TLDR — cada item es link + resumen de 2-3 líneas. Conciso.

### Categorías/Tags en Beehiiv

Configurar estas categorías para organizar el contenido:

- [x] **Aspiradores** — reviews, comparativas, guías de compra
- [x] **Cortacéspedes** — reviews, configuración, mantenimiento
- [x] **Humanoides** — noticias, análisis, opinión
- [x] **Asistentes IA** — robots de escritorio, compañeros IA
- [x] **Robot Mascotas** — robot pets, compañeros emocionales
- [x] **Smart Home** — domótica, integración, ecosistemas
- [x] **Noticias** — última hora, lanzamientos
- [x] **Guías** — tutoriales, configuración, troubleshooting
- [x] **Opinión** — editoriales, futuro, debate

> [!tip]
> Cada artículo web post = 1 categoría + 2-3 tags. Las categorías aparecen como badges en las cards (como TLDR usa "Tech", "AI", "Dev").

---

## FASE 1C: Base de Conocimiento Newsletter & Email

> Antes de crear contenido o templates, instalamos el conocimiento base de email marketing
> que informará todas las decisiones de newsletter, templates y automatización.
> Fuentes: beehiiv-newsletter-advisor (datos de plataforma) + email-marketing-bible (best practices generales).

### Referencia unificada de email marketing

- [x] Clonar temporalmente repos fuente (beehiiv-newsletter-advisor + email-marketing-bible)
- [x] Curar y fusionar contenido relevante por tema (excluir: ecommerce, cold email, case studies)
- [x] Crear `references/newsletter/email-marketing-playbook.md` con 11 secciones:
  - Benchmarks & KPIs (beehiiv 2025 + genéricos)
  - Growth Stack (canales ordenados por impacto)
  - Welcome Series (6 emails adaptados a ROBOHOGAR)
  - Subject Lines & Copywriting (frameworks PAS/BAB/1-3-1)
  - Email Design Patterns (specs + anti-slop + 57 diseños curados)
  - Deliverability (autenticación + Gmail Primary + cambios 2025-2026)
  - Segmentation (5 tiers de engagement)
  - Testing (prioridades)
  - Compliance GDPR (audiencia EU)
  - Creator Milestones (revenue stack, inflexión 10K)
  - Send Timing (martes/miércoles, 9:00 AM)
- [x] Verificar: archivo accesible y referenciado desde `/content-draft`

### Regla compacta de newsletter

- [x] Crear `rules/newsletter.md` (≤40 líneas) — mecánicas de email
- [x] Ownership claro: `editorial.md` = voz/tono, `newsletter.md` = entrega/diseño/optimización
- [x] Añadir `@rules/newsletter.md` a `CLAUDE.md`
- [x] Verificar: ≤40 líneas, sin duplicación con `editorial.md`

### Actualizar skill de contenido

- [x] Añadir tipo "Newsletter" a la tabla de tipos en `.claude/commands/content-draft.md`
- [x] Añadir template en tabla de templates
- [x] Añadir referencia condicional al playbook para tipo Newsletter

### Investigación de templates de referentes

> Investigar qué estructuras usan las newsletters exitosas antes de diseñar los nuestros.

- [ ] Scrape 2-3 issues de cada referente con Firecrawl:
  - **TLDR** — estructura ultra-concisa (emoji + bold + 2-line summary + link)
  - **The Hustle** — storytelling + data, reviews largos, headers grandes
  - **Morning Brew** — gold standard (estructura de secciones, ratio texto/imagen, CTAs)
  - **Newsletter Operator** — reviews, comparison tables
  - **Chartr** — data-driven, uso de charts/tablas inline
- [ ] Extraer: estructura HTML, ancho, tipografía, espaciado, ratio imagen/texto
- [ ] Documentar patrones en `references/newsletter/template-patterns.md`

### Sistema de templates ROBOHOGAR

**Principios de diseño:**
1. **Automation-ready**: slots claros que `/content-draft` puede rellenar
2. **Mobile-first**: 600px max, 14-16px body, single-column, touch targets 44px
3. **Consistencia visual**: misma estructura = lectores saben qué esperar
4. **Anti-slop**: personalidad > perfección. Voz ROBOHOGAR visible
5. **Escalable**: añadir secciones o tipos sin rediseñar

**Templates a crear/iterar:**

| Template | Archivo | Tipo | Status |
|---|---|---|---|
| Review/Comparativa | `content/templates/review-comparativa.md` | 70% — productos | 🔄 En iteración |
| Newsletter Issue | `content/templates/newsletter-issue.md` | Email quincenal | ⏳ Pendiente |
| Noticias/Roundup | `content/templates/noticias-roundup.md` | Noticias curadas | ⏳ Pendiente |
| Editorial/Opinión | `content/templates/editorial-opinion.md` | 30% — futuro | ⏳ Pendiente |

**Proceso por template (7 pasos):**
1. Investigar 3+ ejemplos reales del mismo tipo
2. Diseñar estructura (secciones, headings, slots)
3. Definir frontmatter (campos YAML para `/content-draft`)
4. Crear checklist pre-publicación
5. Probar en Beehiiv (post de prueba + mobile preview)
6. Iterar según cómo se ve publicado
7. Documentar versión final con ejemplos

**Template 1: Review/Comparativa (✅ COMPLETADO)**
- [x] Revisar estructura vs patrones de referentes
- [x] Verificar slots de frontmatter para `/content-draft`
- [x] Ajustar tabla comparativa → 4 columnas (Producto/Precio/Lo clave/Nota ⭐)
- [x] Probar en Beehiiv con post de prueba, verificar mobile
- [x] Finalizar checklist (22 puntos)

**Template 2: Newsletter Issue (NUEVO)**
- [ ] Crear `content/templates/newsletter-issue.md`
- [ ] Estructura: 5 secciones + frontmatter + pre-send checklist
- [ ] Consultar playbook para fórmula 1-3-1 y subject lines
- [ ] CTA placement: mid-article + footer

**Template 3: Noticias/Roundup (NUEVO)**
- [ ] Crear `content/templates/noticias-roundup.md`
- [ ] Formato: emoji + bold título + resumen + "Por qué importa:" + link
- [ ] SEO-friendly con H2 por noticia para artículos web

**Template 4: Editorial/Opinión (NUEVO)**
- [ ] Crear `content/templates/editorial-opinion.md`
- [ ] Estructura: hook → contexto → desarrollo → contraargumento → posición → cierre

### Template visual de email en Beehiiv

- [ ] Configurar en **Settings → Email → Default Template**
- [ ] Header: `newsletter-header.png` (ya generado)
- [ ] Colores: fondo #FFFFFF, texto #0C0C0C, CTAs #F5A623
- [ ] Footer: social links + unsubscribe
- [ ] Verificar dark mode y mobile
- [ ] Enviar test email a personal

### Limpiar

- [x] Eliminar repos clonados temporales
- [x] Commit con cambios de conocimiento base

---

## FASE 2: Contenido Base (semana 1-2)

### Crear template Review/Comparativa en Beehiiv

- [x] Template creado directamente en Beehiiv (Design Mode)
- [x] HTML exportado: `content/templates/review-comparativa-beehiiv.html`
- [x] Template .md actualizado: `content/templates/review-comparativa.md`
- [x] Template HTML de output: `content/templates/review-comparativa-output.html`
- [x] Voz de marca documentada: `docs/brand-voice.md`
- [x] Verificado en mobile preview

**Estructura final del template (43 bloques):** ver tabla completa en `review-comparativa.md`

---

### Workflow por artículo (aplica a todos)

1. **Claude** genera research + borrador HTML → `content/articulos/<slug>/borrador.html`
2. **Rafael** copia secciones del HTML a Beehiiv bloque por bloque
3. **Rafael** edita con su voz, añade imágenes de producto (fotos fabricante)
4. **Claude** genera hero image con `/nano-banana` (square o landscape) → sirve para artículo + thumbnail + OG/SEO. Verificar en opengraph.xyz tras publicar
5. **Rafael** configura en Beehiiv (ver settings abajo)
6. **Rafael** revisa checklist pre-publicación (`content/templates/review-comparativa.md`)
7. **Publicar** → actualizar Welcome Email con URL real → mover borrador a `content/published/`

### Settings de publicación en Beehiiv

| Setting | Valor | Notas |
|---------|-------|-------|
| **Publish to** | `Web only` | Artículos de blog. `Email and web` solo para newsletter quincenal |
| **Post URL** | `<slug>` definido en SEO del artículo | Siempre corto, sin stop words |
| **Post thumbnail** | Subir `thumbnail-<slug>.png` (16:9) | Aparece en landing, cards, OG, Google |
| **Show thumbnail on top** | ✅ Activado | La hero se muestra dentro del artículo |
| **Advanced email capture** | `Content Gate` | Primeros párrafos gratis, luego pide email |
| **Comments** | Activados | Engagement + señales SEO |
| **Meta title** | Copiar del frontmatter del borrador | Max 60 chars |
| **Meta description** | Copiar del frontmatter del borrador | Max 155 chars, con CTA implícito |

---

### Artículo 0: "Robots de escritorio con IA: cuál merece tu dinero (y cuál es humo)"

| Campo | Valor |
|-------|-------|
| SEO Title | `Mejor robot asistente IA escritorio 2026 — Comparativa honesta` |
| Meta description | `Eilik, EMO, LOOI, Loona y Vector: los comparamos sin filtro. Cuál vale la pena, cuál es hype y cuál es tirar el dinero.` |
| Slug | `mejor-robot-asistente-ia-2026` |
| Tags | `Asistentes IA`, `Robot Mascotas` |
| Tipo | Review/Comparativa |
| Borrador | `content/articulos/mejor-robot-asistente-ia-2026/borrador.html` |

**Productos:** Eilik (~140€), LOOI (~160-190€), Loona (~500€). No recomendados: EMO Go Home, Vector 2.0, Miko 3.

- [x] Research completado
- [x] Borrador HTML generado
- [x] Copiar a Beehiiv + editar voz
- [x] Hero image generada
- [x] SEO configurado en Beehiiv
- [x] Publicado → https://robohogar.com/p/mejor-robot-asistente-ia-2026
- [ ] Welcome Email configurado y activado (ver sección abajo)

---

### Welcome Email (configurar AHORA — después de publicar Artículo 0)

> El Welcome Email es lo primero que recibe alguien al suscribirse.
> **50-55% de open rate** — el doble que un email normal. Es tu mejor oportunidad de causar buena impresión.
> Según el playbook: pedir reply (señal #1 para Gmail Primary) + pedir mover a bandeja principal.

**Paso 1** — Ir a **Automations** en el menú lateral de Beehiiv

**Paso 2** — Buscar **Welcome Email** (Beehiiv lo tiene como automatización predeterminada). Click en **Edit**

**Paso 3** — Configurar:

| Campo | Valor |
|-------|-------|
| Subject | `Bienvenido/a a ROBOHOGAR 🤖` |
| Preview text | `Tu casa se está robotizando y yo te lo cuento` |
| Sender name | `Rafael de ROBOHOGAR` |

**Paso 4** — Pegar este contenido en el editor (copy-paste):

```
¡Hola!

Soy Rafael, y esto es ROBOHOGAR — tu casa se está robotizando
y yo te lo cuento cada 2 semanas.

Esto es lo que vas a recibir:

• Lo que ha pasado en robótica doméstica, sin tecnicismos
• Reviews sin filtro de robots que ya están a la venta
• Humanoides y el futuro de tu casa robotizada
• Un dato curioso + el mejor enlace que he encontrado

Para que no me pierda en tu spam, haz esto:
→ Arrastra este email a tu bandeja principal
→ Añade hola@robohogar.com a tus contactos

Mientras tanto, empieza por aquí:
👉 Robots de escritorio con IA: cuál merece tu dinero
    https://robohogar.com/p/mejor-robot-asistente-ia-2026

Si tienes un robot en casa y quieres contarme tu experiencia,
responde a este email — los leo todos.

Un saludo robótico,
Rafael
ROBOHOGAR
```

**Paso 5** — Verificar:
- [ ] ¿El link al artículo funciona?
- [ ] ¿El sender name dice "Rafael de ROBOHOGAR"?
- [ ] ¿El subject tiene el emoji 🤖?

**Paso 6** — Pulsar **Save & Activate**

**Paso 7** — Probar: suscríbete tú mismo con un email alternativo y verifica que llega

---

### Redes sociales (configurar ANTES de crear más contenido)

> Todo esto se configura una vez. Cuando publiques artículos nuevos, solo tienes que compartir desde Buffer.

**Instagram**

- [ ] Crear cuenta: username `robohogar_es`
- [ ] Convertir a profesional: Settings → Account → Switch to professional → Creator → Technology
- [ ] Foto de perfil: mascota principal
- [ ] Bio: `🤖 Robots que llegan a tu casa | 📬 Newsletter gratis cada 2 semanas | 🔍 Reviews · Noticias · Opinión | 👇 Suscríbete`
- [ ] Link en bio → `https://robohogar.com`

**LinkedIn**

- [ ] Añadir a tu headline: `| Fundador de ROBOHOGAR 🤖`
- [ ] Publicar post de lanzamiento (link en primer comentario, NO en el cuerpo)

**WhatsApp Channel**

- [ ] WhatsApp → Updates → Channels → `+` → Create Channel
- [ ] Nombre: `ROBOHOGAR 🤖`
- [ ] Descripción: `Newsletter quincenal sobre robótica doméstica. robohogar.com`
- [ ] Foto: mascota principal
- [ ] Publicar primer mensaje de bienvenida

**Buffer**

- [ ] Registrarse en buffer.com (plan gratuito: 3 canales, 10 posts/canal)
- [ ] Conectar: Instagram + LinkedIn
- [ ] Horarios: IG lunes/miércoles/viernes 12:00 PM · LinkedIn martes/jueves 9:00 AM

**Canva Brand Kit**

- [ ] Registrarse/login en canva.com
- [ ] Brand Kit: logo mascota + colores (#F5A623, #0C0C0C, #FFFFFF, #F2F2F2)
- [ ] Guardar 2-3 templates adaptados para posts de IG

---

### Monetización y legal (configurar ANTES de crear más contenido)

**Amazon Afiliados España** ⏳ PENDIENTE — registrarse cuando haya tráfico y artículos con enlaces de producto

- [ ] Registrarse en afiliados.amazon.es (necesitas NIF + IBAN personal, no hace falta empresa)
- [ ] Website → `robohogar.com`
- [ ] Categorías → Electrónica, Hogar
- [ ] Insertar tag de afiliado en los links de Amazon de los artículos

> ⚠️ Tienes **180 días** para generar al menos 1 venta. No registrarse sin audiencia. Comisiones: 3-7%. Cookie: 24h (89 días si añade al carrito).

**Páginas legales (obligatorias por ley española para cualquier web)**

Paso a paso en Beehiiv:

1. Ve a **Settings** (rueda dentada) → **Website** → busca la sección **Pages**
2. Pulsa **Add Page** (o **New Page**)
3. Crea cada página rellenando título, slug y contenido como se indica abajo

**Página 1: Aviso Legal**

- [ ] Título: `Aviso Legal`
- [ ] Slug: `aviso-legal` (la URL será robohogar.com/aviso-legal)
- [ ] Contenido a poner:

```
AVISO LEGAL

Titular: Rafael [tu apellido]
NIF: [tu DNI]
Email de contacto: robohogar@gmail.com
Dominio: robohogar.com

Este sitio web es un proyecto personal de divulgación sobre robótica doméstica.
El contenido publicado refleja opiniones personales del autor.
Los enlaces a productos pueden incluir enlaces de afiliado (Amazon Afiliados).
```

**Página 2: Política de Privacidad**

- [ ] Título: `Política de Privacidad`
- [ ] Slug: `privacidad` (la URL será robohogar.com/privacidad)
- [ ] Contenido a poner:

```
POLÍTICA DE PRIVACIDAD

Responsable: Rafael [tu apellido]
Email: robohogar@gmail.com
Finalidad: Envío de newsletter quincenal sobre robótica doméstica
Legitimación: Consentimiento del interesado (doble opt-in)
Datos recogidos: Email
Destinatarios: Beehiiv Inc. (proveedor de email marketing, EEUU,
               sujeto a cláusulas contractuales tipo UE)
Conservación: Mientras mantengas tu suscripción activa
Derechos: Puedes acceder, rectificar o eliminar tus datos
          escribiendo a robohogar@gmail.com
          Puedes darte de baja en cualquier momento desde
          el enlace en cada email

Última actualización: abril 2026
```

**Añadir links en el footer**

- [ ] Ve a **Settings** → **Website** → sección de diseño/footer
- [ ] Añade enlaces a `/aviso-legal` y `/privacidad` en el pie de página

**Picos de conversión (marcar en calendario)**

- [ ] Prime Day (julio) → comparativas 1-2 semanas antes
- [ ] Black Friday (noviembre) → actualizar precios día del evento
- [ ] Navidad (diciembre) → "Guía de regalos tech: robots para casa"

---

### Artículo 1: "¿Qué robot aspirador compro en 2026?"

| Campo | Valor |
|-------|-------|
| SEO Title | `Mejor robot aspirador 2026 — Guía de compra honesta` |
| Meta description | `Comparativa de los mejores robots aspiradores de 2026. Sin publi, sin hype — solo cuál merece tu dinero según uso y presupuesto.` |
| Slug | `mejor-robot-aspirador-2026` |
| Tags | `Aspiradores` |
| Tipo | Review/Comparativa |

- [ ] Research
- [ ] Borrador HTML
- [ ] Copiar a Beehiiv + editar
- [ ] Hero image
- [ ] Publicado

### Artículo 2: "5 robots humanoides que llegarán a tu casa"

| Campo | Valor |
|-------|-------|
| SEO Title | `Robots humanoides para casa — 5 que llegarán antes de 2030` |
| Meta description | `Figure, Optimus, Unitree, 1X Neo y Xiaomi CyberOne. Cuáles son reales, cuáles humo, y cuándo podrías tener uno en el salón.` |
| Slug | `robots-humanoides-casa-2030` |
| Tags | `Humanoides` |
| Tipo | Editorial (30%) — sin afiliados, sin gating |

- [ ] Research
- [ ] Borrador HTML
- [ ] Copiar a Beehiiv + editar
- [ ] Hero image
- [ ] Publicado

### Artículo 3: "Mi experiencia con robots en casa"

| Campo | Valor |
|-------|-------|
| SEO Title | `Convivir con robots en casa — experiencia real` |
| Meta description | `Llevo años con robots en casa. Te cuento qué funciona, qué no, y qué cambiaría si empezara de cero.` |
| Slug | `experiencia-robots-casa` |
| Tags | `Opinión` |
| Tipo | Personal — sin afiliados, sin gating. Construye confianza |

- [ ] Borrador (Rafael escribe, Claude apoya)
- [ ] Copiar a Beehiiv + editar
- [ ] Hero image
- [ ] Publicado

---

## FASE 3: Obsidian Knowledge Base

### Crear estructura de carpetas

- [ ] Abrir Obsidian → Create New Vault → nombre `ROBOHOGAR` → ubicación donde Syncthing ya sincroniza

> [!tip]
> Si ya tienes un vault principal, puedes crear estas carpetas dentro de él en una carpeta `ROBOHOGAR/`.

- [ ] Crear carpetas:

```
00-Inbox/
01-Research/
02-Drafts/
03-Published/
04-Wiki/
  04-Wiki/Robots/
  04-Wiki/Empresas/
05-Templates/
06-Calendar/
07-Resources/
```

### Instalar plugins

- [ ] Settings → Community Plugins → Turn on community plugins
- [ ] Browse → buscar e instalar cada uno:
  1. **Templater** — templates con variables dinámicas
  2. **Dataview** — consultas tipo base de datos
  3. **QuickAdd** — macros para crear notas rápido
  4. **Periodic Notes** — notas periódicas (quincenal)
  5. **Omnivore** o **ReadItLater** — guardar artículos web para investigación
- [ ] Activar todos en Settings → Community Plugins

### Templates (crear en `05-Templates/`)

**`05-Templates/Research-Digest.md`:**
```markdown
---
date: {{date}}
type: research-digest
status: raw
---
# Research Digest — {{date:YYYY-MM-DD}}

## Fuentes revisadas
- [ ] The Robot Report
- [ ] IEEE Spectrum
- [ ] Weekly Robotics
- [ ] Xataka
- [ ] Blogs de marcas (Roborock, Dreame, iRobot, Ecovacs)

## Noticias relevantes
### 1. [Título]
- **Fuente:** 
- **Resumen:** 
- **Ángulo ROBOHOGAR:** 
- **Prioridad:** 🔴 alta / 🟡 media / 🟢 baja

### 2. [Título]
(repetir)

## Selección para newsletter
- [ ] Noticia para sección LA NOTICIA:
- [ ] Tema para EL FUTURO:
- [ ] Candidato a DATO CURIOSO:
- [ ] Enlace para ENLACE DE LA QUINCENA:
```

**`05-Templates/Article-Draft.md`:**
```markdown
---
date: {{date}}
type: article
status: draft
slug: 
seo-title: 
meta-desc: 
keyword: 
category: review | editorial | guia | opinion
affiliate: true | false
---
# {{title}}

## SEO checklist
- [ ] H1 con keyword principal
- [ ] Meta desc < 155 chars
- [ ] Slug corto y descriptivo
- [ ] Alt text en imágenes
- [ ] 2+ internal links
- [ ] 800+ palabras
- [ ] Opinión personal incluida

## Borrador

### [H2 — sección 1]

### [H2 — sección 2]

### [H2 — veredicto / cierre]

## Notas de edición
- 
```

**`05-Templates/Robot-Wiki.md`:**
```markdown
---
type: robot
brand: 
model: 
category: aspirador | friegasuelos | cortacesped | humanoid | piscina | cocina
price-range: 
amazon-link: 
date-reviewed: 
rating: /10
---
# {{title}}

## Specs clave
- **Precio:** 
- **Navegación:** 
- **Batería:** 
- **Punto fuerte:** 
- **Punto débil:** 

## Mi experiencia
(notas personales)

## Artículos donde aparece
- [[]]

## Competidores directos
- [[]]
```

**`05-Templates/Company-Wiki.md`:**
```markdown
---
type: company
sector: consumer | humanoid | industrial
country: 
website: 
---
# {{title}}

## Productos relevantes
- [[]]

## Noticias recientes
- {{date}} — 

## Notas
```

**`05-Templates/Editorial-Calendar.md`:**
```markdown
---
type: calendar
period: {{date:YYYY-MM}}
---
# Calendario Editorial — {{date:YYYY MMMM}}

## Newsletter (quincenales)
| # | Fecha envío | Título tentativo | Status |
|---|---|---|---|
| | | | 📝 idea / ✍️ borrador / ✅ enviado |
| | | | |

## Artículos web (SEO)
| Fecha pub | Título | Keyword | Afiliado |
|---|---|---|---|
| | | | sí/no |

## Redes sociales
| Fecha | Canal | Contenido | Status |
|---|---|---|---|
| | IG Reel | | |
| | LinkedIn | | |
| | WhatsApp | | |
```

### Configurar QuickAdd

- [ ] Settings → QuickAdd → Add Choice:
  - Name: `Nuevo Research Digest` → Type: Template → Template path: `05-Templates/Research-Digest.md` → Folder: `01-Research` → File name: `{{date:YYYY-MM-DD}}-digest`
  - Name: `Nuevo Artículo` → Type: Template → Template path: `05-Templates/Article-Draft.md` → Folder: `02-Drafts`
  - Name: `Nuevo Robot` → Type: Template → Template path: `05-Templates/Robot-Wiki.md` → Folder: `04-Wiki/Robots`
  - Name: `Nueva Empresa` → Type: Template → Template path: `05-Templates/Company-Wiki.md` → Folder: `04-Wiki/Empresas`

### Configurar Periodic Notes

- [ ] Settings → Periodic Notes → activar **Weekly Note** (o crear macro quincenal manual)
- [ ] Format: `YYYY-[W]ww`
- [ ] Template: `05-Templates/Editorial-Calendar.md`
- [ ] Folder: `06-Calendar`

---

## FASE 4: Newsletter #1 (semana 3-4)

### Estructura del issue

Cada newsletter sigue este template (de `docs/plan-v2.md`):

```
🤖 ROBOHOGAR #01 — [Título del issue]

1. LA NOTICIA — [Novedad más relevante de la quincena]
   (2-3 párrafos con contexto y opinión propia)

2. EN PRUEBA — [Review o experiencia con un robot]
   (Opcional si no hay review — sustituir por mini-comparativa)

3. EL FUTURO — [Avance en humanoides o robótica avanzada]
   (1-2 párrafos + opinión: ¿por qué importa?)

4. DATO CURIOSO — [Estadística o curiosidad]
   (1 párrafo corto, sorprendente)

5. ENLACE DE LA QUINCENA — [Mejor artículo/vídeo que he leído]
   (Link + 2 líneas de por qué merece la pena)

---
¿Te ha gustado? Reenvíaselo a alguien a quien le mole la robótica.
[Suscríbete aquí si te lo han reenviado](URL_LANDING)
```

### Preparar el issue

- [ ] Consultar `references/newsletter/email-marketing-playbook.md` para subject line (<25 chars)
- [ ] Usar template `content/templates/newsletter-issue.md` (cuando esté creado)
- [ ] Verificar estructura 1-3-1 (intro, 3 puntos, CTA) — ver `rules/newsletter.md`
- [ ] Subject line: curiosity gap o pregunta, sin clickbait

### Escribir en Beehiiv

- [ ] **Posts → Create Post**
- [ ] Escribir siguiendo la estructura de arriba
- [ ] Usar `/` (slash commands) en el editor para insertar bloques:
  - `/heading` para H2 de cada sección
  - `/divider` para separadores entre secciones
  - `/button` para el CTA final
  - `/image` para imágenes (usar mascota como separador visual)
- [ ] Settings → **Send as email** (esta vez sí como email, no solo web post)
- [ ] Settings → **Also publish as web post** → activar (para SEO)
- [ ] Audience → All subscribers
- [ ] Preview: pulsar **Send Test Email** a tu email personal
- [ ] Verificar en móvil que se ve bien
- [ ] Programar envío: **Schedule** → elegir día y hora (martes o jueves, 9:00 AM)

### Backup

- [ ] Copiar el contenido final (markdown) a `content/published/2026-XX-XX-issue-01.md` en el repo
- [ ] En Obsidian: mover el borrador de `02-Drafts/` a `03-Published/`

---

## FASE 5: Automatización

### Visión general del pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│  AUTOMÁTICO (sin intervención)                                  │
│                                                                 │
│  RSS feeds ──→ research_aggregator.py ──→ Claude API            │
│  (8+ fuentes)    (fetch + scrape)          (categoriza por tag, │
│                                             puntúa relevancia,  │
│                                             resume en español)  │
│                          ↓                                      │
│              content/drafts/YYYY-MM-DD-raw-digest.md            │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  MANUAL (Rafael, ~15 min)                                       │
│                                                                 │
│  Lee el digest → elige 5-6 noticias → decide ángulo/tema       │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  SEMIAUTOMÁTICO (Claude API + templates)                        │
│                                                                 │
│  Rafael indica: tema + ángulo + tipo (review/noticias/opinión)  │
│       ↓                                                         │
│  Claude API + template del tipo de artículo                     │
│       ↓                                                         │
│  content/drafts/YYYY-MM-DD-borrador-slug.md                    │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  MANUAL (Rafael, ~30-45 min)                                    │
│                                                                 │
│  Edita borrador: añade voz propia, opinión, humor               │
│  → Publica en Beehiiv                                           │
│  → Mueve a content/published/                                   │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  AUTOMÁTICO (post-publicación)                                  │
│                                                                 │
│  Claude API genera posts sociales desde artículo publicado      │
│       ↓                                                         │
│  Make.com / Buffer programa publicación:                        │
│    → LinkedIn (martes 9:00 AM)                                  │
│    → X/Twitter (martes 12:00 PM)                                │
│    → Instagram Reel (miércoles 12:00 PM)                        │
│    → WhatsApp Channel (martes 10:00 AM)                         │
└─────────────────────────────────────────────────────────────────┘
```

**Principio clave:** automatizar TODO excepto juicio editorial y voz propia.
Rafael decide QUÉ contar y CÓMO contarlo. El resto lo hacen scripts + API.

---

### Paso 1 — Research aggregator

- [ ] Script: `utilities/research_aggregator.py`
- [ ] Fuentes RSS:

```python
RSS_FEEDS = [
    # Robótica general (EN)
    "https://www.therobotreport.com/feed/",
    "https://spectrum.ieee.org/feeds/topic/robotics.rss",
    "https://weeklyrobotics.com/feed.xml",
    "https://techcrunch.com/tag/robotics/feed/",
    # Robótica doméstica / smart home (ES)
    "https://www.xataka.com/tag/robots/feed",
    "https://www.xatakahome.com/feed",
    # Marcas (solo novedades de producto, no marketing)
    "https://global.roborock.com/blogs/news.atom",
    "https://www.dreametech.com/blogs/news.atom",
]
```

- [ ] Fuentes web (scraping con Firecrawl, sin RSS):
  - robotsaroundthehouse.com — foro companion robots
  - robotinhouse.com — blog español competidor
  - mia-cat.com — reviews de companion robots

- [ ] Ejecución: programada cada lunes (cron o Make.com trigger)
- [ ] Output: `content/drafts/YYYY-MM-DD-raw-digest.md`

### Paso 2 — Categorización con Claude API

Qué hace la API con el digest crudo:

1. **Clasifica cada noticia** por content tag de Beehiiv (Aspiradores, Cortacéspedes, Humanoides, Asistentes IA, Robot Mascotas, Smart Home, Noticias, Opinión, Guías)
2. **Puntúa relevancia** (1-5) según: novedad, impacto en consumidor, potencial editorial
3. **Resume en español** cada noticia en 2-3 frases (aunque la fuente sea en inglés)
4. **Detecta duplicados** entre fuentes (la misma noticia en 3 sitios = 1 entrada)
5. **Output**: digest estructurado por tag, ordenado por relevancia

Prompt base para la API (se guardará en `utilities/prompts/categorize-digest.md`):
```
Eres el asistente editorial de ROBOHOGAR, una newsletter sobre robótica
doméstica en español. Clasifica estas noticias por categoría, puntúa
su relevancia (1-5), resume en español y elimina duplicados.
Categorías: [lista de tags de Beehiiv]
Criterios de relevancia: producto disponible para compra > anuncio con
fecha > rumor. España/Europa > EEUU > Asia. Consumidor > industria.
```

### Paso 3 — Generación de borrador con Claude API

Cuando Rafael elige tema y ángulo, la API genera un borrador usando:

1. **Template del tipo de artículo** (de `content/templates/`)
   - `review-comparativa.md` — para reviews y comparativas de productos
   - `noticias-roundup.md` — para newsletter quincenal (futuro)
   - `editorial-opinion.md` — para piezas de opinión (futuro)
2. **Fuentes seleccionadas** del digest + fuentes de `references/fuentes-por-categoria.md`
3. **Reglas editoriales** de `.claude/rules/editorial.md` (tono, estructura, voz)
4. **Reglas SEO** de `.claude/rules/seo.md` (title tag, meta, estructura H2/H3)

Output: `content/drafts/YYYY-MM-DD-borrador-slug.md`

### Paso 4 — Edición manual (Rafael)

- Lee el borrador, añade opinión personal, humor, experiencias
- Ajusta tono (el borrador será correcto pero necesita VOZ)
- Publica en Beehiiv
- Mueve archivo a `content/published/`

### Paso 5 — Social media automático (post-publicación)

Claude API genera desde el artículo publicado:

- [ ] **LinkedIn**: resumen profesional (150 palabras) + opinión + "link en primer comentario"
- [ ] **X/Twitter**: hilo de 3-5 tweets con los puntos clave
- [ ] **Instagram**: texto para Reel (30s) + caption con hashtags
- [ ] **WhatsApp Channel**: resumen ultra-corto (3 líneas) + link

Prompt base (se guardará en `utilities/prompts/social-posts.md`):
```
Genera posts para redes sociales a partir de este artículo de ROBOHOGAR.
Tono: cercano, informado, con humor sutil. Nunca clickbait.
LinkedIn: profesional pero no corporativo. X: directo y punchy.
Instagram: visual, con emojis moderados. WhatsApp: ultra-breve.
```

Programación con Make.com → Buffer:
- [ ] Make.com scenario: webhook recibe los posts → envía a Buffer API
- [ ] Buffer programa publicación según horarios configurados

### Welcome Series completa (6 emails)

> Referencia detallada: `references/newsletter/email-marketing-playbook.md` sección 3.
> Beehiiv free plan: solo welcome + reminder. Serie completa requiere plan de pago.

- [ ] **Email 1** (día 0): Bienvenida + mejor artículo + pedir reply (ya existe como Welcome Email)
- [ ] **Email 2** (día 1): Pregunta engagement "¿Qué robot tienes?" (ya existe como Reminder)
- [ ] **Email 3** (día 3): Artículo editorial (humanoides) — construye marca, muestra el 30%
- [ ] **Email 4** (día 5): Guía de compra — muestra valor práctico, el 70%
- [ ] **Email 5** (día 10): Experiencia personal con robots — genera confianza
- [ ] **Email 6** (día 14): Resumen de lo que viene + CTA referral + link preferencias
- [ ] Configurar en Beehiiv Automations cuando se upgrade a plan de pago

### HTML Email Template (cuando sea necesario)

> Para campañas especiales o templates personalizados. Workflow: generar HTML → copy-paste en Beehiiv.

- [ ] Consultar playbook sección "Email Design Patterns" para specs (600px, inline CSS, dark mode)
- [ ] Generar HTML con inline styles, ancho max 600px
- [ ] Testear dark mode y mobile (enviar test email)
- [ ] Pegar en Beehiiv editor (bloque HTML)

### Herramientas y costes

| Herramienta | Función en el pipeline | Coste |
|---|---|---|
| Claude API (Haiku) | Categorización del digest (paso 2) | ~$0.02/run |
| Claude API (Sonnet) | Generación de borradores + social (pasos 3, 5) | ~$0.10/run |
| Make.com | Orquestación: cron → aggregator → API → Buffer | 9€/mes |
| Buffer | Programación de posts sociales | 6€/mes |
| Firecrawl | Scraping de fuentes sin RSS | Free tier (500 créditos/mes) |

**Coste total pipeline**: ~15€/mes + ~$0.25 por issue de newsletter

### Calendario editorial

- [ ] Cadencia: newsletter cada 2 semanas, en martes
- [ ] Calendario:
  - Semana A (lunes): Aggregator corre automático → digest listo
  - Semana A (lunes-martes): Rafael revisa digest, elige tema, lanza borrador
  - Semana A (miércoles): Edición personal → publicar en Beehiiv
  - Semana A (miércoles): Social posts se generan y programan automáticamente
  - Semana B: Artículo evergreen SEO + 2-3 Reels para Instagram

---

## FASE 6: Métricas y Revisión

### Qué rastrear

| Métrica | Dónde | Objetivo mes 3 | Objetivo mes 12 |
|---|---|---|---|
| Suscriptores totales | Beehiiv → Dashboard | 100 | 1.000 |
| Open rate | Beehiiv → Posts → Analytics | >50% | >45% |
| Click-through rate | Beehiiv → Posts → Analytics | >10% | >6% |
| Revenue afiliado | Amazon Afiliados → Reports | €0 | €50+/mes |
| Tráfico web | Google Search Console | — | 3.000 visitas/mes |
| IG seguidores | Instagram → Insights | 100 | 1.500 |

### Google Search Console

- [ ] Ir a **https://search.google.com/search-console**
- [ ] Add Property → URL prefix → `https://robohogar.com`
- [ ] Verificar con DNS: añadir registro TXT en Namecheap
  - Tipo: `TXT`
  - Host: `@`
  - Value: el código que te da Search Console (empieza por `google-site-verification=...`)
  - TTL: Auto
- [ ] Enviar sitemap: en Search Console → Sitemaps → escribir `https://robohogar.com/sitemap.xml` (Beehiiv lo genera automáticamente)
- [ ] Esperar 2-3 días para los primeros datos

### Revisión mensual (template)

Cada primer lunes del mes, dedicar 30 min a esto:

```
## Revisión mensual — [MES YYYY]

### Números
- Subs inicio de mes:
- Subs fin de mes:
- Crecimiento neto:
- Open rate promedio:
- CTR promedio:
- Revenue afiliado:
- Top artículo por tráfico:

### Qué funcionó
- 

### Qué no funcionó
- 

### Acciones para el próximo mes
- [ ] 
- [ ] 
- [ ] 
```

### Evaluación trimestral

Cada 3 meses, revisar contra los objetivos de `docs/plan-v2.md`:

- [ ] ¿Estoy en cadencia? (¿He enviado todos los newsletters programados?)
- [ ] ¿Crecimiento de subs está en línea con objetivos?
- [ ] ¿Qué tipo de contenido genera más suscripciones? (reviews vs editorial vs guías)
- [ ] ¿Los artículos SEO están posicionando? (Search Console → Performance)
- [ ] ¿Merece la pena invertir en alguna herramienta de pago?

### Criterio de abandono

> [!warning]
> Si después de 6 meses con cadencia consistente (12 newsletters enviados sin fallar) hay **menos de 100 suscriptores**, el nicho no funciona en español. Opciones: pivotar el posicionamiento o cerrar.

---

## FASE 7: Post-lanzamiento y mantenimiento con Claude Code

### Workflow quincenal (cada 2 semanas, ~30 min con Claude Code)

**Agentes automáticos (Claude Code ejecuta):**
- [ ] `/research-digest` — Agente Research: scrape RSS → digest + wiki update
- [ ] `/content-draft` — Agente Escritura: genera borrador SEO desde el digest
- [ ] `/nano-banana` — Agente Imágenes: genera hero branded (1200x630) + actualiza catálogo

**Manual (Rafael):**
- [ ] Editar borrador (añadir voz, opinión, humor) — 45-75 min
- [ ] Publicar en Beehiiv (copiar contenido + subir hero image + programar envío)

**Post-publicación (Claude Code ejecuta):**
- [ ] `/social-content` — Agente Social: genera posts para LinkedIn, X, Instagram, WhatsApp
- [ ] Revisar y programar posts en Buffer
- [ ] `/obsidian-robohogar sync-published` — copia el artículo publicado al vault
- [ ] `/obsidian-robohogar wiki-update` — actualiza wiki con robots/empresas mencionados
- [ ] Mover borrador a `content/published/` y hacer commit

### Mantenimiento mensual (~15 min)

- [ ] `/obsidian-robohogar calendar-update` — actualizar calendario editorial
- [ ] `/obsidian-robohogar audit` — revisar naming, frontmatter, wikilinks
- [ ] Revisar métricas en Beehiiv (subs, open rate, CTR)
- [ ] Revisar Google Search Console (qué keywords posicionan)
- [ ] Actualizar `Metricas/` en el vault con los datos del mes

### Mantenimiento trimestral (~30 min)

- [ ] `/obsidian-robohogar archive` — archivar digests y borradores viejos
- [ ] Actualizar artículos evergreen (precios, modelos nuevos, links rotos)
- [ ] Revisar y actualizar SEO: meta descriptions, títulos, keywords
- [ ] Evaluar: ¿Qué artículos generan más tráfico? → escribir más de ese tipo
- [ ] Evaluar: ¿Qué lead magnets convierten? → mantener gated o abrir

### Actualizar landing en Beehiiv

**Añadir secciones:**
- En Beehiiv: **Website → Design Mode → Add Section**
- Secciones candidatas: testimonios (cuando haya), contador de suscriptores, vídeo embed de YouTube

**Cambiar imágenes:**
- En Beehiiv: **Design Mode → clic en imagen → Replace**
- Generar nuevas con `/nano-banana` → subir a Beehiiv
- Assets van a `assets/images/` en el repo (backup)

**Añadir vídeos:**
- En Beehiiv: **Design Mode → Add Section → Video/Embed**
- Pegar URL de YouTube — Beehiiv genera el embed automáticamente
- Recomendado: 1 vídeo en la landing cuando haya contenido en YouTube

**Actualizar FAQ:**
- En Beehiiv: **Design Mode → FAQ section → Edit**
- Añadir preguntas nuevas basadas en feedback de suscriptores

**Actualizar social proof:**
- Cuando alcances 100 subs: cambiar "Quincenal · 5 min" → "Únete a 100+ lectores"
- Cuando alcances 500: "Únete a 500+ lectores que ya viven con robots"

### Skills de Claude Code disponibles

| Skill | Trigger | Qué hace |
|---|---|---|
| `/research-digest` | "agrega noticias", "digest" | Scrape RSS → digest + wiki update |
| `/content-draft` | "borrador", "nuevo artículo" | Genera borrador con SEO desde digest |
| `/social-content` | "genera social", "posts" | Posts para LinkedIn, X, Instagram, WhatsApp |
| `/obsidian-robohogar` | "sync vault", "wiki update" | Mantiene wiki, calendario, archivado |
| `/nano-banana` | "genera imagen" | Assets visuales (mascota, headers, OG) |
| `/commit` | "commitea" | Git commit con formato estándar |

## FASE 8: Crecimiento de suscriptores (cuando haya >50 subs)

Tácticas para aumentar la base de suscriptores de forma orgánica y no invasiva.

### Content gate ("Subscribe to keep reading")

- Beehiiv permite bloquear el contenido a mitad de artículo con un muro de suscripción gratuita
- El lector ve el inicio del artículo, se engancha, y debe suscribirse para seguir leyendo
- **Cuándo activar:** en artículos largos tipo review o comparativa (>1200 palabras), NO en newsletters
- **Configuración en Beehiiv:** Settings → Content → Content Gate (activar por artículo, no globalmente)
- **Referencia visual:** pantallazo guardado — modal con "Subscribe to keep reading", email input y "Not now"

### Engagement-based emails

- Configurar emails automáticos cuando un lector interactúa (likes, clicks, shares)
- Ejemplo: "Veo que te gustó el artículo de humanoides — te aviso cuando publique la parte 2"
- **En Beehiiv:** Automations → Triggers (disponible en planes de pago, planificar para cuando escale)

### Referral program

- Beehiiv tiene sistema de referidos integrado (Refer a Friend)
- Recompensar con contenido exclusivo o mención en la newsletter
- **Cuándo activar:** cuando haya masa crítica (~200+ subs)

### Otras tácticas pendientes de evaluar

- [ ] Lead magnet (PDF "Guía de compra de robots 2026") a cambio de email
- [ ] Cross-promotion con newsletters similares en español
- [ ] Pop-up de salida en artículos web (exit intent)
- [ ] Firma de email personal con link a ROBOHOGAR
- [ ] Compartir en comunidades (Reddit r/homeautomation, foros de domótica España)

---

## FASE 9: Optimización Newsletter (cuando haya >200 subs)

### A/B Testing

- [ ] Testear sender name: "Rafael" vs "ROBOHOGAR" vs "Rafael de ROBOHOGAR"
- [ ] Testear formato CTA: botón ámbar vs text link
- [ ] Testear template: minimalista vs con hero image
- [ ] Testear subject: pregunta vs statement vs número
- [ ] Referencia: `references/newsletter/email-marketing-playbook.md` sección Testing
- [ ] Solo 1 de cada 7 tests da resultado significativo — paciencia

### Segmentación por engagement

> Implementar 5 tiers del playbook (sección Segmentation).

- [ ] Tier 1 (clicked 30d): recibe todo
- [ ] Tier 2 (clicked 60d): recibe 75% de envíos
- [ ] Tier 3 (opened 90d): solo el mejor contenido
- [ ] Tier 4 (sin engagement 90-180d): solo re-engagement flow
- [ ] Tier 5 (180+ días): sunset flow → suprimir
- [ ] Resultados esperados: +15-30% opens, -20-40% complaints
- [ ] Requiere plan Scale de Beehiiv para segmentación avanzada

### Deliverability audit

- [ ] Verificar SPF/DKIM/DMARC con herramienta online (ej: mxtoolbox.com)
- [ ] Monitorear Gmail Primary vs Promotions (enviar test emails)
- [ ] Revisar bounce rate y spam complaints vs benchmarks del playbook
- [ ] Implementar sunset flow para inactivos >90 días
- [ ] Referencia: playbook sección Deliverability

### Upgrade a Beehiiv Scale (cuando >2,500 subs o revenue lo justifique)

- [ ] Evaluar ROI: ¿el revenue (afiliados + sponsors) cubre los $34/mes?
- [ ] Activar: segmentación avanzada, A/B testing nativo, analytics detallados
- [ ] Activar: automations completas (welcome series de 6 emails)
- [ ] Evaluar: API access para subscribers → integrar en pipeline de automatización
- [ ] Considerar: Beehiiv MCP (si disponible en el plan)

---

## FASE 10: Pipeline Avanzado (cuando el workflow manual sea el bottleneck)

### Research Aggregator Script

- [ ] Implementar `utilities/research_aggregator.py` (diseñado en FASE 7)
- [ ] Conectar RSS feeds (8+ fuentes) + Firecrawl para scraping
- [ ] Integrar Claude API (Haiku) para categorización automática
- [ ] Output: `content/drafts/YYYY-MM-DD-raw-digest.md`
- [ ] Cron job semanal (lunes) via Make.com o cron local

### Make.com Integration

- [ ] Crear scenario: cron semanal → trigger research_aggregator
- [ ] Crear scenario: artículo publicado → genera posts sociales → Buffer API
- [ ] Coste: 9€/mes

### Buffer Integration

- [ ] Conectar Instagram, LinkedIn, WhatsApp Channel
- [ ] Configurar horarios: IG Lun/Mié/Vie 12:00, LinkedIn Mar/Jue 9:00
- [ ] Coste: 6€/mes

### Beehiiv MCP (cuando esté disponible en tu plan)

- [ ] Solicitar acceso si upgradeas a plan de pago
- [ ] Configurar en `.mcp.json`:
  ```json
  {
    "beehiiv": {
      "url": "https://mcp.beehiiv.com/mcp",
      "headers": { "Authorization": "Bearer <token>" }
    }
  }
  ```
- [ ] V1: consultar métricas directamente desde Claude Code
- [ ] V2 (futuro): crear borradores directamente en Beehiiv desde Claude Code

### Pipeline end-to-end automatizado

Workflow objetivo — tiempo de Rafael: ~1h por issue (vs 3h+ manual):

```
┌── AUTOMÁTICO ────────────────────────────────────────────────┐
│ /research-digest → digest automático (lunes)                  │
│ Fuentes RSS + Firecrawl → Claude API categoriza → digest.md  │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── MANUAL (~15 min) ──────────────────────────────────────────┐
│ Rafael lee digest → elige 3-5 temas → define ángulo          │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── SEMIAUTOMÁTICO ────────────────────────────────────────────┐
│ /content-draft → borrador con SEO + playbook de newsletter   │
│ /nano-banana → hero image automático                          │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── MANUAL (~45 min) ──────────────────────────────────────────┐
│ Rafael edita voz/opinión/humor → publica en Beehiiv          │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── AUTOMÁTICO ────────────────────────────────────────────────┐
│ /social-content → posts generados                             │
│ Buffer programa publicación automática                        │
│ /obsidian-robohogar sync → vault actualizado                  │
└──────────────────────────────────────────────────────────────┘
```

---

*Guía viva — actualizar cuando se complete cada FASE.*
*Fuentes: `docs/plan-v2.md`, `docs/website-brief.md`, `references/newsletter/email-marketing-playbook.md`, research de mercado (abr 2026)*
