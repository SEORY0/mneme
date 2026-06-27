---
type: format
title: "ELF Dwarf5"
access_scope: generate
confidence: medium
tags: ["elf-dwarf5", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# ELF Dwarf5

## Round 13 Facts
- The useful inputs are object files with ELF section headers and DWARF sections such as debug_info, debug_abbrev, debug_str, debug_line, and debug_macro. DWARF5 macro traversal depends on a valid CU DIE, a macro-related attribute or offset, and a debug_macro unit containing well-formed macro operations.
