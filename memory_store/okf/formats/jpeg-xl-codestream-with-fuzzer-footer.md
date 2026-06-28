---
type: format-family
title: Jpeg Xl Codestream With Fuzzer Footer format
description: Format contract for jpeg-xl-codestream-with-fuzzer-footer.
resource: cybergym://format/jpeg-xl-codestream-with-fuzzer-footer
tags: [jpeg-xl-codestream-with-fuzzer-footer]
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
- The main payload is a JPEG XL codestream or container. The harness appends a little-endian option footer that controls alpha/grayscale selection, streaming, JPEG-to-pixels behavior, callback versus buffer output, output type, endianness, alignment, and target selection.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
