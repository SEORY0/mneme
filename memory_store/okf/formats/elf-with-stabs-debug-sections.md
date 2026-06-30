---
type: format-family
title: "elf-with-stabs-debug-sections format"
description: "Structure and invariants for the elf-with-stabs-debug-sections input format."
tags: ["elf-with-stabs-debug-sections", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- Stabs debug information uses fixed-size records with a string-table index, type, descriptor, and value. BFD looks for .stab and .stabstr sections, loads both contents, optionally canonicalizes relocations against the stabs section, and builds a function index from source-file and function stabs.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- ELF object reachability depends on a coherent ELF header, section header table, section-name string table, and BFD-recognized allocated sections. Stabs debug data uses a record section plus a companion string table; BFD finds these sections by their conventional names, loads their contents, and then builds a nearest-line index from fixed-size stabs records. An empty stabs string table is structurally representable but violates the backend assumption that the loaded string table has a last byte to terminate.

### Harness Links
- [[libfuzzer-binutils-addr2line]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
