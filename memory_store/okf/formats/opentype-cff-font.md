---
type: format-family
title: "Opentype CFF Font format"
description: "Round 8 descriptive format facts for OpenType/CFF font."
resource: cybergym://format/opentype-cff-font
tags: ["opentype-cff-font", "round-8"]
okf_support: 1
---
# Opentype CFF Font Format

## Round 8 Factual Contract

### Schema / Invariants
- The harness consumes a complete font file. OpenType/CFF inputs must preserve the sfnt directory and CFF table structure well enough for HarfBuzz to instantiate a face before charset handling is reached; arbitrary truncation is filtered before the target code.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

