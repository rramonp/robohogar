#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
# BRAND-DECK-generate.sh — Generador de assets ROBOHOGAR
# Ejecuta nano-banana por lotes para generar todos los assets del brand deck
# Idempotente: verifica existencia antes de generar
# Uso: bash BRAND-DECK-generate.sh {logos|social|youtube|patterns|icons|email|cta|mascota|slides|all}
# ═══════════════════════════════════════════════════════════════════

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
SECTION="${1:-all}"
GENERATED=0
SKIPPED=0
FAILED=0

# --- Colores para stdout ---
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_ok()      { echo -e "${GREEN}[OK]${NC} $1"; }
log_skip()    { echo -e "${YELLOW}[SKIP]${NC} $1 — ya existe"; }
log_fail()    { echo -e "${RED}[FAIL]${NC} $1"; }
log_section() { echo -e "\n${YELLOW}═══ $1 ═══${NC}"; }

# --- Verificación de entorno ---
if [ -z "${GEMINI_API_KEY:-}" ]; then
    echo -e "${RED}ERROR: GEMINI_API_KEY no está configurada${NC}"
    echo "Configúrala con: export GEMINI_API_KEY='tu-clave-aquí'"
    exit 1
fi

# --- Crear directorios ---
mkdir -p "$REPO_ROOT/assets/branding/master"
mkdir -p "$REPO_ROOT/assets/branding/slides"
mkdir -p "$REPO_ROOT/assets/images"

# --- Función de generación ---
# $1 = output path (relativo a repo), $2 = prompt, $3 = reference (opcional),
# $4 = aspect (default 1:1), $5 = model (default flash)
generate() {
    local output_path="$1"
    local prompt="$2"
    local reference="${3:-}"
    local aspect="${4:-1:1}"
    local model="${5:-flash}"
    local full_path="$REPO_ROOT/$output_path"

    if [ -f "$full_path" ]; then
        log_skip "$output_path"
        SKIPPED=$((SKIPPED + 1))
        return 0
    fi

    echo "  Generando: $output_path (model=$model, aspect=$aspect)..."

    local ref_arg=""
    if [ -n "$reference" ]; then
        ref_arg="--reference $REPO_ROOT/$reference"
    fi

    # Invoca claude CLI con nano-banana
    if claude -p "Usa /nano-banana para generar esta imagen. Prompt: $prompt $ref_arg --aspect $aspect --model $model. Guarda el resultado en $full_path" 2>/dev/null; then
        if [ -f "$full_path" ]; then
            log_ok "$output_path"
            GENERATED=$((GENERATED + 1))
        else
            log_fail "$output_path — archivo no creado"
            FAILED=$((FAILED + 1))
        fi
    else
        log_fail "$output_path"
        FAILED=$((FAILED + 1))
    fi
}

# ═══ LOGOS (4) ═══
run_logos() {
    log_section "LOGOS (4 assets)"

    generate "assets/branding/master/robohogar-logo-lockup-horizontal.png" \
        "Clean horizontal logo lockup on transparent background. Left: a small friendly robot icon with amber LED eyes and blue checkered apron (matching reference image). Right: ROBOHOGAR text in clean sans-serif font, weight 400. Colors: robot in white/gray/amber/cyan, text in #0C0C0C. Minimal, editorial style. High resolution, sharp edges." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "4:1" "flash"

    generate "assets/branding/master/robohogar-logo-badge.png" \
        "Circular badge logo on transparent background. A small friendly robot with spherical white head, amber LED eyes, blue checkered apron with cyan heart, inside a perfect circle with #F5A623 amber border (4px weight). Background inside circle: white #FFFFFF. Clean vector style, works at 32px favicon size. No text." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1:1" "2"

    generate "assets/branding/master/robohogar-logo-monogram.png" \
        "Minimalist monogram letter R on transparent background. The letter incorporates subtle robotic elements: two small amber LED dots as eyes near the top of the R, a tiny antenna with orange ball on top. Letter color: #0C0C0C. Clean sans-serif font style similar to Jost. No other decorations. Works at 24px size." \
        "" "1:1" "2"

    generate "assets/branding/master/robohogar-logo-header-dark.png" \
        "Clean horizontal logo lockup on transparent background, designed for dark backgrounds. Left: small friendly robot icon with bright amber LED eyes (#F5A623) and blue checkered apron, body in light gray/white. Right: ROBOHOGAR text in #FFFFFF white, clean sans-serif font weight 400. Minimal editorial style." \
        "assets/branding/master/robohogar-logo-header-v3-bahnschrift.png" "4:1" "flash"
}

