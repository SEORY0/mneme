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

## Round 30 Input Contract

### Input Contract
- The ftfuzzer libFuzzer target consumes the PoC as raw bytes. It first tries to parse the raw bytes as an uncompressed tar archive and otherwise treats the whole byte stream as one font file. It opens the font from memory to enumerate faces, then opens each face and named instance, optionally attaches additional archive members, sets an outline size, sets intermediate variation coordinates for non-instance variable faces, and calls FT_Load_Glyph over all glyphs. There is no FuzzedDataProvider layout, prefix selector, or checksum trailer outside the font format itself.

### Format Links
- [[opentype-cff2-font]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
