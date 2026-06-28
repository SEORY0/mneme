---
type: harness-contract
title: "Libfuzzer Raw Transcript Chunks harness"
description: "Input contract facts for libfuzzer-raw-transcript-chunks."
tags: ["libfuzzer-raw-transcript-chunks"]
okf_support: 0
---
# Libfuzzer Raw Transcript Chunks Harness

## Round 10 Input Contract
- The harness installs a fuzz reader, connects a virtual card, binds PKCS#15, then consumes additional chunks as operation inputs only after a p15 card exists. Raw ASN.1 bytes at the start are interpreted as an ATR, not as file content.

## Round 10 Format Links
- [[opensc-virtual-card-transcript]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
