---
type: format-family
title: "raw-ipv4-tcp-xcsl-packet format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/raw-ipv4-tcp-xcsl-packet"
tags: ["raw-ipv4-tcp-xcsl-packet", "round-35"]
okf_support: 1
train_only: true
---
# raw-ipv4-tcp-xcsl-packet Format

## Round 35 Factual Contract
### Schema / Invariants
- XCSL is selected as a TCP heuristic when the TCP payload begins with the protocol marker followed by a delimiter-like version separator. Fields are parsed as semicolon-, carriage-return-, or newline-separated text items. A field without an early separator is copied into a fixed item buffer and then null-terminated before the main command/reply switch handles it.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
