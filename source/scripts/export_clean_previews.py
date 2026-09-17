#!/usr/bin/env python3
"""Export transparent GIFs with an explicit shared palette and binary alpha."""
import argparse
import json
from pathlib import Path
from PIL import Image

DURATIONS = {
    "idle": [280, 110, 110, 140, 140, 320],
    "running-right": [120] * 7 + [220],
    "running-left": [120] * 7 + [220],
    "waving": [140] * 3 + [280],
    "jumping": [140] * 4 + [280],
    "failed": [140] * 7 + [240],
    "waiting": [150] * 5 + [260],
    "running": [120] * 5 + [220],
    "review": [150] * 5 + [280],
}

def palette_for(frames):
    colors = []
    for frame in frames:
        colors.extend((r, g, b) for r, g, b, a in frame.getdata() if a >= 128)
    height = max(1, (len(colors) + 255) // 256)
    sample = Image.new("RGB", (256, height), "white")
    sample.putdata(colors + [(255, 255, 255)] * (256 * height - len(colors)))
    quantized = sample.quantize(colors=255, method=Image.Quantize.MEDIANCUT)
    visible_palette = quantized.getpalette()[:765]
    visible_palette += [255, 255, 255] * ((765 - len(visible_palette)) // 3)
    palette = Image.new("P", (1, 1))
    palette.putpalette([255, 0, 255] + visible_palette)
    return palette

def indexed_frame(frame, palette):
    indexed = frame.convert("RGB").quantize(palette=palette, dither=Image.Dither.NONE)
    alpha = list(frame.getchannel("A").getdata())
    indices = list(indexed.getdata())
    for i, a in enumerate(alpha):
        if a < 128:
            indices[i] = 0
        elif indices[i] == 0:
            raise ValueError("An opaque sprite pixel mapped to the reserved transparent index")
    indexed.putdata(indices)
    indexed.info["transparency"] = 0
    return indexed

def validate_gif(path, frames, durations):
    decoded = Image.open(path)
    source_ends = []
    total = 0
    for duration in durations:
        total += duration
        source_ends.append(total)
    elapsed = 0
    mismatches = 0
    blue = 0
    decoded_frames = 0
    while True:
        rgba = decoded.convert("RGBA")
        source_index = next(i for i, end in enumerate(source_ends) if elapsed < end)
        expected_alpha = frames[source_index].getchannel("A")
        actual_alpha = rgba.getchannel("A")
        mismatches += sum((a >= 128) != (b > 0) for a, b in zip(expected_alpha.getdata(), actual_alpha.getdata()))
        blue += sum(a > 0 and b > r + 25 and b > g + 25 for r, g, b, a in rgba.getdata())
        elapsed += decoded.info.get("duration", 0)
        decoded_frames += 1
        try:
            decoded.seek(decoded.tell() + 1)
        except EOFError:
            break
    if mismatches or blue or elapsed != total:
        raise ValueError(f"{path.name}: mask={mismatches}, blue={blue}, duration={elapsed}/{total}")
    return {"frames": decoded_frames, "duration_ms": elapsed, "alpha_mask_mismatches": mismatches, "visible_blue_pixels": blue}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--atlas", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--json-out", required=True)
    args = p.parse_args()
    atlas = Image.open(args.atlas).convert("RGBA")
    if atlas.size != (1536, 2288):
        raise ValueError("Expected a v2 atlas")
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    reports = {}
    for row, (state, durations) in enumerate(DURATIONS.items()):
        frames = [atlas.crop((c * 192, row * 208, (c + 1) * 192, (row + 1) * 208)) for c in range(len(durations))]
        palette = palette_for(frames)
        indexed = [indexed_frame(frame, palette) for frame in frames]
        path = output / f"{state}.gif"
        indexed[0].save(path, save_all=True, append_images=indexed[1:], duration=durations, loop=0,
                        disposal=2, transparency=0, background=0, optimize=False)
        reports[state] = validate_gif(path, frames, durations)
        frames[0].save(output / f"{state}.webp", save_all=True, append_images=frames[1:],
                       duration=durations, loop=0, lossless=True, quality=100, method=4, exact=True)
    report = {"ok": True, "source": str(Path(args.atlas).resolve()), "alpha_threshold": 128,
              "palette": "shared per animation; index 0 reserved for transparency",
              "dither": "none", "states": reports}
    Path(args.json_out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
