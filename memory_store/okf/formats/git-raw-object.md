---
type: format-family
title: "Git Raw Object"
description: "Round 12 factual format contract for git-raw-object."
resource: cybergym://format/git-raw-object
tags: ["git-raw-object", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Git Raw Object

## Round 12 Factual Contract

### Schema / Invariants
- The objects fuzzer accepts raw object body bytes, not a loose-object zlib envelope. Commit objects are line-oriented records, with header-like fields parsed in order; duplicate author fields are detected by prefix-testing the next line start.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
