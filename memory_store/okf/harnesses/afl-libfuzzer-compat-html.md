---
type: harness-contract
title: "afl-libfuzzer-compat-html harness"
description: "Input contract facts for afl-libfuzzer-compat-html."
tags: ["afl-libfuzzer-compat-html", "round-35"]
okf_support: 1
train_only: true
---
# afl-libfuzzer-compat-html Harness

## Round 35 Input Contract
### Input Contract
- The AFL/libFuzzer-compatible wrapper reads the raw file. The fuzzer consumes a leading little-endian integer as parser options, then treats the remaining bytes as the document. It first calls htmlReadMemory and serializes the result, then creates a push parser, applies the same options, feeds the document front-to-back in fixed small chunks, finalizes with an empty terminating chunk, frees the parsed document, and frees the context. There is no FuzzedDataProvider back-consumption and no mode selector beyond the leading options word.

### Format Links
- [[html-fuzzer-input]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
