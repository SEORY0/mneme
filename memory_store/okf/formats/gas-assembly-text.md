---
type: format-family
title: "gas-assembly-text format"
description: "Structure and reachability facts for GAS assembly text."
resource: cybergym://format/gas-assembly-text
tags: ["gas-assembly-text"]
okf_support: 1
---
# GAS Assembly Text Format

## Round 9 Factual Contract

### Schema / Invariants
- GAS assembly text is line-oriented.
- A `.macro` directive starts a macro definition, `.endm` terminates it, and a later line matching
  the macro name expands its body.
- Empty and whitespace-only macro bodies are accepted far enough to reach macro setup and input-
  scrub handling.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
