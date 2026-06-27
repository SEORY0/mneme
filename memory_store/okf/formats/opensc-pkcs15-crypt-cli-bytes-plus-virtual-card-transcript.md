---
type: format-family
title: opensc-pkcs15-crypt-cli-bytes-plus-virtual-card-transcript format
description: Structure and reachability facts for opensc-pkcs15-crypt-cli-bytes-plus-virtual-card-transcript inputs.
tags: [opensc-pkcs15-crypt-cli-bytes-plus-virtual-card-transcript]
okf_support: 0
---
# Opensc Pkcs15 Crypt Cli Bytes Plus Virtual Card Transcript Format

## Round 10 Factual Contract

### Schema / Invariants
- The card transcript portion uses little-endian length-prefixed chunks: first ATR, then APDU responses with trailing status words. IDPrime initialization reads card OS data, selects internal files, and consumes container and index records before crypt operations can reference keys.

### Harness Links
- [[libfuzzer-cli-option-and-card-response-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
