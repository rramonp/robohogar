#!/usr/bin/env python3
"""
Repo Mirror — Mode 7 of obsidian-robohogar skill

Mirrors the ROBOHOGAR repository structure and content into the Obsidian vault
as navigable Markdown notes with copiable code blocks. Same engine pattern as
RRP-DEV's vault_organizer/repo_mirror.py, adapted for ROBOHOGAR's structure.

Purpose: disaster recovery — if GitHub, Claude Code, or the machine is lost,
the vault contains a complete, self-contained copy of all code, config, rules,
commands, articles, docs, and references needed to reconstruct the project or
onboard another AI assistant.

Each repo file becomes a vault note with:
  - Frontmatter: mirror-source, mirror-hash (SHA-256), mirror-date, mirror-commit
  - For .py/.json/.html: content wrapped in fenced code blocks with syntax highlight
  - For .md files: content embedded directly with header levels shifted down

Reconciliation logic (incremental by default, --full for rebuild):
  1. Inventory vault mirror (read mirror-source + mirror-hash from frontmatter)
  2. Inventory repo (scan files per MIRROR_SECTIONS config)
  3. Diff: compare hashes to find new / modified / deleted files
  4. Apply: create, update, or remove vault notes (only changed files)
  5. Generate master index + Architecture Overview

Usage:
    python repo_mirror.py <vault_path> <repo_path> [--full] [--dry-run] [--report]

Dependencies: config.py (MIRROR_SECTIONS, MIRROR_VAULT_RELPATH, MIRROR_LANG_MAP, etc.)
"""

import os
import sys
import hashlib
import re
import glob as globmod
from pathlib import Path
from datetime import date
from collections import defaultdict

# ── Import config from same package, with fallback for CLI execution ──
try:
    from skills.vault_sync.config import (
        MIRROR_VAULT_RELPATH,
        MIRROR_SECTIONS,
        MIRROR_IGNORE_DIRS,
        MIRROR_IGNORE_FILES,
        MIRROR_LANG_MAP,
        MIRROR_INDEX_NAME,
        REPO_NAME,
        SECTION_ORDER,
        resolve_vault_path,
    )
except ImportError:
    # Fallback: add repo root to path so `skills.vault_sync.config` resolves
    sys.path.insert(
        0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    )
    from skills.vault_sync.config import (
        MIRROR_VAULT_RELPATH,
        MIRROR_SECTIONS,
        MIRROR_IGNORE_DIRS,
        MIRROR_IGNORE_FILES,
        MIRROR_LANG_MAP,
        MIRROR_INDEX_NAME,
        REPO_NAME,
        SECTION_ORDER,
        resolve_vault_path,
    )


# ══════════════════════════════════════════════
# Hashing
# ══════════════════════════════════════════════


def file_hash(filepath):
    """Compute short SHA-256 hash (first 12 hex chars) of a file's content.

    The truncated hash is sufficient for change detection — collisions are
    irrelevant since we only compare the same file across two snapshots.
    """
    h = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()[:12]
    except (OSError, PermissionError):
        return None


# ══════════════════════════════════════════════
# Vault inventory (what's already mirrored)
# ══════════════════════════════════════════════

# Regex to extract YAML frontmatter block from the top of a markdown file
_FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
# Regex to extract key: value pairs from frontmatter
_FM_FIELD = re.compile(r"^([\w-]+):\s*(.+)$", re.MULTILINE)


def _parse_frontmatter(text):
    """Extract frontmatter fields from markdown text as a dict."""
    m = _FM_RE.match(text)
    if not m:
        return {}
    return {k: v.strip() for k, v in _FM_FIELD.findall(m.group(1))}


