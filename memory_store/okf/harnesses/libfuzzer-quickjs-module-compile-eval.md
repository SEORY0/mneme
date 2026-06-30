---
type: harness-contract
title: "Libfuzzer Quickjs Module Compile Eval harness"
description: "Input contract facts for libfuzzer-quickjs-module-compile-eval."
tags: ["libfuzzer-quickjs-module-compile-eval", "round-31"]
okf_support: 1
train_only: true
---
# Libfuzzer Quickjs Module Compile Eval Harness

## Round 31 Input Contract

### Input Contract
- The active libFuzzer target is the compile/evaluate harness. It rejects inputs missing the required trailing terminator, then treats all preceding bytes as JavaScript source. It compiles with module flags, serializes the module to bytecode, deserializes it in the same context, resolves module imports, sets import.meta for modules, evaluates the resulting function, and then drains the standard job loop for non-exception results. There is no FuzzedDataProvider split, mode selector, or external multi-file PoC contract.

### Format Links
- [[javascript-module-source]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
