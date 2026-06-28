---
type: harness-contract
title: "Honggfuzz Libfuzzer Raw File Bytes harness"
description: "Input contract facts for honggfuzz-libfuzzer-raw-file-bytes."
tags: ["honggfuzz-libfuzzer-raw-file-bytes", "round-24"]
okf_support: 1
---
# Honggfuzz Libfuzzer Raw File Bytes Harness

## Round 24 Factual Contract

### Input Contract
- Raw bytes are written to a temporary file, opened with dwarf_init_b, then the first CU is traversed. The harness calls source-file and source-line APIs, including line-header checks, line-context creation, two-level line extraction, and per-line accessors.

### Format Links
- [[elf-or-debug-object-with-dwarf-line-info]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
