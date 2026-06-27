---
type: format-family
title: "Raw Lzxpress Roundtrip Plain Bytes"
description: "Round 12 factual format contract for raw-lzxpress-roundtrip-plain-bytes."
resource: cybergym://format/raw-lzxpress-roundtrip-plain-bytes
tags: ["raw-lzxpress-roundtrip-plain-bytes", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Raw Lzxpress Roundtrip Plain Bytes

## Round 12 Factual Contract

### Schema / Invariants
- The fuzzer input is the uncompressed byte string. The target compresses it with LZXpress into an internal compressed buffer, immediately decompresses the result into an internal output buffer, and checks size and byte equality.

### Harness Links
- [[honggfuzz-style-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
