---
type: harness
title: "Libfuzzer Libdwarf Macro Dwarf5"
harness_convention: libfuzzer-libdwarf-macro-dwarf5
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Libdwarf Macro Dwarf5

## Input Contract
- For `elf-dwarf5`, The selected libdwarf harness writes the raw input to a temporary file, initializes libdwarf from that file, reads the first CU header, obtains the CU DIE with sibling traversal, then asks for DWARF5 macro context and iterates macro operations. The verifier selected the DWARF5 macro fuzzer, not a plain die-CU-only harness.
