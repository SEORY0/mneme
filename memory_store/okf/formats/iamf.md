---
type: format-family
title: "Iamf"
description: "Round 12 factual format contract for iamf."
resource: cybergym://format/iamf
tags: ["iamf", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Iamf

## Round 12 Factual Contract

### Schema / Invariants
- IAMF streams are composed of OBU-style records with header fields, size coding, descriptor OBUs, audio element metadata, mix presentation metadata, and padding or reserved bit regions. Parser reachability depends on coherent descriptor order and declared sizes.

### Harness Links
- [[file-parser]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
