---
type: harness-contract
title: "Honggfuzz Libfuzzer Persistent"
description: "Round 36 factual harness contract for honggfuzz-libfuzzer-persistent."
tags: ["honggfuzz-libfuzzer-persistent", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Honggfuzz Libfuzzer Persistent

## Round 36 Input Contract
- The first chunk is consumed as card connection data. Later chunks are consumed as transmit responses, with status words stripped before parser code sees the response body. There is no FuzzedDataProvider layout or mode selector; parser progress depends on the order of the simulated smart-card conversation.

## Round 36 Format Links
- [[opensc-pkcs15-reader-chunk-stream]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
