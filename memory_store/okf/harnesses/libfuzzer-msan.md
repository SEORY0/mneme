---
type: harness-contract
title: "Libfuzzer Msan harness"
description: "Input contract facts for libfuzzer-msan."
tags: ["libfuzzer-msan", "round-9"]
okf_support: 1
---
# Libfuzzer Msan Harness

## Round 9 Input Contract
- The libFuzzer target is built with MemorySanitizer and a custom mutator.
- The wrapper invokes cryptofuzz-libecc directly on the raw input; operation dispatch is internal to
  the cryptofuzz datasource rather than a simple leading text command.

## Round 9 Format Links
- [[cryptofuzz-binary-operation-stream]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
