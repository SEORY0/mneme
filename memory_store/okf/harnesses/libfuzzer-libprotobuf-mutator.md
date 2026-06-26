---
type: harness-contract
title: "Libfuzzer Libprotobuf Mutator Harness"
description: "Round 7 input contract facts for libfuzzer-libprotobuf-mutator."
tags: ["libfuzzer-libprotobuf-mutator", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Libprotobuf Mutator Harness

## Round 7 Input Contract
- The active binary parses protobuf text and converts it to Ruby before executing mruby. Raw Ruby text
is treated as bad input for this harness, so the PoC must satisfy the proto schema first.

## Round {ROUND} Format Links
- [[protobuf-text-mruby-function]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
