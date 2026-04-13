# ROBOHOGAR — Guía de Implementación (micro-pasos)

> Cada paso es una acción concreta. Si una fase no aplica todavía, sáltala — cada FASE es autocontenida.
> Referencia estratégica: `docs/plan-v2.md` · Referencia visual: `docs/website-brief.md`

---

## FASE 0: Beehiiv Setup (30 min)

### Crear cuenta

- [ ] Ir a **https://app.beehiiv.com/signup**
- [ ] Rellenar: nombre → `Rafael`, email → tu email personal, contraseña
- [ ] Publication Name → `ROBOHOGAR`
- [ ] Description → `Robots que llegan (y llegarán) a tu casa. Reviews honestos, noticias curadas y opinión sobre robótica doméstica. Quincenal, 5 min, gratis.`
- [ ] Category → `Technology`
- [ ] Frequency → `Biweekly`

### Subir branding

- [ ] Ir a **Settings → Publication → Branding**
- [ ] Logo: subir `assets/branding/master/robohogar-mascot-principal.png`
- [ ] Favicon: subir la misma imagen (Beehiiv la recorta)
- [ ] Accent color → `#F5A623`
- [ ] Background → `#FFFFFF`
- [ ] Text color → `#0C0C0C`
- [ ] Font: Beehiiv no permite Jost/DM Sans custom en free plan — elegir la sans-serif más limpia disponible (Inter o el default)

### Conectar dominio robohogar.com

- [ ] En Beehiiv: ir a **Settings → Publication → Domains → Add Custom Domain**
- [ ] Escribir `robohogar.com` y pulsar Continue
- [ ] Beehiiv muestra los registros DNS necesarios — déjalos abiertos en una pestaña

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

- [ ] Añadir cada registro en Namecheap: botón **Add New Record** → seleccionar tipo → pegar Host y Value
- [ ] Volver a Beehiiv y pulsar **Verify Domain**
- [ ] Si dice "Pending" — esperar. Propagación DNS: 15 min a 72h (normalmente <2h)

> [!tip]
> Para comprobar propagación: https://dnschecker.org — busca tu dominio y tipo de registro (CNAME, TXT, etc.)

### Configurar email sender

- [ ] En Beehiiv: **Settings → Publication → Sending → Sender Email**
- [ ] Configurar como `hola@robohogar.com` o `robot@robohogar.com`
- [ ] Sender Name → `Rafael de ROBOHOGAR`
- [ ] Reply-to → tu email personal (para recibir respuestas directas)

### DMARC

