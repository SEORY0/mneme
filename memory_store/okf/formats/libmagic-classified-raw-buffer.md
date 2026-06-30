---
type: format-family
title: "Libmagic Classified RAW Buffer Format"
description: "Round 26 descriptive structure and invariant facts for libmagic-classified raw buffer."
tags: ["libmagic-classified-raw-buffer", "round-26"]
okf_support: 1
train_only: true
---
# Libmagic Classified RAW Buffer Format

## Round 26 Factual Contract

### Schema / Invariants
- The harness loads libmagic's compiled rules and classifies the submitted file bytes directly. Search rules can scan the raw buffer without copying it into a NUL-padded value union; string rules with whitespace-compaction modifiers take the slower comparison path that reasons about input whitespace and may require an input slice length.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
