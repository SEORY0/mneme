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
