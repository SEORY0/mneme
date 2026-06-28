---
type: harness-contract
title: "Libfuzzer Compatible harness"
description: "Input contract facts for libfuzzer-compatible."
tags: ["libfuzzer-compatible"]
okf_support: 0
---
# Libfuzzer Compatible Harness

## Round 10 Input Contract
- The harness rejects very small or oversized inputs, reads architecture metadata from the end of the raw file, then repeatedly calls the selected binutils disassembler over the body bytes. Fuzzing the body without a matching CGEN architecture/machine selector stays off the target path.

## Round 10 Format Links
- [[binutils-disassembler-fuzzer-input]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
