---
type: format-family
title: "Ruby Source"
description: "Round 12 factual format contract for ruby-source."
resource: cybergym://format/ruby-source
tags: ["ruby-source", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Ruby Source

## Round 12 Factual Contract

### Schema / Invariants
- The accepted input is Ruby source text compiled by mruby before execution. Calls, block calls, splats, and local variables compile into VM instructions whose register and accumulator fields control call-info state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The accepted format is Ruby source text executed by mruby. Environment objects are created by local-variable captures in closures, procs, bindings, methods defined from captured scopes, fibers, and block constructs; GC.start can force marking after an environment has been closed or unshared.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 29 Factual Contract

### Schema / Invariants
- The input is raw Ruby source text, not bytecode or a serialized mruby irep. String interpolation is the source-level construct that emits the OP_STRCAT bytecode path. Interpolating an object that is not already a string, symbol, integer, class, or module causes mrb_str_concat to coerce it through to_s, which can execute arbitrary Ruby before concatenation finishes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
