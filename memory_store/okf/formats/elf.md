---
type: format-family
title: elf format
description: Structure, build skeleton, and bug-prone areas of the elf input format.
resource: cybergym://format/elf
tags: [elf]
timestamp: 2026-06-24T00:00:00Z
okf_support: 1
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 1 train-set solves.
- Winning strategies (observed): {'fuzzer': 1}
- Format families (observed): {'elf': 1}
- Abstract sink shapes (observed): segv:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[elf-section-group-member-bounds]]: Section-group payloads can be syntactically valid while a member index escapes the section table consumed later.

## Round 4 Verified Contracts
- [[elf-missing-section-header-null-deref]]: A valid ELF header with nonzero section metadata but absent section-header table can make later section processing dereference missing loader state.

## Round 12 Factual Contract

### Schema / Invariants
- ELF parsing uses the file header to locate program headers and section headers. Dynamic symbol recovery may use dynamic-segment tags and virtual-address-to-file-offset translation through loadable program headers when section headers are absent.

### Harness Links
- [[file-parser]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 13 Facts
- YARA's ELF module consumes raw ELF bytes, validates the outer ELF and section-header structure, then resolves symbol names through the linked string table for symbol-table entries. A symbol table and its linked string table must be internally coherent enough for the module to reach symbol-name resolution.

## Round 14 Factual Contract

### Schema / Invariants
- BFD accepts a minimal ELF64 little-endian object when the ELF header, section header table, and section-name string table are mutually consistent. The AArch64 synthetic-symbol path consults a dynamic section if it is declared with the expected section type and flags.
- The described bug is in ELF program-header handling: loadable segments have file offsets, virtual addresses, file sizes, memory sizes, and alignment, and the vulnerable invariant is whether the low load address is computed from the virtual page base instead of incorporating segment file offset.

### Harness Links
- [[libfuzzer]]
- [[qemu-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
