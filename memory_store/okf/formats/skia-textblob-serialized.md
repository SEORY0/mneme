---
type: format-family
title: "Skia Textblob Serialized format"
description: "Round 28 descriptive format facts for skia-textblob-serialized."
resource: cybergym://format/skia-textblob-serialized
tags: ["skia-textblob-serialized", "round-28"]
okf_support: 0
---
# Skia Textblob Serialized Format

## Round 28 Factual Contract

### Schema / Invariants
- A serialized SkTextBlob begins with rectangle bounds, followed by repeated runs and a zero-glyph-count end marker. Each run stores a glyph count, a packed positioning/extended flag word, optional text byte count, a point offset, a flattened paint, then length-prefixed glyph and position byte arrays, plus cluster and text arrays for extended runs. The paint must deserialize with glyph-id text encoding for the builder to allocate a run. The top-level size must be word-aligned for SkReadBuffer to accept the input.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
