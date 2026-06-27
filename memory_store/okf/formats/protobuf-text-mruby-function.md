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

## Round 14 Factual Contract

### Schema / Invariants
- The input is protobuf text for a Ruby AST-like Function message. The converter emits a Ruby method wrapper, scoped begin blocks, sequential variable assignments, constants, variable references, and binary operators. Variable references are modulo the current live variable count, so assignments must establish live operands before later expressions can use them.

### Harness Links
- [[libfuzzer-libprotobuf-mutator]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
