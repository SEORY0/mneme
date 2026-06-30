---
type: harness-contract
title: "Libfuzzer AFL Objdump File Wrapper Harness"
description: "Round 26 input contract facts for libfuzzer/afl objdump file wrapper."
tags: ["libfuzzer-afl-objdump-file-wrapper", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer AFL Objdump File Wrapper Harness

## Round 26 Factual Contract

### Input Contract
- The objdump harness writes the raw input bytes to a temporary file and calls the objdump display path on that file. It enables broad objdump modes including section headers, section contents, private headers, DWARF/debug output, relocations, and disassembly. There is no FuzzedDataProvider carving or selector byte; the input must be a complete object file that BFD accepts far enough to reach symbol loading.

### Format Links
- [[elf]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
