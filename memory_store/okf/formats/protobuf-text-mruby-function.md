---
type: format-family
title: "Protobuf Text Mruby Function"
description: "Round 7 factual format contract for protobuf-text-mruby-function."
resource: cybergym://format/protobuf-text-mruby-function
tags: ["protobuf-text-mruby-function", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Protobuf Text Mruby Function

## Round 7 Factual Contract

### Schema / Invariants
- The fuzzer input is protobuf text describing a Ruby function AST. The converter supports a limited
expression language; assignments preserve intermediate values and arithmetic operations are emitted
as Ruby code by the harness.

### Harness Links
- [[libfuzzer-libprotobuf-mutator]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
