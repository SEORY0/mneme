---
type: harness-contract
title: "libfuzzer-bfd harness"
description: "Descriptive harness contract facts for libfuzzer-bfd."
tags: ["libfuzzer-bfd", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer BFD Harness

## Round 18 Input Contract

### Schema / Invariants
- The BFD fuzzer writes the raw input to a temporary file, opens it through BFD, classifies archive versus object input, and then exercises object/archive display or parsing paths. There is no FuzzedDataProvider carving; the whole file is passed to BFD as-is.

### Format Links
- [[coff-object-or-ar-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
