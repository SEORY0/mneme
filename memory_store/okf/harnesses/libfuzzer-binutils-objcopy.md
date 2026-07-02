---
type: harness-contract
title: "Libfuzzer Binutils Objcopy harness"
description: "Input contract facts for libfuzzer-binutils-objcopy."
tags: ["libfuzzer-binutils-objcopy", "round-29"]
okf_support: 0
---
# Libfuzzer Binutils Objcopy Harness

## Round 29 Input Contract

- The objcopy fuzzer writes the raw libFuzzer bytes to a temporary file and invokes a fixed objcopy copy path with compression, extraction, and debug-related options. There is no selector byte or FuzzedDataProvider layout; BFD auto-detects the raw file as an object/archive format before objcopy writes a temporary output file.

## Round 29 Format Links
- [[x86-64-coff-object]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
