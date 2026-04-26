# Validate Prose ES — second reader de 2 capas (grep first, LLM después)

**Propósito.** Validador de prosa de ficción ES peninsular. Arquitectura de 2 capas — grep deterministic (Capa 1, infalible en su scope) + Agent LLM para ambigüedades (Capa 2, complementario nunca único). Diseñado tras el test empírico del 2026-04-20 que demostró que un Agent LLM solo — sin greps — falla en detectar los calcos léxicos más evidentes por sesgo estructural del modelo.

---

## Por qué 2 capas y no 1

**Test empírico 2026-04-20.** Sobre el v1 de *El que viene a tomar café* (10 errores conocidos detectados por Rafael leyendo), un Agent Explore sin greps previos detectó **3/10**. Se le escaparon los dos más obvios: *"El centro de demostración fue en septiembre"* y *"vio la escena en boca de una actriz"*. Además alucinó un personaje (*"Martín"*) que no está en ese relato.

**Diagnóstico.** El LLM tiene sesgo estructural: las construcciones calcadas del inglés las produce él mismo habitualmente, así que no las lee como "raras". El grep determinista no tiene ese sesgo — si el patrón está documentado, matchea al 100%.

**Conclusión.** El LLM debe ejecutar **después** del grep, sobre lo que al grep se le escapa. Nunca antes, nunca en solitario, nunca como juez final.

---

## Frases trigger

| Qué quiero | Frase exacta |
|---|---|
| Validar un relato ya escrito | `/validate-prose-es <path>` · ej. `/validate-prose-es content/ficciones/_one-shots/el-que-viene-a-tomar-cafe/2026-04-19-el-que-viene-a-tomar-cafe.md` |
| Validación automática al final de `/ficcion-draft` | Invocado sin frase explícita en paso 8.4 del skill generador |
| Validar texto pegado inline | Pegar texto + *"valida este texto con /validate-prose-es"* — el skill lo guarda como tempfile y ejecuta |

---

## When to activate

- Cuando Rafael escribe `/validate-prose-es <path>`.
- Cuando `/ficcion-draft` llega al paso 8.4 (integración obligatoria).
- NUNCA auto-activar — es paso explícito.

---

## Arquitectura · 2 capas

```
┌────────────────────────────────────────────────┐
│ CAPA 1 · GREP DETERMINISTIC (obligatoria,      │
│ primera, infalible en su scope)                │
│                                                │
│ Ejecuta los 22 greps del knowledge ES          │
│ (castellano-literario-es.md §§ 3 + 8.1)        │
│ sobre el path dado. Reporta CADA match con     │
│ contexto (±1 línea).                           │
│                                                │
│ Output:                                        │
│ - Lista de matches por calco (1-22)            │
│ - Total de hits                                │
└──────────────────┬─────────────────────────────┘
                   │
           ┌───────▼────────┐
           │ ¿Hay matches?  │
           └───┬────────┬───┘
               │        │
          SÍ   │        │  NO
               │        │
┌──────────────▼──┐  ┌──▼─────────────────────────────┐
│ BLOQUEO         │  │ CAPA 2 · AGENT LLM COMPLEMENTO │
│ Reportar todos  │  │ (solo si Capa 1 está limpia)   │
│ los matches +   │  │                                │
│ forzar fix      │  │ Busca lo que el grep NO coge:  │
│ antes de pasar  │  │ - Colocaciones no documentadas │
│ a Capa 2        │  │ - Registros mezclados          │
│                 │  │ - Ritmo incoherente            │
└─────────────────┘  │ - Frases que requieren releer  │
                     │                                │
                     │ Devuelve 0-15 preguntas        │
                     │ de challenge al autor          │
                     └──────────────┬─────────────────┘
                                    │
                     ┌──────────────▼─────────────────┐
                     │ VEREDICTO COMBINADO             │
                     │                                 │
                     │ - Capa 1 hits + Capa 2 hits → │
                     │   unión de severidades          │
                     │ - LLM solo SUBE severidad,     │
                     │   nunca la baja                 │
                     │                                 │
                     │ READY / PENDING / REWRITE      │
                     └─────────────────────────────────┘
```

### Principio inviolable

