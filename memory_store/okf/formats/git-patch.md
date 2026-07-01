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

## Round 34 Factual Contract

### Schema / Invariants
- Git patch input uses a diff header, optional mode/index metadata, old/new file path headers, and hunk headers with line bodies. The path parser trims header payloads and can represent an empty path as a NULL detached buffer. Filename validation compares diff-header paths with file-header paths and falls back to the diff-header path when a file-header path is absent.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
