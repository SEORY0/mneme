---
type: format-family
title: "Opensc Fuzz Card Chunk Stream Format"
description: "Input contract facts for opensc-fuzz-card-chunk-stream."
tags: ["opensc-fuzz-card-chunk-stream", "round-30"]
okf_support: 0
train_only: true
---
# Opensc Fuzz Card Chunk Stream Format

## Round 30 Factual Contract

### Schema / Invariants
- The card fuzzer input starts with a native unsigned-long flag and one byte used as a challenge length. The remaining bytes are the OpenSC fuzz-reader chunk stream: a two-byte little-endian chunk length followed by chunk data. The first chunk is the ATR, and later chunks are consumed as APDU responses with trailing status bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
