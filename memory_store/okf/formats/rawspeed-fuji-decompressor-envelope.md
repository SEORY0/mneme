---
type: format-family
title: "Rawspeed Fuji Decompressor Envelope"
description: "Round 12 factual format contract for rawspeed-fuji-decompressor-envelope."
resource: cybergym://format/rawspeed-fuji-decompressor-envelope
tags: ["rawspeed-fuji-decompressor-envelope", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Rawspeed Fuji Decompressor Envelope

## Round 12 Factual Contract

### Schema / Invariants
- The direct rawspeed Fuji fuzzer expects little-endian image metadata and CFA dimensions/entries, followed by a big-endian Fuji compressed header, per-strip compressed sizes, optional alignment padding, and strip payload bytes. Valid Fuji gates include fixed block width, matching rounded width, supported bit depth/type, and total lines matching image height.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
