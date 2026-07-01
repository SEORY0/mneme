---
type: harness-contract
title: "Afl Libfuzzer File Fuzzer"
description: "Round 36 factual harness contract for afl-libfuzzer-file-fuzzer."
tags: ["afl-libfuzzer-file-fuzzer", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer File Fuzzer

## Round 36 Input Contract
- The harness consumes the complete input as raw HEIF file bytes through the libheif file fuzzer. It does not use a mode selector or FuzzedDataProvider carving; it checks the file type, opens the memory-backed context, then decodes primary and top-level images into a fixed output colorspace.

## Round 36 Format Links
- [[heif-isobmff]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
