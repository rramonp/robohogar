---
name: ROBOHOGAR pronunciation in TTS audio assets
description: Brand mentions in any TTS audiobook/podcast asset must use 'ROBO, OGAR' (comma + space), never 'ROBOHOGAR' nor 'ROBO OGAR' (single space) — comma forces ~150-300 ms prosodic pause that prevents Multilingual v2 from aspirating the H English-style.
type: feedback
---

**Rule:** every brand mention in TTS-bound text for ROBOHOGAR audio assets must use the canonical token `ROBO, OGAR` (comma + space). Never `ROBOHOGAR` (joined), never `ROBO OGAR` (single space), never `ROBO,OGAR` (no space after comma), never `ROBO. OGAR` (period).

**Why:** ElevenLabs Multilingual v2 with the Luis voice (Spanish peninsular narrative) inconsistently aspirates the silent Spanish H when the brand appears as a contiguous token (`ROBOHOGAR`), producing audible "RoboJOgar" — the English aspirated H, jarring to a Spanish ear because the H in Spanish is silent. The earlier convention `ROBO OGAR` (single space, validated by Rafael 2026-04-22) reduced the problem but did not eliminate it: in some prosodic contexts (consonant before, vowel after) the model still glued both tokens together. The comma forces a deterministic prosodic pause of ~150-300 ms — long enough to keep the words separate, short enough not to read as a sentence break (period would).

Alternatives evaluated and discarded:
- Period (`ROBO. OGAR`): pause too long, sounds like end of sentence, breaks rhythm.
- SSML `<break time="200ms"/>`: ElevenLabs only honors SSML on Pro+ plans, not on Starter (Rafael's plan).
- Double space: ignored by the model.
- Hyphen (`ROBO-OGAR`): read as "ROBO menos OGAR" or "ROBO guión OGAR" depending on context.

**How to apply:** wherever ROBOHOGAR appears in a text destined for TTS (audiobook narration body, intro/outro brand assets, podcast trailer, future audio promos), substitute the brand token with `ROBO, OGAR`. The substitution lives ONLY in TTS-bound text. The visible written brand stays `ROBOHOGAR` (no comma) in HTML, banners, social copy, metadata visible to the reader, post titles, etc. — the comma is purely a phonetic crutch for the speech engine.

**Operational guarantees in the pipeline:**
- `utilities/generate_audio.py` applies an idempotent safety-net regex (`\bROBO\s*,?\s*H?OGAR\b` → `ROBO, OGAR`) on the input text before chunking + TTS, normalizing all variants (`ROBOHOGAR`, `ROBO OGAR`, `ROBO  OGAR`, `ROBO,OGAR`) to canonical. Logs how many non-canonical mentions it normalized.
- `.claude/commands/audiobook-generate.md § paso 2` documents the rule in the TTS transformations table.
- `.claude/commands/audiobook-generate.md § paso 3` runs a pre-output grep verification that blocks generation if `\bROBOHOGAR\b` or `\bROBO +OGAR\b` matches in `audiolibro.txt`.
- `docs/plan-audiolibros-ficciones.md § Decisiones cerradas` reflects the change with changelog 2026-04-25.

**Inheritance:** every future skill that produces brand TTS (channel trailers, podcast promos, audio ads) must apply the same rule. Specifically inherits to `/audiobook-distribute` when generating any new TTS asset (e.g. FASE 3.5 channel trailer).

**Origin incident (2026-04-25):** while planning the FASE 3 audio distribution to YouTube + RSS podcast, Rafael flagged that the convention `ROBO OGAR` (single space, in production since 2026-04-22) was still leaving traces of aspirated H in some test audios — when the brand token sat between certain vowel/consonant contexts, the engine collapsed the gap. Reinforcement to comma + space canonicalized as the new rule.

**Pre-existing audio assets (not yet re-recorded):** `assets/audio/intro-ficciones.mp3` (2.53s) and `outro-ficciones.mp3` (11.89s) were generated 2026-04-22 with `ROBO OGAR`. Decision: re-record only if production episodes distributed to YouTube/Spotify reveal audible aspiration. Cost of re-recording is trivial (~$0.10 ElevenLabs, 2 minutes work). Until then, the existing assets remain in service.
