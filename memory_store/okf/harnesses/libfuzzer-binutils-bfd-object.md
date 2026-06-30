---
type: harness-contract
title: "Libfuzzer Binutils Bfd Object Harness"
description: "Input contract facts for libfuzzer-binutils-bfd-object."
tags: ["libfuzzer-binutils-bfd-object", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Binutils Bfd Object Harness

## Round 30 Input Contract

### Input Contract
- The active binutils libFuzzer target writes the raw input bytes to a temporary file, opens it through BFD as an object, and calls BFD format recognition before the debug-file loading path. There is no leading mode byte, archive wrapper, extra integrity gate, or FuzzedDataProvider split; the PoC itself must be a complete BFD-recognized object file.

### Format Links
- [[pe-coff-bigobj]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
