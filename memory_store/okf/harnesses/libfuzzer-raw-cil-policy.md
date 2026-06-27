---
type: harness-contract
title: "libfuzzer-raw-cil-policy harness"
description: "Descriptive harness contract facts for libfuzzer-raw-cil-policy."
tags: ["libfuzzer-raw-cil-policy", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw CIL Policy Harness

## Round 18 Input Contract

### Schema / Invariants
- The fuzzer passes raw bytes directly as a CIL source buffer to the secilc compile path. There is no file envelope, selector byte, checksum, or back-carved field layout.

### Format Links
- [[cil-policy-text]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
