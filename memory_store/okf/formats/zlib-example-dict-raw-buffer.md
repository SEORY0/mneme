---
type: format-family
title: "Zlib Example Dict RAW Buffer Format"
description: "Round 26 descriptive structure and invariant facts for zlib-example-dict-raw-buffer."
tags: ["zlib-example-dict-raw-buffer", "round-26"]
okf_support: 1
train_only: true
---
# Zlib Example Dict RAW Buffer Format

## Round 26 Factual Contract

### Schema / Invariants
- The input is not a zlib stream. It is a raw byte buffer consumed by the example dictionary fuzzer. The leading byte controls dictionary length and deflateInit2 parameters; the remaining bytes are compressed by the harness and then inflated for comparison.

### Harness Links
- [[libfuzzer-zlib-example-dict-fuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
