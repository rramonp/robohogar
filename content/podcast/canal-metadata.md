---
title: "Ficciones Domésticas — ROBOHOGAR"
description: "Relatos de ciencia ficción próxima sobre robótica doméstica. Lo que pasa cuando los robots llegan a casa: humanoides, aspiradores con IA, cuidados, soledades, hogares que aprenden. Cada semana, junto al newsletter en robohogar.com."
language: "es"
author: "ROBOHOGAR"
owner_name: "ROBOHOGAR"
owner_email: "bakalap2@gmail.com"
category_main: "Fiction"
category_sub: "Drama"
explicit: false
artwork_url: "https://feed.robohogar.com/podcast-canal-artwork-3000x3000.jpg"
link: "https://robohogar.com"
copyright: "© ROBOHOGAR · Rafael"
spotify_url: "https://open.spotify.com/show/1pNQVVzcjtfbTM214SZbBc"
apple_url: "https://podcasts.apple.com/es/podcast/ficciones-domésticas-robohogar/id1895482632"
amazon_url: "https://music.amazon.es/podcasts/461615a7-4094-4e90-b867-565e40393f0d/ficciones-domésticas-—-robohogar"
youtube_channel_url: "https://www.youtube.com/@robohogar"
---

# Canal podcast — Ficciones Domésticas (ROBOHOGAR)

> Frontmatter canónico del canal podcast. Lo consume `utilities/generate_podcast_rss.py` para construir cada `feed.xml`.

## Cómo se rellena

| Campo | Qué pongo |
|---|---|
| `owner_email` | Email Apple-verified que controlo (Rafael personal o `hola@robohogar.com` si existe). Apple manda código de verificación aquí al dar de alta. |
| `artwork_url` | URL pública del JPG 3000×3000 del canal podcast (no del episodio). Se sube una vez a R2 al setup. Sugerido path: `https://feed.robohogar.com/podcast-canal-artwork-3000x3000.jpg`. |
| `category_main` | Categoría iTunes top-level. `Fiction` para ficción narrativa. Lista oficial: https://podcasters.apple.com/support/1691-apple-podcasts-categories |
| `category_sub` | Sub-categoría iTunes. `Drama` para ficción literaria. Otras opciones: `Science Fiction`, `Comedy Fiction`, `Stories for Kids`. |

## URLs públicas en plataformas — estado 2026-04-25

| Plataforma | URL | Estado | Notas |
|---|---|---|---|
| Spotify | [show/1pNQVVzcjtfbTM214SZbBc](https://open.spotify.com/show/1pNQVVzcjtfbTM214SZbBc) | ✅ Available | Alta + verificación email + aprobación en minutos. |
| Apple Podcasts | [id1895482632](https://podcasts.apple.com/es/podcast/ficciones-domésticas-robohogar/id1895482632) | ✅ Available | Show ID `1895482632`. URL canónica `/es/` con slug `ficciones-domésticas-robohogar`. La URL corta `https://podcasts.apple.com/podcast/id1895482632` también funciona (Apple redirige por geo). |
| Amazon Music | [461615a7-…/ficciones-domésticas-—-robohogar](https://music.amazon.es/podcasts/461615a7-4094-4e90-b867-565e40393f0d/ficciones-domésticas-—-robohogar) | ✅ Available | Show UUID `461615a7-4094-4e90-b867-565e40393f0d`. Pasó de `PENDING` a `Available` tras minutos-horas (alta misma sesión 2026-04-25). URL canónica `/es/` con slug `ficciones-domésticas-—-robohogar` (incluye em-dash `—`, codificado como `%E2%80%94` en HTTP). |
| YouTube canal | [@robohogar](https://www.youtube.com/@robohogar) | ✅ Live | Channel ID `UCcEbi-DOO2KHLsmsXl21Vlg`. Activo desde FASE 3 piloto (2026-04-25). |

`/audiobook-distribute` consume el frontmatter de arriba (`spotify_url`, `apple_url`, `amazon_url`, `youtube_channel_url`) para el resumen final tras cada episodio publicado y para los enlaces del outro de show notes.

## Convenciones

- **Idioma `language`**: ISO 639-1 minúscula. `es` para español genérico (Apple/Spotify lo aceptan sin distinguir variantes peninsulares vs LATAM).
- **`copyright`**: el símbolo © sí (no es problema en RSS UTF-8).
- **`explicit`**: `false` por default. Si un relato puntual es explícito, su `<item>` puede sobrescribirlo individualmente (modificación pendiente en `generate_podcast_rss.py` si pasa).
- **Cambios en este archivo**: rebuild del feed obligatorio (`python utilities/generate_podcast_rss.py && python utilities/upload_rss_to_r2.py`). Las plataformas re-leen el feed cada hora aprox.