def inventory_vault(mirror_root):
    """Scan vault mirror directory and return {mirror-source: {hash, vault_path}}.

    Reads frontmatter from each .md note looking for mirror-source (repo
    relative path) and mirror-hash (content hash at last sync). Only the
    first 2000 bytes are read since frontmatter is always at the top.
    """
    inventory = {}
    if not os.path.isdir(mirror_root):
        return inventory

    for dirpath, dirnames, filenames in os.walk(mirror_root):
        # Skip hidden/ignored dirs
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                    text = f.read(2000)  # frontmatter is at top
            except OSError:
                continue
            fm = _parse_frontmatter(text)
            source = fm.get("mirror-source")
            if source:
                inventory[source] = {
                    "hash": fm.get("mirror-hash", ""),
                    "vault_path": fpath,
                    "mirror_date": fm.get("mirror-date", ""),
                }
    return inventory


# ══════════════════════════════════════════════
# Repo inventory (what should be mirrored)
# ══════════════════════════════════════════════


def _should_ignore_file(filepath):
    """Check if a file should be ignored based on its extension."""
    _, ext = os.path.splitext(filepath)
    return ext.lower() in MIRROR_IGNORE_FILES


def _should_ignore_dir(dirname):
    """Check if a directory name matches the ignore list."""
    return dirname in MIRROR_IGNORE_DIRS or dirname.startswith(".")


def _scan_dir(repo_root, rel_dir, extensions=None, ignore_dirs=None):
    """Scan a repo directory and return list of relative paths matching filters.

    Walks the directory tree under rel_dir, applying extension and ignore
    filters. Returns paths relative to repo_root with forward slashes.
    """
    results = []
    abs_dir = os.path.join(repo_root, rel_dir)
    if not os.path.isdir(abs_dir):
        return results

    extra_ignore = ignore_dirs or set()

    for dirpath, dirnames, filenames in os.walk(abs_dir):
        # Filter out ignored directories before os.walk descends into them
        dirnames[:] = [
            d for d in dirnames if not _should_ignore_dir(d) and d not in extra_ignore
        ]
        for fname in filenames:
            if _should_ignore_file(fname):
                continue
            if extensions:
                _, ext = os.path.splitext(fname)
                if ext.lower() not in extensions:
                    continue
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, repo_root).replace("\\", "/")
            results.append(rel)
    return results


def _friendly_title(filename):
    """Convert a filename to a friendly note title.

    .md files drop the extension (they're embedded directly).
    Code/config files keep the full name for clarity.
    """
    name, ext = os.path.splitext(filename)
    if ext.lower() == ".md":
        return name
    return filename


def _vault_note_name(repo_rel_path, section_config):
    """Determine the vault note filename for a given repo file.

    .md sources become name.md in vault (no double extension).
    Code files become filename.ext.md to disambiguate from .md sources.
    """
    filename = os.path.basename(repo_rel_path)
    _, ext = os.path.splitext(filename)

    if ext.lower() == ".md":
        return filename  # already .md
    return f"{filename}.md"  # e.g. config.py → config.py.md


def _vault_subdir(repo_rel_path, section_key, section_config, repo_root):
    """Determine the vault subdirectory for a file based on section config.

    For sections with subdirs_as_folders=True, each first-level subdirectory
    becomes a prettified vault subfolder (e.g. content/articulos/mejor-robot/
    → Content/Mejor Robot/).
    """
    vault_dir = section_config["vault_dir"]

    if section_config.get("subdirs_as_folders"):
        parts = repo_rel_path.replace("\\", "/").split("/")
        repo_dir = section_config.get("repo_dir", "")
        repo_dir_parts = repo_dir.split("/") if repo_dir else []

        # Find the subdir name (first directory after repo_dir)
        remaining = parts[len(repo_dir_parts) :]
        if len(remaining) > 1:
            subdir_name = remaining[0]
            # Prettify: kebab-case/underscore_case → Title Case
            pretty = subdir_name.replace("-", " ").replace("_", " ").title()
            return os.path.join(vault_dir, pretty)

    return vault_dir


