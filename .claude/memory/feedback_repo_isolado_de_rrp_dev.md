---
name: ROBOHOGAR repo aislado de RRP-DEV — cero cross-calls
description: El repo robohogar es 100% autocontenido desde 2026-04-27. NO invocar scripts ni cargar memoria desde RRP-DEV. Toda dependencia funcional vive bajo c:\Users\cri-c\robohogar.
type: feedback
---

Decisión Rafael 2026-04-27: el repo robohogar y el repo RRP-DEV viven aislados, **nunca se llaman entre sí**. Cada uno autocontenido. Razón literal de Rafael: *"estoy cansado de estar cruzando repositorios todo el tiempo. Quiero que cada uno esté aislado del otro y nunca sacan llamadas de uno a otro"*.

**Why:** mantener dependencias en RRP-DEV (ej. `$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py`) significa que clonar/sincronizar solo ROBOHOGAR no basta — hace falta también RRP-DEV. Eso rompe la portabilidad laptop ↔ desktop, complica backups, y mete fricción cognitiva al editar el repo. Cada repo debe poder correr todo su pipeline sin más checkouts.

**Migración aplicada 2026-04-27:**

- `utilities/nano_banana_image.py` ← copiado de `RRP-DEV/skills/external/nano_banana/scripts/image.py` (script de generación con Gemini API, 13.6 KB).
- `skills/ui_ux_pro_max/scripts/{search,core,design_system}.py` ← copiados de `RRP-DEV/skills/external/ui_ux_pro_max/scripts/`.
- `skills/ui_ux_pro_max/data/*.csv` ← 15+ databases BM25 copiadas desde RRP-DEV.

**Skills actualizados:**

- `.claude/commands/nano-banana.md` § Script + § Invocation → `uv run utilities/nano_banana_image.py` (cero referencias a RRP-DEV).
- `.claude/commands/ui-ux-pro-max.md` § Location + § Usage → `python skills/ui_ux_pro_max/scripts/search.py`.
- `.claude/commands/content-draft.md` § Generar hero → `utilities/nano_banana_image.py`.
- `assets/branding/asset-catalog.md` § Parámetros técnicos → `utilities/nano_banana_image.py`.

**How to apply (regla operativa):**

- Cualquier nueva skill o script que se añada al repo robohogar **vive en robohogar**, no en RRP-DEV. Si hay tentación de poner algo en `$HOME/RRP-DEV/skills/external/<nombre>/` "porque también lo usaré en otro proyecto", duplicarlo en cada repo donde se use, no compartirlo. La duplicación es más barata que la dependencia cruzada.
- Cualquier `.md` o `.py` del repo que mencione `$HOME/RRP-DEV/` o `RRP-DEV/skills/external/` como ruta funcional (no como referencia documental al ecosistema general del usuario) **es bug** — actualizar a path local del repo.
- La memoria sigue las reglas previas (`feedback_memoria_local_robohogar.md`): toda memoria de proyecto en `c:\Users\cri-c\robohogar\.claude\memory\`. Memoria global del usuario en `c:\Users\cri-c\RRP-DEV\.claude\memory\` queda como índice transversal de Rafael, sin contenido específico de robohogar.

**Excepciones documentales (NO funcionales, no requieren cambio):**

- `.claude/rules/config.md § Rutas del proyecto` menciona la ruta de RRP-DEV como referencia geográfica del entorno, no como dependencia funcional. Mantener.
- `CLAUDE.md` puede mencionar RRP-DEV en contexto histórico/explicativo. Mantener.
- Memorias del repo que mencionan paths del usuario (`feedback_memoria_local_robohogar.md`, `project_robohogar_paths.md`) son documentales. Mantener.

**Verificación pre-commit / post-merge:**

```bash
# Llamadas funcionales a scripts de RRP-DEV — debe ser 0
grep -rE 'RRP-DEV/skills/external/[^/]+/scripts/[^"]+\.py' \
  --include="*.md" --include="*.py" \
  /c/Users/cri-c/robohogar/ | grep -v '\.git/'
```

Si devuelve >0 → arreglar antes de commit. Las menciones documentales en `config.md`, `CLAUDE.md` y memorias no deben tener path completo a script ejecutable; si lo tienen, esa línea es un bug.

**Efecto en `git pull` desde laptop:** ahora la laptop también necesita los mismos cambios. Cuando Rafael sincronice ambas máquinas, los scripts copiados viajan con `git push/pull`. Tras eso, la laptop puede borrar `$HOME/RRP-DEV/skills/external/nano_banana/` y `$HOME/RRP-DEV/skills/external/ui_ux_pro_max/` si no los usa para otros proyectos.
