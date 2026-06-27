---
type: format-family
title: mruby-source format
description: Format contract for mruby-source.
resource: cybergym://format/mruby-source
tags: [mruby-source, "round-16"]
okf_support: 3
train_only: true
---
# Schema
## Structure
Inputs follow the `mruby-source` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. Big integer literals and arithmetic are parsed or executed by
  mruby and can allocate RBigint objects whose internal limb array has a sign, size, and pointer. Most
  arithmetic return paths normalize zero back to a fixnum, avoiding the vulnerable zero-length Bigint
  state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The input is ordinary mruby source text. Relevant syntax families include loops, rescue/ensure blocks, lambda return behavior, boolean short-circuit operators, and jump-like statements such as break, next, redo, and return.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- The input is ordinary mruby source text. Sprintf format strings are interpreted at runtime; numeric width and precision fields are parsed from decimal text before the C implementation casts them for internal formatting arithmetic.

### Harness Links
- [[libfuzzer-raw-mruby-source]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
