# Email Marketing Playbook — ROBOHOGAR

> Referencia unificada de best practices para newsletter y email marketing.
> Fuentes: beehiiv State of Newsletters 2026 (28B emails) + Email Marketing Bible V2 (908 fuentes, 68K palabras).
> Curado para: newsletter quincenal en español sobre robótica doméstica, Beehiiv free plan, audiencia España/EU + LATAM.
> Consultar desde: `/content-draft` (tipo Newsletter), diseño de templates, optimización de envíos.

---

## 1. Benchmarks & KPIs

### Benchmarks beehiiv 2025 (28B emails, 255M+ lectores)

| Métrica | 2025 | 2024 | Objetivo ROBOHOGAR |
|---|---|---|---|
| Open Rate | 41.24% | 37.67% | >45% (nicho = mejor que media) |
| Click-Through Rate | 3.23% | 4.74% | >5% (contenido de valor) |
| Delivery Rate | 98.90% | 98.31% | >98% |
| Bounce Rate | 1.48% | 1.64% | <2% |
| Spam Complaint Rate | 0.02% | 0.04% | <0.05% |

> Nota: CTR bajó porque los lectores consumen dentro del email (no hacen clic fuera).
> Nota: Open rates inflados por Apple MPP — usar click-based metrics como primario.

### Benchmarks generales por tipo de email

| Tipo | Open Rate | CTR | Objetivo |
|---|---|---|---|
| Welcome series | 50-60% | 5-8% | Conversión, RPR 2.5x |
| Newsletter | 20-30% (genérico) / 41%+ (beehiiv) | 3-5% | >40% open, >5% CTR |
| Promotional | 15-20% | 2-3% | Revenue, CTR |
| Win-back | 10-15% | 1-2% | Reactivación |

### KPIs para ROBOHOGAR por fase

| Fase | Subs | Open Rate | CTR | Revenue |
|---|---|---|---|---|
| Mes 3 | 100 | >50% | >10% | €0 |
| Mes 6 | 300 | >50% | >8% | €50 (afiliado) |
| Mes 12 | 1,000 | >45% | >6% | €200+ |

### Umbrales de salud

| Métrica | Sano | Warning | Crítico |
|---|---|---|---|
| Bounce Rate | <2% | 2-5% | >5% |
| Complaint Rate | <0.05% | 0.05-0.1% | >0.1% |
| Unsub Rate | <0.3% | 0.3-0.5% | >0.5% |
| List Growth | >2%/mes | 0-2% | Negativo |

### Crecimiento de newsletters nuevos (mediana beehiiv 2025)

- Mes 1: **482 suscriptores**
- Año 1: **8,314 suscriptores** (17x)
- Días al primer dólar: **66 días**
- Revenue paid subs 2025: **$19M** (+138% vs 2024)

---

## 2. Growth Stack

Canales ordenados por impacto, filtrados a lo disponible en beehiiv:

| # | Canal | Impacto | Disponible en free plan | Notas |
|---|---|---|---|---|
| 1 | **Recommendations** | 2.75x crecimiento | ✅ | Cross-promo con newsletters de tech/hogar. Activar primero |
| 2 | **Referral Program** | +30-40% growth | ✅ (básico) | Recompensas: contenido exclusivo, mención en newsletter |
| 3 | **Lead magnets** | +384% signups | ✅ (content gating) | Templates/guías > ebooks. "Get my guide" > "Subscribe" (+33%) |
| 4 | **Content gating** | Alta conversión | ✅ | Artículos con email gate a mitad — convierte sin crear nada extra |
| 5 | **Pop-ups** | 3-5% conversión | ✅ (básico) | Exit-intent: 4-7%. Two-step: +30-50% mejor |
| 6 | **Boosts** | +84 subs/mes avg | ❌ (paid) | Comprar subs verificados de otros newsletters |
| 7 | **Magic Links** | Bajo fricción | ✅ | One-click subscribe para redes, partnerships |
| 8 | **Cadencia consistente** | Compound | ✅ | 1-3x/semana. Consistencia > cantidad |

### List building data

- Popups bien cronometrados: 3-5% conversión (top 10%: 9.28%)
- Exit-intent: 4-7% (top 10%: 12%+)
- Content upgrades: 5-15% (5-10x mejor que formulario genérico)
- Squeeze page: 20-30%
- Homepage: 1-3%
- Footer: 0.1-0.5%

### Higiene de lista

