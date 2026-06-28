---
type: format-family
title: palm-pdb-image format
description: Structure and reachability facts for palm-pdb-image inputs.
tags: [palm-pdb-image]
okf_support: 0
---
# Palm Pdb Image Format

## Round 10 Factual Contract

### Schema / Invariants
- Palm/PDB images carry a database-style header followed by image metadata and scanline payloads. Low-bit-depth grayscale variants require row padding and bit packing, while scanline/RLE variants add per-row encoding rules.

### Harness Links
- [[libfuzzer-image-coder-roundtrip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
