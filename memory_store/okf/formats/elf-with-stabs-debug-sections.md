---
type: format-family
title: "elf-with-stabs-debug-sections format"
description: "Structure and invariants for the elf-with-stabs-debug-sections input format."
tags: ["elf-with-stabs-debug-sections", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- Stabs debug information uses fixed-size records with a string-table index, type, descriptor, and value. BFD looks for .stab and .stabstr sections, loads both contents, optionally canonicalizes relocations against the stabs section, and builds a function index from source-file and function stabs.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
