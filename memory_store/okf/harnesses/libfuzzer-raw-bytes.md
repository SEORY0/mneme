---
type: harness-contract
title: "Libfuzzer Raw Bytes Harness"
description: "Round 7 input contract facts for libfuzzer-raw-bytes."
tags: ["libfuzzer-raw-bytes", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Bytes Harness

## Round 7 Input Contract
- LibFuzzer calls the entrypoint with raw file bytes and a size. The vulnerable entrypoint declaration
uses a character pointer where libFuzzer expects a byte pointer, producing a callback ABI/type
mismatch.

## Round {ROUND} Format Links
- [[yara-rule-text]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
