---
type: format-family
title: "Postscript Eps format"
description: "Round 8 descriptive format facts for postscript-eps."
resource: cybergym://format/postscript-eps
tags: ["postscript-eps", "round-8"]
okf_support: 1
---
# Postscript Eps Format

## Round 8 Factual Contract

### Schema / Invariants
- The input is a PostScript or EPS stream read from memory-backed FILE I/O. Ordinary PostScript headers and EPS examples reach document loading, but malformed binary tails can shift failure into generic interpreter handling rather than the target variable-initialization path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

