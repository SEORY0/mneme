---
type: format-family
title: "opensc-virtual-reader-apdu-stream format"
description: "Descriptive format contract facts for opensc-virtual-reader-apdu-stream."
tags: ["opensc-virtual-reader-apdu-stream", "round-18"]
okf_support: 1
train_only: true
---
# Opensc Virtual Reader APDU Stream Format

## Round 18 Factual Contract

### Schema / Invariants
- The OpenSC fuzzer input is a virtual smart-card transcript: initial card identity/ATR-like bytes followed by APDU response chunks. Response status words and payload lengths must be coherent enough to select the epass2003 card path and reach PKCS#15 initialization operations.

### Harness Links
- [[opensc-card-fuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