- [ ] Verificar que el registro TXT `_dmarc` está activo en Namecheap (paso #9 arriba)
- [ ] En Beehiiv, en la sección de Domain, debe aparecer DMARC como ✅ verificado
- [ ] Si no aparece tras 24h, revisar que el Host es exactamente `_dmarc` (sin el dominio, Namecheap añade `.robohogar.com` automáticamente)

---

## FASE 1: Landing Page (1 hora)

### AI Website Builder

- [ ] En Beehiiv: **Website → AI Website Builder** (o Design Mode si no aparece AI)
- [ ] Pegar este prompt exacto:

```
Newsletter sobre robótica doméstica en español. Audiencia: adultos españoles
30-55, curiosos de tecnología. Acento naranja #F5A623 sobre fondo blanco.
Tono: editorial cálido, como revista tech accesible. Hero con email input
visible, CTA "Suscríbete gratis". JUSTO debajo del hero: sección de artículos
destacados con cards visuales (imagen + título + excerpt) estilo magazine.
Después: qué recibirás (4 bullets), sobre el autor, FAQ (3 preguntas),
footer con segundo CTA. Mobile-first. Sin navegación compleja.
Foco total en conversión a suscriptor.
```

- [ ] Pulsar Generate y esperar

### Ajustar sección por sección (Design Mode)

**Hero (above the fold):**
- [ ] Headline → `Los robots ya están en tu casa. Solo que aún no lo sabes.`
- [ ] Subtítulo → `Cada 2 semanas, en 5 minutos: reviews honestos, noticias curadas y opinión sobre robótica doméstica.`
- [ ] Placeholder del input → `tu@email.com`
- [ ] Botón → `Suscríbete gratis` con fondo `#F5A623`, texto `#FFFFFF`
- [ ] Texto bajo botón → `100% gratis · Sin spam · Cancela cuando quieras`
- [ ] Añadir imagen de la mascota: subir `assets/branding/master/robohogar-mascot-saludando.png`

**Artículos destacados (justo bajo el hero):**
- [ ] En Design Mode: añadir bloque **"Recent Posts"** o **"Featured Posts"**
- [ ] Configurar para mostrar 2-3 posts con imagen + título + excerpt
- [ ] Título de sección → `Lo último en ROBOHOGAR`

> [!warning]
> Esta sección estará vacía hasta que publiques los primeros artículos (FASE 2). Publica al menos 2 posts ANTES de compartir la landing públicamente.

**Qué recibirás:**
- [ ] Título → `¿Qué recibirás cada 2 semanas?`
- [ ] 4 bullets:
  - `🤖 La noticia más relevante en robótica doméstica — explicada sin jerga`
  - `🔍 Reviews honestos de robots que ya puedes comprar`
  - `🚀 Avances en humanoides y el futuro del hogar robotizado`
  - `💡 Datos curiosos y el mejor enlace de la quincena`

**Sobre el autor:**
- [ ] Imagen: subir `assets/branding/master/robohogar-mascot-leyendo.png`
- [ ] Texto → `Soy Rafael. Pruebo robots en casa, investigo lo que viene y te cuento lo que merece la pena — sin comunicados de prensa ni hype vacío.`

**FAQ:**
- [ ] Pregunta 1: `¿Con qué frecuencia llega?` → `Cada 2 semanas. Nada de bombardear tu inbox.`
- [ ] Pregunta 2: `¿Es gratis?` → `Sí, 100%. Sin trucos, sin versión premium, sin paywall.`
- [ ] Pregunta 3: `¿Quién escribe esto?` → `Rafael, un entusiasta de la tecnología doméstica que lleva años conviviendo con robots en casa. Opiniones propias, no publi-reportajes.`

**Footer:**
- [ ] Segundo CTA: `¿Te lo vas a perder?` + formulario de email
- [ ] Links a redes cuando estén creadas (FASE 5)

### Mobile testing

- [ ] En Beehiiv Design Mode: usar el icono de preview móvil (📱)
- [ ] Verificar: el formulario de email es visible sin scroll
- [ ] Verificar: las cards de artículos se apilan verticalmente
- [ ] Verificar: el texto es legible (mínimo 16px body)
- [ ] Verificar: el botón CTA es fácil de pulsar con el pulgar (mínimo 44px alto)
- [ ] Publicar la landing: **Website → Publish**

---

## FASE 2: Contenido Base (semana 1-2)

### Welcome email

- [ ] En Beehiiv: **Automations → Welcome Email → Edit**
- [ ] Subject → `Bienvenido/a a ROBOHOGAR 🤖`
- [ ] Contenido:

```
¡Hola!

Soy Rafael, y esto es ROBOHOGAR — tu dosis quincenal sobre los robots
que llegan (y llegarán) a tu casa.

Cada 2 semanas recibirás:
• La noticia más relevante en robótica doméstica
• Reviews sin filtro de robots que puedes comprar hoy
• Un vistazo al futuro: humanoides, IA en el hogar, y lo que viene

Para que no me pierda en tu spam, haz esto:
→ Arrastra este email a tu bandeja principal
→ Añade hola@robohogar.com a tus contactos

Mientras tanto, empieza por aquí:
👉 [¿Qué robot aspirador compro en 2026?](URL_DEL_ARTICULO_1)

Si tienes un robot en casa y quieres contarme tu experiencia,
responde a este email — los leo todos.

Un saludo robótico,
Rafael
ROBOHOGAR
```

- [ ] Pulsar **Save & Activate**

### Reminder email (4-6h post-signup)

- [ ] En **Automations → Create Automation**
- [ ] Trigger → `New Subscriber`
- [ ] Delay → `6 hours`
- [ ] Action → Send Email
- [ ] Subject → `¿Todo bien por ahí? 🤖`
- [ ] Contenido:

```
¡Hola de nuevo!

Solo quería asegurarme de que recibiste bien el email de bienvenida.

Una pregunta rápida: ¿tienes algún robot en casa? ¿Aspirador,
friegasuelos, cortacésped?

Respóndeme con una línea — me ayuda a saber qué contenido te
interesa más.

Y si aún no lo has leído:
👉 [Los 5 robots humanoides que llegarán a tu casa](URL_DEL_ARTICULO_2)

¡Nos leemos en la próxima!
Rafael
```

- [ ] **Save & Activate**

### Artículo 1: "¿Qué robot aspirador compro en 2026?"

**Estructura SEO:**
- [ ] En Beehiiv: **Posts → Create Post**
- [ ] Title (H1) → `¿Qué robot aspirador me compro en 2026? Guía sin rodeos`
- [ ] SEO Title (Settings → SEO) → `Mejor robot aspirador 2026 — Guía de compra honesta`
- [ ] Meta description → `Comparativa de los mejores robots aspiradores de 2026. Sin publi, sin hype — solo cuál merece tu dinero según uso y presupuesto.`
- [ ] URL slug → `mejor-robot-aspirador-2026`
- [ ] Estructura del artículo:
  - H2: `¿Qué necesitas realmente?` (3 perfiles de usuario)
  - H2: `Mi top 3 por rango de precio` (cada uno con H3: nombre del modelo)
  - H2: `¿Y los que NO recomiendo?`
  - H2: `Veredicto final`
- [ ] Incluir links de afiliado Amazon en cada modelo mencionado (ver FASE 6)
- [ ] Imágenes: fotos de producto de Amazon (o propias), alt text descriptivo
- [ ] Mínimo 1.000 palabras
- [ ] Añadir internal link al artículo 3 cuando esté publicado

**Email gating (lead magnet):**
- [ ] En el post editor → **Settings → Content Gating**
- [ ] Activar **Web Content Gating**
- [ ] Seleccionar: mostrar los primeros ~3 párrafos, luego pedir email para seguir leyendo
- [ ] Esto convierte el artículo en lead magnet automático sin crear nada extra

**Publicar:**
- [ ] Settings → **Publish as web post** (NO como email)
- [ ] Audience → Public (para SEO)
- [ ] Pulsar **Publish**

### Artículo 2: "5 robots humanoides que llegarán a tu casa"

- [ ] Create Post
- [ ] Title → `Los 5 robots humanoides que llegarán a tu casa antes de 2030`
- [ ] SEO Title → `Robots humanoides para casa — 5 que llegarán antes de 2030`
- [ ] Meta desc → `Figure, Optimus, Unitree, 1X Neo y Xiaomi CyberOne. Cuáles son reales, cuáles humo, y cuándo podrías tener uno en el salón.`
- [ ] Slug → `robots-humanoides-casa-2030`
- [ ] Estructura: H2 por cada robot, H2 opinión personal final
- [ ] SIN email gating — este es contenido editorial abierto para SEO
- [ ] SIN links de afiliado (no hay producto a la venta)
- [ ] Publicar como web post

### Artículo 3: "Mi experiencia con robots en casa"

- [ ] Title → `Así es convivir con un robot: mi experiencia real`
- [ ] SEO Title → `Convivir con robots en casa — experiencia real`
- [ ] Meta desc → `Llevo años con robots en casa. Te cuento qué funciona, qué no, y qué cambiaría si empezara de cero.`
- [ ] Slug → `experiencia-robots-casa`
- [ ] Tono personal y honesto — este artículo construye confianza
- [ ] Publicar como web post, sin gating

### SEO checklist por artículo

- [ ] H1 contiene keyword principal
- [ ] H2/H3 usan variaciones semánticas
- [ ] Meta description < 155 caracteres, incluye CTA implícito
- [ ] URL slug corto, sin stop words
- [ ] Alt text en todas las imágenes
- [ ] Al menos 2 internal links a otros artículos propios
- [ ] Mínimo 800 palabras

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
- [ ] Programar envío: **Schedule** → elegir día y hora (martes o jueves, 9:00 AM CET)

### Backup

- [ ] Copiar el contenido final (markdown) a `content/published/2026-XX-XX-issue-01.md` en el repo
- [ ] En Obsidian: mover el borrador de `02-Drafts/` a `03-Published/`

---

## FASE 5: Social Media Setup

### Instagram

- [ ] Descargar Instagram (si no lo tienes) o ir a instagram.com
- [ ] Crear cuenta nueva: username `robohogar_es`
- [ ] Convertir a cuenta profesional: Settings → Account → Switch to professional → Creator → Technology
- [ ] Foto de perfil: `assets/branding/master/robohogar-mascot-principal.png`
- [ ] Bio:

```
🤖 Robots que llegan a tu casa
📬 Newsletter quincenal gratis
🔍 Reviews · Noticias · Opinión
👇 Suscríbete
```

- [ ] Link en bio → `https://robohogar.com`
- [ ] Primeros 3 Reels (ideas):
  1. "3 robots que ya puedes tener en casa por menos de 300€" (15s, texto animado sobre B-roll)
  2. "Este robot humanoid sirve café" (clip viral + comentario en texto)
  3. "El error que todos cometen al comprar un robot aspirador" (hook fuerte, 20s)

> [!tip]
> Primeros 3 segundos del Reel son críticos — empieza con un hook visual o texto que detenga el scroll. Objetivo: 60%+ de retención. Duración ideal: 7-30 segundos.

### LinkedIn

- [ ] Usar tu perfil personal de LinkedIn (no crear company page — el alcance orgánico de páginas es muy bajo)
- [ ] Añadir a la bio/headline: `...| Fundador de ROBOHOGAR 🤖`
- [ ] Primer post (plantilla):

```
He lanzado ROBOHOGAR — una newsletter quincenal sobre los robots
que llegan a nuestras casas.

¿Por qué? Porque en español no hay nadie que cubra robótica doméstica
para consumidores normales. Ni un solo newsletter.

Cada 2 semanas: reviews sin filtro, noticias curadas, y opinión sobre
el futuro del hogar robotizado.

100% gratis. Sin spam.

👉 Link en primer comentario

¿Tienes un robot en casa? Cuéntame cuál en los comentarios.
```

- [ ] Publicar el link a `robohogar.com` en el PRIMER COMENTARIO (no en el post — LinkedIn penaliza links en el cuerpo)

### WhatsApp Channel

- [ ] Abrir WhatsApp → Updates (pestaña) → Channels → botón `+` → **Create Channel**
- [ ] Nombre: `ROBOHOGAR 🤖`
- [ ] Descripción: `Newsletter quincenal sobre robótica doméstica. Reviews, noticias y opinión. robohogar.com`
- [ ] Foto: mascota principal
- [ ] Primer mensaje:

```
¡Bienvenido/a a ROBOHOGAR! 🤖

Aquí compartiré:
• Resúmenes de cada newsletter
• Noticias urgentes de robótica doméstica
• Links a reviews y guías

📬 Para la versión completa, suscríbete gratis:
robohogar.com
```

> [!tip]
> WhatsApp Channels tiene ~98% de tasa de apertura. Es unidireccional (broadcast), perfecto para notificaciones de nuevo contenido sin gestionar comunidad.

### Buffer

- [ ] Ir a **https://buffer.com** → Sign up (plan gratuito: 3 canales, 10 posts/canal)
- [ ] Conectar: Instagram, LinkedIn, y 1 canal más (X/Twitter si decides usarlo)
- [ ] Configurar horarios de publicación:
  - Instagram: Lunes/Miércoles/Viernes 12:00 CET
  - LinkedIn: Martes/Jueves 9:00 CET
- [ ] Cada vez que publiques newsletter → crear 2-3 posts derivados y programarlos en Buffer

### Canva Brand Kit

- [ ] Ir a **https://canva.com** → Sign up / Login
- [ ] **Brand Kit** (disponible en free con limitaciones):
  - Subir logo: mascota principal
  - Color primario: `#F5A623`
  - Color texto: `#0C0C0C`
  - Color fondo: `#FFFFFF`
  - Color secundario: `#F2F2F2`
- [ ] Buscar templates: `tech newsletter instagram` → elegir 2-3 que encajen con el estilo editorial
- [ ] Adaptar con colores ROBOHOGAR y guardar como templates propios

### ManyChat (cuando tengas >100 seguidores en IG)

- [ ] Ir a **https://manychat.com** → Sign up (free hasta 1.000 contactos)
- [ ] Conectar cuenta de Instagram
- [ ] Crear automation: **"Comment to get"**
  - Trigger: comentario con keyword `ROBOT` en un Reel
  - Action: enviar DM automático con link a la guía de compra (artículo 1)
  - Mensaje DM: `¡Hola! 🤖 Aquí tienes la guía: [link]. Y si quieres recibirla quincenal, suscríbete gratis en robohogar.com`
- [ ] Publicar un Reel con CTA: "Comenta ROBOT y te envío mi guía de compra"

> [!tip]
> 90% de tasa de apertura en DMs de Instagram. Mucho más efectivo que el link en bio.

---

## FASE 6: Monetización Inicial

### Amazon Afiliados España

- [ ] Ir a **https://afiliados.amazon.es**
- [ ] Pulsar **Únete ahora gratis**
- [ ] Rellenar datos personales (necesitas datos fiscales / NIF español)
- [ ] Website → `robohogar.com`
- [ ] Descripción del sitio → `Newsletter y blog sobre robótica doméstica: reviews, comparativas y guías de compra de robots aspiradores, friegasuelos, cortacéspedes y humanoides.`
- [ ] Categorías → Electrónica, Hogar
- [ ] Método de pago → transferencia bancaria (requiere IBAN)

> [!warning]
> Tienes **180 días** para generar al menos 1 venta o Amazon cierra la cuenta. Publica la guía de compra con links de afiliado cuanto antes.

**Comisiones relevantes:**
| Categoría | Comisión |
|---|---|
| Electrónica | 3% |
| Hogar y cocina | 3-7% |
| Aspiradoras | ~3% |

**Cookie window:** 24h desde el clic. Si el usuario añade al carrito, 89 días.

**Las mejores conversiones:** comparativas "X vs Y" y guías de compra (no reviews individuales).

### Insertar links de afiliado en artículos

- [ ] En Amazon Afiliados → **SiteStripe** (barra de herramientas en Amazon cuando estás logueado)
- [ ] Buscar el producto → clic en **Text** en SiteStripe → copiar el link corto
- [ ] En el artículo de Beehiiv: insertar como hyperlink normal en el nombre del producto

> [!warning]
> **NUNCA** pongas links de afiliado directamente en emails. Amazon puede cerrarte la cuenta. Los links van en los artículos WEB, y el email enlaza al artículo.

### Páginas legales obligatorias

Crear 3 páginas en Beehiiv (**Website → Pages → Add Page**):

**Aviso Legal** (slug: `aviso-legal`):
```
AVISO LEGAL

Titular: [Tu nombre completo]
NIF: [Tu NIF]
Email: hola@robohogar.com
Dominio: robohogar.com

Este sitio web es un proyecto personal de divulgación sobre robótica doméstica.
El contenido es informativo y refleja opiniones personales del autor.
```

**Política de Privacidad** (slug: `privacidad`):
```
POLÍTICA DE PRIVACIDAD

Responsable: [Tu nombre]
Finalidad: Envío de newsletter quincenal sobre robótica doméstica.
Legitimación: Consentimiento del interesado.
Destinatarios: Beehiiv Inc. (proveedor de email marketing, servidores en EEUU,
adherido a las cláusulas contractuales tipo de la UE).
Derechos: Acceso, rectificación, supresión, portabilidad. Escribe a hola@robohogar.com.
Baja: Link de cancelación en cada email.

No compartimos datos con terceros con fines comerciales.
```

**Disclosure de afiliados** (añadir al footer de cada artículo con links de afiliado):
```
En calidad de Afiliado de Amazon, obtengo ingresos por las compras adscritas
que cumplen los requisitos aplicables. Los precios y disponibilidad de los
productos pueden variar.
```

- [ ] Añadir link a Aviso Legal y Privacidad en el footer de la landing

### Picos de conversión (planificar contenido)

- [ ] **Prime Day** (julio): publicar comparativas 1-2 semanas antes
- [ ] **Black Friday** (noviembre): idem, actualizar precios día del evento
- [ ] **Navidad** (diciembre): "Guía de regalos tech: robots para casa"
- [ ] Marcar estas fechas en el calendario editorial de Obsidian

---

## FASE 7: Automatización

### Research aggregator

- [ ] Fuentes RSS para el script (`utilities/research_aggregator.py`):

```python
RSS_FEEDS = [
    "https://www.therobotreport.com/feed/",
    "https://spectrum.ieee.org/feeds/topic/robotics.rss",
    "https://weeklyrobotics.com/feed.xml",
    "https://www.xataka.com/tag/robots/feed",
    "https://www.xatakahome.com/feed",
    "https://global.roborock.com/blogs/news.atom",
    "https://www.dreametech.com/blogs/news.atom",
    "https://techcrunch.com/tag/robotics/feed/",
]
```

- [ ] Pipeline quincenal (día antes de escribir newsletter):
  1. Ejecutar aggregator → genera `content/drafts/YYYY-MM-DD-raw-digest.md`
  2. Revisar manualmente (15 min) → seleccionar 5-6 noticias
  3. Usar Claude Code para generar borrador con el template del newsletter
  4. Editar con voz propia (30-45 min)
  5. Publicar en Beehiiv
  6. Mover a `content/published/`

### Flujo social media (post-newsletter)

De cada newsletter publicado, generar:
- [ ] 1 Reel de IG: noticia principal con texto animado (Canva template)
- [ ] 1 post de LinkedIn: resumen + opinión + link en primer comentario
- [ ] 1 mensaje en WhatsApp Channel: resumen de 3 líneas + link al issue web

Programar los 3 en Buffer el mismo día de publicación.

### Calendario editorial en Obsidian

- [ ] Cadencia: newsletter cada 2 semanas, en martes
- [ ] Calendario:
  - Semana A (lunes): Research Digest → selección de temas
  - Semana A (martes-miércoles): Borrador con Claude Code → edición personal
  - Semana A (jueves): Publicar + crear posts sociales
  - Semana B: Escribir artículo evergreen SEO + 2-3 Reels

---

## FASE 8: Métricas y Revisión

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

*Guía viva — actualizar cuando se complete cada FASE.*
*Fuentes: `docs/plan-v2.md`, `docs/website-brief.md`, research de mercado (abr 2026)*
