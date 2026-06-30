---
type: format-family
title: "Jxl Format"
description: "Input contract facts for jxl."
tags: ["jxl", "round-30"]
okf_support: 0
train_only: true
---
# Jxl Format

## Round 30 Factual Contract

### Schema / Invariants
- The accepted input is a raw JPEG XL codestream for djxl_fuzzer, with fuzzer option bits appended at the tail. JPEG-derived YCbCr codestreams preserve chroma subsampling metadata and drive the decoder's YCbCr upsampling path; plain RGB/Y4M VarDCT encoding is rejected in this revision, while modular lossless YCbCr does not hit this reconstruction edge path.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
