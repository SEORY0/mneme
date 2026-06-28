---
type: format-family
title: Python Source Expression format
description: Format contract for python-source-expression.
resource: cybergym://format/python-source-expression
tags: [python-source-expression]
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
- The observed input is Python source text for literal evaluation, terminated so the C API can build a Unicode string. Valid carriers are Python literals such as lists, tuples, constants, and nested literal containers.

### Harness Links
- [[libfuzzer-cpython-ast-literal-eval]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
