---
type: format-family
title: riff-qcp format
description: Structure, build skeleton, and bug-prone areas of the riff-qcp input format.
resource: cybergym://format/riff-qcp
tags: [riff-qcp, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- QCP is RIFF-based: a RIFF envelope advertises the QLCM form and a format chunk. The demuxer skips fixed header fields and reads a codec GUID from the format chunk before comparing it against known GUIDs. A short read of that GUID leaves part of the local buffer undefined in the vulnerable version.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
