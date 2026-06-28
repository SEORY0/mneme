---
type: harness-contract
title: "Libfuzzer Execute harness"
description: "Input contract facts for libfuzzer-execute."
tags: ["libfuzzer-execute", "round-9"]
okf_support: 1
---
# Libfuzzer Execute Harness

## Round 9 Input Contract
- LibFuzzer feeds the input directly as a PHP request body to the execute fuzzer.
- The harness compiles and executes the source, enforces a step budget, rejects very large source
  inputs, and wraps internal calls to limit very large string arguments, but it does not carve mode
  bytes from the input.

## Round 9 Format Links
- [[php-script]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
