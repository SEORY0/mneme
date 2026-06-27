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

## Round 14 Factual Contract

### Schema / Invariants
- The active input is a raw libgit2 object body. The fuzzer tries the same bytes as blob, tree, commit, and tag content. Commit and tag bodies can contain signature lines with decimal timestamp and timezone fields, but the object parser does not require a loose-object envelope around the bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
