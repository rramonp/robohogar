---
name: feedback_ficcion_hero_cotidiano_mas_scifi
description: ROBOHOGAR heros de ficción — regla permanente "cotidiano + toque sci-fi siempre". La miniatura NUNCA es solo still life doméstico puro; tiene que llevar siempre un elemento de robótica humanoide / sci-fi que rompa la tendencia cotidiana. Pedida 2x por Rafael, canon no-opcional.
type: feedback
originSessionId: 1e39fbdd-e33b-474f-a953-ab4576725eec
---
Regla editorial permanente para heros de Ficciones Domésticas ROBOHOGAR. Rafael pidió explícitamente guardarla en memoria 2026-04-24 señalando *"ya te lo he pedido otra vez"* — había sido transmitida antes sin persistir. Queda aquí con ese peso.

**Regla:** la miniatura de un relato de Ficciones Domésticas es SIEMPRE **imagen cotidiana del día a día con un toque de ciencia ficción o robótica humanoide que rompa un poco la tendencia que se esperaba de algo cotidiano**. La mezcla es el sello. Ni puro still life doméstico, ni puro objeto sci-fi; siempre los dos registros en el mismo frame.

**Por qué:** sin el toque sci-fi la imagen se lee como "foto bonita de mesa / rincón / objeto" y se confunde con cualquier revista de decoración o still life fotográfico. Sin lo cotidiano se lee como "render de robot" y pierde la textura doméstica que define la serie. La mezcla es lo que ancla Ficciones Domésticas como Black Mirror-adjacent a escala hogar: todo parece normal hasta que no lo es.

**Cómo aplicar** (integrado en `assets/branding/ficcion-hero-archetypes.md`):

1. El **ADN fijo de la serie** de `asset-catalog.md § 5` incluye, sin excepción, un elemento del eje C (familia "Presencia humanoide"). Los archetypes que en el catálogo parecían permitir "sin humanoide" (archetype 05 "Cenital ritual" con B1 puro, archetype 12 "Macro textura" con solo detalle del objeto) NO son válidos por sí solos — deben combinarse con C1-C5 (mano, silueta, fragmento corporal, ausencia marcada como percha vacía con forma humanoide / tarjeta ID / cable de carga / sombra).
2. El toque sci-fi puede ser **explícito** (mano matte, silueta humanoide, fragmento corporal) o **indirecto** (percha con forma de uniforme humanoide, cable de carga sintético, tarjeta ID institucional del robot, sombra humanoide proyectada desde off-frame). Nunca ausente.
3. El toque sci-fi siempre se describe `plain matte cream-white with no glowing parts, no LEDs, no lights, no panels, no colored accents` — no es cyberpunk, no brilla, no es de catálogo.
4. El toque sci-fi tiene que estar **anclado narrativamente en el relato concreto** (mencionado o justificado en `PASOS.md § Hero`). Si el relato no tiene humanoide protagonista pero sí IA o wearable doméstico, el toque va por ahí (pulsera smart, dispositivo de pared, altavoz contextual con articulación mecánica).

**Incidente origen 2026-04-24:** al regenerar La objeción con 2 archetypes distintos (cenital ritual + silueta de espaldas) después de diagnosticar que v1 y v2 tenían composición idéntica a El que viene a tomar café v3, generé una v3 "cenital ritual" SIN figura humanoide — bandera tri-fold + carpeta lacrada sobre mesa wenge, sin toque sintético. Rafael detectó al instante: *"siempre quiero una mezcla entre vida cotidiana y algún toque de ciencia ficción, ya sea un humanoide, etc."*. Segunda vez que lo pedía. Regeneré como v5 añadiendo mano matte cream-white entrando desde el borde superior del frame cenital hacia la carpeta lacrada — mezcla recuperada. La variante v4 "silueta de espaldas" ya cumplía desde el primer render porque lleva al humanoide entero como figura principal.

**Triaje al elegir archetype** (para `/nano-banana` modo ficción):
- ¿El archetype elegido incluye al menos un fragmento de la familia C (humanoide) — C1, C2, C3, C4 o C5? → OK.
- ¿Solo tiene B1/B4/B3/B5 (objeto) sin C? → añadir un C antes de generar. Nunca dar por bueno un prompt de hero de ficción que haya eliminado la familia C.
- Si es un archetype raro (A4 "a través de marco" con solo objeto al fondo, A5 "macro extremo" con detalle puro), meter C5 como toque indirecto — sombra humanoide, tarjeta ID, cable de carga.

**Relación con el catálogo:** esta regla prevalece sobre cualquier combinación A·B·D pura. La familia C no es opcional — es ADN. El archivo `ficcion-hero-archetypes.md` se ajusta para reflejarlo explícitamente.
