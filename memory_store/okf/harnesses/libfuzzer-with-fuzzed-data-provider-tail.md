---
type: harness-contract
title: "Libfuzzer With Fuzzed Data Provider Tail Harness"
description: "Input contract facts for libfuzzer-with-fuzzed-data-provider-tail."
tags: ["libfuzzer-with-fuzzed-data-provider-tail", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Libfuzzer With Fuzzed Data Provider Tail Harness

## Round 19 Input Contract

- The harness uses FuzzedDataProvider for runtime options and then passes the remaining bytes to LibRaw as an in-memory file buffer. LLVM FuzzedDataProvider scalar consumers take data from the back, so preserving the front as the camera file and appending option bytes is the useful layout.
- Format link: [[raw-camera-dng-or-tiff-derived-buffer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
