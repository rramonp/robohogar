"""
Genera el MP4 de YouTube para un audiolibro siguiendo el formato D++ híbrido.

Uso:
    python utilities/generate_youtube_video.py <slug>

Layout del vídeo (1280×720, 25 fps):
  - Background full-frame: cover YouTube del relato (estático todo el vídeo).
  - Waveform inferior: barra ámbar `#F5A623` de 120 px alto siguiendo el audio.
  - Chyron de capítulo: "Capítulo I — La cocina" con fade in/out de 1 s + 3 s
    sostenido + 1 s fade out, centrado vertical 15% desde arriba, aparece al
    cruzar la marca temporal de cada capítulo del `chunks-index.json`.
  - Logo robot 200×200 esquina inferior derecha (margen 30 px), permanente.

Inputs (todos relativos al repo root):
  - `assets/audio/ficciones/<slug>.mp3` (audio source)
  - `assets/audio/ficciones/<slug>-chunks-index.json` (capítulos + timestamps)
  - `assets/audio/ficciones/covers/<slug>-yt-1280x720.png` (background)
  - `assets/branding/logo-robohogar-200x200.png` (overlay esquina)

Output (versionado, nunca sobreescribe):
  - `assets/audio/ficciones/<slug>-youtube.mp4` (1ª vez)
  - `assets/audio/ficciones/<slug>-youtube-v2.mp4`, `-v3.mp4`... (regeneraciones)

Encoding:
  - libx264 preset veryfast (1-4 min para 15 min audio en CPU portátil).
  - yuv420p para compatibilidad universal (YouTube re-encoda igual, pero
    así pasa el upload sin warnings).
  - AAC 192 kbps para el audio (overkill para voz pero sin coste real).

Algoritmo YouTube 2026: el waveform animado + chyrons cambiantes cumplen
"movimiento real" — no se penaliza como "AI slop" / inauthentic content.
La voz Luis ElevenLabs de calidad humana sintetizada también pasa el filtro.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Reutilizamos find_ffmpeg de generate_audio.py para no duplicar la lógica
# de detección del binario.
sys.path.insert(0, str(Path(__file__).parent))
from generate_audio import find_ffmpeg, probe_duration  # noqa: E402


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = REPO_ROOT / "assets" / "audio" / "ficciones"
COVERS_DIR = AUDIO_DIR / "covers"
LOGO_PATH = REPO_ROOT / "assets" / "branding" / "logo-robohogar-200x200.png"

# Font para drawtext. Arial Bold viene en cualquier Windows. Si en el futuro
# queremos DM Sans (font oficial de marca), añadirla al repo y apuntar aquí.
# El path va con `/` no `\\` porque ffmpeg's filter parser interpreta `\` como
# escape — `/` funciona también en Windows internamente.
FONT_FILE = "C:/Windows/Fonts/arialbd.ttf"

# Resolución del MP4. 1280×720 (HD ready) es suficiente para audiolibro
# (no hay detalle visual que justifique 1080p), reduce render time y peso
# del fichero. YouTube re-encoda al subir.
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720
WAVEFORM_HEIGHT = 120

# Color ámbar ROBOHOGAR para el waveform — coherencia visual con la marca.
WAVEFORM_COLOR = "0xF5A623"

# Timing de los chyrons de capítulo. La onset es 1 s antes de la marca
# del capítulo (fade in mientras el oyente aún oye el final del capítulo
# anterior, da contexto visual antes del cambio narrativo). Total visible:
# fade_in + sustain + fade_out = 1 + 3 + 1 = 5 s.
CHYRON_FADE_IN_SEC = 1.0
CHYRON_SUSTAIN_SEC = 3.0
CHYRON_FADE_OUT_SEC = 1.0


def find_versioned_output(slug: str) -> Path:
    """Devuelve la próxima ruta versionada para el MP4 output.

    Si no existe `<slug>-youtube.mp4` → usa esa ruta.
    Si existe → busca `<slug>-youtube-v2.mp4`, `-v3.mp4`, ... hasta encontrar
    una libre. Patrón heredado de la regla `feedback_never_overwrite_images.md`:
    nunca sobrescribir un asset generado, versionar siempre.
    """
    base = AUDIO_DIR / f"{slug}-youtube.mp4"
    if not base.exists():
        return base
    for v in range(2, 100):
        candidate = AUDIO_DIR / f"{slug}-youtube-v{v}.mp4"
        if not candidate.exists():
            return candidate
    sys.exit(f"ERROR: ya hay 100 versiones de {slug}-youtube*.mp4. Limpia manual antes.")


def escape_drawtext_text(text: str) -> str:
    """Escapa caracteres especiales del filter drawtext de ffmpeg.

    ffmpeg's drawtext filter parser tiene 4 caracteres conflictivos:
      - `\\` (backslash) → debe duplicarse
      - `'`  (single quote) → wrap completo en escape unicode \\u0027
      - `:`  (colon, separador de opciones del filter) → debe escaparse `\\:`
      - `,`  (comma, separador de filters) → debe escaparse `\\,`

    Para evitar problemas con ' (que es común en español: "L'Hospitalet",
    contracciones), reemplazamos por el typographic apostrophe `’`
    (U+2019) que es visualmente idéntico y no rompe el parser.
    """
    text = text.replace("\\", "\\\\")
    text = text.replace("'", "’")
    text = text.replace(":", "\\:")
    text = text.replace(",", "\\,")
    return text


def build_chyron_filter(chapter: dict, video_label_in: str, video_label_out: str) -> str:
    """Construye un drawtext filter con fade in/out para un capítulo.

    Layout:
      - Texto: `Capítulo {N} — {título}` (em-dash entre número y título,
        coherente con la convención editorial ROBOHOGAR de em-dashes en
        prosa narrativa).
      - Posición: centrado horizontal (x=(w-text_w)/2), 15% desde arriba
        (y=h*0.15) — fuera de la zona del waveform inferior, sobre el cover.
      - Color: blanco con borde negro 3 px (legible sobre cualquier cover).
      - Tamaño: 42 px (visible en mobile sin abrumar el cover).

    Timing del alpha:
      - t < start - fade_in : alpha = 0  (no visible)
      - start - fade_in ≤ t < start : alpha = ramp 0→1 (fade in)
      - start ≤ t < start + sustain : alpha = 1 (sostenido)
      - start + sustain ≤ t < start + sustain + fade_out : alpha = ramp 1→0 (fade out)
      - t ≥ start + sustain + fade_out : alpha = 0
    El `enable=between(t,X,Y)` evita compute innecesario fuera de la ventana.
    """
    start = chapter["start_seconds"]
    fade_in_start = start - CHYRON_FADE_IN_SEC
    sustain_end = start + CHYRON_SUSTAIN_SEC
    fade_out_end = sustain_end + CHYRON_FADE_OUT_SEC

    text = escape_drawtext_text(f"Capítulo {chapter['number']} — {chapter['title']}")

    # alpha expression: piecewise linear con if/lt nested.
    # Fórmula: si t<start, ramp lineal 0→1 entre fade_in_start y start.
    #          si t<sustain_end, sostener 1.
    #          si no, ramp lineal 1→0 entre sustain_end y fade_out_end.
    alpha = (
        f"if(lt(t,{start}),"
        f"max(0,(t-{fade_in_start})/{CHYRON_FADE_IN_SEC}),"
        f"if(lt(t,{sustain_end}),1,"
        f"max(0,1-(t-{sustain_end})/{CHYRON_FADE_OUT_SEC})))"
    )

    return (
        f"[{video_label_in}]drawtext="
        f"text='{text}'"
        f":fontfile='{FONT_FILE}'"
        f":fontsize=42"
        f":fontcolor=white"
        f":bordercolor=black"
        f":borderw=3"
        f":x=(w-text_w)/2"
        f":y=h*0.15"
        f":enable='between(t,{fade_in_start},{fade_out_end})'"
        f":alpha='{alpha}'"
        f"[{video_label_out}]"
    )


def build_filter_complex(chapters: list[dict]) -> str:
    """Construye el filter_complex completo del MP4 D++ híbrido.

    Pipeline de streams (números de input fijados por el orden de -i):
      [0:a] = audio MP3
      [1:v] = cover hero (loop static)
      [2:v] = logo robot (loop static)

    Outputs intermedios:
      [bg]   = cover scaled + format yuv420p
      [wave] = showwaves overlay del audio
      [v0]   = bg + wave
      [v1], [v2], [v3], ... = v0 con un drawtext de chyron añadido cada vez
      [outv] = vN + logo overlay esquina

    Comma `,` separa filters dentro de un mismo nodo; `;` separa nodos.
    """
    parts = []

    # 1. Background: cover scaled al canvas + format yuv420p para compat upload.
    parts.append(
        f"[1:v]scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},format=yuv420p[bg]"
    )

    # 2. Waveform: showwaves del audio en color ámbar, mode cline (continuous line).
    parts.append(
        f"[0:a]showwaves=s={VIDEO_WIDTH}x{WAVEFORM_HEIGHT}"
        f":colors={WAVEFORM_COLOR}:mode=cline,format=rgba[wave]"
    )

    # 3. Bg + waveform inferior. y=H-h pone el wave pegado al borde inferior.
    parts.append(f"[bg][wave]overlay=0:H-h[v0]")

    # 4. Chyrons por capítulo, cada uno chained al anterior.
    current_label = "v0"
    for i, chapter in enumerate(chapters):
        next_label = f"v{i + 1}"
        parts.append(build_chyron_filter(chapter, current_label, next_label))
        current_label = next_label

    # 5. Logo overlay esquina inferior derecha. Margen 30 px.
    parts.append(f"[{current_label}][2:v]overlay=W-w-30:H-h-30[outv]")

    # Unimos todos los nodos con `;` separator.
    return ";".join(parts)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(
            f"Uso: python {sys.argv[0]} <slug>\n"
            f"Ejemplo: python utilities/generate_youtube_video.py papa-desde-singapur"
        )
    slug = sys.argv[1]

    # Inputs requeridos — chequeo upfront para fallar amigable.
    audio = AUDIO_DIR / f"{slug}.mp3"
    chunks_index = AUDIO_DIR / f"{slug}-chunks-index.json"
    cover_yt = COVERS_DIR / f"{slug}-yt-1280x720.png"

    missing = []
    if not audio.exists():
        missing.append(f"  - {audio.relative_to(REPO_ROOT)} (correr /audiobook-generate)")
    if not chunks_index.exists():
        missing.append(
            f"  - {chunks_index.relative_to(REPO_ROOT)} "
            f"(regenerar con /audiobook-generate tras actualizar generate_audio.py)"
        )
    if not cover_yt.exists():
        missing.append(
            f"  - {cover_yt.relative_to(REPO_ROOT)} "
            f"(correr `python utilities/generate_audiobook_covers.py {slug}`)"
        )
    if not LOGO_PATH.exists():
        missing.append(
            f"  - {LOGO_PATH.relative_to(REPO_ROOT)} "
            f"(generar logo 200x200 desde profile-icon-1080x1080 — ver guía Bloque 1.6)"
        )
    if missing:
        print("ERROR: faltan inputs:")
        for m in missing:
            print(m)
        sys.exit(1)

    # Verifica que el font existe (Windows-specific).
    if not Path(FONT_FILE).exists():
        sys.exit(f"ERROR: no existe el font {FONT_FILE}. "
                 f"Edita FONT_FILE en {Path(__file__).name} apuntando a un .ttf bold instalado.")

    ffmpeg = find_ffmpeg()

    # Carga chunks-index para los timestamps de capítulos.
    index_data = json.loads(chunks_index.read_text(encoding="utf-8"))
    chapters = index_data["chapters"]
    print(f"Audio   : {audio.relative_to(REPO_ROOT)} "
          f"({index_data['total_duration_seconds']:.1f}s = {index_data['total_duration_seconds']/60:.1f} min)")
    print(f"Cover   : {cover_yt.relative_to(REPO_ROOT)}")
    print(f"Logo    : {LOGO_PATH.relative_to(REPO_ROOT)}")
    print(f"Capítulos: {len(chapters)}")
    for ch in chapters:
        m, s = divmod(int(ch["start_seconds"]), 60)
        print(f"  {m:02d}:{s:02d} · {ch['number']}. {ch['title']}")
    print()

    output = find_versioned_output(slug)
    print(f"Output  : {output.relative_to(REPO_ROOT)}")
    print()

    filter_complex = build_filter_complex(chapters)

    cmd = [
        ffmpeg, "-y",
        "-i", str(audio),               # [0:a]
        "-loop", "1", "-i", str(cover_yt),     # [1:v]
        "-loop", "1", "-i", str(LOGO_PATH),    # [2:v]
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", "0:a",
        # Vídeo: H.264 fast preset, 25 fps, yuv420p para compat universal.
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-r", "25",
        # Audio: AAC 192k. -shortest para que dure exactamente el audio.
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        # Movflags +faststart pone el moov atom al inicio — YouTube empieza
        # a procesar el upload sin esperar a recibir el fichero entero.
        "-movflags", "+faststart",
        str(output),
    ]

    print("Ejecutando ffmpeg...")
    print(f"  Filter complex: {len(filter_complex)} chars, {filter_complex.count(';') + 1} nodos")
    print()

    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        print("ffmpeg FAIL — últimos 1000 chars de stderr:")
        print(result.stderr[-1000:])
        sys.exit(1)

    duration = probe_duration(ffmpeg, output)
    size_mb = output.stat().st_size / 1024 / 1024
    print()
    print("=" * 72)
    print(f"MP4 GENERADO · {slug}")
    print("=" * 72)
    print(f"Output    : {output.relative_to(REPO_ROOT)}")
    print(f"Tamaño    : {size_mb:.1f} MB")
    print(f"Duración  : {duration / 60:.1f} min ({duration:.1f}s)")
    print(f"Capítulos : {len(chapters)} chyrons con fade in/out")
    print("=" * 72)


if __name__ == "__main__":
    main()
