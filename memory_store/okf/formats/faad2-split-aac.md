---
type: format-family
title: faad2-split-aac format
description: Structure, build skeleton, and bug-prone areas of the faad2-split-aac input format.
resource: cybergym://format/faad2-split-aac
tags: [faad2-split-aac, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- AAC decoder setup may use an AudioSpecificConfig with object type, sampling-frequency index, and channel configuration. A channel configuration of zero indicates that a program configuration element supplies channel layout information; raw data blocks can also carry PCE syntax that should be ignored for decoder configuration.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
