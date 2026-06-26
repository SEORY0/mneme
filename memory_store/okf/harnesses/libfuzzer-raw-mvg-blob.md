---
type: harness-contract
title: "Libfuzzer Raw MVG Blob harness"
description: "Input contract facts for Libfuzzer Raw MVG Blob."
tags: ["libfuzzer-raw-mvg-blob", "round-6"]
okf_support: 1
---
# Libfuzzer Raw MVG Blob Harness

## Round 6 Input Contract
- The GraphicsMagick coder fuzzer feeds the entire file as raw bytes to the MVG coder. There is no leading selector byte or FuzzedDataProvider splitting; the first accepted MVG header line is the main parser gate.

## Format Links
- [[mvg]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
