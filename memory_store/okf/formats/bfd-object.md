---
type: format-family
title: "Bfd Object format"
description: "Round 28 descriptive format facts for bfd-object."
resource: cybergym://format/bfd-object
tags: ["bfd-object", "round-28"]
okf_support: 0
---
# Bfd Object Format

## Round 28 Factual Contract

### Schema / Invariants
- BFD object inputs are auto-detected binary object files. ELF objects use a section-header string table plus section headers naming debug, string, symbol, and payload sections; section flags distinguish contents, allocation, debug, and compressed sections. COFF objects use a fixed file header, section headers with raw-data pointers, and an optional symbol table whose records can declare auxiliary entries. The vulnerable helper reads full section contents using BFD section metadata, and some callers preallocate a debug-section buffer from the logical section size before asking BFD to fill it.

### Harness Links
- [[libfuzzer-raw-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
