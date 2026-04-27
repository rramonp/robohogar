#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai",
#     "pillow",
# ]
# ///
"""
Nano Banana — Image generation via Google Gemini API.

Generates themed wallpapers, branding assets, and artwork using Gemini's image
models (Flash, Pro, and 2). Supports multiple aspect ratios, resolution tiers,
and style-transfer from reference images.

Key capabilities:
  - Three model tiers: flash (fast/1024px), pro (up to 4K), 2 (fast + up to 4K)
  - 14 aspect ratios from 1:1 to 21:9 (model-dependent availability)
  - Reference image input for style/composition transfer (single or multi-image)
  - Automatic sign-content guard for urban/cyberpunk scenes (prevents blank signs)

Dependencies:
  - google-genai: Official Google Generative AI SDK
  - Pillow: Image I/O for reference loading and output saving
  - GEMINI_API_KEY environment variable (configured in .claude/settings.local.json)

Usage:
    uv run image.py --prompt "A colorful abstract pattern" --output "./hero.png"
    uv run image.py --prompt "Minimalist icon" --output "./icon.png" --aspect landscape
    uv run image.py --prompt "Similar style image" --output "./new.png" --reference "./existing.png"
    uv run image.py --prompt "Blend these styles" --output "./new.png" --reference "./a.png" --reference "./b.png"
    uv run image.py --prompt "High quality art" --output "./art.png" --model pro --size 2K
    uv run image.py --prompt "Fast high-res" --output "./fast.png" --model 2 --size 2K --aspect 4:3
"""

import argparse
import os
import sys

from google import genai
from google.genai import types
from PIL import Image

# ═══════════════════════════════════════════════════════════════════════════════
# Model & Aspect Ratio Configuration
# ═══════════════════════════════════════════════════════════════════════════════

# Each model maps to a Gemini model ID with different speed/quality tradeoffs
MODEL_IDS = {
    "flash": "gemini-2.5-flash-image",
    "pro": "gemini-3-pro-image-preview",
    "2": "gemini-3.1-flash-image-preview",
}

ASPECT_ALIASES = {
    "square": "1:1",
    "landscape": "16:9",
    "portrait": "9:16",
}

ALL_ASPECT_RATIOS = [
    "1:1", "1:4", "1:8", "2:3", "3:2", "3:4", "4:1",
    "4:3", "4:5", "5:4", "8:1", "9:16", "16:9", "21:9",
]

MODEL_ASPECT_RATIOS = {
    "flash": ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
    "pro": ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
    "2": ALL_ASPECT_RATIOS,
}


def resolve_aspect(aspect: str) -> str:
    """Resolve a named alias or direct ratio string to a ratio string."""
    return ASPECT_ALIASES.get(aspect, aspect)


def get_aspect_instruction(aspect_ratio: str) -> str:
    """Return aspect ratio instruction for the prompt."""
    descriptions = {
        "1:1": "Generate a square image (1:1 aspect ratio).",
        "1:4": "Generate a tall narrow image (1:4 aspect ratio).",
        "1:8": "Generate a very tall narrow image (1:8 aspect ratio).",
        "2:3": "Generate a tall image (2:3 aspect ratio).",
        "3:2": "Generate a wide image (3:2 aspect ratio).",
        "3:4": "Generate a tall image (3:4 aspect ratio).",
        "4:1": "Generate a wide panoramic image (4:1 aspect ratio).",
        "4:3": "Generate a landscape image (4:3 aspect ratio).",
        "4:5": "Generate a slightly tall image (4:5 aspect ratio).",
        "5:4": "Generate a slightly wide image (5:4 aspect ratio).",
        "8:1": "Generate a very wide panoramic image (8:1 aspect ratio).",
        "9:16": "Generate a portrait/tall image (9:16 aspect ratio).",
        "16:9": "Generate a landscape/wide image (16:9 aspect ratio).",
        "21:9": "Generate an ultrawide image (21:9 aspect ratio).",
    }
    return descriptions.get(aspect_ratio, f"Generate an image with {aspect_ratio} aspect ratio.")


# ═══════════════════════════════════════════════════════════════════════════════
# Sign Guard — Prevents Blank Signs in Urban Scenes
# ═══════════════════════════════════════════════════════════════════════════════

# Gemini tends to generate empty/dark signs in cyberpunk and urban scenes.
# When any of these keywords appear in the prompt, a directive is auto-appended
# instructing the model to fill every visible sign with glowing content.
SIGN_KEYWORDS = [
    "city", "cyberpunk", "neon", "street", "market", "alley", "metro",
    "sign", "billboard", "storefront", "intersection", "building",
    "ciudad", "calle", "mercado", "cartel", "letrero",
]

NO_EMPTY_SIGNS_SUFFIX = (
    " CRITICAL: Every sign, billboard, neon display, or storefront panel visible in the scene "
    "MUST contain visible glowing content — text, kanji glyphs, equalizer bars, pictograms, or "
    "geometric symbols. NO sign may be blank, empty, or dark. Fill each sign with different "
    "content in varied neon colors (teal, hot pink, purple, amber)."
)


def _needs_sign_guard(prompt: str) -> bool:
    """Detect if the prompt describes an urban scene that would have signs.

    Strips the common 'NO text/signs/writing' boilerplate before checking,
    so that the safety suffix doesn't false-positive on keywords like 'sign'.
    """
    # Remove the boilerplate safety suffix before checking keywords
    lower = prompt.lower()
    lower = lower.replace("no signs", "").replace("no sign", "")
    lower = lower.replace("no writing", "").replace("no text", "")
    lower = lower.replace("no letters", "").replace("no words", "")
    return any(kw in lower for kw in SIGN_KEYWORDS)


