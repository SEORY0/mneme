---
type: format-family
title: "Javascript Source"
description: "Round 12 factual format contract for javascript-source."
resource: cybergym://format/javascript-source
tags: ["javascript-source", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Javascript Source

## Round 12 Factual Contract

### Schema / Invariants
- The input is plain JavaScript source text. It must parse successfully and run far enough to allocate many objects or arrays so the runtime enters garbage collection.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
