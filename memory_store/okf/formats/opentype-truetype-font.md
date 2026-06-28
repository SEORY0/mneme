---
type: format-family
title: opentype-truetype-font format
description: Structure and reachability facts for opentype-truetype-font inputs.
tags: [opentype-truetype-font]
okf_support: 1
---
# Opentype Truetype Font Format

## Round 10 Factual Contract

### Schema / Invariants
- The input is an sfnt font blob with table directory and glyf/loca/hmtx relationships preserved. Appended bytes can influence fuzzer-controlled shaping text or variation coordinates, but corrupting top-level table structure usually prevents the glyf path from being useful.

### Harness Links
- [[libfuzzer-harfbuzz-shape-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- An sfnt font has a header, table directory, and independently tagged tables. In TrueType outlines, glyph parsing depends on location data and maximum-profile metrics; a version mismatch in the maximum-profile table can leave fields absent even though glyph and location tables are still present. Directory-integrity fields may need to remain coherent for OTS to parse the mutated font deeply.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
