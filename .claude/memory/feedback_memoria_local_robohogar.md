---
name: Memoria ROBOHOGAR local y aislada — nunca a RRP-DEV
description: Toda memoria generada trabajando en el repo ROBOHOGAR se guarda EXCLUSIVAMENTE en robohogar/.claude/memory/. Prohibido escribir en RRP-DEV/.claude/memory/ durante sesiones con CWD=robohogar, aunque el system-prompt genérico de auto-memoria apunte allí.
type: feedback
---

Regla dura establecida por Rafael 2026-04-24:

**Toda memoria que se guarde trabajando en este repo (ROBOHOGAR) se queda aquí, exclusivamente en `c:\Users\bakal\robohogar\.claude\memory\`. Nada se comparte, duplica ni escribe en `c:\Users\bakal\RRP-DEV\.claude\memory\`.**

**Why:** el repositorio ROBOHOGAR es un proyecto autocontenido (newsletter + blog de robótica doméstica). Rafael quiere que el conocimiento del proyecto viaje con el repo — si clona robohogar en otra máquina, o si en algún momento sincroniza el repo via git hacia otro entorno, las memorias deben estar dentro del propio repo, no dispersas en un directorio transversal que no viaja con el código. Además evita que memorias del proyecto ROBOHOGAR contaminen el contexto de otros proyectos (HBX, Neon, etc.).

**How to apply (regla operativa simple):**

- **CWD = `c:\Users\bakal\robohogar\` → toda memoria a `c:\Users\bakal\robohogar\.claude\memory\`**. Sin excepciones. Sin bifurcación por tema.
- No importa si la memoria es editorial, técnica, project-state, feedback, reference o infra específica de este repo — siempre se guarda aquí.
- El MEMORY.md a actualizar es `c:\Users\bakal\robohogar\.claude\memory\MEMORY.md`.
- **El system-prompt genérico de auto-memoria apunta a `RRP-DEV/.claude/memory/` pero esa ruta es el default para OTROS proyectos (HBX, Neon) y para cuando no hay un `.claude/memory/` local en el repo activo. ROBOHOGAR tiene su propio folder local y por tanto se auto-contiene.**
- Si dudo entre ROBOHOGAR y transversal: ROBOHOGAR gana. Nunca escribir en RRP-DEV desde sesiones con CWD=robohogar.

**Excepción única permitida:** si Rafael pide EXPLÍCITAMENTE que algo se guarde en RRP-DEV porque es genuinamente transversal (ej: *"guarda esto en RRP-DEV"* / *"esta es cross-project"*), entonces sí. Nunca por iniciativa propia desde el repo ROBOHOGAR.

**Aplicación inversa:** cuando trabajemos en otros repos (RRP-DEV, HBX, Neon), no escribir NUNCA memoria en `robohogar/.claude/memory/`. Cada proyecto se auto-contiene.

**Incidente origen:** 2026-04-24 Rafael migró ~56 memorias ROBOHOGAR de RRP-DEV a robohogar/.claude/memory/ (reorganización en 7 secciones). Minutos después yo guardé por error `feedback_memory_routing_por_scope.md` en RRP-DEV proponiendo una bifurcación por tema. Rafael corrigió: la regla es CWD-based y dura — lo que se genere aquí, se queda aquí. Archivo eliminado de RRP-DEV y esta memoria lo sustituye en el sitio correcto.
