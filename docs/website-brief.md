# ROBOHOGAR — Website Brief (5 Preguntas + Guía Beehiiv)

Basado en scraping de 5 landing pages top (2026-04-13):
Newsletter Operator, Morning Brew, Milk Road, The Hustle, TLDR.

---

## 1. ¿Para quién es esta web?

**Persona principal:** Adulto español (30-55), curioso de tecnología, no técnico.
Busca: "¿Qué robot aspirador me compro?", "¿Merece la pena un cortacésped robot?",
"¿Cuándo llegarán los humanoides a mi casa?".

**No es:** ingeniero de robótica, inversor, ni profesional B2B.
Es un **consumidor curioso** que quiere opiniones honestas.

**El GAP:** Ningún newsletter en español cubre robótica doméstica para consumidores.

---

## 2. ¿Cuál es LA ÚNICA acción?

### Suscribirse a la newsletter.

**Formato:** Un solo campo (email) + botón. Sin nombre, sin empresa.

**CTA recomendado (basado en research):**
- Principal: **"Únete gratis — cada semana en tu inbox"**
- Alternativo: **"Suscríbete gratis"** (simple como Morning Brew)
- Social proof cuando tengamos datos: "Únete a [X]+ lectores"

**Patrón confirmado:** Los 5 sitios analizados usan 1 campo + CTA visible above the fold.

---

## 3. ¿Qué objeciones tiene el visitante?

| Objeción | Cómo resolverla |
|---|---|
| "Otro newsletter más" | Hero: "Semanal. 5 min. Solo lo que importa." |
| "¿Quién eres?" | Sección autor: entusiasta que prueba robots en casa |
| "¿Contenido genérico de IA?" | Preview de issue real con opinión y humor |
| "¿Es gratis?" | Texto explícito: "100% gratis. Sin spam. Cancela cuando quieras." |
| "No sé si me interesa" | Hook: "Los robots ya están en tu casa. Solo que aún no lo sabes." |

**Secciones resultantes (orden crítico — content-first):**
1. Hero — headline + CTA email (above the fold)
2. **Artículos destacados** — 2-3 cards visuales con artículos reales publicados en Beehiiv. Imagen + título + excerpt + "Leer →". Formato magazine atractivo. **Esta sección es la que retiene al visitante** — demuestra calidad del contenido antes de pedir la suscripción.
3. Qué recibirás — 3-4 bullets concretos
4. Sobre el autor — 2 líneas + mascota
5. Social proof — stats o frecuencia/duración
6. FAQ — 3 preguntas cortas
7. Footer — redes + segundo CTA

**Principio:** Enseñar antes de pedir. El visitante necesita ver contenido REAL atractivo justo después del hero. Si ve solo texto informativo sin artículos, se va.

---

## 4. ¿Cuál es el vibe?

### **Editorial cálido** — revista de tech que lees en el sofá con café.

| Atributo | En práctica | Referente |
|---|---|---|
| Editorial | Tipografía con contraste heading/body, espaciado generoso | Morning Brew (serif vs sans), The Hustle (Oswald condensado) |
| Cálido | Acento naranja #F5A623, fondo blanco limpio | Newsletter Operator (#FB8500, fondo #FFFCF9) |
| Accesible | Sin jerga, imágenes grandes, mobile-first | TLDR (Nunito friendly, layout minimal) |
| Con opinión | Punto de vista claro, veredictos en reviews | The Hustle (bold, directo) |

**Paleta:** Fondo #FFFFFF, acento #F5A623, texto #0C0C0C, gris #F2F2F2, border rgba(12,12,12,0.15).
**Tipografía:** Jost (títulos) + DM Sans (cuerpo). Contraste heading/body confirmado como patrón universal.

---

## 5. ¿Tienes assets de marca?

### Sí. Marca definida y assets producidos.

| Asset | Estado | Ubicación |
|---|---|---|
| Paleta de colores | Definida | `.claude/rules/design.md` |
| Tipografía | Jost + DM Sans + JetBrains Mono | `.claude/rules/design.md` |
| Mascota (11 poses) | 2K + 1K producidas | `assets/branding/master/` |
| Mascota prompt base | Documentado | `assets/branding/mascota-prompt.md` |
| Landing prototype | HTML estático | `assets/landing-prototype.html` |
| Tono editorial | Documentado | `.claude/rules/editorial.md` |

**Assets pendientes:** ver `docs/assets-needed.md`.

**Ventaja competitiva:** La mascota robot es un diferenciador — ningún competidor tiene personaje visual.

---

## 6. Estética del blog Beehiiv

### Configuración de colores en Beehiiv

