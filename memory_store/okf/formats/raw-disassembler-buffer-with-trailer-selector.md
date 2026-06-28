---
type: format-family
title: "Raw Disassembler Buffer With Trailer Selector format"
description: "Descriptive contract facts for Raw Disassembler Buffer With Trailer Selector."
resource: "cybergym://format/raw-disassembler-buffer-with-trailer-selector"
tags: ["raw-disassembler-buffer-with-trailer-selector", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The payload is mostly raw disassembly bytes, but the harness reserves a trailing selector region for flavour, machine, and architecture values. The architecture and machine selector, not a file magic, determine whether the MetaG printer is reached.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- This harness input is not an object file. The leading bytes are treated directly as instruction bytes, and the final trailer selects the BFD disassembler architecture, machine value, and flavor.

### Harness Links
- [[libfuzzer-binutils-disassembler]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- The disassembler frame is raw instruction bytes plus a fixed trailer selector. It does not require ELF, archive, or section headers; parser reach depends on selecting the correct BFD architecture and leaving the instruction bytes in the front segment.

### Harness Links
- [[libfuzzer-binutils-disassembler]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
