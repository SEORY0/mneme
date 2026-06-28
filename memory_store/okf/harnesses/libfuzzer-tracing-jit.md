---
type: harness-contract
title: "Libfuzzer Tracing Jit Harness"
description: "Input contract facts for libfuzzer-tracing-jit."
tags: ["libfuzzer-tracing-jit", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Libfuzzer Tracing Jit Harness

## Round 19 Input Contract

- The libFuzzer tracing-JIT harness treats raw bytes as PHP source with a size cap. It first runs with JIT disabled to reject scripts that bail out, then enables tracing JIT and runs the script repeatedly with hot counters configured to trigger quickly.
- Format link: [[php-source]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
