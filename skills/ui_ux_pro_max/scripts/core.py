#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Pro Max Core — BM25 search engine for UI/UX style guides.

Provides a lightweight, dependency-free information retrieval system over
15+ CSV knowledge bases covering styles, colors, charts, typography, icons,
UX guidelines, landing page patterns, and framework-specific best practices.

The engine uses Okapi BM25 (Best Matching 25) for ranking, combined with
keyword-based domain auto-detection so callers can simply pass a natural
language query without specifying which database to search.

Architecture:
    CSV_CONFIG  — registry mapping domain names → CSV files + column sets
    BM25        — stateless ranker: fit(documents) then score(query)
    detect_domain() — regex keyword scan to route queries automatically
    search()    — public entry point: detect domain → load CSV → rank → return top N

Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (MIT)
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION — CSV registry and search defaults
# Each domain entry maps to a CSV file in data/ with explicit search and output
# column lists. Search columns feed the BM25 index; output columns control what
# gets returned to the caller (keeping responses focused).
# ═══════════════════════════════════════════════════════════════════════════════
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3  # Default top-N results per query

# Domain → CSV mapping. Keys are domain slugs used by detect_domain() and search().
CSV_CONFIG = {
    # Visual design styles: glassmorphism, brutalism, neumorphism, etc.
    "style": {
        "file": "styles.csv",
        "search_cols": [
            "Style Category",
            "Keywords",
            "Best For",
            "Type",
            "AI Prompt Keywords",
        ],
        "output_cols": [
            "Style Category",
            "Type",
            "Keywords",
            "Primary Colors",
            "Effects & Animation",
            "Best For",
            "Performance",
            "Accessibility",
            "Framework Compatibility",
            "Complexity",
            "AI Prompt Keywords",
            "CSS/Technical Keywords",
            "Implementation Checklist",
            "Design System Variables",
        ],
    },
    # Color palettes: product-type-specific token sets (primary, accent, destructive, etc.)
    "color": {
        "file": "colors.csv",
        "search_cols": ["Product Type", "Notes"],
        "output_cols": [
            "Product Type",
            "Primary",
            "On Primary",
            "Secondary",
            "On Secondary",
            "Accent",
            "On Accent",
            "Background",
            "Foreground",
            "Card",
            "Card Foreground",
            "Muted",
            "Muted Foreground",
            "Border",
            "Destructive",
            "On Destructive",
            "Ring",
            "Notes",
        ],
    },
    # Chart selection guide: maps data types to recommended chart types with a11y grades
    "chart": {
        "file": "charts.csv",
        "search_cols": [
            "Data Type",
            "Keywords",
            "Best Chart Type",
            "When to Use",
            "When NOT to Use",
            "Accessibility Notes",
        ],
        "output_cols": [
            "Data Type",
            "Keywords",
            "Best Chart Type",
            "Secondary Options",
            "When to Use",
            "When NOT to Use",
            "Data Volume Threshold",
            "Color Guidance",
            "Accessibility Grade",
            "Accessibility Notes",
            "A11y Fallback",
            "Library Recommendation",
            "Interactive Level",
        ],
    },
    # Landing page patterns: section order, CTA placement, conversion optimization
    "landing": {
        "file": "landing.csv",
        "search_cols": [
            "Pattern Name",
            "Keywords",
            "Conversion Optimization",
            "Section Order",
        ],
        "output_cols": [
            "Pattern Name",
            "Keywords",
            "Section Order",
            "Primary CTA Placement",
            "Color Strategy",
            "Conversion Optimization",
        ],
    },
    # Product-type recommendations: SaaS, ecommerce, fintech, etc. with style + palette
    "product": {
        "file": "products.csv",
        "search_cols": [
            "Product Type",
            "Keywords",
            "Primary Style Recommendation",
            "Key Considerations",
        ],
        "output_cols": [
            "Product Type",
            "Keywords",
            "Primary Style Recommendation",
            "Secondary Styles",
            "Landing Page Pattern",
            "Dashboard Style (if applicable)",
            "Color Palette Focus",
        ],
    },
    # UX guidelines: usability do/don't patterns with severity and code examples
    "ux": {
        "file": "ux-guidelines.csv",
        "search_cols": ["Category", "Issue", "Description", "Platform"],
        "output_cols": [
            "Category",
            "Issue",
            "Platform",
            "Description",
            "Do",
            "Don't",
            "Code Example Good",
            "Code Example Bad",
            "Severity",
        ],
    },
    # Typography pairings: heading + body font combos with mood keywords and CSS imports
    "typography": {
        "file": "typography.csv",
        "search_cols": [
            "Font Pairing Name",
            "Category",
            "Mood/Style Keywords",
            "Best For",
            "Heading Font",
            "Body Font",
        ],
        "output_cols": [
            "Font Pairing Name",
            "Category",
            "Heading Font",
            "Body Font",
            "Mood/Style Keywords",
            "Best For",
            "Google Fonts URL",
            "CSS Import",
            "Tailwind Config",
            "Notes",
        ],
    },
    # Icon library reference: Lucide, Heroicons, etc. with import code and usage
    "icons": {
        "file": "icons.csv",
        "search_cols": ["Category", "Icon Name", "Keywords", "Best For"],
        "output_cols": [
            "Category",
            "Icon Name",
            "Keywords",
            "Library",
            "Import Code",
            "Usage",
            "Best For",
            "Style",
        ],
    },
    # React performance: memo, suspense, bundle splitting, server components
    "react": {
        "file": "react-performance.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description"],
        "output_cols": [
            "Category",
            "Issue",
            "Platform",
            "Description",
            "Do",
            "Don't",
            "Code Example Good",
            "Code Example Bad",
            "Severity",
        ],
    },
    # Web interface patterns: ARIA, focus management, forms, semantic HTML
    "web": {
        "file": "app-interface.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description"],
        "output_cols": [
            "Category",
            "Issue",
            "Platform",
            "Description",
            "Do",
            "Don't",
            "Code Example Good",
            "Code Example Bad",
            "Severity",
        ],
    },
    # Google Fonts catalog: family, stroke, classifications, variable axes, popularity
    "google-fonts": {
        "file": "google-fonts.csv",
        "search_cols": [
            "Family",
            "Category",
            "Stroke",
            "Classifications",
            "Keywords",
            "Subsets",
            "Designers",
        ],
        "output_cols": [
            "Family",
            "Category",
            "Stroke",
            "Classifications",
            "Styles",
            "Variable Axes",
            "Subsets",
            "Designers",
            "Popularity Rank",
            "Google Fonts URL",
        ],
    },
    # HBX-specific dashboard components: pulse cards, KPI chips, toggle pills
    "hbx-dashboard": {
        "file": "hbx-dashboard.csv",
        "search_cols": ["Component", "Keywords", "Spec", "Notes"],
        "output_cols": [
            "Component",
            "Keywords",
            "Spec",
            "CSS Variables",
            "Responsive",
            "Notes",
        ],
    },
}

