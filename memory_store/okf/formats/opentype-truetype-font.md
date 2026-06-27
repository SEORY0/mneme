---
type: format-family
title: opentype-truetype-font format
description: Structure and reachability facts for opentype-truetype-font inputs.
tags: [opentype-truetype-font]
okf_support: 0
---
# Opentype Truetype Font Format

## Round 10 Factual Contract

### Schema / Invariants
- The input is an sfnt font blob with table directory and glyf/loca/hmtx relationships preserved. Appended bytes can influence fuzzer-controlled shaping text or variation coordinates, but corrupting top-level table structure usually prevents the glyf path from being useful.

### Harness Links
- [[libfuzzer-harfbuzz-shape-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
