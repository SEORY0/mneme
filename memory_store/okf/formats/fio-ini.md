---
type: format-family
title: "Fio Ini"
description: "Round 7 factual format contract for fio-ini."
resource: cybergym://format/fio-ini
tags: ["fio-ini", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Fio Ini

## Round 7 Factual Contract

### Schema / Invariants
- fio job input is line-oriented ini text with section headers and key-value options. The filename
option is split into path entries and each entry is passed to file setup, where a fixed path-sized
stack buffer is populated from the option value.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
