---
type: harness-contract
title: "Libfuzzer Freetype Ftfuzzer harness"
description: "Input contract facts for libfuzzer-freetype-ftfuzzer."
tags: ["libfuzzer-freetype-ftfuzzer", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Freetype Ftfuzzer Harness

## Round 11 Input Contract
- The FreeType fuzzer consumes raw font bytes, and can also process archive-style multi-file inputs in other cases. For this target path there is no front selector byte; parser reachability depends on the font container and table-directory consistency.

## Format Links
- [[cff2-opentype-variable-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 29 Input Contract

- The FreeType ftfuzzer consumes raw font bytes unless the input is an uncompressed tar archive, in which case archive members become attached font files. There is no leading selector byte. The harness first opens the font to count faces, then opens selected faces and instances; SFNT face initialization loads optional CPAL/COLR data before the glyph-loading loop.

## Round 29 Format Links
- [[opentype-truetype-sfnt-cpal]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
