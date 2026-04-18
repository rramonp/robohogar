#!/usr/bin/env python3
"""
Vault Sync Configuration — ROBOHOGAR

Defines mirror sections, paths, and conventions for syncing the robohogar
repository into the Obsidian vault as navigable Markdown notes. Follows the
same patterns as RRP-DEV's vault_organizer/config.py but tailored for the
ROBOHOGAR project structure.

This config is the single source of truth for what gets mirrored and where.
Modify MIRROR_SECTIONS to add/remove mirrored content.

Usage context: called by repo_mirror.py (Mode 7 of obsidian-robohogar skill).
"""

import os

# ══════════════════════════════════════════════
# Vault paths
# ══════════════════════════════════════════════

# Subpath from $HBX_VAULT to the HBX vault root (shared convention with RRP-DEV)
VAULT_HBX_SUBPATH = os.path.join("RRP", "RRP_ONEDRIVE", "HBX")

# Mirror destination — sits next to RRP-DEV's mirror under Repo Mirrors/
MIRROR_VAULT_RELPATH = os.path.join(
    "03_Resources", "03-01_Claude", "Repo Mirrors", "ROBOHOGAR"
)

# Editorial content area (where Rafael works in Obsidian day-to-day)
ROBOHOGAR_VAULT_RELPATH = os.path.join("05_Personal", "05-01_Robotica Newsletter")


def resolve_vault_path():
    """Resolve the HBX vault root from $HBX_VAULT env var.

    Returns the full path to the HBX vault root, e.g.:
    C:/Users/cri-c/OneDrive - HBX Group/Desktop/DEMAND/Obsidian/RRP/RRP_ONEDRIVE/HBX
    """
    base = os.environ.get(
        "HBX_VAULT",
        os.path.join(
            os.path.expanduser("~"),
            "OneDrive - HBX Group",
            "Desktop",
            "DEMAND",
            "Obsidian",
        ),
    )
    return os.path.join(
        os.path.expandvars(os.path.expanduser(base)),
        VAULT_HBX_SUBPATH,
    )


# ══════════════════════════════════════════════
# Mirror sections — what to mirror and where
# ══════════════════════════════════════════════

# Each section maps repo paths to a vault subdirectory with extension filters.
# - 'generated': True → hand-written overview, not mapped from repo files
# - 'subdirs_as_folders': True → each first-level subdir becomes a vault subfolder
# - 'repo_paths': explicit file list (for individual files outside scanned dirs)
# - 'repo_dir' + 'extensions': directory scan with extension filter
# - 'repo_glob': glob pattern for scattered files across the repo
MIRROR_SECTIONS = {
    "Architecture": {
        "vault_dir": "Architecture",
        "generated": True,  # hand-written overview, created once
    },
    "Configuration": {
        "vault_dir": "Configuration",
        "repo_paths": [
            "CLAUDE.md",
            ".mcp.json",
            ".gitignore",
        ],
    },
    "Rules": {
        "vault_dir": "Rules",
        "repo_dir": ".claude/rules",
        "extensions": {".md"},
    },
    "Commands": {
        "vault_dir": "Commands",
        "repo_dir": ".claude/commands",
        "extensions": {".md"},
    },
    "Memory": {
        "vault_dir": "Memory",
        "repo_dir": ".claude/memory",
        "extensions": {".md"},
    },
    "Articles": {
        "vault_dir": "Content",
        "repo_dir": "content/articulos",
        "extensions": {".md"},
        "subdirs_as_folders": True,  # each article slug → vault subfolder
    },
    "Content Templates": {
        "vault_dir": os.path.join("Content", "Templates"),
        "repo_dir": "content/templates",
        "extensions": {".md", ".html"},
    },
    "Content Root": {
        "vault_dir": "Content",
        "repo_paths": [
            "content/registro-articulos.md",
        ],
    },
    "Docs": {
        "vault_dir": "Docs",
        "repo_dir": "docs",
        "extensions": {".md"},
    },
    "References": {
        "vault_dir": "References",
        "repo_dir": "references",
        "extensions": {".md"},
        "subdirs_as_folders": True,  # references/newsletter/ → subfolder
    },
    "Utilities": {
        "vault_dir": "Utilities",
        "repo_dir": "utilities",
        "extensions": {".py", ".md"},
        "ignore_dirs": {"_archive", "__pycache__"},
    },
    "Vault Sync": {
        "vault_dir": "Skills",
        "repo_dir": "skills/vault_sync",
        "extensions": {".py"},
    },
    "Branding Docs": {
        "vault_dir": "Assets",
        "repo_paths": [
            "assets/branding/asset-catalog.md",
            "assets/branding/nano-banana-prompt-base.md",
        ],
    },
    "Root Documents": {
        "vault_dir": "Root Documents",
        "repo_paths": [
            "README.md",
        ],
    },
}


# ══════════════════════════════════════════════
# Ignore patterns
# ══════════════════════════════════════════════

# Directories excluded from mirror scans (binary assets, caches, temp files)
MIRROR_IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".obsidian",
    ".playwright-mcp",
    "node_modules",
    "_archive",
    "branding",  # binary images handled via explicit Branding Docs section
    "images",  # binary images — not mirrored
}

# File extensions excluded from mirror (binaries, compiled, media)
MIRROR_IGNORE_FILES = {
    ".pyc",
    ".pyo",
    ".exe",
    ".dll",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".woff2",
    ".woff",
    ".ttf",
    ".eot",
    ".zip",
    ".tar",
    ".gz",
    ".min.js",
    ".log",
    ".yml",  # playwright logs and page snapshots
}


# ══════════════════════════════════════════════
# Language map for fenced code blocks
# ══════════════════════════════════════════════

# Maps file extensions to Markdown syntax highlight identifiers
MIRROR_LANG_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".json": "json",
    ".md": "markdown",
    ".html": "html",
    ".css": "css",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".sh": "bash",
    ".bat": "batch",
    ".ps1": "powershell",
    ".toml": "toml",
}


# ══════════════════════════════════════════════
# Display constants
# ══════════════════════════════════════════════

# Index note name — the master navigation page in the vault
MIRROR_INDEX_NAME = "ROBOHOGAR Mirror Index"

# Repo display name for generated content (titles, descriptions)
REPO_NAME = "ROBOHOGAR"

# Section order for the index (controls display order in Mirror Index.md)
SECTION_ORDER = [
    "Architecture",
    "Configuration",
    "Rules",
    "Commands",
    "Memory",
    "Articles",
    "Content Templates",
    "Content Root",
    "Docs",
    "References",
    "Utilities",
    "Vault Sync",
    "Branding Docs",
    "Root Documents",
]
