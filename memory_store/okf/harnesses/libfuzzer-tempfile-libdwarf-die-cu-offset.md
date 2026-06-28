---
type: harness-contract
title: "libfuzzer-tempfile-libdwarf-die-cu-offset harness"
description: "Descriptive harness contract facts for libfuzzer-tempfile-libdwarf-die-cu-offset."
tags: ["libfuzzer-tempfile-libdwarf-die-cu-offset", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Tempfile Libdwarf Die Cu Offset Harness

## Round 18 Input Contract

### Schema / Invariants
- The libFuzzer bytes are written to a temporary file, opened with dwarf_init_b, then walked through dwarf_next_cu_header_d and dwarf_siblingof_b before the vulnerable API call. There is no selector byte or FuzzedDataProvider layout.

### Format Links
- [[elf-dwarf]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
