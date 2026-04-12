# Literate Code

ALL Python code must be understandable by a non-developer or a future AI agent.

## Requirements

1. **Module docstring**: every `.py` file — purpose, usage, dependencies
2. **Function docstring**: functions with >5 lines — what it does, args, return
3. **Section headers**: `# ═══` or `# ---` separators for logical blocks in files >100 lines
4. **Inline narrative**: minimum 1 comment per 15 lines of executable code
5. **Business logic**: explain WHY, not WHAT

## Exemptions

- `__init__.py` under 20 lines
- Pure config/constant files
