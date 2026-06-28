---
type: format-family
title: opensc-pkcs15init-profile-reader-chunks format
description: "Round 23 descriptive structure and invariant facts for opensc-pkcs15init-profile-reader-chunks."
resource: cybergym://format/opensc-pkcs15init-profile-reader-chunks
tags: ["opensc-pkcs15init-profile-reader-chunks", "round-23"]
okf_support: 1
train_only: true
---
# Opensc Pkcs15init Profile Reader Chunks Format

## Round 23 Factual Contract

### Schema / Invariants
- The pkcs15init input is split at a NUL delimiter. The prefix is an OpenSC profile configuration, and the suffix is a virtual-reader stream of host-endian two-byte length-prefixed chunks. The first reader chunk is the ATR; subsequent chunks are APDU responses with status words at the end.

### Harness Links
- [[libfuzzer-opensc-pkcs15init]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
