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
