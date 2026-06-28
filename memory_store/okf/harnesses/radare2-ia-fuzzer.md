---
type: harness-contract
title: "Radare2 Ia Fuzzer harness"
description: "Input contract facts for radare2-ia-fuzzer."
tags: ["radare2-ia-fuzzer", "round-20"]
okf_support: 1
---
# Radare2 Ia Fuzzer Harness

## Round 20 Input Contract
- The radare2 harness loads raw bytes into an in-memory file, opens binary analysis at base address, and runs the class-analysis command. There is no archive/container layer. A valid enough Mach-O is needed for the bin plugin before the class parser is exercised.

## Round 20 Format Links
- [[mach-o-binary]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
