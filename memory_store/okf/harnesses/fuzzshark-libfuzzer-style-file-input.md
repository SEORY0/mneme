---
type: harness-contract
title: "Fuzzshark Libfuzzer Style File Input harness"
description: "Input contract facts for fuzzshark-libfuzzer-style-file-input."
tags: ["fuzzshark-libfuzzer-style-file-input", "round-20"]
okf_support: 1
---
# Fuzzshark Libfuzzer Style File Input Harness

## Round 20 Input Contract
- The extracted harness initializes epan, preferences, and a target dissector handle, then dissects frames from the supplied file bytes through fuzzshark. There is no observed FuzzedDataProvider split in the task source read.

## Round 20 Format Links
- [[wireshark-fuzzshark-capture-dissector-input]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
