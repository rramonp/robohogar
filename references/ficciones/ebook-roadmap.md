# Ebook Roadmap — Compilación de Ficciones Domésticas

> Plan para agrupar los relatos del pilar "Ficciones Domésticas" en un ebook recopilatorio y (posiblemente) autopublicarlo. Milestone: ~15-20 relatos de calidad con ≥2 arcos cerrados. Cadencia actual (3 series × 1 relato/3-4 semanas) → masa crítica en 9-12 meses.
> Estado: **F0 — plan aprobado**. Se ejecuta en F4-F5 del roadmap, no ahora.

---

## Fases

### F0 — ahora (2026-04-18)
Estado actual. Plan aprobado, 3 series activas creadas, 0 relatos publicados.

**Hito para cerrar F0**: 3 flash pilotos publicados (uno por serie).

### F1 — piloto y validación (semanas 1-4)
- 3 flash fictions (500-800 palabras) — uno por serie activa.
- Mediar engagement: opens, replies, menciones en redes.
- Criterio: si al 3er flash hay ≥1 serie con engagement claro (>media del newsletter) → continuar con mini-serie en ella.

**Hito para cerrar F1**: 3 flashes publicados + decisión sobre qué 2 series priorizar.

### F2 — acumulación base (meses 2-6)
- 2 series en mini-serie activa + 1 antológica.
- 1 episodio cada 3-4 semanas por serie activa.
- Episode 0 de cada mini-serie publicado.
- Objetivo: **12 relatos totales** (4 Amparo + 4 Ronda 3 + 4 MAIA, aproximadamente).
- Recap Index creado y mantenido en Beehiiv.

**Hito para cerrar F2**: 12 relatos publicados, arcos en mid-serie en las 2 ganadoras.

### F3 — maduración (meses 7-12)
- Añadir 3ª serie activa (potencialmente una de las 🟡 propuestas).
- Llegar a **20-24 relatos totales**.
- Cerrar arcos en al menos 2 series (finales de mini-serie publicados).
- Empezar a introducir crossovers ocasionales.

**Hito para cerrar F3**: ≥2 arcos cerrados, masa crítica suficiente para ebook.

### F4 — construcción del ebook (mes 12-13)
- Construir el skill `/ficcion-ebook` con:
  - Lectura de todos los relatos `content/ficciones/<serie>/*.md`.
  - Filtro por criterios de selección (ver §Selección).
  - Compilación en EPUB + PDF.
  - Generación de portada con Nano Banana.
  - Metadata ISBN, ficha técnica, tabla de contenidos.
- Primera compilación: **"Ficciones Domésticas — Volumen 1: Hogares 2033"** (título provisional).

**Hito para cerrar F4**: ebook en archivo, listo para revisión editorial manual.

### F5 — revisión y autopublicación (mes 13-14)
- Revisión editorial completa del ebook (Rafael + posible editor externo).
- Decisión de plataforma (ver §Plataformas).
- Registro ISBN (opcional).
- Subida a plataforma(s).
- Anuncio en newsletter + redes.
- Regalo gratis a suscriptores los primeros 3 meses (construye lealtad).
- Pago a partir del 4º mes (opcional según KDP terms).

**Hito de éxito**: ≥100 descargas/ventas en primeros 3 meses.

---

## Criterios de selección de relatos para el ebook

Lógica: **no todos los relatos publicados entran al ebook**. Se cura.

### Criterios inclusión
1. Arcos cerrados prioridad alta. Si una serie tiene mini-serie completa → incluir todos los episodios en orden.
2. Standalone excepcionales (≥ media de engagement). Pueden ir en sección "Relatos sueltos".
3. Calidad literaria estable: relatos que pasen anti-IA checklist (§1+§2) sin flags al revisar.
4. Equilibrio de tonos: mezcla de series para variedad.

### Criterios exclusión
1. Flash pilotos que no cumplan calidad post-revisión (se archivan en `_archive/`).
2. Episodios con datos anclados desactualizados (AI Act que cambió, spec de robot discontinuado).
3. Canon conflicts sin resolver.

### Volumen objetivo
- Volumen 1: ~15-20 relatos, 200-300 páginas.
- Volumen 2 (si hay masa crítica): +20 relatos tras F3.

---

## Plataformas de autopublicación — evaluación

