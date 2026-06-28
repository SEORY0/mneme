---
type: harness-contract
title: "Libfuzzer Libdwfl harness"
description: "Input contract facts for Libfuzzer Libdwfl."
tags: ["libfuzzer-libdwfl", "round-21"]
okf_support: 1
---
# Libfuzzer Libdwfl Harness

## Round 21 Input Contract (elf-gnu-hash)

- The active wrapper runs an elfutils DWFL/libelf fuzzer over raw ELF files. The file must pass ELF header and section-table recognition; local libdwfl wrapper crashes are not sufficient without official vulnerable/fixed confirmation.

## Round 21 Format Links (elf-gnu-hash)
- [[elf-gnu-hash]]

## Round 21 Notes (elf-gnu-hash)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
