# Vault Organizer — Cross-Repo Invocation

Run the vault organizer skill from the RRP-DEV repository. This command delegates
to the full vault-organizer implementation that lives in `c:/Users/bakal/RRP-DEV/`.

## When to activate

- "organiza mi vault", "audit vault", "limpia obsidian", "vault lint"
- "mirror repo", "sincroniza el repo", "actualiza el mirror"
- Any vault organization or repo mirror request

## How it works

This repo (robohogar) does NOT contain its own vault organizer scripts.
The full implementation lives in RRP-DEV at `skills/vault_organizer/`.

When invoked from robohogar, execute the vault organizer from RRP-DEV:

1. **Read the main command** at `c:/Users/bakal/RRP-DEV/.claude/commands/vault-organizer.md`
2. **Follow those instructions** — all modes, cardinal rules, and execution flow apply
3. **Repo mirror (Mode 12)** will mirror BOTH RRP-DEV and robohogar to the vault
   using `MIRROR_REPOS` config in `skills/vault_organizer/config.py`

## Key paths

| Item | Path |
|---|---|
| Vault organizer scripts | `c:/Users/bakal/RRP-DEV/skills/vault_organizer/` |
| Config | `c:/Users/bakal/RRP-DEV/skills/vault_organizer/config.py` |
| Main command | `c:/Users/bakal/RRP-DEV/.claude/commands/vault-organizer.md` |
| This repo (mirror source) | `c:/Users/bakal/robohogar/` |
