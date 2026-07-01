---
type: format-family
title: "Elf32 Relocatable Msp430"
description: "Round 36 factual format contract for elf32-relocatable-msp430."
tags: ["elf32-relocatable-msp430", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Elf32 Relocatable Msp430

## Round 36 Factual Contract

### Schema / Invariants
- The useful ELF shape is ET_REL with section headers, a SHT_NOTE payload section, SHT_SYMTAB and string table sections, and a SHT_RELA relocation section whose section-header link points at the symbol table and whose info points at the target payload section. MSP430 relocation info combines a valid symbol index with the target-specific GNU subtract/set ULEB relocation types. The classic MSP430 relocation numbering requires avoiding the MSP430X interpretation gate.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
