---
type: format-family
title: "SKIA Pathmeasure Fuzz Stream Format"
description: "Round 26 descriptive structure and invariant facts for skia-pathmeasure-fuzz-stream."
tags: ["skia-pathmeasure-fuzz-stream", "round-26"]
okf_support: 1
train_only: true
---
# SKIA Pathmeasure Fuzz Stream Format

## Round 26 Factual Contract

### Schema / Invariants
- The fuzz input is a compact Skia path stream rather than a serialized image. The leading control byte selects path-measure options, several little-endian scalar fields configure distance and query behavior, and the remaining bytes are consumed as path verbs and coordinates. Conic path records include endpoints and a weight; segment extraction can later request only a subrange of that curve.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
