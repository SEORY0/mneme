---
type: format-family
title: "Elf Core Note format"
description: "Descriptive contract facts for elf-core-note."
resource: "cybergym://format/elf-core-note"
tags: ["elf-core-note", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The relevant ELF shape is an ET_CORE file with program headers and a PT_NOTE segment.
- Notes are aligned records containing note header fields, a name string, and a descriptor body; core-module discovery depends on segment mappings and note metadata being mutually consistent.

### Harness Links
- [[libfuzzer-elfutils-dwfl-core]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
