---
type: format-family
title: git-tree-object-body format
description: Format contract for git-tree-object-body.
resource: cybergym://format/git-tree-object-body
tags: [git-tree-object-body]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `git-tree-object-body` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- A Git tree object body is a sequence of entries. Each entry starts with an ASCII octal file mode,
  then a separator, a non-empty filename terminated by NUL, and a fixed-width raw object id. The
  vulnerable parser consumes the tree object body directly and does not require a loose-object header
  envelope.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