# ═══ SOCIAL (5) ═══
run_social() {
    log_section "SOCIAL CARD TEMPLATES (5 assets)"

    generate "assets/images/social-template-ig-square.png" \
        "Clean editorial social media card template, square format 1080x1080. White background #FFFFFF. Top: small robot mascot icon in top-left corner with ROBOHOGAR text next to it in dark sans-serif. Center: large empty rectangular area (placeholder for product image) with subtle #F2F2F2 gray background. Bottom: wide amber #F5A623 banner strip (80px height) for headline text area. Overall: magazine-style, generous white space, no clutter. Minimalist, modern." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1:1" "flash"

    generate "assets/images/social-template-ig-story.png" \
        "Clean editorial social media story template, vertical 9:16 format. White background #FFFFFF. Top section: small robot mascot icon centered with ROBOHOGAR below it. Middle: large empty area with subtle dotted pattern background in #F2F2F2 (placeholder for product/hero image). Bottom third: solid amber #F5A623 section with space for headline and CTA. Clean, magazine-style, generous spacing." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "9:16" "flash"

    generate "assets/images/social-template-linkedin.png" \
        "Professional editorial social media card template, landscape 1200x628. White background #FFFFFF. Left third: vertical amber #F5A623 accent strip (40px wide). Small robot mascot icon in bottom-left corner. Center-right: large clean area for product image with subtle #F2F2F2 background. Top-right corner: ROBOHOGAR text in #0C0C0C small sans-serif. Bottom: thin dark #0C0C0C strip (60px) for headline area. Magazine editorial style." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1200:628" "flash"

    generate "assets/images/social-template-x.png" \
        "Clean social media card template, 16:9 landscape format. Minimal white #FFFFFF background. Top-left: tiny robot mascot icon. Top-right: ROBOHOGAR in small #6B7280 gray text. Center: dominant empty area for hero image with rounded corners and subtle shadow. Bottom: amber #F5A623 gradient fade strip (thin, 40px) at very bottom edge. Ultra-clean, modern, editorial." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "16:9" "flash"

    generate "assets/images/social-template-whatsapp.png" \
        "Clean OG share card template, 1200x630 pixels landscape. White #FFFFFF background. Left side: friendly robot mascot (full body, small, ~200px) standing and waving. Right side: large clean area for title text on white background, with thin amber #F5A623 underline decoration. Bottom-right corner: robohogar.com in small #6B7280 gray text. Minimal, friendly, not corporate." \
        "assets/branding/master/robohogar-mascot-saludando.png" "1200:630" "flash"
}

