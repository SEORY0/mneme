---
type: harness-contract
title: "Libfuzzer Raw File To Gas Harness"
description: "Input contract facts for libfuzzer-raw-file-to-gas."
tags: ["libfuzzer-raw-file-to-gas", "round-27"]
okf_support: 1
---
# Libfuzzer Raw File To Gas Harness

## Round 27 Input Contract
- libFuzzer bytes are written unchanged to a temporary assembly file and the assembler is invoked on that file.
- The harness does not carve fields from the input and does not use FuzzedDataProvider; every byte is interpreted as assembler source text.

## Round 27 Format Links
- [[gas-assembly-source]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
