---
type: format-family
title: canon-ciff-crw format
description: "Round 23 descriptive structure and invariant facts for canon-ciff-crw."
resource: cybergym://format/canon-ciff-crw
tags: ["canon-ciff-crw", "round-23"]
okf_support: 1
train_only: true
---
# Canon Ciff Crw Format

## Round 23 Factual Contract

### Schema / Invariants
- CRW is parsed as a Canon CIFF tree: little-endian CIFF marker, a value-data area, and directory entries for make/model, sensor information, decoder table, and raw data. The CRW decoder requires Canon make/model discovery plus sensor dimensions and decoder table metadata before invoking the CRW decompressor.

### Harness Links
- [[libfuzzer-rawspeed-ciff-parser]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
