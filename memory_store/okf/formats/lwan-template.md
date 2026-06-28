---
type: format-family
title: "Lwan Template format"
description: "Structure and invariants for the lwan-template input format."
tags: ["lwan-template", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Lwan templates use mustache-like tags for escaped variables, unescaped variables, sections, inverted sections, and partial/template references. Variable names must match the descriptor table supplied by the harness; unknown or overlong lexemes are parser errors rather than expansion-time data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
