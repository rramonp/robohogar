# Commit — Git Commit

## When to activate

- "commit", "haz commit", "commitea", "guarda los cambios"

## Workflow

### 1. Pre-flight

Run in parallel:
- `git status` — changed/untracked files
- `git diff` + `git diff --staged` — all modifications
- `git log --oneline -5` — recent commit style

### 2. Sanity checks

- No API keys, secrets, or `.env` content staged
- No accidental large binaries (>1MB) unless in `assets/`
- No unresolved shell variables in committed files

### 3. Stage and commit

- Stage relevant files by name (NOT `git add -A`)
- Draft commit message:

```
Short descriptive title

Changes: <files added/modified/removed and why>

Co-Authored-By: Claude <model> <noreply@anthropic.com>
```

- Create the commit
- Run `git status` to verify clean state

### 4. Push (only if Rafael asks)

Do NOT auto-push. If Rafael says "y push" or "pushea", then push.
