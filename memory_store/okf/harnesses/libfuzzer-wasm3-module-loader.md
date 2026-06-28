---
type: harness-contract
title: "Libfuzzer Wasm3 Module Loader harness"
description: "Input contract facts for Libfuzzer Wasm3 Module Loader."
tags: ["libfuzzer-wasm3-module-loader", "round-6"]
okf_support: 1
---
# Libfuzzer Wasm3 Module Loader Harness

## Round 6 Input Contract
- The libFuzzer harness feeds raw bytes to `m3_ParseModule`, loads the module into a runtime with a small stack, looks up an exported `fib` function, and calls it. Data/global initialization expressions are evaluated during module loading before the exported call.

## Format Links
- [[wasm]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