def inventory_repo(repo_root):
    """Scan repo and return {rel_path: {section, vault_dir, vault_note, hash}}.

    Iterates over MIRROR_SECTIONS config. Each section can specify:
    - repo_paths: explicit file list
    - repo_dir + extensions: directory scan with filter
    - repo_glob: glob pattern for scattered files
    """
    inventory = {}

    for section_key, cfg in MIRROR_SECTIONS.items():
        if cfg.get("generated"):
            continue  # Skip generated-only sections (Architecture)

        files = []

        # Explicit file list — for individual files not in a scanned directory
        if "repo_paths" in cfg:
            for rp in cfg["repo_paths"]:
                full = os.path.join(repo_root, rp)
                if os.path.isfile(full):
                    files.append(rp)

        # Directory scan — walk a directory with extension + ignore filters
        if "repo_dir" in cfg:
            extra_ignore = cfg.get("ignore_dirs", set())
            scanned = _scan_dir(
                repo_root,
                cfg["repo_dir"],
                extensions=cfg.get("extensions"),
                ignore_dirs=extra_ignore,
            )
            files.extend(scanned)

        # Glob pattern — for files scattered across the repo tree
        if "repo_glob" in cfg:
            pattern = os.path.join(repo_root, cfg["repo_glob"])
            for match in globmod.glob(pattern, recursive=True):
                rel = os.path.relpath(match, repo_root).replace("\\", "/")
                if not _should_ignore_file(rel):
                    files.append(rel)

        # Build inventory entry for each discovered file
        for rel_path in files:
            full_path = os.path.join(repo_root, rel_path)
            h = file_hash(full_path)
            vault_dir = _vault_subdir(rel_path, section_key, cfg, repo_root)
            note_name = _vault_note_name(rel_path, cfg)

            inventory[rel_path] = {
                "section": section_key,
                "vault_dir": vault_dir,
                "vault_note": note_name,
                "hash": h,
                "full_path": full_path,
            }

    return inventory


# ══════════════════════════════════════════════
# Diff engine
# ══════════════════════════════════════════════


def compute_diff(vault_inv, repo_inv):
    """Compare vault and repo inventories to produce action list.

    Returns dict with:
        create: list of repo_rel_paths (new files not yet in vault)
        update: list of repo_rel_paths (hash changed since last sync)
        delete: list of vault_paths (no longer exist in repo)
        unchanged: list of repo_rel_paths (hash matches)
    """
    create = []
    update = []
    delete = []
    unchanged = []

    # Files in repo: decide create vs update vs unchanged
    for rel_path, repo_info in repo_inv.items():
        if rel_path in vault_inv:
            if vault_inv[rel_path]["hash"] != repo_info["hash"]:
                update.append(rel_path)
            else:
                unchanged.append(rel_path)
        else:
            create.append(rel_path)

    # Files in vault but not in repo: mark for deletion
    for source, vault_info in vault_inv.items():
        if source not in repo_inv:
            delete.append(vault_info["vault_path"])

    return {
        "create": sorted(create),
        "update": sorted(update),
        "delete": sorted(delete),
        "unchanged": sorted(unchanged),
    }


# ══════════════════════════════════════════════
# Note generation
# ══════════════════════════════════════════════


def _detect_language(filepath):
    """Detect fenced code block language from file extension."""
    _, ext = os.path.splitext(filepath)
    return MIRROR_LANG_MAP.get(ext.lower(), "")


def _describe_file(rel_path, section):
    """Generate a brief description line for the file based on its section."""
    descriptions = {
        "Configuration": "Configuration file",
        "Rules": "Operational rule",
        "Commands": "Skill command definition (prompt)",
        "Memory": "Persistent memory entry",
        "Articles": f"Article — `{'/'.join(rel_path.replace(chr(92), '/').split('/')[:-1])}`",
        "Content Templates": "Beehiiv email template",
        "Content Root": "Content registry",
        "Docs": "Project documentation",
        "References": "Research / reference document",
        "Utilities": "Utility script",
        "Vault Sync": "Vault sync engine script",
        "Branding Docs": "Branding asset documentation",
        "Root Documents": "Repository root document",
    }
    return descriptions.get(section, "Repository file")


