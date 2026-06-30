---
type: harness-contract
title: "Libfuzzer Djxl Harness"
description: "Input contract facts for libfuzzer-djxl."
tags: ["libfuzzer-djxl", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Djxl Harness

## Round 30 Input Contract

### Input Contract
- The selected djxl fuzzer treats the final four input bytes as little-endian decoder-option flags and decodes all preceding bytes as the JPEG XL input. There is no FuzzedDataProvider layout, checksum wrapper, or leading mode byte; seed replay must append a separate flag tail so the codestream itself is not truncated.

### Format Links
- [[jpeg-xl-codestream]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
