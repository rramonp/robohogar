---
name: Branding images — always white bg + crop
description: EVERY branding image must have pure white background and be cropped to content — no exceptions, no reminders needed
type: feedback
originSessionId: 1a16a728-ecd0-4da1-9d8c-0c2ce1670708
---
EVERY branding/logo image delivered to Rafael must be:
1. Pure white background (255,255,255) — clean checkerboard artifacts from Gemini
2. Cropped tight to content (~15px padding max)
3. Exported as JPG in addition to PNG (email/Beehiiv can't handle transparency)
4. Upscaled 2x with Lanczos if source is 1K

**Why:** Rafael had to ask THREE TIMES for this in the same session. Checkerboard artifacts baked into Gemini outputs are not transparency — they're actual gray pixels (~204,204,204) that must be detected and replaced. This is a post-processing step that must happen AUTOMATICALLY after every branding image generation, without being asked.

**How to apply:** After EVERY nano-banana generation for branding (logos, badges, lockups, monograms), run the clean+crop+export script BEFORE showing the result to Rafael. Never deliver a raw Gemini output for branding. This applies to all contexts, not just the nano-banana skill.