- Las listas decaen 22-30% anual. Suscriptores inactivos cuestan dinero Y dañan deliverability.
- **Sunset flow:** Reducir frecuencia → serie re-engagement (2-3 emails) → suprimir no-respondedores.
- **Spam traps:** Pristine (honeypots), recycled (direcciones abandonadas), typo (gnail.com), role-based (info@).
- **Prevención:** Doble opt-in, validación en signup, limpieza regular, envío basado en engagement.

---

## 3. Welcome Series (6 emails)

Open rate: 51-55%. Revenue: 320% más por email vs promocional.
Adaptada al contexto ROBOHOGAR:

| # | Timing | Contenido | Objetivo |
|---|---|---|---|
| 1 | Inmediato | Bienvenida + link al mejor artículo + pedir arrastar a bandeja principal + pedir respuesta | Confirmar, deliverability |
| 2 | Día 1 | Pregunta de engagement: "¿Tienes robot en casa? ¿Cuál?" | Segmentar, generar reply (ISP signal) |
| 3 | Día 3 | Artículo editorial (humanoides/futuro) — muestra el 30% editorial | Construir marca |
| 4 | Día 5 | Guía de compra — muestra el 70% práctico | Demostrar valor |
| 5 | Día 10 | Experiencia personal con robots — genera confianza | Autenticidad |
| 6 | Día 14 | Resumen de lo que viene + CTA referral + link preferencias | Retener, crecer |

> Beehiiv free plan: solo welcome email + reminder. La serie completa de 6 requiere plan de pago (Automations).
> Mientras tanto: welcome email (email 1) + reminder 6h (email 2) cubren lo esencial.

---

## 4. Subject Lines & Copywriting

### Subject lines

- **<25 caracteres** = mejores opens
- Personalización (nombre): +14% opens
- First-person CTA > second-person: +25-35%
- Preguntas y curiosity gaps funcionan
- Evitar: trigger words de spam, puntuación excesiva, ALL CAPS
- 64% decide abrir basándose solo en el subject

### Frameworks de copywriting

| Framework | Estructura | Mejor para |
|---|---|---|
| **1-3-1** | 1 intro + 3 items + 1 CTA | Newsletters (EL framework) |
| **PAS** | Problema → Agitar → Solución | Reviews, comparativas |
| **BAB** | Before → After → Bridge | Casos de uso, testimonios |
| **AIDA** | Atención → Interés → Deseo → Acción | Promocional, lanzamientos |

### Reglas de copy

- Pirámide invertida: mensaje clave primero. Párrafos cortos.
- Ratio 3:1: tres emails de valor por cada uno promocional.
- Escribe, luego corta 30%.
- **CTAs:** Botones > texto (+27% CTR). CTA único: +42% vs múltiples. Above fold + below content (+35% total).

### Ejemplos adaptados a ROBOHOGAR

**Subject lines buenos:**
- `El robot que SÍ merece la pena` (23 chars, curiosity gap)
- `¿Tu aspirador hace esto?` (24 chars, pregunta)
- `5 robots por menos de 300€` (25 chars, lista + precio)
- `Adiós, Roomba` (13 chars, provocador)

**Subject lines malos:**
- `ROBOHOGAR Newsletter #03 — Lo Último en Robótica Doméstica` (demasiado largo, genérico)
- `🤖🔥 INCREÍBLE ROBOT que CAMBIARÁ tu VIDA!! 🔥🤖` (spam triggers)

---

## 5. Email Design Patterns

### Specs técnicas (mobile-first obligatorio)

| Spec | Valor | Por qué |
|---|---|---|
| Ancho máximo | 600px (472px = premium) | Legibilidad en todos los clientes |
| Font body | 14-16px | Legible en móvil sin zoom |
| Font headlines | 20-22px | Jerarquía visual |
| Layout | Single-column | 60%+ opens en móvil |
| Touch targets | 44x44px mínimo | Usabilidad móvil |
| Peso imágenes | <200KB cada, <800KB total | Velocidad de carga |
| Dark mode | PNGs transparentes, off-white bg, CSS media query | 33%+ usuarios |
| Accesibilidad | Contraste 4.5:1, alt text, orden lógico | Inclusión + deliverability |

### Spec ROBOHOGAR para email

