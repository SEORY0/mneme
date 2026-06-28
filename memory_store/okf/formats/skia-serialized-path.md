---
type: format-family
title: skia-serialized-path format
description: "Round 23 descriptive structure and invariant facts for skia-serialized-path."
resource: cybergym://format/skia-serialized-path
tags: ["skia-serialized-path", "round-23"]
okf_support: 1
train_only: true
---
# Skia Serialized Path Format

## Round 23 Factual Contract

### Schema / Invariants
- A serialized SkPath begins with a packed header carrying version, type, and fill metadata. The public general-path form then carries point, conic-weight, and verb counts, followed by point data, conic data, verb bytes, and alignment padding. Verbs are interpreted in reverse order during reconstruction.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
