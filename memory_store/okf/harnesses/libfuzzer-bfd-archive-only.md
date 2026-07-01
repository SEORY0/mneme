---
type: harness-contract
title: "libfuzzer-bfd-archive-only harness"
description: "Input contract facts for libfuzzer-bfd-archive-only."
tags: ["libfuzzer-bfd-archive-only", "round-35"]
okf_support: 1
train_only: true
---
# libfuzzer-bfd-archive-only Harness

## Round 35 Input Contract
### Input Contract
- The libFuzzer target passes the PoC as raw bytes with no selector and no FuzzedDataProvider split. It writes the bytes to a temporary file, opens it with BFD using the default target, calls archive-format detection, then closes the BFD; it does not explicitly iterate archive members in the harness.

### Format Links
- [[bfd-vms-alpha-archive-or-object]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

## Round 36 Input Contract
- The harness writes the raw bytes to a temporary file, opens it with BFD using the default target, and calls the archive-format check only. It does not iterate archive members or explicitly ask for object format. There is no FuzzedDataProvider layout, no mode selector, and local verification for this target may need a bounded honggfuzz invocation because the direct wrapper can report only harness usage.

## Round 36 Format Links
- [[bfd-vms-alpha-archive-or-object]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
