---
type: format-family
title: "Fio Ini Job File format"
description: "Structure and invariants for the fio-ini-job-file input format."
tags: ["fio-ini-job-file", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- fio job files are line-oriented ini text with section headers and key-value options. A normal global section plus at least one job section is accepted; options such as rw, size, filename, and description are parsed from text lines.

### Harness Links
- [[afl-style-fio-parseini-buffer-with-trailing-type-byte]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
