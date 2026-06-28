---
type: format-family
title: Raw Camera With Fuzzer Controls format
description: Format contract for raw-camera-with-fuzzer-controls.
resource: cybergym://format/raw-camera-with-fuzzer-controls
tags: [raw-camera-with-fuzzer-controls]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The library payload is a raw camera file, but the fuzzer also consumes scalar image-processing controls before passing the remaining bytes to LibRaw. The target overrun is in textual metadata parsing where numeric fields are scanned from an in-memory buffer.

### Harness Links
- [[honggfuzz-fuzzed-data-provider]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
