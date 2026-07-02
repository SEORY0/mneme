---
type: format-family
title: "x86_64-coff-object format"
description: "Structure, build skeleton, and bug-prone areas of the x86_64-coff-object input format."
resource: cybergym://format/x86-64-coff-object
tags: ["x86-64-coff-object", "round-29"]
okf_support: 0
---
# X86 64 COFF Object Format

## Round 29 Factual Contract

### Schema / Invariants
- A COFF object has a fixed file header with machine type, section count, optional-header length, symbol-table pointer/count, and flags. It is followed by an optional header when present, a table of section headers, raw section data, relocation/line metadata if any, then fixed-size symbol records and an optional string table. For the x86_64 COFF backend, marking an object executable is the important gate that makes objcopy synthesize an output optional header.

### Harness Links
- [[libfuzzer-binutils-objcopy]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
