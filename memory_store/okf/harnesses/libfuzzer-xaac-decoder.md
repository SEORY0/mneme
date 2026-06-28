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

## Round 17 Input Contract
- The XAAC libFuzzer harness feeds the whole input buffer to the decoder setup/decode path; there is no separate FuzzedDataProvider layout in the PoC.
- A local seed corpus existed and was used for mutation, but official submit showed the vulnerable build stayed clean.

## Round 17 Format Links
- [[aac-xaac-decoder-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[aac-xaac-decoder-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
