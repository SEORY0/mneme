---
type: harness-contract
title: "Libfuzzer Zlib Example Dict Fuzzer Harness"
description: "Round 26 input contract facts for libfuzzer-zlib-example_dict_fuzzer."
tags: ["libfuzzer-zlib-example-dict-fuzzer", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Zlib Example Dict Fuzzer Harness

## Round 26 Factual Contract

### Input Contract
- The active libFuzzer binary is the zlib example dictionary fuzzer. It rejects empty and oversized inputs, derives compression level, window bits, memory level, strategy, and dictionary length from the first input byte, then compresses and inflates the same raw input. There is no carved trailer or FuzzedDataProvider layout.

### Format Links
- [[zlib-example-dict-raw-buffer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
