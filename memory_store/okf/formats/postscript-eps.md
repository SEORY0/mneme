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

## Round 35 Factual Contract

### Schema / Invariants
- PostScript/EPS inputs are raw text or wrapper bytes consumed as a stream. A DOS EPS wrapper starts with a distinct binary signature followed by fixed-width little-endian section descriptors for the embedded PostScript region and optional preview regions. If that wrapper is recognized, the parser seeks to the declared PostScript section and then scans ordinary DSC lines; the wrapper header therefore must either be complete or the failed fixed-size reads become the relevant invariant.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
