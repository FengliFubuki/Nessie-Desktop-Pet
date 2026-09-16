# Reproduction source

This directory contains the readable source used by the Nessie production run.

- `prompts/` holds the base, state-row, retry, gaze-direction, and repair prompts.
- `scripts/export_clean_previews.py` exports the final atlas as animated GIF and WebP previews with a reserved transparent palette entry, no dithering, and decoded-frame validation.
- `notes/` records the character specification and gaze mechanics.

The complete image-source evidence—references, generated strips, extracted frames, final atlas variants, and QA artifacts—is in the split archive at the repository root. Join every `Nessie-source-artifacts.zip.part-*` file into `Nessie-source-artifacts.zip` before extracting it.