**El LLM nunca sustituye al grep.** Si Capa 1 encuentra 5 matches y el LLM en Capa 2 dice *"me parecen todos correctos"*, veredicto = PENDING_FIXES igual. El LLM solo **añade** hallazgos que al grep se le escapan; nunca los quita.

---

## CAPA 1 · Grep deterministic

### Patrones a ejecutar (22 calcos)

Los 22 calcos están documentados en [`references/ficciones/castellano-literario-es.md § 3 + § 8.1`](../../references/ficciones/castellano-literario-es.md) con sus regex exactas.

**Comando consolidado (ejecutar vía bash tool):**

```bash
#!/bin/bash
# /validate-prose-es · Capa 1 · 22 greps deterministic
# Uso: bash validate-layer-1.sh <path-al-relato.md>

TEXT="$1"
TOTAL=0

echo "═══ CAPA 1 · GREP DETERMINISTIC · 22 calcos ═══"

check() {
  local num="$1" name="$2" pattern="$3" flags="${4:--niE}"
  local matches
  matches=$(grep $flags "$pattern" "$TEXT" 2>/dev/null)
  local count=$(echo -n "$matches" | grep -c . || true)
  if [ "$count" -gt 0 ]; then
    echo ""
    echo "── Calco $num · $name · $count match(es) ──"
    echo "$matches"
    TOTAL=$((TOTAL + count))
  fi
}

check  1 "Posesivo + parte del cuerpo"        "sus (manos|ojos|piernas|brazos|labios|dedos|pies|hombros|rodillas|cabezas?|caras?)"
check  3 "De repente"                          "de repente"
check  4 "Adverbios -mente" "[a-záéíóúñ]+mente" -oniE
check  5 "Pasiva ser+participio"               "\\b(fue|fueron|era|eran) [a-záéíóú]+ad[oa]s?\\b"
check  7 "Conectores anglo"                    "sin embargo|de hecho|por supuesto|en definitiva"
# PATRONES UNICODE-SAFE (v3 · 2026-04-20 tarde) — cross-platform Windows/Linux/macOS.
# Alternaciones literales (con-tilde|sin-tilde) en vez de clases [oó] que fallan en Windows.
check 13 "Sustantivos compuestos 'X center'"   "(centro de (demostración|demostracion|llamadas|datos|servicio|atención|atencion|operaciones)|call center|data center)"
check 14 "'En [órgano] de [actor]' no-verbal"  "en (boca|ojos|cabeza|mano) de [^.]*(actriz|actor|personaje|humanoide|robot|máquina|maquina)"
check 15 "Voz técnica en narrador"             "\\b(configuré|configuró|configuro|configura|configurado|configurada|registra|registró|registro|registrado|registrada|activó|activo|activa|activado|activada|ejecutó|ejecuto|ejecuta|módulo|modulo|input|output|backend|lanzó (la|una) (actualización|actualizacion)|cruzó con (los |las |el |la )?(datos|fotos|archivos|registros|imágenes|imagenes|perfiles|contactos|campos))\\b"
check 16 "Colocaciones idiomáticas forzadas"   "(de medio lado|a medio camino de|en el medio de)"
check 17 "Microcopy UI anglo"                  "(No, gracias|¿Estás seguro|¿Estas seguro|Enviar feedback|Aprender más|Aprender mas|Configuraciones|[Gg]ot it)"
check 18 "Preposiciones espaciales calcadas"   "\\b(enfrente|en frente) (del|de la|de los|de las) (humanoide|robot|androide|autómata|automata|aparato|asistente|máquina|maquina|sistema|ordenador|teléfono|telefono|madre|padre|hijo|hija|hermano|hermana|usuario|cliente|cuidadora?|operadora?)"
check 19 "Clarificación anglo 'Es decir X y'"  "\\bEs decir, [^.,]{1,40}, y [a-z]"
check 20 "Inciso em-dash cerrando con ', y, '"  "— [^—]{3,80} — y, "
check 21 "Pasiva con dar a actor institucional" "\\bse (da|dio|daba|dan|dieron|daban) (al|a los|a las|a la) (tutora?|usuario|cliente|representante|sistema|responsable|cuidadora?|paciente|administradora?)"
# Calco 22 (v5 · 2026-04-24) — frase relativa descriptiva en lugar de adjetivo/sustantivo ES idiomático
# Origen: subtítulo "un botón que no hace ruido" en La objeción (detectado por Rafael leyendo, validador no lo cogió)
check 22 "Frase relativa descriptiva ↔ adjetivo ES" "(un[oa]?|el|la|los|las|este|esta|estos|estas|ese|esa|esos|esas) [a-záéíóúñ]+ que no (hace|se [a-záéíóúñ]+|para de [a-záéíóúñ]+|deja de [a-záéíóúñ]+|tiene [a-záéíóúñ]+)"
# Calco 23 (v6 · 2026-04-26) — referencia espacial 2D ("columna izquierda/derecha", "lado izquierdo") en bloques que en mobile-first se renderizan apilados
# Origen: borrador 'mejor-robot-aspirador-barato-2026' decía "Si las cinco cosas de la columna izquierda te bastan y las cinco de la derecha..." cuando el cuadro qué-sí qué-no es stack vertical en móvil (80% del tráfico). Rafael lo detectó al leer el .md.
# Reescribir usando referencia semántica: "el bloque verde / el rojo", "lo que sí / lo que no", "el primer cuadro / el segundo", "la lista de arriba / la de abajo".
check 23 "Referencia espacial 2D en stack vertical mobile-first" "\\b(columnas? (izquierd[oa]|derech[oa])|lados? (izquierd[oa]|derech[oa])|del (lado|panel|cuadro|recuadro) (izquierd[oa]|derech[oa])|a la (izquierda|derecha)|en la (izquierda|derecha))\\b"

echo ""
echo "═══ CAPA 1 TOTAL · $TOTAL matches literales (calcos 20 aparte) ═══"
```