# ═══════════════════════════════════════════════════════════════════════════════
# WebP Compression — Auto-generates a web-optimized copy after each generation
# ═══════════════════════════════════════════════════════════════════════════════

# OG images and web previews should be <500 KB for fast loading on WhatsApp,
# social cards, and Core Web Vitals (LCP). Pillow's WebP encoder with quality 80
# typically compresses a 1-2 MB PNG down to 150-300 KB without visible loss.
MAX_WEB_KB = 500
WEBP_QUALITY_START = 82


def _compress_webp(png_path: str, webp_path: str) -> None:
    """Save a WebP copy from the PNG file, targeting <500 KB.

    Reopens the saved PNG with Pillow (Gemini's image object doesn't support
    WebP kwargs). Starts at quality 82 and steps down if needed.
    """
    # Reopen with pure Pillow to get full save() support
    pil_image = Image.open(png_path)
    quality = WEBP_QUALITY_START
    for attempt in range(2):
        pil_image.save(webp_path, "WEBP", quality=quality, method=4)
        webp_size = os.path.getsize(webp_path)
        if webp_size <= MAX_WEB_KB * 1024:
            break
        quality -= 10

    webp_kb = webp_size / 1024
    print(f"WebP copy saved to: {webp_path} ({webp_kb:.0f} KB, quality={quality})")


def generate_image(
    prompt: str,
    output_path: str,
    aspect: str = "square",
    references: list[str] | None = None,
    model: str = "2",
    size: str = "1K",
) -> None:
    """Generate an image using Gemini and save to output_path."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    aspect_ratio = resolve_aspect(aspect)

    valid_ratios = MODEL_ASPECT_RATIOS[model]
    if aspect_ratio not in valid_ratios:
        print(f"Error: Aspect ratio '{aspect_ratio}' not supported for model '{model}'. Valid ratios: {', '.join(valid_ratios)}", file=sys.stderr)
        sys.exit(1)

    # Auto-inject sign guard for urban scenes
    if _needs_sign_guard(prompt) and "no empty" not in prompt.lower() and "no blank" not in prompt.lower():
        prompt = prompt + NO_EMPTY_SIGNS_SUFFIX
        print("Sign guard: auto-injected NO EMPTY SIGNS directive")

    aspect_instruction = get_aspect_instruction(aspect_ratio)
    full_prompt = f"{aspect_instruction} {prompt}"

    contents: list = []
    if references:
        for ref_path in references:
            if not os.path.exists(ref_path):
                print(f"Error: Reference image not found: {ref_path}", file=sys.stderr)
                sys.exit(1)
            contents.append(Image.open(ref_path))
        if len(references) == 1:
            full_prompt = f"{full_prompt} Use the provided image as a reference for style, composition, or content."
        else:
            full_prompt = f"{full_prompt} Use the provided {len(references)} images as references for style, composition, or content."
    contents.append(full_prompt)

    model_id = MODEL_IDS[model]

    if model in ("pro", "2"):
        valid_sizes = ["512", "1K", "2K", "4K"] if model == "2" else ["1K", "2K", "4K"]
        if size not in valid_sizes:
            print(f"Error: Size '{size}' not supported for model '{model}'. Valid sizes: {', '.join(valid_sizes)}", file=sys.stderr)
            sys.exit(1)
        config = types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=size,
            ),
        )
        response = client.models.generate_content(
            model=model_id,
            contents=contents,
            config=config,
        )
    else:
        response = client.models.generate_content(
            model=model_id,
            contents=contents,
        )

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    for part in response.parts:
        if part.text is not None:
            print(f"Model response: {part.text}")
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output_path)
            png_size = os.path.getsize(output_path)
            print(f"Image saved to: {output_path} ({png_size / 1024:.0f} KB)")

            # Auto-generate compressed WebP copy for OG/web use (<500 KB target)
            webp_path = os.path.splitext(output_path)[0] + ".webp"
            _compress_webp(output_path, webp_path)
            return

    print("Error: No image data in response", file=sys.stderr)
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════════════
# CLI Entry Point
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Parse CLI arguments and invoke image generation.

    Supports --prompt, --output, --aspect, --reference (repeatable),
    --model (flash/pro/2), and --size (512/1K/2K/4K). Designed for
    invocation via `uv run image.py` with inline script dependencies.
    """
    parser = argparse.ArgumentParser(
        description="Generate images using Nano Banana (Gemini Flash, Pro, or 2)"
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Description of the image to generate",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path (PNG format)",
    )
    parser.add_argument(
        "--aspect",
        choices=list(ASPECT_ALIASES.keys()) + ALL_ASPECT_RATIOS,
        default="square",
        help="Aspect ratio: named shortcut (square, landscape, portrait) or direct ratio (e.g. 4:3, 21:9). Default: square",
    )
    parser.add_argument(
        "--reference",
        action="append",
        dest="references",
        help="Path to a reference image (can be specified multiple times)",
    )
    parser.add_argument(
        "--model",
        choices=["flash", "pro", "2"],
        default="2",
        help="Model: flash (fast, 1024px), pro (up to 4K), 2 (fast + up to 4K, default)",
    )
    parser.add_argument(
        "--size",
        choices=["512", "1K", "2K", "4K"],
        default="1K",
        help="Image resolution for pro/2 models: 512 (model 2 only), 1K (default), 2K, 4K.",
    )

    args = parser.parse_args()
    generate_image(args.prompt, args.output, args.aspect, args.references, args.model, args.size)


if __name__ == "__main__":
    main()
