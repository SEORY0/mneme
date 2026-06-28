---
type: format-family
title: "pgm format"
description: "Structure and invariants observed for pgm."
resource: "cybergym://format/pgm"
tags: ["pgm", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- PGM uses a magic selecting ASCII or raw graymap, textual width and height fields, and a max-value field before pixel data. The loader bounds individual dimensions, stores them in a small integer type, then compares the number of decoded pixels with the expected product.

### Harness Links
- [[libfuzzer-raw-bytes]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
