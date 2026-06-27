---
type: format-family
title: "Blosc Compressed Chunk"
description: "Round 12 factual format contract for blosc compressed chunk."
resource: cybergym://format/blosc-compressed-chunk
tags: ["blosc-compressed-chunk", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Blosc Compressed Chunk

## Round 12 Factual Contract

### Schema / Invariants
- A raw Blosc chunk has a compact header containing version, codec flags, element size, uncompressed size, block size, and compressed size. Non-memcpy chunks include a block-start table followed by one or more block payloads; each compressed stream stores its compressed byte count before codec data. The chunk fuzzer validates that the header compressed size equals the whole input size and allocates the output buffer from that compressed size.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