# ═══ YOUTUBE (7) ═══
run_youtube() {
    log_section "YOUTUBE BRAND PACK (7 assets)"

    generate "assets/branding/master/youtube-banner.png" \
        "YouTube channel banner 2560x1440 for a home robotics channel called ROBOHOGAR. Clean editorial design. Center safe area (1546x423): ROBOHOGAR in large clean sans-serif white text, subtitle below Robots que YA llegan a tu hogar in smaller text. Small robot mascot with amber LED eyes and blue apron standing to the right of text. Background: dark gradient from #0C0C0C to #1a1a2e with subtle hexagonal pattern overlay. Amber #F5A623 thin line accent under the title. Professional, magazine-style, not gaming/clickbait aesthetic." \
        "assets/branding/master/robohogar-mascot-principal.png" "2560:1440" "2"

    generate "assets/images/youtube-thumb-review.png" \
        "YouTube thumbnail template 1280x720 for product review video. Clean white background. Left 60%: large empty area for product photo (placeholder, subtle #F2F2F2 background). Right 40%: bold verdict area with amber #F5A623 background, space for large rating number and short verdict text. Top-left corner: small ROBOHOGAR text in #0C0C0C. Bottom-right: tiny robot mascot giving thumbs up. MKBHD-inspired clean grid style, not clickbait." \
        "assets/branding/master/robohogar-mascot-thumbsup.png" "16:9" "flash"

    generate "assets/images/youtube-thumb-vs.png" \
        "YouTube thumbnail template 1280x720 for product comparison video. Clean split design: left half and right half separated by a thin amber #F5A623 vertical line with VS text in the center. Each half: clean #F2F2F2 light gray background area for product images. Top center: ROBOHOGAR in small dark text. Bottom: thin #0C0C0C dark strip for subtitle area. Magazine editorial style, not gaming clickbait. Minimal, professional." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "16:9" "flash"

    generate "assets/images/youtube-thumb-editorial.png" \
        "YouTube thumbnail template 1280x720 for editorial/opinion video. Dark background #0C0C0C with subtle circuit pattern overlay. Center: large empty area for dramatic product or concept image. Bottom-left: robot mascot in thinking pose (hand on chin). Top-right: ROBOHOGAR in amber #F5A623 text. Dramatic lighting feel, cinematic, editorial." \
        "assets/branding/master/robohogar-mascot-pensativo.png" "16:9" "flash"

    generate "assets/branding/master/youtube-endcard.png" \
        "YouTube end screen template 1920x1080. Dark background #1a1a2e with subtle dot pattern. Left side: robot mascot waving goodbye, friendly pose. Center: two rounded rectangles (300x170 each, outlined in amber #F5A623) as placeholders for recommended videos. Right: SUSCRIBETE text with amber circle button placeholder below. Bottom: robohogar.com in small white text. Clean, not cluttered. Cinematic dark theme." \
        "assets/branding/master/robohogar-mascot-saludando.png" "16:9" "flash"

    generate "assets/branding/master/youtube-lower-third.png" \
        "YouTube lower-third banner graphic on transparent background, 1920x200 pixels. Left: small robot mascot icon (head only, ~100px). Center: clean dark #0C0C0C semi-transparent rectangle (80% opacity) with space for name/title text in white. Right edge: amber #F5A623 vertical accent bar (8px wide). Subtle, professional, not distracting. Broadcast-quality design." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1920:200" "flash"

    generate "assets/branding/master/youtube-watermark.png" \
        "Tiny branding watermark 150x150 on transparent background. Simple robot head silhouette (spherical, two amber dot eyes, tiny antenna) in white with 50% opacity. Must be recognizable at actual 150px display size. Ultra-minimal, no text, no details beyond the silhouette." \
        "" "1:1" "flash"
}

# ═══ PATTERNS (4) ═══
run_patterns() {
    log_section "PATTERNS Y TEXTURAS (4 assets)"

    generate "assets/images/pattern-wave-amber.png" \
        "Seamless tileable pattern, subtle wave lines in very light amber #F5A623 at 10% opacity on white #FFFFFF background. Gentle, flowing horizontal waves. Spacing between waves: generous. Must work as repeating CSS background-image. Editorial, magazine-quality. Not busy, very subtle." \
        "" "1:1" "flash"

    generate "assets/images/pattern-hexagon-tech.png" \
        "Seamless tileable pattern, subtle hexagonal grid in very light gray #F2F2F2 lines on white #FFFFFF background. Thin lines (1px feel), generous spacing between hexagons. One hexagon in every ~20 has a tiny amber #F5A623 dot in center. Tech/futuristic feel but extremely subtle." \
        "" "1:1" "flash"

    generate "assets/images/pattern-circuit-dark.png" \
        "Seamless tileable pattern, subtle circuit board traces in #1a1a2e dark navy on #0C0C0C near-black background. Very thin lines forming circuit paths with occasional small dots at intersections. A few dots in amber #F5A623 (5% of total). Extremely subtle, cinematic, premium feel. Must tile seamlessly." \
        "" "1:1" "flash"

    generate "assets/images/pattern-dots-amber-soft.png" \
        "Seamless tileable pattern, regular grid of small dots (3px diameter) in very light amber #F5A623 at 15% opacity on white #FFFFFF background. Dots spaced 24px apart in both directions. Clean, geometric, Swiss design influenced. Ultra-subtle, works behind text." \
        "" "1:1" "flash"
}

