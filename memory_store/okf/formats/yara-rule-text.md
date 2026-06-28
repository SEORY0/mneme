---
type: format-family
title: "Yara Rule Text"
description: "Round 7 factual format contract for yara-rule-text."
resource: cybergym://format/yara-rule-text
tags: ["yara-rule-text", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Yara Rule Text

## Round 7 Factual Contract

### Schema / Invariants
- The input is raw YARA rule source text compiled from a NUL-terminated copy of the fuzzer bytes. A
minimal rule with a true condition is sufficient to satisfy the parser gate.

### Harness Links
- [[libfuzzer-raw-bytes]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
