---
type: format-family
title: isobmff-compressed-box format
description: "Round 23 descriptive structure and invariant facts for isobmff-compressed-box."
resource: cybergym://format/isobmff-compressed-box
tags: ["isobmff-compressed-box", "round-23"]
okf_support: 1
train_only: true
---
# Isobmff Compressed Box Format

## Round 23 Factual Contract

### Schema / Invariants
- GPAC accepts compressed top-level ISO boxes that replace normal movie or fragment boxes. The root box header carries a replacement type and a zlib-compressed payload; after inflation, the parser treats the uncompressed bytes as the contents of the corresponding ordinary box.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
