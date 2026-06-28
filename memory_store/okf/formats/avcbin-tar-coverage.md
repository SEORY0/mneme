---
type: format-family
title: "Avcbin Tar Coverage format"
description: "Descriptive contract facts for avcbin-tar-coverage."
resource: "cybergym://format/avcbin-tar-coverage"
tags: ["avcbin-tar-coverage", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The AVCBIN fuzzer expects a tar archive whose opened path contains a coverage directory named testavc plus associated INFO directory files.
- Binary coverage files include ADF component files such as arc, label, polygon, boundary, tolerance, and INFO tables.
- The target class involves an index value inside AVCBIN component records driving an out-of-bounds read.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
