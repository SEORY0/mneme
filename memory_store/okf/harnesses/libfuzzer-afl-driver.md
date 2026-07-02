---
type: harness-contract
title: "Libfuzzer Afl Driver"
description: "Abstract harness facts observed during verifier-causal consolidation."
tags: ["libfuzzer-afl-driver", "harness_contract"]
okf_support: 0
---
# Libfuzzer Afl Driver

## Notes
- These are descriptive harness facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The effective target reads the raw input as a full TIFF/DNG file through the RawSpeed parser and decoder. The raw strip must be valid enough to allocate image storage before metadata handling. There is no byte carving or checksum wrapper around the file bytes.

### Format Links
- [[dng]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