| Elemento | Valor | Notas |
|---|---|---|
| Background | `#FFFFFF` | Fondo principal |
| Texto | `#0C0C0C` | Negro principal |
| CTA / Accent | `#F5A623` | Botones, links, badges — ámbar ROBOHOGAR |
| Secundario | `#F2F2F2` | Fondos de sección |
| Texto secundario | `#6B7280` | Captions, metadata |
| Borders | `rgba(12,12,12,0.15)` | Separadores |
| Tipografía | Sans-serif limpia (la más cercana a DM Sans en Beehiiv) | Beehiiv no permite custom fonts en free |

### Principio anti-slop

> "El patrón más fuerte de los 57 emails curados es que personalidad, restricción y punto de vista superan consistentemente a templates genéricos pulidos."

- **theSkimm** creció a 3.5M+ subs con voz sola
- **Patagonia** envía emails sobre su causa, no sobre productos — genera más lealtad
- **Liquid Death** tiene el producto más aburrido (agua) y la identidad más distintiva
- Templates genéricos con fotos de stock se ignoran. Emails con personalidad se leen.

**Para ROBOHOGAR:** La voz de "amigo techie" + opiniones honestas ES el diseño. No necesitamos templates elaborados — necesitamos que cada email suene a Rafael.

### Referentes de diseño por tipo

| Tipo | Referente | Qué copiar |
|---|---|---|
| Newsletter curada | theSkimm, Morning Brew | Estructura fija, voz consistente, concisión |
| Reviews largo | The Hustle "Originals" | Headers grandes, storytelling + data |
| Roundup de noticias | TLDR | emoji + bold title + 2-line summary + link |
| Transaccional | Stripe | 472px, una fuente, un color acento, precisión |
| Welcome | Superhuman | Plain-text supera HTML en onboarding |

### 57 diseños curados — quick reference

| Categoría | Destacados | Takeaway principal |
|---|---|---|
| Welcome (8) | Superhuman (plain text), Figma | Plain text > HTML para onboarding |
| Newsletters (9) | Patagonia, theSkimm, Liquid Death | Voz > templates |
| Product Launches (8) | Apple (minimal), Fridja (25% stock pre-launch) | Menos = más |
| Promotional (9) | Feastables (trivia), Frank Body ($20M en tono) | Interactividad + personalidad |
| Brand & Storytelling (11) | Patagonia (advocacy), Dior (lookbook) | Misión > producto |

---

## 6. Deliverability

### Autenticación (obligatorio desde Feb 2024)

| Protocolo | Qué hace | Estado ROBOHOGAR |
|---|---|---|
| **SPF** | Lista IPs autorizadas para enviar | ✅ Configurado en Namecheap |
| **DKIM** | Firma digital en emails | ✅ Configurado via Beehiiv |
| **DMARC** | Política de rechazo para emails no autenticados | ✅ `p=quarantine` activo |

### Señales para Gmail Primary tab

- **Replies** son la señal más fuerte — pedir respuestas en welcome email
- Nombre personal > nombre de marca (ej: "Rafael de ROBOHOGAR")
- Templates simples ayudan (menos HTML = menos "promotions")
- Polls y encuestas en emails mejoran reputación ISP

### Cambios 2025-2026 en inbox

- **Gmail Promotions:** Ahora ordenado por relevancia (sept 2025), no cronológico. Bajo engagement = enterrado.
- **Gmail Gemini AI:** Resúmenes IA. El contenido debe sobrevivir la sumarización.
- **Apple Mail Categories (iOS 18.2):** Newsletters en "Updates" (mejor que Gmail Promotions). Resúmenes IA reemplazan preheaders.
- **Microsoft Outlook (mayo 2025):** SPF/DKIM/DMARC obligatorio para 5K+/día. Sin compliance = rechazo 550.
- **La realidad del 60%:** Solo ~60% de emails "entregados" llegan a inbox visible; ~36% filtrados a spam post-SMTP.

### Sunset flow (inactivos)

1. 90 días sin engagement → reducir frecuencia
2. Serie re-engagement: 2-3 emails ("Te echamos de menos" → oferta de valor → breakup email)
3. No responden → suprimir de lista activa
4. Breakup email = 2-3x reply rate del mid-sequence

---

## 7. Segmentation

### Engagement-Based Sending (5 tiers)

| Tier | Criterio | Frecuencia de envío | Acción |
|---|---|---|---|
| 1 | Clicked últimos 30d | Todo | Audiencia core |
| 2 | Clicked últimos 60d | 75% de envíos | Bueno pero menos activo |
| 3 | Clicked últimos 90d | Solo el mejor contenido (50%) | En riesgo |
| 4 | Sin engagement 90-180d | Solo re-engagement flow | Inactivo |
| 5 | 180+ días | Sunset flow | Candidato a suprimir |

