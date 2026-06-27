---
type: format-family
title: "Openexr format"
description: "Descriptive contract facts for openexr."
resource: "cybergym://format/openexr"
tags: ["openexr", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- OpenEXR starts with magic and version, then a sequence of typed attributes terminated by an empty name, followed by chunk offset tables.
- Scanline and tiled files store different chunk-table counts and chunk records.
- Chunk offsets are little-endian 64-bit file positions in normal single-part files.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
