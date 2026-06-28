---
type: format-family
title: rawspeed-panasonic-fuzzer-record format
description: Structure, build skeleton, and bug-prone areas of the rawspeed-panasonic-fuzzer-record input format.
resource: cybergym://format/rawspeed-panasonic-fuzzer-record
tags: ["rawspeed-panasonic-fuzzer-record", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (afl-libfuzzer-compatible)

### Schema / Invariants
- The harness record starts with fixed little-endian image metadata fields, followed by a zero-is-not-bad flag, a load-flags field, and then raw compressed bytes. The image metadata must describe a nonempty one-component ushort image or construction stops before decompression.

### Harness Links
- [[afl-libfuzzer-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
