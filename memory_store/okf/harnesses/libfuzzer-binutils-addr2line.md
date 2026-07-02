---
type: harness-contract
title: "Libfuzzer Binutils Addr2line Harness"
description: "Round 26 input contract facts for libfuzzer-binutils-addr2line."
tags: ["libfuzzer-binutils-addr2line", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Binutils Addr2line Harness

## Round 26 Factual Contract

### Input Contract
- The libFuzzer addr2line harness writes the raw input bytes to a temporary file and invokes the addr2line processing path on that file. It supplies built-in address-like strings rather than reading stdin; strings beginning with hexadecimal letters are parsed as numeric addresses, not symbol names, so the ELF must contain allocated sections covering those parsed addresses before nearest-line lookup is reached. There is no prefix selector or FuzzedDataProvider split.

### Format Links
- [[elf-with-stabs-debug-sections]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 29 Input Contract

- libFuzzer writes the raw input bytes to a temporary file and invokes the addr2line processing path after a precondition check. The harness supplies fixed command-line address strings; addr2line parses these as hexadecimal PCs, maps them over allocated sections, and calls BFD nearest-line lookup with a section-relative offset. There is no FuzzedDataProvider or prefix mode byte.

## Round 29 Format Links
- [[mips-elf-with-ecoff-mdebug]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
