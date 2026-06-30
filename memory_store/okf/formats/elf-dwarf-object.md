---
type: format-family
title: "elf-dwarf-object format"
description: "Structure and reachability facts for ELF/DWARF object."
resource: cybergym://format/elf-dwarf-object
tags: ["elf-dwarf-object", "round-16"]
okf_support: 3
---
# ELF Dwarf Object Format

## Round 9 Factual Contract

### Schema / Invariants
- The useful inputs are ELF-like objects carrying DWARF sections, including compile-unit
  information, abbreviations, and DIE attributes.
- The target family depends on a CU/DIE tree that remains structurally valid enough for attribute
  iteration and loclist processing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- The fuzzer expects a complete object/debug file container, not a raw DWARF section. It initializes libdwarf on the file and then queries frame data from standard frame sections, requiring valid section metadata plus CIE/FDE records for augmentation parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The relevant DWARF carrier is an object file with normal ELF structure plus debug sections. A .debug_addr section alone can be syntactically present, but address extraction also depends on CU context fields such as address size and address base, and on lookup indexes supplied through libdwarf APIs.

### Harness Links
- [[libfuzzer-libdwarf-debug-addr]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- The input is an object file carrying DWARF debug sections. Useful seeds need ELF structure plus compilation-unit metadata, DIE trees, line information, and any target-specific location-list or attribute sections needed by the selected libdwarf example path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- The input must be a complete ELF/DWARF object, not a raw DWARF section. The relevant object needs section headers naming debug types, abbreviations, line data, and macro data. A DWARF4 type unit has the common unit header plus a type signature and type-offset field before the first DIE. The experimental two-level line table has the usual line-table prefix, a standard-opcode operand table, empty legacy directory and file lists, an experimental marker, logical and actual table offsets, DWARF5-style directory and file tables, and then an experimental subprogram table.

### Harness Links
- [[afl-libfuzzer-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
