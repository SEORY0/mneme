---
type: format-family
title: opentype-sbix-font format
description: Structure and reachability facts for opentype-sbix-font inputs.
tags: [opentype-sbix-font]
okf_support: 0
---
# Opentype Sbix Font Format

## Round 10 Factual Contract

### Schema / Invariants
- An sbix font is an sfnt font with normal table directory, cmap/glyf/metrics tables, and an sbix table. The sbix table has a header, a strike offset list, and per-strike glyph image offset arrays. Subsetting must preserve enough cmap and glyph selection for the strike/glyph image path to execute.

### Harness Links
- [[libfuzzer-afl-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The input is an OpenType font with an SFNT table directory and an sbix table. The sbix table contains a version, flags, a strike count, a strike-offset array, and strike records. Each strike has PPEM/resolution fields followed by a glyph-offset array; glyph data ranges are derived from adjacent offsets and must pass monotonicity and available-length checks during subsetting.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
