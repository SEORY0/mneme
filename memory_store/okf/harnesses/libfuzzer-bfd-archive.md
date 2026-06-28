---
type: harness-contract
title: "libfuzzer-bfd-archive harness"
description: "Descriptive harness contract facts for libfuzzer-bfd-archive."
tags: ["libfuzzer-bfd-archive", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer BFD Archive Harness

## Round 18 Input Contract

### Schema / Invariants
- The libFuzzer harness writes the raw input bytes to a temporary file and opens it with BFD. There is no fuzzer-side length prefix or field carving; all structure must be present in the raw archive bytes.

### Format Links
- [[alpha-ecoff-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