| Plataforma | Alcance | ISBN | Precio gestión | Pros | Contras |
|---|---|---|---|---|---|
| **Amazon KDP** | Global | Gratis (ASIN) o propio | 35% o 70% royalties | Kindle + paperback integrados, mayor alcance global | Exclusividad Kindle Unlimited si quieres promo, curva de aprendizaje |
| **Lektu (ES)** | Hispano | Requiere propio | 30% comisión | Especializada ES, comunidad sci-fi activa, DRM-free | Menor alcance que KDP |
| **Leanpub** | Técnico/nicho | ISBN opcional | 10% comisión | Versiones evolutivas (vas actualizando), buen para ebook en progreso | Más orientado a tech books, comunidad menor en ficción |
| **Bookwire / Libranda** | ES + LATAM | Requiere propio | Comisión variable | Distribución librerías ES profesional | Proceso editorial más lento, coste fijo |
| **Beehiiv integración** | Suscriptores actuales | N/A | 0€ | Directo a suscriptores, MVP sin fricción | No es "publicación real", no llega a nuevos lectores fuera del newsletter |

**Recomendación preliminar (a validar en F4)**:
1. **MVP**: publicar PDF + EPUB descargable gratis desde robohogar.com como "regalo ROBOHOGAR+" para suscriptores actuales. Sin fricción, mide demanda.
2. **Si la respuesta es buena**: **KDP + Lektu en paralelo**. KDP para alcance global, Lektu para comunidad ES especializada.
3. **Si ROBOHOGAR crece a +5K subs**: evaluar Bookwire para librería física (nicho tangible que la propia marca puede explotar).

---

## ISBN — conveniencia

- **KDP** regala ASIN (código interno Amazon). Si publicas solo en Amazon, no necesitas ISBN propio.
- **Lektu** requiere ISBN propio.
- **Librería física** requiere ISBN propio obligatorio.
- **ISBN propio en España**: ~50€ por título, se gestiona en [Agencia del ISBN](https://www.agenciaisbn.es/).
- **Recomendación**: si vas a Lektu o librería física → ISBN propio. Si solo KDP/Beehiiv → ASIN basta.

---

## Portada — generación Nano Banana

Prompt base propuesto (adaptar):

```
Editorial book cover, minimalist speculative fiction, Spanish short stories anthology.
Title: "FICCIONES DOMÉSTICAS" (Jost bold, warm amber #F5A623 on white).
Subtitle: "Hogares 2033, Volumen 1" (DM Sans regular, charcoal #0C0C0C).
Author: "ROBOHOGAR" (DM Sans medium, charcoal, small).
Central image: minimal silhouette composition — a modest Spanish living room at dusk
with a domestic robot of indeterminate form in soft focus.
Light: motivated warm window light + cool blue glow from screen (matches hero-fiction style).
Style reference: Penguin Modern Classics minimalism + Black Mirror editorial.
Format: 1600x2560 (Kindle standard).
NO stock photo look. NO generic robot. NO text cluttering.
```

Aplicar regla `feedback_never_overwrite_images.md`: versionar (`cover-v1.png`, `cover-v2.png`, etc.).

---

## Precio

**Anchors autopublicación ES 2025-2026:**
- EPUB: 2,99€ - 6,99€ (sweet spot 4,99€).
- Paperback: 9,99€ - 14,99€ (sweet spot 12,99€).
- Hardcover: si aplica, 18,99€ - 24,99€.

**Plan escalonado recomendado:**
1. **Meses 1-3**: gratis para suscriptores ROBOHOGAR (como thank-you).
2. **Mes 4+**: 4,99€ EPUB / 12,99€ paperback en KDP + Lektu.
3. **Descuentos estacionales**: 2,99€ en promos (Black Friday, Día del Libro 23 abril, Reyes).

---

## Marketing — launch checklist

Cuando el ebook esté listo:
1. [ ] Email de anuncio a suscriptores (subject curiosity gap).
2. [ ] Landing page específica en robohogar.com (o tag Beehiiv).
3. [ ] Posts en LinkedIn, X, Instagram, WhatsApp (skill `/social-content`).
4. [ ] Envío a reseñistas: medios ES sci-fi (La Laguna Negra, Scifiworld, Hipertextual), bookstagrammers, editores SuperSonic/Constelación.
5. [ ] AMA en Reddit r/librosespanol o comunidad similar.
6. [ ] Inclusión en directorios ES de ficción especulativa ([directorio.substack.com](https://directorio.substack.com/)).
7. [ ] Featured en newsletter propio durante 2 semanas.

---

## Frases trigger para retomar

Cuando Rafael retome trabajo sobre el ebook en sesiones espaciadas:

| Intención | Frase trigger |
|---|---|
| Ver estado del roadmap | **"¿En qué fase del ebook ROBOHOGAR estamos?"** |
| Listar relatos candidatos | **"Lista los relatos que cumplen criterios de selección para el ebook"** |
| Evaluar masa crítica | **"¿Tenemos masa crítica para arrancar F4?"** |
| Arrancar F4 | **"Retomamos ebook ROBOHOGAR — empezamos F4 (construcción)"** |
| Arrancar F5 | **"Retomamos ebook ROBOHOGAR — empezamos F5 (publicación)"** |

## Changelog

- **2026-04-18** — creación inicial. Milestones y plataformas preliminares. A validar al llegar a F4.
