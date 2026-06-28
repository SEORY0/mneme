---
type: format-family
title: "coff-object-or-ar-archive format"
description: "Descriptive format contract facts for coff-object-or-ar-archive."
tags: ["coff-object-or-ar-archive", "round-18"]
okf_support: 1
train_only: true
---
# COFF Object Or Ar Archive Format

## Round 18 Factual Contract

### Schema / Invariants
- A COFF object has a fixed file header, optional section headers, raw section data, a symbol table, auxiliary symbol records, and a string table. Symbols can declare auxiliary record counts, and C_FILE/comdat-related entries are interpreted specially by BFD. Unix ar archives wrap member files with archive headers before BFD dispatches each member to an object parser.

### Harness Links
- [[libfuzzer-bfd]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
