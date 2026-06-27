---
type: format-family
title: "Openthread Cli Uart"
description: "Round 12 factual format contract for openthread-cli-uart."
resource: cybergym://format/openthread-cli-uart
tags: ["openthread-cli-uart", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Openthread Cli Uart

## Round 12 Factual Contract

### Schema / Invariants
- The input is CLI text, usually newline-terminated commands. Address-bearing commands pass tokenized arguments into IPv6 string parsing; IPv6 literals may include compressed hextets and an embedded dotted IPv4 tail. The parser treats a space as an address terminator.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
