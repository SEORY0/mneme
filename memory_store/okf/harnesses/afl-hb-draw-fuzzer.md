---
type: harness-contract
title: "Afl Hb Draw Fuzzer harness"
description: "Input contract facts for Afl Hb Draw Fuzzer."
tags: ["afl-hb-draw-fuzzer", "round-21"]
okf_support: 1
---
# Afl Hb Draw Fuzzer Harness

## Round 21 Input Contract (opentype-variable-font)

- The active HarfBuzz target is hb-draw-fuzzer. It consumes the whole input as a font blob, derives normalized variation coordinates from trailing bytes, caps drawing to early glyph ids, and calls hb_font_draw_glyph for each selected glyph.

## Round 21 Format Links (opentype-variable-font)
- [[opentype-variable-font]]

## Round 21 Notes (opentype-variable-font)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 35 Input Contract

### Input Contract
- The active HarfBuzz target is hb-draw-fuzzer. It consumes the whole input as a raw font blob, creates an hb_face and hb_font, derives normalized variation coordinates from trailing input bytes, caps drawing to early glyph ids, and calls hb_font_draw_glyph for each selected glyph. There is no FuzzedDataProvider split, checksum wrapper, or leading mode selector outside the font format.

### Format Links
- [[opentype-variable-font]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
