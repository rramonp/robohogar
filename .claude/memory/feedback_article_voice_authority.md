---
name: article_voice_authority
description: ROBOHOGAR — nunca narrar el proceso de investigación ("hemos leído X, Y, Z medios") en el texto publicado. Voz de autoridad propia.
type: feedback
originSessionId: fb181127-6137-468a-851e-9fa2059a15ed
---
En artículos, newsletters y posts sociales de ROBOHOGAR, **NUNCA mencionar en el texto publicado** frases del tipo *"hemos leído / revisado / comparado / contrastado con X, Y, Z newsletters o medios para hacer este artículo"*. Queda cutre — da la impresión de que el autor solo ha agregado fuentes sin aportar autoridad propia.

**Las fuentes externas se citan de dos formas permitidas:**
1. **Como autoridad puntual de un dato concreto.** Ejemplo OK: *"Xataka Home lo explica sin rodeos: el vapor va a las mopas, no al suelo"*.
2. **Como link contextual dentro de un párrafo** (hipertexto), sin narrativa del proceso. Ejemplo OK: *"según [Vacuum Wars](url), el brazo acierta aproximadamente la mitad de las veces"*.

**Formas prohibidas:**
- ❌ "Hemos leído Xataka Home, SamMobile y Vacuum Wars, y…"
- ❌ "Contrastado con X, Y, Z newsletters"
- ❌ "Nos hemos metido en 10 reviews internacionales y este es el resumen"
- ❌ "Hemos recopilado toda la información de…"

**Why:** Rafael rechazó este framing explícitamente el 18-abr-2026 en el hook del review Samsung Jet Bot Steam Ultra (artículo #6). Texto literal de su corrección: *"Queda muy cutre decir: 'Me he metido en esta página, en esta página, en esta página; he cogido de aquí, de aquí, de allí y lo he mezclado todo y aquí tienes el artículo'"*. La voz de marca ROBOHOGAR es de autoridad propia que cita fuentes puntuales — no de agregador que compila otros medios.

**How to apply:**
- En **hooks y aperturas**: NUNCA mencionar medios terceros. El hook ataca directo al claim/tesis.
- En el **cuerpo del artículo**: citar fuente como autoridad de un dato concreto (1-2 fuentes máximo por sección), no como proceso narrado.
- La **tabla completa de fuentes** vive en `PASOS.md` § Fuentes del artículo (decisión editorial interna, no texto publicable).
- Si un artículo necesita citar >3 fuentes externas en el cuerpo, revisar si el ángulo editorial es lo bastante fuerte — probablemente el problema no es la voz, es que no hay tesis propia.
- Skill `/content-draft` debe respetar esta regla al generar hooks y primeras secciones.
