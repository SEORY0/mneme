---
type: format-family
title: "Git Patch"
description: "Round 19 factual format contract for git-patch."
resource: cybergym://format/git-patch
tags: ["git-patch", "format-contract", "round-19"]
okf_support: 10
train_only: true
---

# Git Patch

## Round 19 Factual Contract

- The patch parser recognizes diff headers, optional index/mode lines, file path headers beginning with old/new markers, hunk headers, and optional binary patch sections. The vulnerable relation concerns a path header whose payload after the marker is empty, allowing an empty buffer detach instead of a valid filename string.
- Harness link: [[afl-libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 27 Factual Contract

- The patch parser accepts a git diff header, an index header, then a GIT binary patch body.
- Binary sides start with a literal or delta size line followed by base85 data lines whose first character encodes decoded length.
- The parser expects encoded data and a newline after that marker.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
