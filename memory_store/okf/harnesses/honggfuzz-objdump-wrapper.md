---
type: harness-contract
title: "Honggfuzz Objdump Wrapper harness"
description: "Input contract facts for honggfuzz-objdump-wrapper."
tags: ["honggfuzz-objdump-wrapper", "round-24"]
okf_support: 1
---
# Honggfuzz Objdump Wrapper Harness

## Round 24 Factual Contract

### Input Contract
- The wrapper copies the raw input to a temporary file and runs a safe objdump-style binary over it. Recognition by BFD is the first gate before any relocation processing is reached.

### Format Links
- [[z80-coff-object]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
