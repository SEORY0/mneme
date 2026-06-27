---
type: harness-contract
title: "Libfuzzer Selabel File Compiled harness"
description: "Input contract facts for libfuzzer-selabel-file-compiled."
tags: ["libfuzzer-selabel-file-compiled", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Selabel File Compiled Harness

## Round 11 Input Contract
- The libFuzzer harness consumes a small control value from the front of the input and splits the remaining bytes around a fixed separator into multiple logical segments. There is no external file wrapper; the segment layout inside the raw buffer determines what the compiled loader sees.

## Format Links
- [[selinux-compiled-fcontext-fuzzer]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
