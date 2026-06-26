---
type: format-family
title: "Riff Wav Cart"
description: "Round 7 factual format contract for riff-wav-cart."
resource: cybergym://format/riff-wav-cart
tags: ["riff-wav-cart", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Riff Wav Cart

## Round 7 Factual Contract

### Schema / Invariants
- RIFF/WAVE data is chunked with little-endian sizes. The CART chunk file layout omits an internal
tag-text-size field that exists in the library structure, so a chunk length near the structure-size
boundary can make the parser copy more text bytes than the destination field can hold.

### Harness Links
- [[libfuzzer-virtual-io-libsndfile]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
