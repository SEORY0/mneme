---
type: harness-contract
title: "Libfuzzer Libdwarf Debug Addr harness"
description: "Input contract facts for libfuzzer-libdwarf-debug-addr."
tags: ["libfuzzer-libdwarf-debug-addr", "round-16"]
okf_support: 1
---
# Libfuzzer Libdwarf Debug Addr Harness

## Round 16 Input Contract
- The libdwarf fuzzer writes the raw input to a temporary object file, opens it with libdwarf, enumerates debug address tables, and queries addresses by index. There is no byte selector or sidecar metadata outside the object file.

## Round 16 Format Links
- [[elf-dwarf-object]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
