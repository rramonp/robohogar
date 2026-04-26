# Beehiiv · snippets audiolibro · El operador nocturno

**Generado:** 2026-04-26 por `/audiobook-generate el-operador-nocturno`.
**Relato fuente:** [`2026-04-19-el-operador-nocturno.md`](2026-04-19-el-operador-nocturno.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/el-operador-nocturno.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/el-operador-nocturno.mp3 |
| **Duración** | 23,1 min (1385,17s) |
| **Tamaño** | 21,1 MB (22.164.001 bytes) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Chunks TTS** | 5 · 19.704 chars · ~15.566 créditos (~12,8% cuota Creator 121.880) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe OK (1385,17s · 128 kbps · 44,1 kHz mono) |
| **chunks-index.json** | 3 capítulos detectados (Uno · Dos · Tres) |
| **Cover YouTube** | `assets/audio/ficciones/covers/el-operador-nocturno-yt-1280x720.png` (664 KB) |
| **Cover podcast** | `assets/audio/ficciones/covers/el-operador-nocturno-podcast-1400x1400.jpg` (80 KB) |
| **Saldo ElevenLabs post** | 92.763 créditos restantes (de 108.329 antes) — `utilities/elevenlabs_balance.py status` |

---

## (a) Título del post Beehiiv

```
🎧 Ficción · El operador nocturno
```

*32 chars — cabe limpio en subject line de email (límite recomendado 45 chars per `@rules/newsletter.md`).*

---

## (b) Subtítulo / dek

```
Madrid 2032, las tres y catorce. Un niño se levanta a beber agua. En la cocina hay alguien. No es el robot. Es el que lo pilota desde Manila — y lleva semanas calibrando el ruido para verlo despierto.
```

---

## (c) Custom HTML block · email-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from web**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">
  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">🎧 Audiolibro disponible · 23 min</p>
  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">
    El reproductor no se muestra en tu cliente de email.
    <a href="https://robohogar.com/p/el-operador-nocturno" style="color: #F5A623; font-weight: 600; text-decoration: none;">Escúchalo en la web</a>
    o
    <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/el-operador-nocturno.mp3" style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.
  </p>
</div>
```

---

## (d) Custom HTML block · web-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from email**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid rgba(12,12,12,0.15); border-radius: 8px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; color: #0C0C0C;">
    🎧 Escuchar · <span style="color: #6B7280; font-weight: 400;">23 min</span>
  </p>
  <audio id="audio-el-operador-nocturno" controls preload="none" style="width: 100%; height: 44px;" src="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/el-operador-nocturno.mp3"></audio>
  <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/el-operador-nocturno.mp3" download style="display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; text-decoration: none; font-weight: 500;">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  (function() {
    var audio = document.getElementById('audio-el-operador-nocturno');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: 'El operador nocturno',
        artist: 'ROBOHOGAR · Ficciones Domésticas',
        artwork: []
      });
    });
  })();
</script>
```

---

## Capítulos detectados (chunks-index.json)

| # | Inicio | Título |
|---|---|---|
| 1 | 00:06 | Madrid, un martes a las tres y catorce |
| 2 | 04:57 | Manila, el mismo martes, las nueve y catorce |
| 3 | 15:36 | Madrid, sábado, doce y seis del mediodía |

Estos timestamps los consume `/audiobook-distribute` (paso 13.5 de `/post-publish`) para componer chyrons del MP4 YouTube + chapters timestamped en la descripción YouTube + show notes RSS.

---

## Orden de pegado en Beehiiv

1. **(a)** como título del post.
2. **(b)** como subtítulo.
3. **(c)** primer Custom HTML block inmediatamente después del subtítulo → engranaje → **hide from web**.
4. **(d)** segundo Custom HTML block inmediatamente después → engranaje → **hide from email**.
5. El cuerpo del relato (`Uno. / Dos. / Tres.` + Lo real + CTA) va **después** de ambos bloques HTML — copia desde [`beehiiv-paste.html`](beehiiv-paste.html).
6. Featured image: subir [`assets/hero-el-operador-nocturno-v6.webp`](assets/hero-el-operador-nocturno-v6.webp).
7. **Tags Beehiiv**: `ficciones`, `humanoide`. **Category**: Opinión.
8. **Publish to**: Email and web. **Content Gate**: OFF.
9. Preview mobile (375 px) antes de publicar.
10. Tras publicar → pasa la URL definitiva al chat para lanzar `/post-publish <URL>`.

## Regeneración parcial

Si algún chunk suena mal (transición rara, nombre pronunciado torcido):

- Chunks persistidos en `assets/audio/ficciones/_chunks-el-operador-nocturno/`.
- Regenerar solo el chunk afectado con ajustes en `voice_settings` (stability / similarity_boost).
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe la key `el-operador-nocturno.mp3`).

Ahorra cuota API vs regenerar los 5 chunks completos.

## Distribución multi-plataforma

Cuando vayas a publicar este relato en Beehiiv:
1. `/post-publish <URL>` lanza limpieza estándar + `/social-content` + `/obsidian-robohogar`.
2. **Paso 13.5 de `/post-publish` auto-fire**: si hay MP3 + chunks-index + covers (ya hay los tres), invoca `/audiobook-distribute el-operador-nocturno` que genera MP4 YouTube + episodio RSS feed para Spotify/Apple/Amazon Music. Tiempo total: ~10-15 min de compute.
