---
type: harness-contract
title: "Honggfuzz Raw Bytes Harness"
description: "Round 7 input contract facts for honggfuzz-raw-bytes."
tags: ["honggfuzz-raw-bytes", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Honggfuzz Raw Bytes Harness

## Round 7 Input Contract
- The honggfuzz wrapper invokes the named-argument fmt fuzzer on raw file bytes. Invalid format
strings and many formatting exceptions are handled by the harness as clean exits rather than
crashes.

## Round {ROUND} Format Links
- [[fmt-named-argument-fuzzer-buffer]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 36 Input Contract
- The active wrapper invokes the named-argument fmt fuzzer on the raw submitted bytes. There is no FuzzedDataProvider layout, external length prefix, integrity field, or multi-file container. The fuzzer catches standard formatting exceptions, so a useful PoC must produce an abort or sanitizer finding rather than an ordinary format_error.

## Round 36 Format Links
- [[fmt-named-argument-fuzzer-buffer]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
