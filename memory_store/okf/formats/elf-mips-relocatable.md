---
type: format-family
title: "ELF MIPS Relocatable"
description: "Round 19 factual format contract for elf-mips-relocatable."
resource: cybergym://format/elf-mips-relocatable
tags: ["elf-mips-relocatable", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# ELF MIPS Relocatable

## Round 19 Factual Contract

- The useful file is an ELF relocatable object, not raw instruction bytes. It needs a coherent ELF header, section-header table, executable text section, string tables, symbol table, and relocation section linked to the text section and symbol table. MIPS and microMIPS behavior is controlled by ELF machine and flag metadata plus the relocation type recorded in the relocation entry.
- Harness link: [[afl-libfuzzer-binutils-nm]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
