---
type: harness-contract
title: "Libfuzzer Addr2line File harness"
description: "Input contract facts for libfuzzer-addr2line-file."
tags: ["libfuzzer-addr2line-file", "round-29"]
okf_support: 0
---
# Libfuzzer Addr2line File Harness

## Round 29 Input Contract

- The addr2line libFuzzer harness writes the raw input bytes to a temporary file, checks that BFD recognizes an object, canonicalizes symbols if present, then calls addr2line processing with fixed address strings. Addr2line maps over allocated sections; when an address falls in one, BFD line lookup loads DWARF info and uses relocated debug-section contents when symbols are available.

## Round 29 Format Links
- [[elf64-bpf-relocatable]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
