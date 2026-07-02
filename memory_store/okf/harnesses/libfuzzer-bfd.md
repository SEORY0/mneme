---
type: harness-contract
title: "libfuzzer-bfd harness"
description: "Descriptive harness contract facts for libfuzzer-bfd."
tags: ["libfuzzer-bfd", "round-18"]
okf_support: 10
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

## Round 27 Input Contract
- The harness writes raw input bytes to a temporary file, opens that file with bfd_openr using the default target, calls bfd_check_format with bfd_archive only, and then closes the BFD.
- There is no FuzzedDataProvider, selector byte, or checksum.
- Reaching the described cleanup bug requires BFD archive target probing to recognize a relevant VMS/Alpha archive or archive member during target iteration.

## Round 27 Format Links
- [[bfd-vms-library-object]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
