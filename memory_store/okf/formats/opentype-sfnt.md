---
type: format-family
title: "Opentype Sfnt Format"
description: "Input contract facts for opentype-sfnt."
tags: ["opentype-sfnt", "round-30"]
okf_support: 0
train_only: true
---
# Opentype Sfnt Format

## Round 30 Factual Contract

### Schema / Invariants
- SFNT/OpenType input begins with a font version and a table directory. Each table record names a table and gives checksum, location, and length metadata. The loader requires the basic font tables before consulting the cmap table. A cmap table starts with version and record count fields followed by encoding records containing platform, encoding, and a multi-byte subtable offset.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
