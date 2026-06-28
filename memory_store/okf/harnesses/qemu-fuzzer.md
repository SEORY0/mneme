---
type: harness-contract
title: "qemu-fuzzer harness"
description: "Input contract facts for qemu-fuzzer."
tags: ["qemu-fuzzer", "round-14"]
okf_support: 1
---
# Qemu Fuzzer Harness

## Round 14 Input Contract
- Task generation needed local tar recovery because the source archive contained an unsafe absolute symlink. The local verifier image invoked a QEMU generic device fuzz target for e1000e rather than a linux-user ELF runner, so raw ELF bytes were not interpreted as an executable by the observed harness.

## Round 14 Format Links
- [[elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
