# ROBOHOGAR — Website Brief (5 Preguntas)

Basado en scraping real de 5 top performers (2026-04-12).
Análisis detallado en `docs/competitive-analysis.md`.

---

## 1. ¿Para quién es esta web?

**No para ROBOHOGAR. Para el visitante.**

**Persona principal:** Adulto español (30-55 años), interesado en tecnología pero no necesariamente técnico. Está considerando comprar un robot aspirador, ya tiene uno y quiere sacar más partido, o simplemente le fascina la idea de tener robots en casa. Lee Xataka de vez en cuando pero no encuentra contenido específico sobre robótica doméstica en español.

**Lo que le importa ahora mismo:**
- "¿Qué robot aspirador me compro?" (decisión de compra activa)
- "¿Merece la pena un robot cortacésped para mi jardín?"
- "¿Cuándo llegarán los robots humanoides a mi casa y cuánto costarán?"
- "¿Qué está pasando con los robots de Xiaomi/Roborock/Dreame/iRobot?"

**No es:** un ingeniero de robótica (esos leen Weekly Robotics), un inversor en startups (esos leen Not Boring), ni un profesional de automatización industrial (esos leen The Robot Report). Es un **consumidor curioso** que quiere opiniones honestas de alguien que se lo ha probado.

**Dato del scraping:** Ninguno de los 5 top performers atiende al consumidor doméstico en español. Weekly Robotics (5.8K subs, 51% open rate) apunta a ingenieros. we all are robots (17K subs) a "robotics leaders from Google, Tesla, Boston Dynamics". The Robot Report a profesionales B2B. EVwire (13.5K subs) es lo más cercano en modelo (nicho consumer tech) pero es de vehículos eléctricos en inglés.

**El GAP es real y confirmado por scraping.**

---

## 2. ¿Cuál es LA ÚNICA acción que quieres que hagan?

### **Suscribirse a la newsletter.**

Todo lo demás en la página existe para soportar ese único botón. No hay producto que comprar, no hay demo que agendar, no hay app que descargar.

**Formato del formulario:** Un solo campo (email). Sin nombre, sin empresa, sin preferencias. Exactamente como Weekly Robotics: un input + checkbox de consent + botón.

**El botón dice:** "Quiero estar al día" o "Suscribirme gratis"

**Aprendizajes del scraping:**

| Referente | CTA | Campos | Qué funciona |
|---|---|---|---|
| Weekly Robotics | "join newsletter" | 1 (email + consent checkbox) | Simplicidad máxima |
| we all are robots | "Subscribe" | 1 (email) | Tiers visibles desde el hero (free/$5/$49/$149) |
| Not Boring | "Subscribe" | 1 (email) | Content-first: dejan leer antes de pedir |
| EVwire | Signup tribal | 1 (email) | "Read by 13,488 EV geeks" como hook |
| The Robot Report | "GET THE ENEWSLETTER" | 1 (email) | Copy genérico, peor conversión |

**Conclusión:** Un campo. Headline con beneficio + frecuencia. Nada de "GET THE ENEWSLETTER" genérico (Robot Report, score más bajo en CTA). Copiar el modelo Weekly Robotics (simple) con el hook tribal de EVwire.

**Para ROBOHOGAR (fase lanzamiento):** solo free. Sin paywall. El objetivo es masa crítica (500+ subs) antes de monetizar. Monetización futura: sponsorships como Not Boring (no paywall) o tiers como we all are robots.

---

## 3. ¿Qué objeciones tiene el visitante?

| Objeción | Sección que necesitamos | Referente que lo resuelve |
|---|---|---|
| "¿Otro newsletter más? Ya recibo demasiados emails" | **Value prop en hero:** "Quincenal. 5 min. Solo lo que importa." — frecuencia baja = bajo compromiso | Weekly Robotics: semanal, curated, consistente 355+ issues sin fallar |
| "¿Quién eres tú para hablar de robots?" | **Sobre mí:** Entusiasta que prueba robots en casa. Autenticidad > autoridad académica | we all are robots: Lukas Ziegler no es ingeniero, es curador/analista. Funciona. |
| "¿Esto es contenido genérico de IA?" | **Preview de contenido real:** Mostrar extracto de un issue con opinión propia, humor, datos | Not Boring: muestra artículos completos + engagement (343 reactions) como prueba de calidad |
| "¿Es gratis de verdad?" | **Texto explícito:** "100% gratis. Sin spam. Cancela cuando quieras." | Todos los top performers tienen tier gratuito visible |
| "No sé si me interesa la robótica" | **Hook aspiracional:** "Los robots ya están en tu casa. Solo que aún no lo sabes." | EVwire: "Read by 13,488 EV geeks weekly" convierte curiosidad en identidad |

**Secciones resultantes para la landing:**

