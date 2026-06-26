---
type: format-family
title: "Binutils Disassembler Fuzz Frame format"
description: "Descriptive contract facts for Binutils Disassembler Fuzz Frame."
resource: "cybergym://format/binutils-disassembler-fuzz-frame"
tags: ["binutils-disassembler-fuzz-frame", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The fuzz frame begins with a fixed-size NUL-terminated option string, followed by bytes that the harness carves into a small header, instruction stream, and trailing architecture controls. CDE printing is reached only when Thumb mode and a CDE coprocessor option are active.

### Harness Links
- [[libfuzzer-carved-option-prefix-plus-instruction-buffer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
