---
type: harness-contract
title: "Libfuzzer Honggfuzz Wrapper Harness"
description: "Input contract facts for libfuzzer/honggfuzz-wrapper."
tags: ["libfuzzer-honggfuzz-wrapper", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Libfuzzer Honggfuzz Wrapper Harness

## Round 19 Input Contract

- The fuzzer writes raw input bytes to a temporary file and runs objdump display logic with section headers, section contents, DWARF display, debugging, relocation, and disassembly paths enabled. There is no internal mode byte; reachability depends on the file being recognized by BFD.
- Format link: [[elf-object-with-dwarf-relocations]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
