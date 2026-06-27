---
type: harness-contract
title: "Libfuzzer Php Function Jit harness"
description: "Input contract facts for libfuzzer-php-function-jit."
tags: ["libfuzzer-php-function-jit", "round-15"]
okf_support: 1
---
# Libfuzzer Php Function Jit Harness

## Round 15 Input Contract
- The selected target is the PHP function-JIT fuzzer. It runs the same script first with JIT disabled
  to detect bailout, invalidates OPcache state, and then reruns with function JIT enabled if the first
  run did not bail out. Inputs are capped in size and passed as raw request source for a fixed
  temporary filename.

## Format Links
- [[php-script]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
