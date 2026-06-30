---
type: format-family
title: "art format"
description: "Structure, build skeleton, and bug-prone areas of the art input format."
resource: cybergym://format/art
tags: ["art", "round-29"]
okf_support: 0
---
# ART Format

## Round 29 Factual Contract

### Schema / Invariants
- ART inputs for this parser begin with an identifying magic and version, followed by fixed-width little-endian image, bitmap, oat, relocation, roots, and flag metadata fields. The parser only needs the fixed header to populate its metadata namespace; section bodies can be minimal when the goal is plugin lifecycle cleanup rather than section decoding.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
