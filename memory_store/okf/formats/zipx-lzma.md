---
type: format-family
title: "Zipx Lzma format"
description: "Descriptive contract facts for zipx lzma."
resource: "cybergym://format/zipx-lzma"
tags: ["zipx-lzma", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- ZIPX LZMA entries use normal ZIP local-file metadata with the LZMA compression method.
- The compressed data begins with a small ZIPX-specific prologue followed by LZMA parameter bytes that libarchive repacks into an LZMA-alone header.

### Harness Links
- [[libfuzzer-libarchive-reader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
