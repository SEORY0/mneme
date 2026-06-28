---
type: harness-contract
title: "oss-fuzz-run_poc-libdwarf-fuzz_globals harness"
description: "Descriptive harness contract facts for oss-fuzz-run_poc-libdwarf-fuzz_globals."
tags: ["oss-fuzz-run-poc-libdwarf-fuzz-globals", "round-18"]
okf_support: 1
train_only: true
---
# Oss Fuzz Run Poc Libdwarf Fuzz Globals Harness

## Round 18 Input Contract

### Schema / Invariants
- The oss-fuzz wrapper writes or passes the raw input file to `/out/fuzz_globals`, not directly to the standalone dnames fuzzer. The target calls dwarf_init_b, enables empty pubnames behavior, and reaches global lookup paths that internally parse `.debug_names`.

### Format Links
- [[elf-dwarf5-debug-names]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
