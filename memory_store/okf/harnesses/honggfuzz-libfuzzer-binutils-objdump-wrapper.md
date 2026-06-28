---
type: harness-contract
title: "Honggfuzz Libfuzzer Binutils Objdump Wrapper harness"
description: "Input contract facts for honggfuzz-libfuzzer-binutils-objdump-wrapper."
tags: ["honggfuzz-libfuzzer-binutils-objdump-wrapper", "round-24"]
okf_support: 1
---
# Honggfuzz Libfuzzer Binutils Objdump Wrapper Harness

## Round 24 Factual Contract

### Input Contract
- The harness writes raw bytes to a temporary file and invokes an objdump-style BFD path. Inputs that fail BFD format recognition exit cleanly before the VMS-specific descriptor printers.

### Format Links
- [[vms-alpha-object-or-library]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
