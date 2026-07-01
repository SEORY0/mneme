---
type: harness-contract
title: "Honggfuzz Libfuzzer Harness"
description: "Round 34 factual contract for honggfuzz-libfuzzer."
tags: ["honggfuzz-libfuzzer", "round-34"]
okf_support: 1
train_only: true
---
# Honggfuzz Libfuzzer Harness

## Round 34 Factual Contract

### Input Contract
- The fuzz target installs a fake OpenSC reader, connects a card from the first ATR chunk, binds PKCS#15, and consumes later chunks as APDU responses. If binding succeeds it consumes additional chunks for operation inputs and iterates PKCS#15 objects, but all card I/O still comes from the same front-to-back chunk stream.

### Format Links
- [[opensc-pkcs15-reader-chunks]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
