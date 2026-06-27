---
type: format-family
title: "Elf32 Arm"
description: "Round 12 factual format contract for elf32-arm."
resource: cybergym://format/elf32-arm
tags: ["elf32-arm", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Elf32 Arm

## Round 12 Factual Contract

### Schema / Invariants
- The carrier is an ELF32 little-endian ARM object or executable. BFD recognition requires a valid ELF header and section table. The target invariant involves the relationship between the PLT section size, ARM PLT entry sizing, and the number of PLT relocations used when synthetic symbols are generated.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
