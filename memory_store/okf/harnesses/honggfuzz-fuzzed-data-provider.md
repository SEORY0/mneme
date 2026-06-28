---
type: harness-contract
title: "Honggfuzz Fuzzed Data Provider harness"
description: "Input contract facts for honggfuzz-fuzzed-data-provider."
tags: ["honggfuzz-fuzzed-data-provider", "round-25"]
okf_support: 0
---
# Honggfuzz Fuzzed Data Provider Harness

## Round 25 Input Contract
- The target consumes fuzz bytes through a FuzzedDataProvider-like control phase, then passes the remaining byte span to LibRaw open_buffer, unpack, and multiple processing modes. Candidate layout matters: control bytes must be arranged so the remaining span still begins with a valid raw-camera file.

## Round 25 Format Links
- [[raw-camera-with-fuzzer-controls]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
