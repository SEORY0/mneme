---
type: harness-contract
title: "Honggfuzz Libfuzzer Compatible Harness"
description: "Input contract facts for honggfuzz/libfuzzer-compatible."
tags: ["honggfuzz-libfuzzer-compatible", "round-12"]
okf_support: 0
train_only: true
---
# Honggfuzz Libfuzzer Compatible Harness

## Round 12 Input Contract
- The harness rejects short inputs, consumes selector bytes for parser type, time fields, time retention, optional fixed key typecasts, and optional decoder setup, then passes the remaining bytes to flb_parser_do. Decoder and typecast selectors can consume bytes that otherwise look like record content.

## Round 12 Format Links
- [[fluent-bit-parser-fuzzer-control-plus-json]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