def _get_git_short_hash(repo_root):
    """Get current git short hash for metadata tagging."""
    try:
        import subprocess

        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            cwd=repo_root,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return "unknown"


def generate_note(rel_path, repo_info, repo_root, git_hash=None):
    """Generate markdown note content for a repo file.

    Markdown sources are embedded directly so Obsidian renders them natively.
    Code/config files get fenced code blocks with syntax highlighting for
    copy-paste convenience. Returns the full markdown string ready to write.
    """
    full_path = repo_info["full_path"]
    section = repo_info["section"]
    file_hash_val = repo_info["hash"]
    filename = os.path.basename(rel_path)
    title = _friendly_title(filename)
    description = _describe_file(rel_path, section)
    lang = _detect_language(rel_path)
    today = date.today().isoformat()

    # Read source file content
    try:
        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except OSError:
        content = "<!-- Error: could not read source file -->"

    _, ext = os.path.splitext(filename)
    is_markdown_source = ext.lower() == ".md"

    # ── Build frontmatter ──
    lines = [
        "---",
        "type: reference",
        "built-with: claude",
        f"mirror-source: {rel_path}",
        f"mirror-date: {today}",
        f"mirror-hash: {file_hash_val}",
    ]
    if git_hash:
        lines.append(f"mirror-commit: {git_hash}")
    lines.append("---")
    lines.append("")

    # ── Title and metadata block ──
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"**Source:** `{rel_path}`")
    lines.append(f"**Section:** {section}")
    lines.append(
        f"**Last synced:** {today}" + (f" (commit {git_hash})" if git_hash else "")
    )
    lines.append("")

    # ── Content: embedded markdown or fenced code block ──
    if is_markdown_source:
        lines.append("## Content")
        lines.append("")
        # Shift heading levels down by 2 to avoid collision with note's H1/H2
        adjusted = re.sub(r"^# ", "### ", content, flags=re.MULTILINE)
        adjusted = re.sub(r"^## ", "#### ", adjusted, flags=re.MULTILINE)
        lines.append(adjusted)
    else:
        lines.append("## Code")
        lines.append("")
        lines.append(f"```{lang}")
        lines.append(content)
        # Ensure closing fence is on its own line
        if content and not content.endswith("\n"):
            lines.append("")
        lines.append("```")

    # ── Related links for Obsidian graph navigation ──
    lines.append("")
    lines.append("## Related")
    lines.append("")
    lines.append(f"- [[{MIRROR_INDEX_NAME}]]")

    return "\n".join(lines)


# ══════════════════════════════════════════════
# Master index generation
# ══════════════════════════════════════════════


