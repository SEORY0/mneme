---
type: harness-contract
title: "Honggfuzz Style Pkcs15 Reader Harness harness"
description: "Input contract facts for honggfuzz-style pkcs15 reader harness."
tags: ["honggfuzz-style-pkcs15-reader-harness", "round-16"]
okf_support: 1
---
# Honggfuzz Style Pkcs15 Reader Harness Harness

## Round 16 Input Contract
- The selected binary is the pkcs15-reader harness. It builds an in-memory reader from the raw bytes, connects a card based on the ATR, binds PKCS#15 state, then exercises object crypto operations only if binding produces objects.

## Round 16 Format Links
- [[opensc-virtual-reader-chunk-stream]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
