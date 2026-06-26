---
type: harness-contract
title: "File Fuzzer Karchive Multi Archive Harness"
description: "Round 7 input contract facts for file-fuzzer-karchive-multi-archive."
tags: ["file-fuzzer-karchive-multi-archive", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# File Fuzzer Karchive Multi Archive Harness

## Round 7 Input Contract
- The harness feeds the raw file bytes through several KArchive handlers. No mode byte or
FuzzedDataProvider layout is carved from the input; parser reachability depends on the archive magic
and member header fields.

## Round {ROUND} Format Links
- [[ar-archive]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
