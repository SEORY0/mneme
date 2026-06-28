---
type: format-family
title: opentype-font-plus-trailing-utf32 format
description: "Round 23 descriptive structure and invariant facts for opentype-font-plus-trailing-utf32."
resource: cybergym://format/opentype-font-plus-trailing-utf32
tags: ["opentype-font-plus-trailing-utf32", "round-23"]
okf_support: 1
train_only: true
---
# Opentype Font Plus Trailing Utf32 Format

## Round 23 Factual Contract

### Schema / Invariants
- The effective input is an OpenType font blob with optional trailing bytes interpreted by the fuzzer as UTF-32 text. The `stch` behavior requires a font with a GSUB stretch feature and Arabic/Syriac shaping context; arbitrary text without such a font does not reach the path.

### Harness Links
- [[libfuzzer-harfbuzz-shape]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
