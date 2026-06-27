---
type: format-family
title: "elf-dwarf format"
description: "Descriptive format contract facts for elf-dwarf."
tags: ["elf-dwarf", "round-18"]
okf_support: 1
train_only: true
---
# ELF DWARF Format

## Round 18 Factual Contract

### Schema / Invariants
- The input is an ELF object or executable with DWARF sections sufficient for libdwarf initialization, CU-header iteration, and sibling DIE lookup. Valid section headers and coherent debug-info/debug-abbrev relationships are more important than application semantics.

### Harness Links
- [[libfuzzer-tempfile-libdwarf-die-cu-offset]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
