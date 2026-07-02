---
type: harness-contract
title: "Afl Libfuzzer Compatible Libfuzzer Whole Buffer Frame Decompressor"
description: "Abstract harness facts observed during verifier-causal consolidation."
tags: ["afl-libfuzzer-compatible-libfuzzer-whole-buffer-frame-decompressor", "harness_contract"]
okf_support: 0
---
# Afl Libfuzzer Compatible Libfuzzer Whole Buffer Frame Decompressor

## Notes
- These are descriptive harness facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The AFL++ wrapper drives a libFuzzer-style decompress-frame target over the whole PoC file. There is no leading selector and no FuzzedDataProvider carving. The target passes the raw bytes to the in-memory frame loader, allocates from the parsed uncompressed size when the frame opens, iterates frame chunk decompression, and finally frees the reconstructed super-chunk.

### Format Links
- [[c-blosc2-frame]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
