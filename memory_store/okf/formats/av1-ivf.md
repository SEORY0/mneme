---
type: format-family
title: "av1-ivf format"
description: "Structure and invariants observed for av1-ivf."
resource: "cybergym://format/av1-ivf"
tags: ["av1-ivf", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The accepted carrier is an IVF-style AV1 decoder stream: a fixed header is read first, then framed payloads are pulled by the IVF frame reader and passed to the AV1 decoder. Random small corpus fragments can satisfy the outer fuzzer call while still being rejected as invalid frame sizes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