| Elemento | Valor | Nota |
|---|---|---|
| Primary/Accent | `#F5A623` | Botones, links, highlights |
| Background | `#FFFFFF` | Blanco limpio (como Morning Brew, Milk Road) |
| Text | `#0C0C0C` | Negro alto contraste |
| Secondary bg | `#F2F2F2` | Secciones alternadas, inputs |
| Border-radius | 6-8px | Newsletter Operator usa 6px, The Hustle 8px |

### Layout — qué hacer

- **Hero above the fold:** headline + descripción + email input + botón.
  Patrón universal en los 5 sitios analizados.
- **Artículos destacados JUSTO después del hero.** 2-3 cards con imagen, título y excerpt.
  Formato magazine visual. **Es lo que retiene al visitante** — sin contenido real visible,
  la página es aburrida y el visitante se va. Beehiiv puede mostrar posts recientes automáticamente.
- **Un solo color vibrante (#F5A623)** para CTAs. El resto neutro (blanco/negro/gris).
- **Social proof con números** cuando los tengamos. Mientras tanto: "Semanal · 5 min de lectura · Gratis".
- **Mascota en hero** como diferenciador visual (ningún competidor tiene esto).
- **Font pairing con contraste:** Jost (geométrica) vs DM Sans (humanist) ya cumple el patrón.
- **Email input visible** — no detrás de un clic, no al final de la página.

### CTA copy en español

| Contexto | Copy recomendado |
|---|---|
| Botón hero | "Suscríbete gratis" |
| Input placeholder | "tu@email.com" |
| Bajo el botón | "Semanal. 5 min. Sin spam." |
| Con social proof (futuro) | "Únete a 500+ lectores" |
| Footer CTA | "¿Te lo vas a perder?" + mismo formulario |

### Hero section — diseño específico

```
[Mascota robot]  ROBOHOGAR
                 Tu dosis de robótica doméstica
                 
                 Te lo contamos cada semana · Gratis, honesto y en español
                 
                 [tu@email.com] [Suscríbete gratis]
                 
                 100% gratis · Sin spam · Cancela cuando quieras
```

### Qué NO hacer (anti-patrones)

- **NO usar CTA genérico** tipo "Subscribe" o "GET THE NEWSLETTER" — personalizar siempre
- **NO poner múltiples colores vibrantes** — solo #F5A623, el resto neutro
- **NO ocultar el formulario** detrás de scroll o clics
- **NO añadir navegación compleja** — 1 página, 1 decisión
- **NO usar fondo oscuro** — ROBOHOGAR es cálido, no tech-frío (TLDR usa dark, no es nuestro vibe)
- **NO saturar con secciones** — máximo 7 secciones en la landing

### Qué robar de cada sitio

| Sitio | Qué copiar | Qué evitar |
|---|---|---|
| **Newsletter Operator** | Fondo cálido, acento naranja en input border, social proof en CTA | — |
| **Morning Brew** | Simplicidad del CTA ("Subscribe"), estética editorial limpia | Tono frío/corporativo |
| **Milk Road** | Pill buttons modernos, tono playful-pero-pro | Teal no encaja con nuestra paleta |
| **The Hustle** | Headlines grandes y bold, social proof "2M+" prominente, rojo acción | Demasiado agresivo para nuestro tono |
| **TLDR** | Layout minimal, friendly font, foco en contenido | Dark theme, tono demasiado tech |

---

## Prompt para Beehiiv AI Builder

Usar en **Website → AI Website Builder**. Pegar íntegro:

```
Build a newsletter landing page for ROBOHOGAR, a Spanish-language weekly 
newsletter about home robotics (robot vacuums, lawnmowers, humanoid robots).

BRAND:
- Primary accent color: #F5A623 (amber/orange). Use ONLY this color for buttons, 
  links, highlights. Everything else is neutral: white background, #0C0C0C text, 
  #F2F2F2 secondary backgrounds.
- Tone: warm editorial, like a tech magazine you'd read on the couch with coffee.
  NOT cold/corporate. NOT dark theme.
- We have a robot mascot character (will upload images manually after generation).

PAGE STRUCTURE (this exact order, based on top-performing newsletter landings):

SECTION 1 — HERO (above the fold, most important):
- Left side: headline + subtitle + email signup form + trust text
- Headline: "Tu dosis de robótica doméstica"
- Subtitle: "Te lo contamos cada semana · Gratis, honesto y en español"
- Email input field with placeholder "tu@email.com"
- Submit button: "Suscríbete gratis" in amber #F5A623
- Below button: "100% gratis · Sin spam · Cancela cuando quieras" in small gray text
- Right side: space for mascot image (I'll upload after)
- Reference: Newsletter Operator uses hero with social proof tagline + single email 
  field. Copy that simplicity.

SECTION 2 — FEATURED ARTICLES (immediately after hero):
- Title: "Lo último en ROBOHOGAR"
- Show 3 most recent posts as visual cards: image + title + excerpt + "Leer →" link
- Cards should have subtle border, 12-16px border-radius, hover shadow effect
- Grid: 3 columns desktop, 1 column mobile
- Reference: Newsletter Operator shows "Featured" section with 3 article thumbnails 
  right after hero. The Hustle shows "Top Stories" with images. TLDR shows featured 
  stories with category badges. Copy the pattern of showing REAL content immediately 
  after the signup form — this is what retains visitors.

SECTION 3 — WHAT YOU'LL GET:
- Title: "¿Qué recibirás cada semana?"
- 4 items with icons:
  • "Lo que ha pasado en robótica doméstica, sin tecnicismos"
  • "Reviews sin filtro de robots que ya están a la venta"
  • "Humanoides y el futuro de tu casa robotizada"
  • "Un dato curioso que no conocías cada semana"
- Reference: Morning Brew uses "Become smarter in 5 minutes" — clear value prop. 
  TLDR uses a numbered list of what each issue contains.

SECTION 4 — ABOUT THE AUTHOR:
- Small section, not too long
- Image placeholder on left (mascot reading pose)
- Text: "Soy Rafael. Pruebo robots en casa, investigo lo que viene y te cuento 
  lo que merece la pena — sin comunicados de prensa ni hype vacío."
- Keep it human, authentic, short

SECTION 5 — FAQ (3 questions, accordion style):
- "¿Con qué frecuencia llega?" → "Cada semana. Nada de bombardear tu inbox."
- "¿Es gratis?" → "Sí, 100%. Sin trucos, sin versión premium, sin paywall."
- "¿Quién escribe esto?" → "Rafael, entusiasta de la tecnología doméstica que 
  lleva años conviviendo con robots. Opiniones propias, no publi-reportajes."

SECTION 6 — FINAL CTA (before footer):
- Title: "¿Te lo vas a perder?"
- Subtitle: "Tu primer issue llega esta semana."
- Repeat email signup form
- Reference: All 5 top newsletters have a second CTA before footer. Morning Brew 
  repeats "Become smarter in 5 minutes" with phone mockup. Copy this repetition.

SECTION 7 — FOOTER:
- Logo text "ROBOHOGAR"
- Social links (Instagram, LinkedIn, X, YouTube, RSS)
- Copyright 2026
- Legal links (Privacidad, Términos)

DESIGN RULES:
- Maximum 7 sections total. No more.
- ONE vibrant color (#F5A623) for all CTAs. Everything else neutral.
- Email signup form must appear AT LEAST twice (hero + final CTA).
- Border-radius: 6-8px for cards and buttons (not rounded pill, not sharp square).
- Generous whitespace between sections. Don't crowd.
- Mobile-first: everything must stack cleanly on 375px screens.
- No complex navigation. No sidebar. No mega menus.
- The page has ONE job: convert visitors to email subscribers.
```

### Después de generar: ajustes manuales en Design Mode

El AI Builder genera una base. Ajustar manualmente:

| Elemento | Ajuste | Por qué |
|---|---|---|
| Hero headline | Verificar tamaño ≥36px desktop, ≥24px móvil | The Hustle usa 54px — headlines grandes convierten |
| Botón CTA | Verificar contraste texto blanco sobre #F5A623 | Newsletter Operator usa naranja similar con texto oscuro — probar ambos |
| Cards artículos | Verificar que muestran imagen + título + excerpt | Si solo muestra títulos, cambiar a layout "card" en las opciones del bloque |
| Spacing entre secciones | Mínimo 48px, máximo 80px | Supahub y Newsletter Operator usan spacing generoso pero no excesivo |
| Footer CTA | Debe ser idéntico al hero CTA | Mismo campo, mismo botón, mismo copy — consistencia |
| Mobile preview | Verificar con el icono 📱 del editor | Formulario visible sin scroll, cards apiladas, botón fácil de pulsar |

### Checklist de calidad visual

- [ ] ¿El formulario de email es visible sin hacer scroll? (above the fold)
- [ ] ¿Hay artículos reales visibles justo después del hero?
- [ ] ¿El botón CTA destaca claramente del resto? (único elemento naranja)
- [ ] ¿La mascota aparece en al menos 2 sitios? (hero + about)
- [ ] ¿El mobile se ve limpio? (texto legible, botón pulsable, sin overflow)
- [ ] ¿Hay al menos 2 formularios de signup? (hero + footer)
- [ ] ¿Las FAQ resuelven las 3 objeciones principales?

---

Sources:
- [Newsletter Operator](https://newsletteroperator.com/)
- [Morning Brew](https://morningbrew.com/)
- [Milk Road](https://milkroad.com/)
- [The Hustle](https://thehustle.co/)
- [TLDR](https://tldr.tech/)
