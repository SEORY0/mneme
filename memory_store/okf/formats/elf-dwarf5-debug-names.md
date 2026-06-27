---
type: format-family
title: "elf-dwarf5-debug-names format"
description: "Descriptive format contract facts for elf-dwarf5-debug-names."
tags: ["elf-dwarf5-debug-names", "round-18"]
okf_support: 1
train_only: true
---
# ELF Dwarf5 Debug Names Format

## Round 18 Factual Contract

### Schema / Invariants
- The carrier is an ELF file with DWARF sections, including DWARF5 `.debug_names` data used as an accelerator for global name lookup. The debug-names header, counts, and table regions must be plausible enough for libdwarf to construct a Dnames handle before querying globals.

### Harness Links
- [[oss-fuzz-run-poc-libdwarf-fuzz-globals]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