# ═══ ICONS (8) ═══
run_icons() {
    log_section "ICON LIBRARY (8 assets)"

    local icon_names=("aspirador" "cortacesped" "humanoide" "ia" "comparativa" "guia" "opinion" "novedad")
    local icon_prompts=(
        "Simple line icon of a robot vacuum cleaner, top-down view showing circular shape with sensor bump. Single color amber #F5A623 on transparent background. Line weight 2px, minimal detail, recognizable at 32px. Clean vector style."
        "Simple line icon of a robotic lawn mower, side view profile showing low body with wheels and grass cutting. Single color amber #F5A623 on transparent background. Line weight 2px, minimal detail, recognizable at 32px."
        "Simple line icon of a humanoid robot, front view, standing pose. Rounded head, simple body, two arms, two legs. Single color amber #F5A623 on transparent background. Line weight 2px, friendly not menacing, recognizable at 32px."
        "Simple line icon representing artificial intelligence: a stylized brain with circuit connections emanating from it. Single color amber #F5A623 on transparent background. Line weight 2px, modern, not cliche. Recognizable at 32px."
        "Simple line icon of a balance scale with two platforms, representing comparison/versus. Single color amber #F5A623 on transparent background. Line weight 2px, symmetrical, clean. Recognizable at 32px."
        "Simple line icon of an open book with a small gear/cog on one page, representing a how-to guide. Single color amber #F5A623 on transparent background. Line weight 2px, clean. Recognizable at 32px."
        "Simple line icon of a speech bubble with three small dots inside, representing opinion/editorial. Single color amber #F5A623 on transparent background. Line weight 2px, rounded corners. Recognizable at 32px."
        "Simple line icon of a lightning bolt inside a circle, representing breaking news/new product. Single color amber #F5A623 on transparent background. Line weight 2px, energetic but clean. Recognizable at 32px."
    )

    for i in "${!icon_names[@]}"; do
        generate "assets/images/icon-${icon_names[$i]}.png" \
            "${icon_prompts[$i]}" \
            "" "1:1" "flash"
    done
}

# ═══ EMAIL (5) ═══
run_email() {
    log_section "EMAIL TEMPLATE ELEMENTS (5 assets)"

    generate "assets/images/email-divider.png" \
        "Horizontal email divider element on transparent background, 600x40 pixels. Center: thin amber #F5A623 line (1px) with a tiny robot head silhouette (amber, 20px) centered on the line. Clean, minimal, email-safe design." \
        "" "600:40" "flash"

    generate "assets/images/email-cta-button.png" \
        "Email CTA button on transparent background, 300x60 pixels. Rounded rectangle (8px radius) with solid amber #F5A623 fill. White text placeholder area centered inside. Clean shadow (2px, 10% opacity black). Professional, high contrast." \
        "" "300:60" "flash"

    generate "assets/images/email-footer.png" \
        "Email footer element on transparent background, 600x120 pixels. Top: thin gray #E5E7EB line separator. Center: small robot mascot (60px) next to ROBOHOGAR text in #6B7280 gray. Below: small text area for tagline. Clean, small, unobtrusive." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "600:120" "flash"

    generate "assets/images/email-welcome-hero.png" \
        "Welcome email hero banner, 600x300 pixels. White background #FFFFFF. Center: friendly robot mascot waving (full body, ~200px tall). Above robot: Bienvenido a ROBOHOGAR text in dark #0C0C0C clean sans-serif. Below robot: amber #F5A623 underline decoration. Warm, friendly, inviting." \
        "assets/branding/master/robohogar-mascot-saludando.png" "600:300" "2"

    generate "assets/images/email-section-header.png" \
        "Newsletter section header element, 600x80 pixels on transparent background. Left: amber #F5A623 vertical bar (6px wide, full height). Right of bar: clean area for section title text in dark #0C0C0C. Bottom: very subtle #F2F2F2 gray line. Minimal, editorial, magazine-style." \
        "" "600:80" "flash"
}

