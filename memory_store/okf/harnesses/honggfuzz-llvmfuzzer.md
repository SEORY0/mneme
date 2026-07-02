---
type: harness-contract
title: "Honggfuzz Llvmfuzzer Harness"
description: "Round 34 factual contract for honggfuzz-llvmfuzzer."
tags: ["honggfuzz-llvmfuzzer", "round-34"]
okf_support: 1
train_only: true
---
# Honggfuzz Llvmfuzzer Harness

## Round 34 Factual Contract

### Input Contract
- The target is an LLVMFuzzerTestOneInput harness run under honggfuzz. It installs a synthetic OpenSC reader over the raw input stream, connects a card, binds PKCS#15, and then may consume extra chunks for operations only after binding. Several card drivers probe with APDUs before OpenPGP when ATR matching is unavailable, so successful OpenPGP responses must be positioned after status-only probe responses.

### Format Links
- [[opensc-pkcs15-reader-chunk-stream]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
