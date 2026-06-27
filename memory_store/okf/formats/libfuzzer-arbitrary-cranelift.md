---
type: format-family
title: libfuzzer-arbitrary-cranelift format
description: Format contract for libfuzzer-arbitrary-cranelift.
resource: cybergym://format/libfuzzer-arbitrary-cranelift
tags: [libfuzzer-arbitrary-cranelift]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `libfuzzer-arbitrary-cranelift` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The Cranelift fuzz targets deserialize structured generator choices from the raw libFuzzer byte
  stream using the Rust Arbitrary API. The cranelift-fuzzgen target builds functions, inputs, ISA
  options, and run/compare settings from those choices rather than reading textual CLIF or WebAssembly
  modules.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
