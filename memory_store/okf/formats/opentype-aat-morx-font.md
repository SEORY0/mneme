---
type: format-family
title: opentype-aat-morx-font format
description: Structure and reachability facts for opentype-aat-morx-font inputs.
tags: [opentype-aat-morx-font]
okf_support: 0
---
# Opentype Aat Morx Font Format

## Round 10 Factual Contract

### Schema / Invariants
- AAT morx fonts are ordinary sfnt fonts with a table directory and a morx table containing chains, subtables, state tables, entries, and substitution table references. Contextual subtables require both a valid state machine and glyph text that drives an entry using mark or current substitution indices.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
