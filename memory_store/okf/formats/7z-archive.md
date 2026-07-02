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

## Round 34 Factual Contract

### Schema / Invariants
- 7z parsing reaches encoded packed-stream decode only after the signature, start header, next-header CRC, PackInfo, Folder coder metadata, CodersUnpackSize, and optional folder CRC records are self-consistent. The encoded header stores metadata separately from the packed stream; PackInfo points back to the packed bytes, and the folder unpack-size vector controls the span later used for CRC verification.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
