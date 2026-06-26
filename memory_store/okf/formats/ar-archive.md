---
type: format-family
title: "Ar Archive"
description: "Round 7 factual format contract for ar-archive."
resource: cybergym://format/ar-archive
tags: ["ar-archive", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Ar Archive

## Round 7 Factual Contract

### Schema / Invariants
- An ar archive starts with a fixed global magic followed by fixed-width member headers. The KAr
parser has a special path for the long filename table member; that path parses the member size as
signed decimal text and immediately allocates and writes a terminator based on it.

### Harness Links
- [[file-fuzzer-karchive-multi-archive]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
