---
type: format-family
title: "elf-crx-object format"
description: "Structure and invariants for the elf-crx-object input format."
tags: ["elf-crx-object", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input must be a BFD-recognized object with the CRX ELF machine type and an executable text section; raw CRX instruction bytes alone do not select the CRX disassembler. CRX instructions are decoded from little-endian halfwords, and table matches are made against the high bits of the assembled instruction word.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