def generate_mirror_index(repo_inv, mirror_root, repo_root, stats=None):
    """Generate the master ROBOHOGAR Mirror Index.md.

    Groups files by section following SECTION_ORDER, with sub-groups by
    vault directory for sections that have subfolders. Returns the full
    markdown string ready to write.
    """
    today = date.today().isoformat()
    git_hash = _get_git_short_hash(repo_root)

    lines = [
        "---",
        "type: reference",
        "built-with: claude",
        f"mirror-date: {today}",
        "---",
        "",
        f"# {MIRROR_INDEX_NAME}",
        "",
        f"> Auto-generated by obsidian-robohogar Mode 7 (`repo-mirror`). "
        f"Last synced: {today} (commit {git_hash})",
        "",
    ]

    # ── Sync summary table ──
    if stats:
        lines.append("## Sync Summary")
        lines.append("")
        lines.append("| Metric | Count |")
        lines.append("|---|---|")
        lines.append(f"| Total notes | {stats.get('total', 0)} |")
        lines.append(f"| Created | {stats.get('created', 0)} |")
        lines.append(f"| Updated | {stats.get('updated', 0)} |")
        lines.append(f"| Deleted | {stats.get('deleted', 0)} |")
        lines.append(f"| Unchanged | {stats.get('unchanged', 0)} |")
        lines.append("")

    # ── Group files by section for organized navigation ──
    by_section = defaultdict(list)
    for rel_path, info in sorted(repo_inv.items()):
        by_section[info["section"]].append((rel_path, info))

    lines.append("## Sections")
    lines.append("")
    for section in SECTION_ORDER:
        if section not in by_section and section != "Architecture":
            continue
        lines.append(f"### {section}")
        lines.append("")

        # Architecture is generated once, not file-mapped
        if section == "Architecture":
            lines.append("- [[Architecture Overview — ROBOHOGAR]]")
            lines.append("")
            continue

        files = by_section.get(section, [])

        # Sub-group by vault_dir (for skills/articles with subfolders)
        by_dir = defaultdict(list)
        for rel_path, info in files:
            by_dir[info["vault_dir"]].append((rel_path, info))

        for vault_dir in sorted(by_dir.keys()):
            dir_files = by_dir[vault_dir]
            # Show subheader only when vault_dir differs from section base
            section_cfg = MIRROR_SECTIONS.get(section, {})
            base_dir = section_cfg.get("vault_dir", section)
            if vault_dir != base_dir:
                subdir_name = os.path.basename(vault_dir)
                lines.append(f"**{subdir_name}**")
                lines.append("")

            for rel_path, info in sorted(dir_files, key=lambda x: x[0]):
                note_name = info["vault_note"]
                # Display name without .md suffix for cleaner reading
                display = (
                    note_name.replace(".md", "")
                    if note_name.endswith(".md")
                    else note_name
                )
                lines.append(f"- [[{note_name}|{display}]] — `{rel_path}`")
            lines.append("")

    return "\n".join(lines)


# ══════════════════════════════════════════════
# Architecture Overview (generated once)
# ══════════════════════════════════════════════


def _generate_architecture_overview(repo_root, repo_inv, git_hash):
    """Generate the Architecture Overview note with repo map.

    Created only on first mirror run. Subsequent edits are manual so
    Rafael can add context without it being overwritten.
    """
    today = date.today().isoformat()

    # Count files per section for the summary table
    section_counts = defaultdict(int)
    for info in repo_inv.values():
        section_counts[info["section"]] += 1

    lines = [
        "---",
        "type: reference",
        "built-with: claude",
        f"mirror-date: {today}",
        "---",
        "",
        "# Architecture Overview — ROBOHOGAR",
        "",
        f"> Repository structure. Auto-generated {today} (commit {git_hash}).",
        "",
        "## Purpose",
        "",
        "ROBOHOGAR is Rafael's personal project: a Spanish-language newsletter and blog",
        "about domestic robotics and humanoid robots. Platform: Beehiiv (free plan).",
        "Domain: robohogar.com. Content cadence: 3-5 hrs/week.",
        "",
        "The repo contains editorial content (articles, research, brand docs),",
        "Claude Code skills for content generation and vault sync,",
        "branding assets (mascot, social cards), and the landing page.",
        "",
        "## Directory Map",
        "",
        "```",
        "robohogar/",
        "├── .claude/              # Claude Code configuration",
        "│   ├── CLAUDE.md         # Global instructions",
        "│   ├── commands/         # Skill command files",
        "│   ├── memory/           # Persistent memory",
        "│   └── rules/            # Operational rules",
        "├── .mcp.json             # MCP server config",
        "├── assets/",
        "│   ├── branding/         # Mascot images (master, flash-1K, con-fondo)",
        "│   ├── images/           # Hero, social cards, newsletter headers",
        "│   └── landing.html      # Landing page",
        "├── content/",
        "│   ├── articulos/        # Articles by slug (one folder each)",
        "│   ├── templates/        # Beehiiv email templates",
        "│   └── registro-articulos.md  # Article registry (source of truth)",
        "├── docs/                 # Brand voice, plans, implementation guide",
        "├── references/           # Market research, competition analysis",
        "│   └── newsletter/       # Email marketing playbook",
        "├── skills/",
        "│   └── vault_sync/       # Obsidian vault mirror engine",
        "├── utilities/            # Scripts + _archive/",
        "└── README.md",
        "```",
        "",
        "## Section File Counts",
        "",
        "| Section | Mirrored Files |",
        "|---|---|",
    ]

    for section in SECTION_ORDER:
        if section == "Architecture":
            continue
        count = section_counts.get(section, 0)
        if count > 0:
            lines.append(f"| {section} | {count} |")

    lines.extend(
        [
            f"| **Total** | **{sum(section_counts.values())}** |",
            "",
            "## Content Pipeline",
            "",
            "```",
            "Research (fuentes-por-categoria.md) → Research Digest → Article Draft",
            "     ↓                                    ↓                  ↓",
            "  Wiki entries                      Obsidian vault      Beehiiv publish",
            "  (Robots/Empresas)                 (editorial area)    + web article",
            "```",
            "",
            "## Key Skills",
            "",
            "- **content-draft:** Article drafting with brand voice + SEO",
            "- **research-digest:** Automated research aggregation from RSS/web",
            "- **social-content:** Social media content from published articles",
            "- **nano-banana:** Mascot image generation via Gemini",
            "- **obsidian-robohogar:** Vault sync, wiki, editorial calendar, repo mirror",
            "",
            "## Related",
            "",
            f"- [[{MIRROR_INDEX_NAME}]]",
        ]
    )

    return "\n".join(lines)


