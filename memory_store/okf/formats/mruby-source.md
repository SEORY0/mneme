---
type: format-family
title: mruby-source format
description: Format contract for mruby-source.
resource: cybergym://format/mruby-source
tags: [mruby-source]
okf_support: 1
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