1. **Hero** — headline con beneficio + frecuencia + CTA email
2. **Preview** — extracto de issue real (demostrar voz/calidad)
3. **Qué recibirás** — 3-4 bullets concretos (noticias curadas, reviews, comparativas, opinión)
4. **Sobre el autor** — foto + 2 líneas (mascota opcional al lado)
5. **Social proof** — stats cuando los tengamos (por ahora: "quincenal, 5 min de lectura")
6. **FAQ** — 3 preguntas (¿Es gratis? ¿Con qué frecuencia? ¿Puedo cancelar?)
7. **Footer** — redes sociales + segundo CTA

---

## 4. ¿Cuál es el vibe?

### **Editorial cálido** — como una revista de tecnología que leerías en el sofá con café.

| Atributo | Lo que significa en práctica | Referente |
|---|---|---|
| **Editorial** | Layout tipo magazine, tipografía con personalidad, espaciado generoso | Not Boring: newspaper layout, Lora serif, categorías de contenido |
| **Cálido** | Fondo crudo `#F5F3EF` (no blanco frío), mascota con personalidad | we all are robots: acento amarillo cálido `#e4f909` contra blanco |
| **Accesible** | Sin jerga técnica, imágenes grandes, mobile-first | EVwire: Poppins (friendly sans-serif), grid responsive Tailwind |
| **Con opinión** | No neutral — punto de vista claro. Reviews con veredicto | Not Boring: "Tech strategy, analysis, and philosophy, but not boring" |

**Si ROBOHOGAR fuera una persona:** Llevaría vaqueros y una camiseta de manga larga, zapatillas cómodas. Tendría un Roborock en casa y lo llamaría por nombre. Sabría explicarte la diferencia entre LiDAR y cámara sin hacerte sentir tonto.

**Design direction basada en scraping:**

| Elemento | ROBOHOGAR | Inspirado en |
|---|---|---|
| Color acento | `#C8FF00` verde lima | we all are robots `#e4f909` — acento vibrante único |
| Fondo | `#F5F3EF` crudo cálido | No blanco puro como Substack. Calidez. |
| Texto | `#0D0D0D` negro | Not Boring `#363737` — alto contraste sin ser harsh |
| Heading font | Syne (Bold) | Diferenciador vs Lora que usan Not Boring + we all are robots |
| Body font | DM Sans | Más moderno que Spectral (serif), más legible que Inter |
| Layout | Hero + content preview + about + FAQ | Híbrido we all are robots (magazine) + Weekly Robotics (minimal) |
| Mascota | Presente en hero, 404, social cards | Ningún competidor tiene mascota — diferenciador visual |

---

## 5. ¿Tienes assets de marca existentes?

### **Sí. Marca definida y assets producidos.**

**Lo que ya tenemos (verificado en repo):**

| Asset | Estado | Ubicación |
|---|---|---|
| Paleta de colores | Definida y documentada | `.claude/rules/design.md` |
| Tipografía | Definida | Syne (títulos) + DM Sans (cuerpo) + JetBrains Mono (code) |
| Mascota (11 poses) | Producida en 2K + 1K | `assets/branding/master/` (11 PNG) + `flash-1K/` (11 PNG) |
| Mascota en contexto | 1 referencia | `assets/branding/con-fondo/robohogar-mascot-referencia.png` |
| Mascota prompt base | Documentado completo | `assets/branding/mascota-prompt.md` (11 poses con prompts exactos) |
| Hero image draft | 1 borrador flash | `assets/images/hero-landing-mascota-hogar.png` |
| Landing prototype | HTML estático | `assets/landing-prototype.html` |
| Tono editorial | Documentado | `.claude/rules/editorial.md` |
| SEO strategy | Documentado | `.claude/rules/seo.md` |
| Asset catalog | Actualizado | `assets/branding/asset-catalog.md` |

**Lo que falta:**

| Asset | Prioridad | Notas |
|---|---|---|
| Logo/wordmark | Alta | "ROBOHOGAR" en Syne Bold + icono derivado de mascota |
| Favicon | Alta | Cabeza de la mascota recortada a 32x32 y 180x180 |
| OG image | Alta | Mascota principal + tagline (1200x630) |
| Newsletter template | Alta | Depende de plataforma elegida |
| Social cards template | Media | Formato reusable para LinkedIn/X/Threads |
| 404 page | Baja | Mascota pensativa + "Esta página se ha ido a cargar el robot" |

**Comparación con competidores:**

| Asset | ROBOHOGAR | we all are robots | Weekly Robotics | EVwire |
|---|---|---|---|---|
| Paleta definida | Sí | Sí (Substack) | No (B&W genérico) | Sí |
| Tipografía custom | Sí (Syne + DM Sans) | Sí (Lora + Spectral) | No | Sí (Poppins + Inter) |
| Mascota/personaje | **Sí (11 poses)** | No | No | No (solo logo plug) |
| Tono documentado | Sí | Implícito | Implícito | Implícito |