# Stack-specific guideline databases (extensible — add new stacks here)
STACK_CONFIG = {
    "react-native": {"file": "stacks/react-native.csv"},
}

# Common columns for all stacks
_STACK_COLS = {
    "search_cols": ["Category", "Guideline", "Description", "Do", "Don't"],
    "output_cols": [
        "Category",
        "Guideline",
        "Description",
        "Do",
        "Don't",
        "Code Good",
        "Code Bad",
        "Severity",
        "Docs URL",
    ],
}

# Exposed for validation in search_stack() and external callers
AVAILABLE_STACKS = list(STACK_CONFIG.keys())


# ═══════════════════════════════════════════════════════════════════════════════
# BM25 IMPLEMENTATION — Okapi Best Matching 25
# A probabilistic ranking function used by search engines. It scores documents
# based on term frequency (TF), inverse document frequency (IDF), and document
# length normalization. k1 controls TF saturation, b controls length penalty.
# ═══════════════════════════════════════════════════════════════════════════════
class BM25:
    """BM25 ranking algorithm for text search over tokenized CSV rows."""

    def __init__(self, k1=1.5, b=0.75):
        """Initialize BM25 with tuning parameters.

        Args:
            k1: Term frequency saturation parameter (1.2-2.0 typical).
                Higher values give more weight to repeated terms.
            b: Length normalization factor (0-1). At 1.0, long documents are
               penalized proportionally; at 0.0, length is ignored.
        """
        self.k1 = k1          # TF saturation — how quickly repeated terms diminish
        self.b = b             # Length normalization — 0.75 is the classic default
        self.corpus = []       # Tokenized documents (list of word lists)
        self.doc_lengths = []  # Token count per document
        self.avgdl = 0         # Average document length across corpus
        self.idf = {}          # Precomputed IDF scores per term
        self.doc_freqs = defaultdict(int)  # How many docs contain each term
        self.N = 0             # Total document count

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r"[^\w\s]", " ", str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from a list of raw text documents.

        Tokenizes each document, computes document frequencies, and
        pre-calculates IDF values for all terms in the corpus.
        """
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        # Count document frequency: how many documents contain each unique term
        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        # IDF with smoothing (+1 inside log prevents negative values for common terms)
        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query):
        """Score all documents against a query string.

        Returns list of (doc_index, score) tuples sorted by descending score.
        Documents with no matching terms get score 0.
        """
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            # Build term frequency map for this document
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            # Accumulate BM25 score across all query terms
            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    # BM25 formula: IDF * (tf * (k1+1)) / (tf + k1 * (1 - b + b * dl/avgdl))
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (
                        1 - self.b + self.b * doc_len / self.avgdl
                    )
                    score += idf * numerator / denominator

            scores.append((idx, score))

        # Highest relevance first
        return sorted(scores, key=lambda x: x[1], reverse=True)


# ═══════════════════════════════════════════════════════════════════════════════
# SEARCH FUNCTIONS — CSV loading, BM25 ranking, domain detection, public API
# ═══════════════════════════════════════════════════════════════════════════════
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search: load CSV, build BM25 index from search columns, return top matches.

    Each CSV row becomes one "document" by concatenating its search_cols values.
    The BM25 ranker scores every row, then we return only the top N with score > 0,
    projecting down to the output_cols subset for a focused response.
    """
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Concatenate search columns into a single searchable text per row
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # Fit and score in one pass (stateless — new BM25 instance per search)
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Filter zero-score rows and project to output columns only
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant CSV domain from a natural language query.

    Scans the query for keyword matches against each domain's trigger words
    using word-boundary regex. The domain with the most hits wins. Falls back
    to "style" when no keywords match (broadest general-purpose database).
    """
    query_lower = query.lower()

    # Each domain has a curated keyword list — matched with word boundaries
    domain_keywords = {
        "color": [
            "color",
            "palette",
            "hex",
            "#",
            "rgb",
            "token",
            "semantic",
            "accent",
            "destructive",
            "muted",
            "foreground",
        ],
        "chart": [
            "chart",
            "graph",
            "visualization",
            "trend",
            "bar",
            "pie",
            "scatter",
            "heatmap",
            "funnel",
        ],
        "landing": [
            "landing",
            "page",
            "cta",
            "conversion",
            "hero",
            "testimonial",
            "pricing",
            "section",
        ],
        "product": [
            "saas",
            "ecommerce",
            "e-commerce",
            "fintech",
            "healthcare",
            "gaming",
            "portfolio",
            "crypto",
            "dashboard",
            "fitness",
            "restaurant",
            "hotel",
            "travel",
            "music",
            "education",
            "learning",
            "legal",
            "insurance",
            "medical",
            "beauty",
            "pharmacy",
            "dental",
            "pet",
            "dating",
            "wedding",
            "recipe",
            "delivery",
            "ride",
            "booking",
            "calendar",
            "timer",
            "tracker",
            "diary",
            "note",
            "chat",
            "messenger",
            "crm",
            "invoice",
            "parking",
            "transit",
            "vpn",
            "alarm",
            "weather",
            "sleep",
            "meditation",
            "fasting",
            "habit",
            "grocery",
            "meme",
            "wardrobe",
            "plant care",
            "reading",
            "flashcard",
            "puzzle",
            "trivia",
            "arcade",
            "photography",
            "streaming",
            "podcast",
            "newsletter",
            "marketplace",
            "freelancer",
            "coworking",
            "airline",
            "museum",
            "theater",
            "church",
            "non-profit",
            "charity",
            "kindergarten",
            "daycare",
            "senior care",
            "veterinary",
            "florist",
            "bakery",
            "brewery",
            "construction",
            "automotive",
            "real estate",
            "logistics",
            "agriculture",
            "coding bootcamp",
        ],
        "style": [
            "style",
            "design",
            "ui",
            "minimalism",
            "glassmorphism",
            "neumorphism",
            "brutalism",
            "dark mode",
            "flat",
            "aurora",
            "prompt",
            "css",
            "implementation",
            "variable",
            "checklist",
            "tailwind",
        ],
        "ux": [
            "ux",
            "usability",
            "accessibility",
            "wcag",
            "touch",
            "scroll",
            "animation",
            "keyboard",
            "navigation",
            "mobile",
        ],
        "typography": [
            "font pairing",
            "typography pairing",
            "heading font",
            "body font",
        ],
        "google-fonts": [
            "google font",
            "font family",
            "font weight",
            "font style",
            "variable font",
            "noto",
            "font for",
            "find font",
            "font subset",
            "font language",
            "monospace font",
            "serif font",
            "sans serif font",
            "display font",
            "handwriting font",
            "font",
            "typography",
            "serif",
            "sans",
        ],
        "icons": [
            "icon",
            "icons",
            "lucide",
            "heroicons",
            "symbol",
            "glyph",
            "pictogram",
            "svg icon",
        ],
        "react": [
            "react",
            "next.js",
            "nextjs",
            "suspense",
            "memo",
            "usecallback",
            "useeffect",
            "rerender",
            "bundle",
            "waterfall",
            "barrel",
            "dynamic import",
            "rsc",
            "server component",
        ],
        "web": [
            "aria",
            "focus",
            "outline",
            "semantic",
            "virtualize",
            "autocomplete",
            "form",
            "input type",
            "preconnect",
        ],
        "hbx-dashboard": [
            "hbx",
            "hotelbeds",
            "demand",
            "daily review",
            "pulse card",
            "contact ratio",
            "flag badge",
            "kpi chip",
            "toggle pill",
            "navy",
            "sky blue",
            "magenta",
            "space grotesk",
            "dm sans",
            "jetbrains mono",
        ],
    }

    # Score each domain by counting how many of its keywords appear in the query
    scores = {
        domain: sum(
            1
            for kw in keywords
            if re.search(r"\b" + re.escape(kw) + r"\b", query_lower)
        )
        for domain, keywords in domain_keywords.items()
    }
    best = max(scores, key=scores.get)
    # Default to "style" (broadest database) when no keywords match at all
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Public entry point: auto-detect domain (or use explicit), search, return results.

    Returns a dict with domain, query, source file, count, and result list.
    On file-not-found, returns an error dict instead of raising.
    """
    # Auto-detect domain from query keywords when caller does not specify
    if domain is None:
        domain = detect_domain(query)

    # Fall back to "style" config for unknown domains
    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(
        filepath, config["search_cols"], config["output_cols"], query, max_results
    )

    # Structured response with metadata for the caller
    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results,
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search framework-specific guideline databases (e.g., React Native).

    Separate from the main search() because stacks share a common column schema
    (_STACK_COLS) and live in the stacks/ subdirectory.
    """
    if stack not in STACK_CONFIG:
        return {
            "error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"
        }

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"Stack file not found: {filepath}", "stack": stack}

    results = _search_csv(
        filepath,
        _STACK_COLS["search_cols"],
        _STACK_COLS["output_cols"],
        query,
        max_results,
    )

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results,
    }
