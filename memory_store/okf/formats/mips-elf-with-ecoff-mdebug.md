---
type: format-family
title: "Mips Elf With Ecoff Mdebug format"
description: "Round 28 descriptive format facts for mips-elf-with-ecoff-mdebug."
resource: cybergym://format/mips-elf-with-ecoff-mdebug
tags: ["mips-elf-with-ecoff-mdebug", "round-28"]
okf_support: 0
---
# Mips Elf With Ecoff Mdebug Format

## Round 28 Factual Contract

### Schema / Invariants
- A usable carrier can be a MIPS ELF object with a .mdebug section whose ECOFF symbolic header stores absolute file offsets to debug sub-tables. The nearest-line path needs at least one allocated section covering the harness-supplied addresses, an FDR with procedure descriptors, a PDR table, a small line table, and a local string table. FDR filename and symbol name fields are string-table indexes; keeping table counts and offsets mutually consistent is necessary before mutating one string index.

### Harness Links
- [[honggfuzz-libfuzzer-binutils-addr2line-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
