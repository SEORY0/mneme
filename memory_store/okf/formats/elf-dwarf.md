---
type: format-family
title: "elf-dwarf format"
description: "Descriptive format contract facts for elf-dwarf."
tags: ["elf-dwarf", "round-18"]
okf_support: 2
train_only: true
---
# ELF DWARF Format

## Round 18 Factual Contract

### Schema / Invariants
- The input is an ELF object or executable with DWARF sections sufficient for libdwarf initialization, CU-header iteration, and sibling DIE lookup. Valid section headers and coherent debug-info/debug-abbrev relationships are more important than application semantics.

### Harness Links
- [[libfuzzer-tempfile-libdwarf-die-cu-offset]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer-tempfile-libdwarf-die-cu-attrs)

### Schema / Invariants
- The input must be a binary object container with DWARF sections. The harness needs libdwarf initialization, at least one compilation-unit header, and a sibling DIE before the DIE attribute APIs are exercised. Generic object files can reach initialization while still missing the precise DIE attributes needed for the invalid-free path.

### Harness Links
- [[libfuzzer-tempfile-libdwarf-die-cu-attrs]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- The input must be a complete object/debug file with ELF section metadata, debug_info, debug_abbrev, and related DWARF sections. DWARF DIE attributes are interpreted according to abbreviation-table form descriptors; changing a reference form without keeping the DIE stream coherent may simply make traversal skip or reject the entry.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
