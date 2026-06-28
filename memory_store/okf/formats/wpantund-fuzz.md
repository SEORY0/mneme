---
type: format-family
title: wpantund-fuzz format
description: Structure, build skeleton, and bug-prone areas of the wpantund-fuzz input format.
resource: cybergym://format/wpantund-fuzz
tags: [wpantund-fuzz, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The first byte selects a harness mode: config text, NCP socket input, or an unimplemented control-interface path. Config-mode inputs are raw wpantund configuration lines after the selector. NCP-mode inputs are byte streams containing HDLC flag-delimited frames, with a special command byte used by the fuzzer to wait for outbound frames or fast-forward simulated time.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
