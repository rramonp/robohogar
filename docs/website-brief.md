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
- Principal: **"Únete gratis — cada 2 semanas en tu inbox"**
- Alternativo: **"Suscríbete gratis"** (simple como Morning Brew)
- Social proof cuando tengamos datos: "Únete a [X]+ lectores"

**Patrón confirmado:** Los 5 sitios analizados usan 1 campo + CTA visible above the fold.

---

## 3. ¿Qué objeciones tiene el visitante?

| Objeción | Cómo resolverla |
|---|---|
| "Otro newsletter más" | Hero: "Quincenal. 5 min. Solo lo que importa." |
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
- **Social proof con números** cuando los tengamos. Mientras tanto: "Quincenal · 5 min de lectura · Gratis".
- **Mascota en hero** como diferenciador visual (ningún competidor tiene esto).
- **Font pairing con contraste:** Jost (geométrica) vs DM Sans (humanist) ya cumple el patrón.
- **Email input visible** — no detrás de un clic, no al final de la página.

### CTA copy en español

| Contexto | Copy recomendado |
|---|---|
| Botón hero | "Suscríbete gratis" |
| Input placeholder | "tu@email.com" |
| Bajo el botón | "Quincenal. 5 min. Sin spam." |
| Con social proof (futuro) | "Únete a 500+ lectores" |
| Footer CTA | "¿Te lo vas a perder?" + mismo formulario |

### Hero section — diseño específico

```
[Mascota robot]  ROBOHOGAR
                 Los robots ya están en tu casa.
                 Solo que aún no lo sabes.
                 
                 Cada 2 semanas, en 5 minutos: reviews honestos,
                 noticias curadas y opinión sobre robótica doméstica.
                 
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

```
Newsletter sobre robótica doméstica en español. Audiencia: adultos españoles
30-55, curiosos de tecnología. Acento naranja #F5A623 sobre fondo blanco.
Tipografía: Jost (títulos) + DM Sans (cuerpo). Tono: editorial cálido,
como revista tech accesible. Hero con email input visible, CTA "Suscríbete
gratis". JUSTO debajo del hero: sección de artículos destacados con cards
visuales (imagen + título + excerpt) estilo magazine — es lo que retiene
al visitante. Después: qué recibirás (4 bullets), sobre el autor, FAQ
(3 preguntas), footer con segundo CTA. Mobile-first. Sin navegación
compleja. Foco total en conversión a suscriptor.
```

---

Sources:
- [Newsletter Operator](https://newsletteroperator.com/)
- [Morning Brew](https://morningbrew.com/)
- [Milk Road](https://milkroad.com/)
- [The Hustle](https://thehustle.co/)
- [TLDR](https://tldr.tech/)