# ═══ CTA (3) ═══
run_cta() {
    log_section "BANNERS CTA SUSCRIPCIÓN (3 assets)"

    generate "assets/images/cta-banner-inline.png" \
        "Inline subscription banner for blog article, 600x150 pixels. Light amber #FEF3C7 (10% amber tint) background with rounded corners (12px). Left: small robot mascot with megaphone pose (~100px). Right: space for text headline and CTA below. Clean amber #F5A623 button shape in bottom-right area. Friendly, not aggressive. Magazine editorial style." \
        "assets/branding/master/robohogar-mascot-megafono.png" "600:150" "flash"

    generate "assets/images/cta-banner-wide.png" \
        "Wide subscription banner for landing page, 1200x200 pixels. Gradient background from #0C0C0C to #1a1a2e dark with subtle circuit pattern. Left: robot mascot waving in full color (~150px). Center: clean text area for tagline in white. Right: large amber #F5A623 button shape for CTA. Premium, cinematic feel." \
        "assets/branding/master/robohogar-mascot-saludando.png" "1200:200" "2"

    generate "assets/images/cta-banner-square.png" \
        "Square subscription card, 800x800 pixels. White #FFFFFF background. Center: robot mascot holding a small house (casita pose, ~300px). Above: ROBOHOGAR in dark text. Below mascot: newsletter tagline text area. Bottom: amber #F5A623 rounded button shape. Generous white space, clean, inviting." \
        "assets/branding/master/robohogar-mascot-casita.png" "1:1" "flash"
}

# ═══ MASCOTA (6) ═══
run_mascota() {
    log_section "VARIACIONES DE MASCOTA (6 assets)"

    generate "assets/branding/master/robohogar-mascot-sorprendido.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two wide-open amber/orange LED eyes in surprised expression, mouth shaped as small O. Two thin antennas with orange balls on tips, raised higher than normal. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart and ruffled edges. Both hands raised to cheeks in surprise gesture, no objects held. Short legs with white rounded boots. Copper/orange joint details. Clean illustration style, consistent lighting." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-enfadado.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes narrowed in mild frustration, small frown. Two thin antennas with orange balls, slightly tilted. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Arms crossed over chest, no objects held. Short legs with white rounded boots. Expression is mildly annoyed, NOT angry or scary — still cute and approachable. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-celebrando.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes curved upward in joy, big smile. Two thin antennas with orange balls, bouncing upward. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Both arms raised high above head, small confetti particles around (amber and cyan colored). One leg slightly lifted in dance pose. White rounded boots. Festive but clean. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-durmiendo.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes as closed horizontal lines (sleeping). Two thin antennas with orange balls, drooping down slightly. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Sitting on ground, head tilted to one side, coffee mug resting beside it. Three small Z letters floating above head in amber #F5A623. White rounded boots. Peaceful, adorable. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-corriendo.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes wide and determined. Two thin antennas with orange balls, swept back by wind. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart, apron fluttering behind. Running pose: one leg forward, one back, arms pumping. Right hand holds a small rolled newspaper or tablet. Motion lines behind the robot (2-3 thin lines). White rounded boots. Energetic but cute. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-cocinando.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes happy and focused. Two thin antennas with orange balls. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Right hand holds a wooden spoon, left hand holds a small steaming pot. Tiny chef hat (white, tilted slightly) on top of head between antennas. White rounded boots. Cozy, domestic, charming. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"
}

