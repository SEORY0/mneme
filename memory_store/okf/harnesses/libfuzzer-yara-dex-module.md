---
type: harness-contract
title: "Libfuzzer Yara Dex Module Harness"
description: "Input contract facts for libfuzzer-yara-dex-module."
tags: ["libfuzzer-yara-dex-module", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Yara Dex Module Harness

## Round 30 Input Contract

### Input Contract
- The YARA dex fuzzer compiles a rule importing the dex module and scans the raw input bytes with no try/catch. The PoC is the complete DEX byte stream; there is no outer wrapper, checksum enforcement by the harness, mode selector, or FuzzedDataProvider front/back carving.

### Format Links
- [[dex]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
