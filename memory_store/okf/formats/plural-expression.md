---
type: format-family
title: Plural Expression format
description: Format contract for plural-expression.
resource: cybergym://format/plural-expression
tags: [plural-expression]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The input is a Wt plural-expression string accepted by a C-like expression parser over variable n. Invalid syntax and unsafe arithmetic throw exceptions that are caught in the fuzz helper.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