**Interpretación de matches:**

- **Calcos 1, 3, 13, 16, 17, 18, 20, 21, 23:** meta = 0. Cualquier match es error. Reescribir.
- **Calcos 4, 5, 7, 14, 15, 19, 22:** revisar contexto. Pueden tener excepciones legítimas (cita de manual en calco 15, adverbio ocasional en calco 4, pasiva refleja legítima en calco 5, frase relativa deliberadamente literaria en calco 22). El autor debe defender cada match en la respuesta.
- Si TOTAL ≥ 1 en calcos meta=0 → **BLOQUEO automático**. Fix obligatorio antes de Capa 2.

### Formato del output de Capa 1

Lo que Claude Code muestra a Rafael:

```
═══ VALIDADOR · CAPA 1 · GREP DETERMINISTIC ═══

Ejecutados los 22 greps sobre <path>.

[Lista de matches por calco si hay]

── Calco 13 · Sustantivos compuestos 'X center' · 1 match ──
51: *"El centro de demostración fue en septiembre"*

── Calco 14 · 'En [órgano] de [actor]' no-verbal · 1 match ──
52: *"vio la escena en boca de una actriz contratada"*

[...]

═══ TOTAL · N matches ═══

→ Si N ≥ 1 en calcos meta=0: BLOQUEO. Fix obligatorio antes de pasar a Capa 2.
→ Si solo hay matches en calcos a revisar (4, 5, 7, 14, 15, 19): continuar a Capa 2 con preguntas sobre esos matches concretos.
```

---

## CAPA 2 · Agent LLM complementario

Solo se ejecuta si Capa 1 está limpia (0 matches en calcos meta=0) o tras aplicar los fixes.

### Prompt del Agent Explore (auto-contenido)

El Agent NO tiene acceso al proceso de generación, NO ve `PASOS.md`, NO ve el prompt original del relato. Solo ve el texto + el knowledge ES + los matches de Capa 1 (si los hay en calcos a revisar).

