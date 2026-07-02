---
type: harness-contract
title: "Libfuzzer Cryptofuzz SP Math"
description: "Abstract harness facts observed during verifier-causal consolidation."
tags: ["libfuzzer-cryptofuzz-sp-math", "harness_contract"]
okf_support: 0
---
# Libfuzzer Cryptofuzz SP Math

## Notes
- These are descriptive harness facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The libFuzzer wrapper passes raw file bytes directly to Cryptofuzz. The active binary is configured for wolfCrypt SP math and includes DH_Derive and DH_GenerateKeyPair. The parent datasource is consumed front-to-back; no FuzzedDataProvider back fields, file magic, checksum, or external container is present.

### Format Links
- [[cryptofuzz-binary-operation-stream]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
