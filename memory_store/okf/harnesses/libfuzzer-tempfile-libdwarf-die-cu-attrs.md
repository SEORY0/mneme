---
type: harness-contract
title: "Libfuzzer Tempfile Libdwarf Die Cu Attrs harness"
description: "Input contract facts for Libfuzzer Tempfile Libdwarf Die Cu Attrs."
tags: ["libfuzzer-tempfile-libdwarf-die-cu-attrs", "round-21"]
okf_support: 1
---
# Libfuzzer Tempfile Libdwarf Die Cu Attrs Harness

## Round 21 Input Contract (elf-dwarf)

- The harness writes raw bytes to a temporary file, opens it with libdwarf, reads compilation-unit headers, obtains a root DIE, then calls multiple DIE and CU attribute routines. The crash is in fuzzer cleanup behavior, not in a separate file-format mode selector.

## Round 21 Format Links (elf-dwarf)
- [[elf-dwarf]]

## Round 21 Notes (elf-dwarf)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
