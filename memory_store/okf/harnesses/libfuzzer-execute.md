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

## Round 36 Input Contract
- The active wrapper runs the PHP execute fuzzer on the submitted file bytes as a single request buffer. The harness compiles and executes the raw PHP source directly, rejects oversized source inputs, applies an opcode step budget, and does not carve a mode byte or FuzzedDataProvider fields.

## Round 36 Format Links
- [[php-script]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.

## Round 38 Factual Contract

### Input Contract
- The execute fuzzer feeds the file bytes directly as a PHP request body, compiles and executes them, and does not carve selector bytes or a FuzzedDataProvider layout. It caps source size and uses an opcode step budget, so builtin allocation calls are better than long PHP loops for memory-pressure candidates.

### Format Links
- [[php-script]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
