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

## Round 29 Factual Contract

### Schema / Invariants
- MIPS ELF .mdebug uses a MIPS-specific section type and an ECOFF symbolic header. The header stores absolute file positions and counts for line bytes, PDR records, FDR records, local strings, and optional symbol tables. ECOFF-32 external FDR records contain compact 16-bit procedure index/count fields, while PDR records carry full procedure VMAs used by nearest-line lookup. FDR filename fields are offsets into the local string table and can be selected without requiring local symbols when only a filename is needed.

### Harness Links
- [[libfuzzer-binutils-addr2line]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