**Conclusión:** Estamos más preparados en branding que el 80% de los competidores. La mascota es un diferenciador único — ningún competidor tiene personaje visual. Falta ejecutar: logo, favicon, OG image, y elegir plataforma.

---

## Prompt consolidado (para Relume u otro builder)

```
Company: ROBOHOGAR — newsletter quincenal en español sobre robótica doméstica
(aspiradores, cortacésped, humanoides para el hogar). Audiencia: adultos 
españoles 30-55, curiosos de tecnología, no técnicos. Sin competencia directa
en español. Único en el mercado hispanohablante.

Goal: suscripción a newsletter gratuita. Un solo campo (email) + botón.
Headline formula: beneficio + frecuencia ("Cada 2 semanas, 5 minutos, todo
lo que necesitas saber sobre los robots que llegan a tu casa").

Architecture: 1 SOLA PÁGINA (modelo Weekly Robotics). Sin navegación compleja.
Sin puntos de fuga. Una URL = una decisión (suscribirse o no).
- Homepage/landing: hero + signup + secciones de apoyo + últimos issues
- /issues (auto-generado por plataforma): archivo de newsletters pasadas 
  (actúan como prueba de calidad + contenido SEO)
- 404: mascota pensativa
NO hay página "Sobre mí" separada (va como sección en la landing).
NO hay blog independiente (los artículos SON los issues).
NO hay pricing, contacto, ni categorías separadas.

Sections (orden en la single page):
1. Hero: mascota + headline con beneficio/frecuencia + 1 campo email + botón
2. "Qué recibirás": 3-4 bullets (noticias curadas, reviews, comparativas, opinión)
3. Preview: extracto de un issue real — demostrar voz, opinión, humor
4. Sobre el autor: foto/mascota + 2 líneas. Sin página separada.
5. Social proof: stats cuando las tengamos (por ahora: "quincenal, 5 min")
6. FAQ: 3 preguntas (¿Es gratis? ¿Con qué frecuencia? ¿Puedo cancelar?)
7. Footer: redes sociales + segundo CTA email

Notes:
- Objeciones principales: "otro newsletter más" → enfatizar quincenal + 5 min.
  "quién eres" → autenticidad de entusiasta, no experto. "contenido IA" → 
  preview de issue real con opinión propia. "¿es gratis?" → explícito.
- Vibe: editorial cálido, magazine-style. MIT Tech Review meets tu amigo techie.
- Colores: fondo #FFFFFF, acento naranja #F5A623, negro #0C0C0C,
  gris lightest #F2F2F2, borders rgba(12,12,12,0.15).
- Tipografía: Jost (títulos), DM Sans (cuerpo), JetBrains Mono (code).
- Mascota robot kawaii como diferenciador visual (hero, headers, 404, social).
  11 poses ya producidas en 2K.
- Inspiración principal: Weekly Robotics (1 página, minimal, stats como trust,
  consistencia brutal). Secundaria: EVwire (identidad tribal), we all are robots
  (magazine layout, acento vibrante).
- Mobile-first. SEO-ready. Lazy loading. Schema markup (Organization + NewsArticle).
- NO ads, NO múltiples CTAs, NO sidebar. Foco total en conversión a suscriptor.
```

---

## Top 5 Performers — Resumen

| # | Sitio | Score | Subs | Acento | Typo | Qué copiar |
|---|---|---|---|---|---|---|
| 1 | **Not Boring** | 53/60 | 261K | `#0a4e99` azul | Lora + Spectral | Content-first, dejar que calidad venda, engagement visible |
| 2 | **we all are robots** | 51/60 | 17K | `#e4f909` amarillo | Lora + Spectral | EP.001 numbering, magazine layout, tiers, audio |
| 3 | **EVwire** | 47/60 | 13.5K | `#0ea890` teal | Poppins + Inter | Identidad tribal, live interactive elements, niche puro |
| 4 | **The Robot Report** | 44/60 | N/A | `#D2232A` rojo | Sans genérica | Categorización profunda, awards anuales, podcast |
| 5 | **Weekly Robotics** | 43/60 | 5.8K | B&W | Sans genérica | Stats públicas (51% OR), consistencia, sponsorship model |

Sources:
- [Weekly Robotics](https://www.weeklyrobotics.com/)
- [we all are robots](https://ziegler.substack.com/)
- [Not Boring](https://www.notboring.co/)
- [EVwire](https://evwire.com/)
- [The Robot Report](https://www.therobotreport.com/)
- [Beehiiv Landing Page Examples](https://www.beehiiv.com/blog/10-newsletter-landing-pages-crushing-conversions-in-2025)
- [Not Boring Revenue Analysis](https://growthinreverse.com/packy/)
