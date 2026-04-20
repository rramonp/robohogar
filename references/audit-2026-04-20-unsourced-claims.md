# Auditoría 2026-04-20 — Claims sin fuente / framing deficiente

Corpus de referencia tras auditar los 8 primeros artículos publicados de ROBOHOGAR contra la regla `@rules/editorial.md § Datos con fuente rastreable`. Sirve como base empírica de la regla y como lista de fixes pendientes.

**Metodología:** WebFetch a cada artículo preguntando por 5 tipos de problema. Falsos positivos filtrados manualmente (tablas "incompletas" que sí estaban completas, links a artículos ROBOHOGAR que sí existen en `registro-articulos.md`, fechas 2026 marcadas como "futuras" por el modelo auditor).

## Hallazgos confirmados (14)

| # | Artículo | Cita problemática | Categoría regla | Fix sugerido |
|---|----------|-------------------|------------------|--------------|
| 0 | [mejor-robot-asistente-ia-2026](https://robohogar.com/p/mejor-robot-asistente-ia-2026) | *"Más de 60.000 unidades vendidas lo avalan"* (Eilik) | 1 Ventas | Añadir link a comunicado/fuente primaria o suavizar a *"supera ampliamente las 50.000 unidades según la marca"* |
| 0 | mejor-robot-asistente-ia-2026 | *"4,8 sobre 5 con más de 1.000 valoraciones reales"* (Loona) | 2 Rating | Especificar plataforma: *"4,8/5 sobre 1.000+ reseñas en Amazon ES"* |
| 0 | mejor-robot-asistente-ia-2026 | *"Es el único de esta lista que funciona como compañero inteligente de verdad"* | 9 "Único/primero" | Suavizar: *"el que mejor entrega la promesa de compañero inteligente sin depender del móvil"* (LOOI también tiene IA) |
| 1 | [humanoides-en-casa-cuanto-falta](https://robohogar.com/p/humanoides-en-casa-cuanto-falta) | *"Figure 02 ya ha producido 30.000 BMW X3. Turnos de 10 h, 90.000 piezas, 1.250 h de operación"* | 1 Ventas / producción | Añadir hipertexto a press release Figure/BMW; si no hay fuente primaria, quitar cifras específicas |
| 1 | humanoides-en-casa-cuanto-falta | *"Han levantado más de 10.000 millones de dólares. Tesla planea 20.000 millones solo en 2026"* | 4 Inversión | Citar Reuters/Bloomberg con link al reporte de inversión, o suavizar a "miles de millones" sin cifra redonda |
| 2 | [roborock-saros-z70-review](https://robohogar.com/p/roborock-saros-z70-review) | *"El brazo acierta aproximadamente la mitad de las veces — Vacuum Wars"* | 3 Eficacia | Enlazar review exacto de Vacuum Wars Saros Z70, no solo citar la marca |
| 2 | roborock-saros-z70-review | *"180 mL — el más pequeño que Vacuum Wars ha probado en la historia"* | 9 "Único/primero" | Enlazar la comparativa específica o reescribir: *"uno de los depósitos más pequeños que hemos visto"* |
| 3 | [neo-humanoide-fabricas-eqt](https://robohogar.com/p/neo-humanoide-fabricas-eqt) | *"Bloomberg proyecta 1,2 M humanoides en 2030. Menos del 15% irán a hogares"* | 5 Proyecciones | Enlazar reporte Bloomberg; si el 15% es inferencia propia marcar autoría: *"nuestra estimación"* |
| 3 | neo-humanoide-fabricas-eqt | *"Desde el 2 de agosto de 2026, por los requisitos de alto riesgo del AI Act europeo"* | 6 Regulación | Enlazar texto oficial EUR-Lex art. 113 AI Act que fija esa fecha. **Verificar la fecha** — el AI Act entra escalonadamente |
| 4 | [humanoides-domesticos-2026-comparativa](https://robohogar.com/p/humanoides-domesticos-2026-comparativa) | Dos productos presentados como "primer humanoide doméstico" (1X NEO y UniX Panther) | 9 "Único/primero" | Diferenciar explícito: *"NEO es el primero anunciado para consumidor"* vs *"Panther es el primero entregado"* |
| 5 | [samsung-jet-bot-steam-ultra-review](https://robohogar.com/p/samsung-jet-bot-steam-ultra-review) | *"Mata el 99,99% de bacterias (E. coli, Salmonella, Staphylococcus aureus según los tests internos de Samsung)"* | 8 Tests fabricante | Cualificar como claim: *"Samsung afirma haber testeado contra E. coli…"* (dejar claro que es claim del fabricante) + link a Samsung Newsroom |
| 5 | samsung-jet-bot-steam-ultra-review | *"Samsung lleva vendiendo robots aspirador desde 2003, con el primer NaviBot"* | 7 Histórico | **Verificar — probablemente incorrecto**: el primer NaviBot de Samsung es de 2009, no 2003. Fact-check con Samsung Global Newsroom y corregir |
| 6 | [mejor-robot-aspirador-2026](https://robohogar.com/p/mejor-robot-aspirador-2026) | *"Solo el 17% de los hogares españoles tiene robot aspirador en 2026, frente al 34% en Alemania y 41% en Corea"* | 3 Estadística | Enlazar URL específica del Statista Market Outlook Spain 2026 (o reemplazar por datos públicos INE/Eurostat si no hay acceso premium) |
| 7 | [humanoide-maraton-pekin-record-mundial](https://robohogar.com/p/humanoide-maraton-pekin-record-mundial) | *"Ningún modelo, ni el mejor del estudio, supera el 25% 'aceptable' en el mundo físico"* | 9 Umbral sin atribución | Aclarar: *"nuestro umbral editorial de 'aceptable' está en 25%"* o *"el informe Stanford fija el umbral aceptable en 25%"* según quién lo definió |
| 7 | humanoide-maraton-pekin-record-mundial | *"89,4% éxito simulación · 48% en 2022 · 12% en Behavior-1K"* (AI Index 2026) | 3 Eficacia | Añadir página/sección del informe Stanford para que el lector verifique en 30 s |

## Falsos positivos descartados del auditor WebFetch

- **Tablas "incompletas"** (art #4 con 7 humanoides, art #6 con 6 aspiradores) — verificado localmente que las tablas sí contienen todas las filas.
- **Links ROBOHOGAR "rotos"** — todos los slugs referenciados existen en `content/registro-articulos.md`.
- **Fechas 2026 "futuras"** — el modelo auditor tenía knowledge cutoff previo; estamos en abril 2026, son fechas presente/pasadas.
- **"Checklist prometida en neo-humanoide-fabricas-eqt"** — el artículo NEO no promete checklist; el auditor leyó mal la sección "Keep Reading" y confundió con referencia cruzada legítima al art #6.

## Prioridad de fix (si Rafael lo aborda)

1. **Crítico — verificar y corregir:** Samsung NaviBot 2003 → probablemente 2009.
2. **Alto — citar fuente o reescribir:** AI Act 2 ago 2026, Figure 02 cifras BMW, inversión 10B/Tesla 20B.
3. **Medio — añadir hipertexto específico:** Statista 17%, Vacuum Wars 180 mL y brazo 50%, Samsung 99,99%.
4. **Menor — suavizar lenguaje:** "el único compañero inteligente" Loona, Eilik 60.000 y Loona 4,8/5, umbral 25%.

## Integración con el pipeline

Desde 2026-04-20 la regla `@rules/editorial.md § Datos con fuente rastreable` es obligatoria en:
- `/content-draft § 8.4 ter` — grep pre-output antes de entregar borrador.
- `/post-publish § 1` — grep post-publish + triaje auto-fix/consultar.

Los 14 casos de esta tabla son el corpus canónico de ejemplos. Si un futuro artículo replica un pattern de esta lista, el pipeline debe detectarlo y arreglarlo (si es evidente) o consultar (si es ambiguo).