```
Eres editor profesional de narrativa en castellano peninsular literario contemporáneo. Tu trabajo es AUDITAR una pieza de ficción para detectar vicios que al grep determinista (ya ejecutado) se le hayan escapado.

NO DUPLIQUES el trabajo del grep. El grep ya peinó el texto con 21 patterns documentados y devolvió 0 matches en calcos meta=0, o los matches en calcos a revisar (que incluyo abajo si los hay). Tu trabajo es COMPLEMENTARIO:

1. Colocaciones léxicas anglo NO documentadas todavía
2. Expresiones idiomáticas forzadas nuevas
3. Registros mezclados (técnico infiltrándose, jerga profesional fuera de lugar)
4. Ritmo incoherente con el registro predominante
5. Frases que un lector ES peninsular tendría que releer para entender

**REGLAS DURAS:**

- Si el texto te parece impecable tras lectura cuidadosa, di "veredicto preliminar: sin hallazgos complementarios" y devuelve 0 preguntas. No inventes problemas.
- Si encuentras vicios, devuelve 3-10 preguntas de challenge específicas al autor.
- NUNCA contradigas los matches del grep. El grep es autoridad — si matchea, es error aunque a ti te parezca correcto.
- NO puedes bajar severidad de veredicto. El grep ya calibró la severidad mínima. Tú solo puedes subirla.

**Input:**

Knowledge de referencia: lee c:\Users\bakal\robohogar\references\ficciones\castellano-literario-es.md §§ 4 (los 12 recursos ES positivos) y § 5 (ritmo ES). NO leas §§ 3 ni 8 ni 3.bis — eso ya lo ejecutó el grep; tú complementas.

Texto del relato (path): <path>
Matches de Capa 1 a revisar (calcos 4, 5, 7, 14, 15, 19): [lista si hay]

**Output formato — SOLO tabla:**

| # | Frase | Vicio sospechado | Pregunta al autor |
|---|---|---|---|

Sé estricto. Si el texto tiene problemas, dilo.
```

---

## Veredicto combinado

```python
def veredicto_combinado(capa1_matches, capa2_hallazgos):
    # Matches en calcos meta=0 bloquean siempre
    bloqueantes_capa1 = sum(capa1_matches[k] for k in [1,3,13,16,17,18,20,21] if k in capa1_matches)
    
    # Matches en calcos a revisar + hallazgos de capa 2
    revisables = sum(capa1_matches[k] for k in [4,5,7,14,15,19] if k in capa1_matches)
    revisables += len(capa2_hallazgos)
    
    total_reescribir = bloqueantes_capa1 + revisables
    
    if bloqueantes_capa1 == 0 and revisables == 0:
        return "READY"
    elif total_reescribir <= 5:
        return "PENDING_FIXES"
    else:
        return "MAJOR_REWRITE"
```

**Tabla de decisión:**

| Capa 1 (meta=0) | Capa 1 (revisar) | Capa 2 (nuevos) | Total | Veredicto |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | READY |
| 0 | 1-3 | 0-2 | 1-5 | PENDING_FIXES |
| 0 | 4+ | 0+ | 6+ | MAJOR_REWRITE |
| 1+ | cualquiera | cualquiera | 6+ | MAJOR_REWRITE (bloqueantes presentes) |

---

## Fase 4 · Auto-catalogación — el validador aprende automáticamente (v4 · 2026-04-20)

**Principio clave:** cada hallazgo de Capa 2 (LLM) que NO corresponde a los 22 calcos existentes genera una propuesta de **auto-documentación** del knowledge. El validador deja de ser filtro pasivo para convertirse en sistema self-learning.

### Por qué

Antes (v3) el protocolo decía: *"cada fallo del validador que Rafael detecte se añade manualmente al knowledge"*. Esto es cuello de botella — si Rafael no tiene tiempo o se le olvida, el grep se queda estático y el validador no mejora. El sistema entero depende de trabajo editorial manual.

Rafael lo formuló así: *"no puedes hacer que, cuando el LM detecte fallos, también lo documente en castellano literario? No lo entiendo. Si tienes un agente de validación que encuentra fallos, pues directamente que lo catalogue también para el futuro. No hace falta que lo hagas solo manualmente, que igual no lo hago en realidad"*.

### Flujo

