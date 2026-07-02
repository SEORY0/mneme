---
type: harness-contract
title: "Libfuzzer Readelf Harness"
description: "Input contract facts for libfuzzer-readelf."
tags: ["libfuzzer-readelf", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Readelf Harness

## Round 30 Input Contract

### Input Contract
- The libFuzzer harness writes the raw input bytes to a temporary file and enables readelf header, section, segment, dynamic, and arch-specific displays before calling the file processor. There is no front selector byte, wrapper format, or FuzzedDataProvider split.

### Format Links
- [[mips-elf-dynamic-options]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
