---
type: harness-contract
title: "Libfuzzer Raw Sav"
description: "Abstract harness facts observed during verifier-causal consolidation."
tags: ["libfuzzer-raw-sav", "harness_contract"]
okf_support: 0
---
# Libfuzzer Raw Sav

## Notes
- These are descriptive harness facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The libFuzzer harness passes raw file bytes into an in-memory buffer and calls the SAV parser directly. There is no FuzzedDataProvider carving, external archive, checksum field managed by the harness, or mode selector; all parser reachability depends on the SAV header, dictionary, metadata records, terminator, and row layout being internally coherent.

### Format Links
- [[spss-sav]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
