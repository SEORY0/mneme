---
type: harness-contract
title: "Honggfuzz Compatible One Input Harfbuzz Shape Fuzzer Harness"
description: "Round 26 input contract facts for honggfuzz-compatible one-input HarfBuzz shape fuzzer."
tags: ["honggfuzz-compatible-one-input-harfbuzz-shape-fuzzer", "round-26"]
okf_support: 1
train_only: true
---
# Honggfuzz Compatible One Input Harfbuzz Shape Fuzzer Harness

## Round 26 Factual Contract

### Input Contract
- The wrapper runs the HarfBuzz shape fuzzer on the PoC path. The fuzzer creates an hb_face and hb_font from the whole input, shapes fixed ASCII and UTF-32 text, and uses trailing bytes as variation/text controls when enough data is present. There is no leading mode selector or FuzzedDataProvider layout; the primary gate is a valid OpenType font blob.

### Format Links
- [[opentype-font]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
