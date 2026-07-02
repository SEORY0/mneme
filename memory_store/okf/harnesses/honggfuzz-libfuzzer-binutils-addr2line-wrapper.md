---
type: harness-contract
title: "Honggfuzz Libfuzzer Binutils Addr2Line Wrapper harness"
description: "Input contract facts for honggfuzz-libfuzzer-binutils-addr2line-wrapper."
tags: ["honggfuzz-libfuzzer-binutils-addr2line-wrapper", "round-28"]
okf_support: 0
---
# Honggfuzz Libfuzzer Binutils Addr2Line Wrapper Harness

## Round 28 Input Contract

- The addr2line fuzz wrapper writes the raw input bytes to a temporary file, opens it through BFD, uses built-in address-like query strings, and maps over allocated sections before calling bfd_find_nearest_line_discriminator. There is no fuzzer prefix, FuzzedDataProvider split, checksum, archive wrapper, or stdin-provided address list.

## Round 28 Format Links
- [[mips-elf-with-ecoff-mdebug]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
