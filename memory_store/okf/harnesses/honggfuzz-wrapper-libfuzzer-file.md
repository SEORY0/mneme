---
type: harness-contract
title: "Honggfuzz Wrapper Libfuzzer File Harness"
description: "Input contract facts for honggfuzz-wrapper-libfuzzer-file."
tags: ["honggfuzz-wrapper-libfuzzer-file", "round-37", "harness-contract"]
okf_support: 1
train_only: true
---
# Honggfuzz Wrapper Libfuzzer File Harness
## Round 37 Input Contract

### Input Contract
- The harness writes the raw input bytes to a temporary GML file and calls the GML reader on that file; there is no FuzzedDataProvider split or mode selector.
- The local wrapper can print honggfuzz usage text even when direct container execution and official submit drive the file through the parser, so the official vulnerable/fixed split is the reliable oracle.

### Format Links
- [[gml]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
