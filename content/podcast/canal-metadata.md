---
title: "Ficciones Domésticas — ROBOHOGAR"
description: "Relatos de ciencia ficción próxima sobre robótica doméstica. Lo que pasa cuando los robots llegan a casa: humanoides, aspiradores con IA, cuidados, soledades, hogares que aprenden. Cada semana, junto al newsletter en robohogar.com."
language: "es"
author: "ROBOHOGAR"
owner_name: "ROBOHOGAR"
owner_email: "REEMPLAZAR_CON_EMAIL_OWNER"
category_main: "Fiction"
category_sub: "Drama"
explicit: false
artwork_url: "REEMPLAZAR_CON_URL_PUBLICA_ARTWORK_3000x3000"
link: "https://robohogar.com"
copyright: "© ROBOHOGAR · Rafael"
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

## URLs públicas en plataformas (rellenar tras alta)

```yaml
spotify_url: "https://open.spotify.com/show/..."
apple_url: "https://podcasts.apple.com/.../..."
amazon_url: "https://music.amazon.com/podcasts/..."
youtube_channel_url: "https://www.youtube.com/@robohogar"
```

`/audiobook-distribute` consume estos campos para el resumen final tras cada episodio publicado.

## Convenciones

- **Idioma `language`**: ISO 639-1 minúscula. `es` para español genérico (Apple/Spotify lo aceptan sin distinguir variantes peninsulares vs LATAM).
- **`copyright`**: el símbolo © sí (no es problema en RSS UTF-8).
- **`explicit`**: `false` por default. Si un relato puntual es explícito, su `<item>` puede sobrescribirlo individualmente (modificación pendiente en `generate_podcast_rss.py` si pasa).
- **Cambios en este archivo**: rebuild del feed obligatorio (`python utilities/generate_podcast_rss.py && python utilities/upload_rss_to_r2.py`). Las plataformas re-leen el feed cada hora aprox.
