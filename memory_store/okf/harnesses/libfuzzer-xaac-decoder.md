---
type: harness-contract
title: "libfuzzer-xaac-decoder harness"
description: "Input contract facts for libfuzzer-xaac-decoder."
tags: ["libfuzzer-xaac-decoder", "round-14"]
okf_support: 1
---
# Libfuzzer Xaac Decoder Harness

## Round 14 Input Contract
- The xaac decoder fuzzer consumes the raw byte stream directly as an AAC decoder input. There is no filename envelope or FuzzedDataProvider split; valid sync/config bits are needed before DRC preselection code is reached.

## Round 14 Format Links
- [[aac-usac-bitstream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
