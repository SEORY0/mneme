---
type: harness-contract
title: "Libfuzzer Yara Macho Module harness"
description: "Input contract facts for libfuzzer-yara-macho-module."
tags: ["libfuzzer-yara-macho-module", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Yara Macho Module Harness

## Round 11 Input Contract
- The YARA fuzzer scans the raw input bytes with rules importing the Mach-O module. There is no leading selector or secondary container; preserving a valid Mach-O seed is the main parser gate.

## Format Links
- [[macho]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
