---
name: feedback_ficcion_tonal_preference
description: ROBOHOGAR ficción — Rafael resuena con categoría tonal radical (cierre irreversible + alguien sigue como si nada). Tie-breaker SUAVE en /ficcion-draft paso 0.5 cuando el auto-balance deja empate técnico; jamás limita variedad ni sobrescribe la matriz canon 40/15/25/10/10.
type: feedback
originSessionId: 454369cd-5a0b-432e-9fc2-cdbadf13fcaf
---
Rafael expresó preferencia editorial por la categoría tonal **radical** (§2.2 de `tonalidad-y-mix-editorial.md`: cierre irreversible + alguien sigue como si nada, empatía dividida, sin villano de cartón) tras leer los 3 one-shots del catálogo inicial. *Setenta y dos horas* fue el que más le resonó — patrón consistente con su feedback previo sobre *El operador nocturno v3* donde también valoró intensidad controlada con filo.

**Cómo se aplica la preferencia** (señal ponderada, nunca restricción):

1. **Tie-breaker suave en auto-balanceo tonal:** cuando `/ficcion-draft` corre sin `--tono` explícito y el algoritmo §3 de `tonalidad-y-mix-editorial.md` calcula dos o más categorías con déficit porcentual similar (rango de ≤3 puntos porcentuales entre ellas), la preferencia rompe el empate hacia radical. Si el déficit manda claro hacia otra categoría (p. ej. inspirador -15pp · radical -3pp), el auto-balance gana: la preferencia se ignora.
2. **Dato en PASOS.md del relato:** anotar *"tonal resonante con el autor: radical"* como contexto para revisión editorial — no como decisor de decisión.

**Kill switches preservados (no negociables):**
- `--tono=X` explícito de Rafael sobrescribe siempre la preferencia.
- Matriz canon 40/15/25/10/10 es suelo duro: si Rafael acumula 3 radicals seguidos (forzados o elegidos por tie-breaker), el skill avisa que el mix se está desviando y propone equilibrar — misma regla §3.5 de `tonalidad-y-mix-editorial.md` vigente.
- Rafael puede decir *"ignora mi preferencia"* en cualquier invocación y queda neutralizada para ese relato.

**Lo que NO se guarda (deliberadamente):**

Preferencia de **estilo o voz narrativa**. La voz global de ROBOHOGAR (castellano peninsular literario, `castellano-literario-es.md`) + la modulación automática por categoría tonal (`tonalidad-y-mix-editorial.md § 4`) ya es el sistema que garantiza variedad estilística. El estilo clínico-distanciado que Rafael valoró en *Setenta y dos horas* (milímetros, segundos, protocolos intercalados con detalles afectivos) **no es preferencia del autor** — es la voz que el tonal *radical* exige (Mariana Enríquez, Fernanda Melchor, Samanta Schweblin). Guardar "estilo preferido" metería dislocación técnica en un futuro relato inspirador y rompería ese inspirador. Mal.

**Why:** Rafael quiere variedad tonal y estilística; teme que su preferencia editorial se convierta en restricción que ate la capacidad del pilar Ficciones Domésticas de producir relatos de categorías distintas. Esta memoria se diseña como señal ponderada con matriz canon prevaleciendo y kill switches explícitos, para preservar esa variedad.

**How to apply:** `/ficcion-draft` paso 0.5 lee esta memoria como input del auto-balance. Si el cálculo de déficit deja dos categorías con diferencia ≤3pp, elige radical; si no, ignora la preferencia. Ante duda, siempre preservar variedad — la matriz 40/15/25/10/10 manda.

**Cuándo revisar esta memoria:** si Rafael tras N relatos expresa que otra categoría le resuena igual o más, se actualiza este archivo con la nueva preferencia (o se elimina si prefiere auto-balance puro). Si detectamos en la práctica que el tie-breaker está sesgando el catálogo más allá del 15% canon de radical, se revisa también.
