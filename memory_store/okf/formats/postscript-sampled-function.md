---
type: format-family
title: "postscript-sampled-function format"
description: "Descriptive format contract facts for postscript-sampled-function."
tags: ["postscript-sampled-function", "round-18"]
okf_support: 1
train_only: true
---
# Postscript Sampled Function Format

## Round 18 Factual Contract

### Schema / Invariants
- The relevant PostScript object is a sampled function dictionary or stream with FunctionType 0-style parameters. The target condition requires function evaluation to consume more operands than the operand stack provides, throw an error, and then resume with stale completion state.

### Harness Links
- [[libfuzzer-ghostscript-gstoraster]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
