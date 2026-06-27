---
type: harness-contract
title: "Honggfuzz Libfuzzer Driver Harness"
description: "Input contract facts for honggfuzz/libfuzzer-driver."
tags: ["honggfuzz-libfuzzer-driver", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Honggfuzz Libfuzzer Driver Harness

## Round 19 Input Contract

- The fuzz_pkcs15_reader harness installs a fake OpenSC reader. It consumes chunks front-to-back for ATR/connect, APDU responses, decipher input, parameters, temporary key material, and later operations; the whole file is not a standalone ASN.1 object.
- Format link: [[opensc-pkcs15-reader-stream]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
