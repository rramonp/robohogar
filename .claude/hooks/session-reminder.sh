#!/usr/bin/env bash
# Hook Stop: recordatorio pre-cierre de sesión.
#
# Se dispara cuando el modelo termina su turno. Mira si hay cambios sin commit
# en content/articulos/ o content/ficciones/ y, si los hay, imprime un
# recordatorio breve. No bloquea (exit 0 siempre).

cd "$CLAUDE_PROJECT_DIR" 2>/dev/null || exit 0

# Cambios sin commit en directorios editoriales sensibles.
DIRTY=$(git status --porcelain -- content/articulos/ content/ficciones/ content/registro-articulos.md content/registro-ficciones.md content/calendario-editorial.md 2>/dev/null | head -20)

if [ -n "$DIRTY" ]; then
  cat << 'EOF'

———————————————————————————————————————————
Recordatorio cierre de sesión ROBOHOGAR
———————————————————————————————————————————
Hay cambios sin commit en contenido editorial.
- Si tocaste un borrador / ficción / registro: revisa que /validate-prose-es ya pasó.
- Si el flujo es ya estable: git add <files> + git commit + git push para que el desktop lo vea.
- Si son experimentos no listos: stash o sigue sin commit.
———————————————————————————————————————————
EOF
fi

exit 0
