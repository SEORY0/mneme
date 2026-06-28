---
type: format-family
title: dng-tiff format
description: "Round 23 descriptive structure and invariant facts for dng-tiff."
resource: cybergym://format/dng-tiff
tags: ["dng-tiff", "round-23"]
okf_support: 1
train_only: true
---
# Dng Tiff Format

## Round 23 Factual Contract

### Schema / Invariants
- DNG is TIFF-based. OpcodeList entries are stored as a count followed by opcode records; DNG opcode payloads are big-endian even when the enclosing TIFF is little-endian. FixBadPixelsList contains a phase field, point and rectangle counts, then point pairs and rectangle bounds that expand into bad-pixel positions.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
