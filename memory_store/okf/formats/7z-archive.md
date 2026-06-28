---
type: format-family
title: "7z archive format"
description: "Descriptive format contract facts for 7z archive."
tags: ["7z-archive", "round-18"]
okf_support: 1
train_only: true
---
# 7z Archive Format

## Round 18 Factual Contract

### Schema / Invariants
- 7z parsing reaches packed-stream decode only after the header, packed stream metadata, folder coder metadata, pack sizes, and unpack-size vectors are coherent. The relevant invariant is a mismatch where decompression yields fewer bytes than the declared unpack size and CRC is then computed over the declared span.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
