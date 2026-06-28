---
type: harness-contract
title: "Afl Libfuzzer Compatible Raw Stdin harness"
description: "Input contract facts for afl-libfuzzer-compatible-raw-stdin."
tags: ["afl-libfuzzer-compatible-raw-stdin", "round-24"]
okf_support: 2
---
# Afl Libfuzzer Compatible Raw Stdin Harness

## Round 24 Factual Contract

### Input Contract
- Raw input bytes are read as a file by the threaded AV1 decoder fuzzer. The fuzzer enables threaded decode with a fixed multi-thread configuration and repeatedly reads IVF frames until the input ends or a frame-size/read error occurs.
- Raw bytes are supplied directly to an AFL-built disassembler fuzzer. The harness does not parse an object file; it assigns the leading bytes as the disassembly buffer and uses the trailing option fields to choose the BFD disassembler.

### Format Links
- [[ivf-av1]]
- [[machine-code-plus-disassembler-options]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
