---
type: harness-contract
title: "Afl Libfuzzer Binutils Nm Harness"
description: "Input contract facts for afl-libfuzzer-binutils-nm."
tags: ["afl-libfuzzer-binutils-nm", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Afl Libfuzzer Binutils Nm Harness

## Round 19 Input Contract

- The active binutils wrapper consumed the raw file as a temporary object through an nm-style BFD path. There is no fuzzer prefix or mode byte. Parser reachability requires a BFD-recognized ELF object with internally linked sections rather than a bare ELF magic header.
- Format link: [[elf-mips-relocatable]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
