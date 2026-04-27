---
name: feedback_ficcion_hero_archetypes_catalogo
description: Catálogo canónico de 15 archetypes compositivos para heros de Ficciones Domésticas en `assets/branding/ficcion-hero-archetypes.md`. Combinatoria A·B/C·D con regla anti-repetición dura y algoritmo de selección por tonalidad.
type: reference
originSessionId: 1e39fbdd-e33b-474f-a953-ab4576725eec
---
El repositorio ROBOHOGAR canoniza 15 archetypes compositivos para heros de Ficciones Domésticas en el archivo [`assets/branding/ficcion-hero-archetypes.md`](../../robohogar/assets/branding/ficcion-hero-archetypes.md). Nace 2026-04-24 como respuesta al incidente "heros idénticos" (El que viene a tomar café v3 y La objeción v2 compartían composición exacta: mesa wenge + mano humanoide lateral derecha + objeto central + luz cálida upper-left).

**Estructura del catálogo** — cada archetype combina 4 familias:

- **Familia A (Encuadre):** A1 lateral eye-level · A2 cenital · A3 ángulo bajo desde el suelo · A4 a través de marco · A5 extreme macro
- **Familia B (Estado del objeto):** B1 objeto único · B2 ausencia/huella · B3 roto/dividido · B4 envuelto · B5 reflejo imposible
- **Familia C (Presencia humanoide) — NO OPCIONAL (ver memoria `feedback_ficcion_hero_cotidiano_mas_scifi`):** C1 mano lateral · C2 silueta encogida al fondo · C3 silueta de espaldas · C4 fragmento corporal aislado · C5 ausencia/sombra/eco
- **Familia D (Luz):** D.i lateral ámbar default · D.ii backlight · D.iii luz desde abajo · D.iv luna fría · D.v celosía

**Los 15 archetypes canónicos** son combinaciones predefinidas A·(B o C)·D validadas. La tabla completa con tonalidades sugeridas vive en el archivo. Ejemplos: 01 "Mesa · mano lateral" (A1·C1·D.i — canon default de los primeros one-shots); 05 "Cenital ritual" (A2·B1+C·D.i o D.ii); 07 "Parquet bajo · humanoide encogido" (A1·C2·D.i — el de Setenta y dos horas); 08 "Silueta de espaldas" (A1·C3·D.i).

**Regla dura anti-repetición:** ningún archetype puede aparecer en 2 heros consecutivos del mismo grupo. El grupo es o bien "one-shots" o bien cada serie individual (cartas-a-maia, cronicas-ronda-3, la-casa-de-amparo, etc.). `/nano-banana` debe leer la columna `Archetype` del registro en `asset-catalog.md § 5 · Registro de heros ficción` antes de generar, y excluir ese número del pool de candidatos.

**Algoritmo de selección por tonalidad:** mapa explícito tonal (canon 40/15/25/10/10) → archetypes recomendados. Inquietante → 01/02/04/07/10/11/12. Radical → 03/05/06/07/11/14/15. Ambiguo → 04/08/10/13. Inspirador → 05/08/09/14. Mundano → 02/07/12/13.

**Meta de variedad:** primeros 10 heros publicados deben cubrir al menos 6 archetypes distintos. Si se llegan a 10 heros con ≤3 archetypes diferentes, revisar el algoritmo.

**Integración operativa:**

- `/nano-banana` modo ficción: leer `asset-catalog.md § 5` + `ficcion-hero-archetypes.md` antes de componer el prompt. Elegir archetype según tonalidad + regla anti-repetición + compatibilidad espacial. Ensamblar prompt desde esqueleto canónico + fragments A·B/C·D del catálogo.
- `/ficcion-draft`: en `PASOS.md § Hero` anotar qué archetype propone y por qué, para que `/nano-banana` lo recoja sin reinterpretación.
- `asset-catalog.md § 5 · Registro de heros ficción`: columna `Archetype` con codificación `NN (A·B/C·D)` es obligatoria desde 2026-04-24. Filas existentes ya retrofiteadas: #1 operador 02 · #2 café 01 · #3 setenta 07 · #4 la-objecion v2 01 (marcada a regenerar).

**Mantenimiento del catálogo:**

- Si en las próximas 10 generaciones aparecen composiciones que no encajan en los 15 archetypes, canonizar como archetype 16, 17... con su fila en la tabla.
- Si un archetype genera reiteradamente neones / texto / caracteres asiáticos pese a las anti-triggers, documentar como "prohibido por modelo" hasta que Gemini cambie.
- La familia C es ADN fijo, no negociable (ver `feedback_ficcion_hero_cotidiano_mas_scifi`). Cualquier propuesta de archetype "solo objeto + solo luz" debe rechazarse antes de generar.

**Cuándo revisar:** al generar hero nuevo, al añadir serie nueva (que se canoniza como nuevo grupo para la regla anti-repetición), o si Rafael valida una composición que rompe ADN fijo — ese caso se trata como excepción editorial puntual documentada en `asset-catalog.md`, no se incorpora al catálogo.
