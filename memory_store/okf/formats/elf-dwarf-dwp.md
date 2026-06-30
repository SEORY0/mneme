---
type: format-family
title: "Elf Dwarf Dwp format"
description: "Round 28 descriptive format facts for elf-dwarf-dwp."
resource: cybergym://format/elf-dwarf-dwp
tags: ["elf-dwarf-dwp", "round-28"]
okf_support: 0
---
# Elf Dwarf Dwp Format

## Round 28 Factual Contract

### Schema / Invariants
- The input is an ELF object whose relevant payload is split-DWARF package data. DWP package indexes contain a header, hash/index tables, a row of DW_SECT column identifiers, and per-unit offset and size rows for contributions such as type-unit data and abbreviation data. DWO type-unit sections carry a DWARF unit header with version, unit type, address size, abbreviation-table displacement, signature data, and a type-offset field before DIE bytes. The abbreviation section is a sequence of LEB128 abbreviation records: code, tag, child flag, then attribute/form pairs terminated by a zero pair.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