```
┌──────────────────────────────────────────────────────┐
│ Capa 2 (LLM) detecta hallazgo                        │
│ ¿Corresponde a calco documentado (1-21)?             │
└──────────────────┬───────────────────────────────────┘
                   │
          ┌────────┴────────┐
          │                 │
       SÍ │                 │ NO
          │                 │
  ┌───────▼──────┐   ┌──────▼────────────────────────┐
  │ Reportar     │   │ Fase 4 · AUTO-CATALOGACIÓN    │
  │ como match   │   │                                │
  │ (normal)     │   │ 1. Clasificar patrón:         │
  └──────────────┘   │    a) Generalizable → nuevo   │
                     │       calco 22+                │
                     │    b) Caso único → solo añadir│
                     │       a §3.bis                 │
                     │    c) Expansión de existente →│
                     │       ampliar regex actual     │
                     │                                │
                     │ 2. Generar propuesta:         │
                     │    - Regex Unicode-safe       │
                     │    - Entry §3 (si a)          │
                     │    - Caso canónico §3.bis     │
                     │    - Checklist §8.1           │
                     │    - Grep del skill §8.3      │
                     │                                │
                     │ 3. Auto-test:                 │
                     │    - ¿Detecta el hallazgo     │
                     │      que lo originó?          │
                     │    - ¿0 matches sobre borrador│
                     │      final (no FP)?           │
                     │    - ¿≥1 match en fixture     │
                     │      canonical-errors.md?     │
                     │                                │
                     │ 4. Presentar a Rafael:        │
                     │    "Propongo Calco 22 [X]     │
                     │     con regex [Y]. ¿OK/skip?" │
                     │                                │
                     │ 5. Si OK:                     │
                     │    - Aplicar edits a los 3    │
                     │      archivos canónicos       │
                     │    - Añadir entrada al fixture│
                     │      test                      │
                     │    - Log en validator-reports │
                     └────────────────────────────────┘
```

### Criterios de clasificación

El LLM de Capa 2 clasifica cada hallazgo nuevo en 3 tipos:

| Tipo | Cuándo | Acción |
|---|---|---|
| **(a) Generalizable** | Patrón repetible: verbo + colocación, sustantivo compuesto, estructura sintáctica clonable | Nuevo calco N+1 en §3 + regex + caso §3.bis |
| **(b) Caso único** | Error idiomático muy específico de un contexto, poco probable que se repita | Solo caso en §3.bis, sin nuevo calco ni regex |
| **(c) Expansión** | Variante de un calco existente (ej: Calco 15 cubre *"cruzar con datos"* pero descubrimos *"cruzar con archivos"*) | Ampliar regex del calco ya documentado |

### Auto-test obligatorio antes de mergear

La regex propuesta debe pasar tres tests antes de proponerse a Rafael:

1. **Positivo:** detecta el hallazgo que la originó (mínimo 1 match en el texto auditado).
2. **Regresión fixture:** aplicada sobre [`_test-fixtures/v2-pre-fixes-canonical-errors.md`](../../content/ficciones/_one-shots/el-que-viene-a-tomar-cafe/_test-fixtures/v2-pre-fixes-canonical-errors.md) no rompe matches existentes (los 9 calcos canónicos siguen detectándose).
3. **No falsos positivos:** aplicada sobre el borrador ya validado del relato auditado, devuelve 0 matches en prosa publicable (permitido matches en comentarios de trazabilidad, que se ignoran).

Si falla cualquiera de los 3 → el skill NO propone la auto-catalogación. Reporta el hallazgo a Rafael como "candidato manual" para que él decida si documentarlo fuera del flujo automático.

### Formato de propuesta al usuario

Cuando la auto-catalogación está lista para aprobar, el skill muestra:

```
═══ AUTO-CATALOGACIÓN · Calco 22 candidato ═══

Patrón detectado en <path>, línea N:
  "<frase literal>"

Clasificación: Generalizable
Ejemplo canónico:
  ❌ <frase con vicio>
  ✅ <fix propuesto>

Regex Unicode-safe propuesta:
  grep -niE "<regex>"

Tests:
  [✅] Detecta el hallazgo original
  [✅] 0 matches sobre borrador validado
  [✅] Fixture canonical-errors.md sigue dando 9/9

Archivos a modificar:
  - references/ficciones/castellano-literario-es.md (§3 + §3.bis + §8.1)
  - .claude/commands/ficcion-draft.md (§8.3)
  - .claude/commands/validate-prose-es.md (Capa 1 bash)
  - content/ficciones/_one-shots/.../​_test-fixtures/v2-pre-fixes-canonical-errors.md

→ Aprobar [OK] · Descartar [skip] · Modificar regex [edit]
```

