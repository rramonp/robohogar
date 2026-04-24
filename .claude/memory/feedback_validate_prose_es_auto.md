---
name: Validate prose ES se ejecuta autonómamente tras generar prosa publicable
description: /validate-prose-es es paso obligatorio del pipeline en /ficcion-draft §8.4 y /content-draft §8.5 quater y /social-content (≥150 palabras) — ejecutar sin pedir autorización
type: feedback
originSessionId: d5820d74-2db3-44d7-be60-f1391a0f2d2e
---
Cualquier skill que genere prosa publicable para ROBOHOGAR (ficción, artículo, review, comparativa, guía, editorial, tutorial, newsletter, LinkedIn long-form, IG caption extenso) debe invocar `/validate-prose-es <path>` **sin pedir autorización**. Es paso del pipeline, no decisión editorial. Rafael recibe el reporte como parte del output; no lo aprueba ni lo dispara.

**Umbrales:**
- `/ficcion-draft` → SIEMPRE (sin umbral, todo relato). Paso §8.4.
- `/content-draft` → SIEMPRE (cualquier artículo publicable ≥800 palabras). Paso §8.5 quater.
- `/social-content` → solo si la pieza tiene ≥150 palabras de prosa sumada (LinkedIn long-form, hilo X concatenado, IG caption extenso, WhatsApp multi-bloque). Posts cortos los cubre la checklist del skill.
- `/pdf-brand` → SIEMPRE sobre el `contenido.md` fuente ANTES de invocar el skill Python (paso §3 bis). Valida la prosa en markdown para atajar calcos antes de generar PDF — regenerar PDF cuesta ~5 min + bump de versión, iterar markdown cuesta 30 segundos.

**Por qué se documenta como feedback y no como hook en settings.json:** el `/validate-prose-es` es invocación de skill desde otro skill — va dentro del propio flujo de cada generador. No es un hook de harness externo. La regla está en los pasos §8.4 (`/ficcion-draft`), §8.5 quater (`/content-draft`) y en el bloque "Second reader externo" de `/social-content`. Esta memoria refuerza que se ejecuten **sin esperar confirmación del usuario**.

**Incidente origen 2026-04-23:** al generar el relato *La objeción* con `/ficcion-draft`, el skill lo marcaba como obligatorio (§8.4) pero la ejecución lo saltó y entregó el borrador sin validar. Rafael tuvo que pedir explícitamente "lanza el validator". Causa: ambigüedad en el texto del paso 8.4 sobre si requería confirmación. Corrección aplicada al skill `ficcion-draft.md` ese mismo día. Esta memoria cierra el agujero: incluso si el texto del paso fuera ambiguo, la norma general es ejecutar autonómamente.

**How to apply:** tras generar el archivo final del relato/artículo/post largo y correr los greps pre-output específicos del skill, encadenar directamente `/validate-prose-es <path>` en la misma respuesta. El reporte y el log en `<carpeta>/validator-reports/YYYY-MM-DD-report.md` forman parte del entregable. Si veredicto = PENDING_FIXES, aplicar fixes y re-invocar una vez; si sigue PENDING, mostrar a Rafael. Si veredicto = MAJOR_REWRITE, bloquear output y volver a generación. Si READY, entregar.

**Por qué importa:** el sesgo estructural del LLM generador le hace invisibles los tics anglo que él mismo produce. El validador es capa independiente — sin él, los greps solos dejan pasar colocaciones ambiguas y registros mezclados. Saltarlo rompe la defensa sistémica que Rafael construyó tras el incidente *el-que-viene-a-tomar-café* v2 (2026-04-20).
