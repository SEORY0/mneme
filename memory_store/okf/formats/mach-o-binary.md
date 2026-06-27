---
type: format-family
title: "Mach O Binary format"
description: "Structure and invariants for the mach-o-binary input format."
tags: ["mach-o-binary", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Mach-O begins with an endian/class magic, CPU type, file type, load-command count, and load-command byte count. Segment load commands describe virtual/file ranges and sections; Objective-C class parsing depends on segment/section names and in-file class metadata, not only the top-level header.

### Harness Links
- [[radare2-ia-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