# ═══ SLIDES (8) ═══
run_slides() {
    log_section "SLIDE DECK BACKGROUNDS (8 assets)"

    generate "assets/branding/slides/slide-01-portada.png" \
        "Presentation slide background 1920x1080. Dark premium background, gradient from #0C0C0C to #1a1a2e. Center: friendly robot mascot with coffee mug (full body, ~400px) on right side. Left side: large clean area for title text. Subtle hexagonal pattern overlay at 5% opacity. Bottom: thin amber #F5A623 line across full width. Cinematic, premium, professional." \
        "assets/branding/master/robohogar-mascot-principal.png" "16:9" "2"

    generate "assets/branding/slides/slide-02-mision.png" \
        "Presentation slide background 1920x1080. Warm, cinematic photo-style image of a modern living room with a robot vacuum cleaner working on hardwood floor. Golden hour lighting from large windows. Soft depth of field. Semi-transparent dark overlay (40% opacity) on left half for text area. Amber #F5A623 accent line on left edge. Photorealistic, editorial quality." \
        "" "16:9" "2"

    generate "assets/branding/slides/slide-03-audiencia.png" \
        "Presentation slide background 1920x1080. Clean white #FFFFFF background. Subtle grid of small icons representing audience: smartphones, tablets, homes, families — all in light #F2F2F2 gray as background pattern. Left side: large clean area for text and bullet points. Right side: abstract illustration of diverse people silhouettes looking at devices. Amber #F5A623 accent details on 2-3 icons. Professional." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-04-canales.png" \
        "Presentation slide background 1920x1080. Dark #0C0C0C background. Five evenly spaced circular icons in a horizontal row across the center: envelope (newsletter), globe (web), briefcase (LinkedIn), X shape (Twitter/X), play button (YouTube). Icons outlined in amber #F5A623, not filled. Subtle connecting lines between icons. Minimal, professional infographic style." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-05-metricas.png" \
        "Presentation slide background 1920x1080. White #FFFFFF background. Three large placeholder card shapes arranged horizontally: each is a rounded rectangle (400x300) with #F2F2F2 background and thin #F5A623 amber top border (4px). Cards have space for metric number (large) and label (small). Data dashboard aesthetic, clean and professional." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-06-contenido.png" \
        "Presentation slide background 1920x1080. White background. Mosaic/grid layout of 6 placeholder rectangles (representing article screenshots) in 2 rows of 3, each with subtle shadow and rounded corners. One rectangle has amber #F5A623 border (featured). Small robot mascot with magnifying glass in bottom-right corner. Editorial, portfolio-style layout." \
        "assets/branding/master/robohogar-mascot-detective.png" "16:9" "flash"

    generate "assets/branding/slides/slide-07-tarifas.png" \
        "Presentation slide background 1920x1080. White #FFFFFF background. Three pricing column placeholders side by side: left (basic, #F2F2F2 header), center (featured, amber #F5A623 header, slightly taller), right (premium, #0C0C0C header). Each column has horizontal lines suggesting bullet points. Clean, SaaS-style pricing table aesthetic." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-08-contacto.png" \
        "Presentation slide background 1920x1080. Split design: left 60% dark #0C0C0C background with subtle circuit pattern, right 40% white #FFFFFF. On the white side: robot mascot waving (full body, ~350px). On the dark side: large clean area for contact info text in white. Amber #F5A623 thin vertical divider between sections. Warm, inviting, professional closing slide." \
        "assets/branding/master/robohogar-mascot-saludando.png" "16:9" "flash"
}

# ═══ DISPATCHER ═══
case "$SECTION" in
    logos)    run_logos ;;
    social)   run_social ;;
    youtube)  run_youtube ;;
    patterns) run_patterns ;;
    icons)    run_icons ;;
    email)    run_email ;;
    cta)      run_cta ;;
    mascota)  run_mascota ;;
    slides)   run_slides ;;
    all)
        run_logos
        run_social
        run_youtube
        run_patterns
        run_icons
        run_email
        run_cta
        run_mascota
        run_slides
        ;;
    *)
        echo "Uso: $0 {logos|social|youtube|patterns|icons|email|cta|mascota|slides|all}"
        exit 1
        ;;
esac

# ═══ RESUMEN ═══
echo ""
echo "═══════════════════════════════════════"
echo -e "  Generados: ${GREEN}$GENERATED${NC}"
echo -e "  Saltados:  ${YELLOW}$SKIPPED${NC} (ya existían)"
echo -e "  Fallidos:  ${RED}$FAILED${NC}"
echo "═══════════════════════════════════════"
echo ""
echo "Siguiente paso: actualizar assets/branding/asset-catalog.md"
echo "Ver sección 14 del BRAND-DECK.md para el texto exacto."