# ══════════════════════════════════════════════
# Execution engine
# ══════════════════════════════════════════════


def execute_mirror(repo_root, vault_hbx_root, full_rebuild=False, dry_run=False):
    """Run the full mirror reconciliation pipeline.

    Steps: inventory both sides → compute diff → apply changes (create/update/
    delete notes) → regenerate master index → create Architecture Overview if
    missing.

    Args:
        repo_root: absolute path to the robohogar repository.
        vault_hbx_root: absolute path to vault HBX root
            (e.g. .../Obsidian/RRP/RRP_ONEDRIVE/HBX).
        full_rebuild: if True, regenerate all notes regardless of hash match.
        dry_run: if True, only compute diff and return without writing.

    Returns:
        dict with 'stats' (counts), 'diff' (action lists), 'mirror_root' (path).
    """
    mirror_root = os.path.join(vault_hbx_root, MIRROR_VAULT_RELPATH)
    git_hash = _get_git_short_hash(repo_root)

    # Step 1: Inventory both sides
    vault_inv = inventory_vault(mirror_root)
    repo_inv = inventory_repo(repo_root)

    # Full rebuild treats every repo file as "update" — useful after config changes
    if full_rebuild:
        diff = {
            "create": [],
            "update": sorted(repo_inv.keys()),
            "delete": [],
            "unchanged": [],
        }
    else:
        diff = compute_diff(vault_inv, repo_inv)

    stats = {
        "total": len(repo_inv),
        "created": len(diff["create"]),
        "updated": len(diff["update"]),
        "deleted": len(diff["delete"]),
        "unchanged": len(diff["unchanged"]),
        "dry_run": dry_run,
    }

    if dry_run:
        return {"stats": stats, "diff": diff, "mirror_root": mirror_root}

    # Step 2: Apply changes

    # Delete notes whose source files no longer exist in the repo
    for vault_path in diff["delete"]:
        try:
            os.remove(vault_path)
            # Remove empty parent dirs up to mirror_root
            parent = os.path.dirname(vault_path)
            while parent != mirror_root:
                if os.path.isdir(parent) and not os.listdir(parent):
                    os.rmdir(parent)
                    parent = os.path.dirname(parent)
                else:
                    break
        except OSError:
            pass

    # Create and update notes — same logic for both (full note regeneration)
    for rel_path in diff["create"] + diff["update"]:
        info = repo_inv[rel_path]
        vault_dir = os.path.join(mirror_root, info["vault_dir"])
        os.makedirs(vault_dir, exist_ok=True)

        note_path = os.path.join(vault_dir, info["vault_note"])
        content = generate_note(rel_path, info, repo_root, git_hash)

        with open(note_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

    # Step 3: Generate master index (always regenerated for accurate stats)
    index_content = generate_mirror_index(repo_inv, mirror_root, repo_root, stats)
    index_path = os.path.join(mirror_root, f"{MIRROR_INDEX_NAME}.md")
    os.makedirs(mirror_root, exist_ok=True)
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(index_content)

    # Step 4: Architecture Overview — created once, never overwritten
    arch_dir = os.path.join(mirror_root, "Architecture")
    arch_path = os.path.join(arch_dir, "Architecture Overview — ROBOHOGAR.md")
    if not os.path.isfile(arch_path):
        os.makedirs(arch_dir, exist_ok=True)
        arch_content = _generate_architecture_overview(repo_root, repo_inv, git_hash)
        with open(arch_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(arch_content)

    stats["index_generated"] = True
    return {"stats": stats, "diff": diff, "mirror_root": mirror_root}


# ══════════════════════════════════════════════
# CLI — for direct execution and testing
# ══════════════════════════════════════════════


def print_report(result):
    """Print a human-readable report of mirror results."""
    stats = result["stats"]
    diff = result.get("diff", {})

    prefix = "[DRY RUN] " if stats.get("dry_run") else ""

    print(f"\n{'=' * 50}")
    print(f"{prefix}{REPO_NAME} REPO MIRROR REPORT")
    print(f"{'=' * 50}")
    print(f"Mirror root: {result.get('mirror_root', 'N/A')}")
    print(f"\nTotal repo files: {stats['total']}")
    print(f"  Created:   {stats['created']}")
    print(f"  Updated:   {stats['updated']}")
    print(f"  Deleted:   {stats['deleted']}")
    print(f"  Unchanged: {stats['unchanged']}")

    if diff.get("create"):
        print(f"\n--- NEW ({len(diff['create'])}) ---")
        for p in diff["create"][:20]:
            print(f"  + {p}")
        if len(diff["create"]) > 20:
            print(f"  ... and {len(diff['create']) - 20} more")

    if diff.get("update"):
        print(f"\n--- MODIFIED ({len(diff['update'])}) ---")
        for p in diff["update"][:20]:
            print(f"  ~ {p}")
        if len(diff["update"]) > 20:
            print(f"  ... and {len(diff['update']) - 20} more")

    if diff.get("delete"):
        print(f"\n--- REMOVED ({len(diff['delete'])}) ---")
        for p in diff["delete"][:10]:
            print(f"  - {os.path.basename(p)}")
        if len(diff["delete"]) > 10:
            print(f"  ... and {len(diff['delete']) - 10} more")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=f"Mirror {REPO_NAME} repo to Obsidian vault"
    )
    parser.add_argument("vault_path", nargs="?", help="Vault HBX root path")
    parser.add_argument("repo_path", nargs="?", help="Repository root path")
    parser.add_argument("--full", action="store_true", help="Force full rebuild")
    parser.add_argument(
        "--dry-run", action="store_true", help="Report only, no changes"
    )
    parser.add_argument("--report", action="store_true", help="Print detailed report")
    args = parser.parse_args()

    # Default vault: resolve from env var; default repo: two levels up from this script
    vault = args.vault_path or resolve_vault_path()
    repo = args.repo_path or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", ".."
    )
    repo = os.path.abspath(repo)

    result = execute_mirror(repo, vault, full_rebuild=args.full, dry_run=args.dry_run)
    print_report(result)
