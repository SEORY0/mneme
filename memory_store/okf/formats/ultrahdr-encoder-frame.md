---
type: format-family
title: Ultrahdr Encoder Frame format
description: Format contract for ultrahdr-encoder-frame.
resource: cybergym://format/ultrahdr-encoder-frame
tags: [ultrahdr-encoder-frame]
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
- The fuzzer input is not a serialized UltraHDR file. It is a control stream consumed by the harness to synthesize raw image buffers, dimensions, quality, transfer metadata, and encoder mode before invoking the library.

### Harness Links
- [[libfuzzer-fuzzed-data-provider]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
