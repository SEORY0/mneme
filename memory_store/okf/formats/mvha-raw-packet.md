---
type: format-family
title: mvha-raw-packet format
description: Structure, build skeleton, and bug-prone areas of the mvha-raw-packet input format.
resource: cybergym://format/mvha-raw-packet
tags: [mvha-raw-packet, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The target-decoder fuzzer treats the main prefix as one or more raw packets separated by an internal delimiter and reserves a fixed-size trailer for codec context controls. For MVHA, the useful packet begins with a frame type and a little-endian size field followed by compressed frame data. Width and height are supplied by the fuzzer trailer, not by a surrounding container.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