**Resultados:** +15-30% better open rates, -20-40% fewer complaints, revenue se mantiene o sube.

> Para ROBOHOGAR: implementar cuando tengas >200 subs y datos suficientes.
> Beehiiv free plan tiene segmentación básica. Segmentación avanzada requiere plan Scale.

### Personalización (6 niveles por impacto)

1. **Behavioral:** Contenido basado en clicks/lectura previos (mayor impacto)
2. **Lifecycle:** Diferente para nuevos, activos, VIP, en riesgo, inactivos
3. **Dynamic content blocks:** Diferentes imágenes/productos por segmento en un template
4. **Send-time:** Hora óptima por suscriptor
5. **Location-based:** País, zona horaria (España vs LATAM)
6. **Name/demographic:** Nombre en subject — funciona como adición, no como principal

---

## 8. Testing

### Prioridades de testing (por impacto)

1. **Sender name** — compounds (lo que más impacta a largo plazo)
2. **CTA format** — botón vs texto, posición, color
3. **Template structure** — minimalista vs con imágenes, 1-column vs mixed

- Solo 1 de cada 7 tests da resultado significativo
- Priorizar tests en flows sobre campaigns (flows compound indefinidamente)
- STO (Send Time Optimization): +5-15% en open rates

### Tests recomendados para ROBOHOGAR (cuando haya volumen)

- Sender: "Rafael" vs "ROBOHOGAR" vs "Rafael de ROBOHOGAR"
- CTA: botón ámbar vs text link
- Template: con hero image vs sin hero image
- Subject: pregunta vs statement vs número

---

## 9. Compliance (GDPR)

### Obligatorio para audiencia EU (España + Europa)

| Requisito | Cómo cumplir |
|---|---|
| Consentimiento explícito | Doble opt-in (recomendado) |
| Right to erasure | Procesar solicitudes en 30 días |
| Registros de consentimiento | Conservar 3-7 años |
| One-click unsubscribe | RFC 8058 — requerido para 5K+/día en Gmail/Yahoo |
| Datos a terceros | Beehiiv en EEUU — cláusulas contractuales tipo EU |

### Ya implementado en ROBOHOGAR

- ✅ Página de privacidad en Beehiiv (slug: `privacidad`)
- ✅ Aviso legal con NIF
- ✅ Link de cancelación en cada email (automático de Beehiiv)
- ✅ Sender reply-to monitoreado

---

## 10. Creator Milestones & Revenue Stack

### Crecimiento típico de newsletter creator

| Hito | Qué pasa | Acción |
|---|---|---|
| 0-500 subs | Validación del nicho | Consistencia, content gating, referral |
| 500-2,500 | Tracción inicial | Amazon afiliados, primera monetización |
| 2,500-10K | **Inflexión** — aquí el crecimiento se acelera | Recommendations, sponsor outreach, upgrade Beehiiv |
| 10K+ | Media brand | Paid subs, digital products, eventos |

### Revenue stack (por orden de implementación)

1. **Afiliados** (Amazon) — desde el día 1, bajo fricción, comisión 3-7%
2. **Sponsorships** — desde ~2,500 subs, nicho > volumen para CPMs
3. **Paid subscriptions** — contenido premium, beehiiv toma 0% comisión
4. **Digital products** — guías, templates (lead magnets que monetizan)
5. **Boosts Earn** — ingreso pasivo por enviar subs a otros newsletters

### Datos clave

- Referral programs aceleran growth +30-40%
- Nicho > generalista: newsletters de nicho con 5K subs pueden cobrar CPMs más altos que generalistas con 100K
- $19M en paid subscriptions en beehiiv 2025 (+138% YoY)
- Mediana 66 días al primer dólar para lanzamientos 2025

---

## 11. Send Timing

### Mejores días y horas (beehiiv data 2025)

| Dimensión | Recomendación |
|---|---|
| Mejores días | **Martes y miércoles** |
| Peak 1 | **Early morning** (más fuerte — lectores revisan email primero) |
| Peak 2 | **Mid-afternoon** (segunda onda) |
| Peor ventana | Overnight (menor engagement) |
| Frecuencia óptima | 1-3x/semana. Consistencia > volumen |

### Para ROBOHOGAR

- **Newsletter quincenal:** Martes 9:00 CET (peak 1, mejor día)
- **Artículos web:** Publicar sin restricción de timing (SEO, no email)
- **Social posts:** Post-publicación según calendario de Buffer
