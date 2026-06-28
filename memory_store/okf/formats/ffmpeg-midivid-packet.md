---
type: format-family
title: "ffmpeg-midivid-packet format"
description: "Structure and invariants for the ffmpeg-midivid-packet input format."
tags: ["ffmpeg-midivid-packet", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The packet body has an ignored leading prefix, an uncompressed flag, vector count, intra flag, a table of fixed-size vectors, then per-block vector indexes. For intra frames, the block count comes from half-resolution video dimensions.

### Harness Links
- [[afl-libfuzzer-compatible-decoder-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
