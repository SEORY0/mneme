---
type: harness-contract
title: "Libfuzzer Carved File Harness"
description: "Round 7 input contract facts for libfuzzer-carved-file."
tags: ["libfuzzer-carved-file", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Carved File Harness

## Round 7 Input Contract
- The libFuzzer target consumes the first input byte as a selector, writes the remaining bytes to a
temporary file, and opens that file with H5Fopen. In this build the selector condition always takes
the H5Fopen branch.

## Round {ROUND} Format Links
- [[hdf5-file]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
