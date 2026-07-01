---
type: format-family
title: "Raw Blosc Compress Buffer"
description: "Round 36 factual format contract for raw-blosc-compress-buffer."
tags: ["raw-blosc-compress-buffer", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Raw Blosc Compress Buffer

## Round 36 Factual Contract

### Schema / Invariants
- The compressed output Blosc builds from this raw source has a compact header, a block-start table, then per-block stream records. Each stream record begins with a stored compressed-size token. A negative size token represents a repeated-byte run, while uncompressible data may be stored as a raw copied stream if the remaining destination budget can hold it. There is no file wrapper or checksum in the fuzzer input; the source bytes themselves drive compression.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
