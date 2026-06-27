---
type: format
title: "Elf Dwarf5"
input_format: elf-dwarf5
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Elf Dwarf5

## Schema
- The useful inputs are object files with ELF section headers and DWARF sections such as debug_info, debug_abbrev, debug_str, debug_line, and debug_macro. DWARF5 macro traversal depends on a valid CU DIE, a macro-related attribute or offset, and a debug_macro unit containing well-formed macro operations.