Rafael solo escribe `OK`, `skip`, o edita la regex. El skill aplica.

### Safeguards

- **Aprobación humana obligatoria** antes del merge (nunca auto-merge sin OK).
- **Auto-test obligatorio** antes de proponer (nunca proponer regex sin testear).
- **Una propuesta por sesión de validación**, no 10 a la vez (evita fatiga de aprobación). Si el LLM detecta 5 hallazgos nuevos, prioriza el más frecuente/severo y reserva los otros 4 para sesiones siguientes.
- **Rollback simple:** los edits se hacen con `Edit` atómico; si algo sale mal, `git restore` limpia.
- **Log permanente** en `validator-reports/YYYY-MM-DD-<slug>-report.md` con regex propuesta + tests + decisión de Rafael + diff aplicado.

### Historial de aprendizaje (versionado)

- **v1** (2026-04-19 mañana) · 12 calcos sintácticos iniciales (anti-IA checklist + castellano literario §3 v1).
- **v2** (2026-04-20 mañana) · +5 calcos léxicos (13-17) — manual, tras incidente editorial *"El que viene a tomar café"*.
- **v3** (2026-04-20 tarde) · +4 calcos (18-21) — manual, tras test empírico del validador LLM-solo.
- **v4** (2026-04-20 tarde) · **Arquitectura self-learning activada** — próximas expansiones del knowledge serán automáticas vía Fase 4 (propuesta LLM + OK humano + auto-test + merge).

---

## Outputs

Archivos que el skill NO modifica (solo lee):
- `<path>` del relato
- `references/ficciones/castellano-literario-es.md`

Archivos que el skill SÍ puede escribir (si Rafael aprueba):
- El propio `<path>` — aplicando fixes de la tabla veredicto
- `content/ficciones/<slug>/validator-reports/YYYY-MM-DD-report.md` — log permanente

---

## Integración en `/ficcion-draft § 8.4`

El skill `/ficcion-draft` invoca `/validate-prose-es` en el paso 8.4 (entre 8.3 greps directos y 8.5 formato Beehiiv). Ver [`.claude/commands/ficcion-draft.md § 8.4`](ficcion-draft.md).

Si veredicto = READY → proceder al paso 8.5.
Si PENDING_FIXES → aplicar fixes al borrador.html + .md. Re-invocar `/validate-prose-es`. Si sigue PENDING tras 2 pases, mostrar a Rafael.
Si MAJOR_REWRITE → BLOQUEAR output. Volver al paso 6 (prosa).

---

## Reglas inviolables

1. **Capa 1 SIEMPRE se ejecuta primero.** No hay atajos, no hay skip.
2. **Capa 2 solo ejecuta si Capa 1 está limpia de bloqueantes** (calcos meta=0 con 0 matches).
3. **El Agent de Capa 2 NUNCA recibe:** el prompt original, el `PASOS.md`, las decisiones del autor.
4. **El LLM nunca baja severidad.** Si Capa 1 encuentra 3 matches, veredicto mínimo = PENDING_FIXES aunque el LLM diga "impecable".
5. **Cada fallo genera regex nueva.** El validador aprende leyendo el feedback de Rafael.
6. **Ejecutar SIEMPRE desde `/ficcion-draft § 8.4`** — y manualmente sobre relatos ya escritos cuando se quiera auditoría fresca.

---

## Cross-references

- Knowledge ES: [`references/ficciones/castellano-literario-es.md`](../../references/ficciones/castellano-literario-es.md) §§ 3, 3.bis, 4, 5, 8.1
- Skill generador: [`.claude/commands/ficcion-draft.md § 8.3-8.4`](ficcion-draft.md)
- Memoria del incidente origen + test: `feedback_anti_calcos_lexicos_es.md`
- Regla de composición ES directa: [`.claude/rules/editorial.md § Narrativa especulativa § Composición ES directa`](../rules/editorial.md)
