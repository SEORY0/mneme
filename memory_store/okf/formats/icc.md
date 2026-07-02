---
type: format-family
title: "ICC Format"
description: "Round 26 descriptive structure and invariant facts for icc."
tags: ["icc", "round-26"]
okf_support: 1
train_only: true
---
# ICC Format

## Round 26 Factual Contract

### Schema / Invariants
- ICC parsing requires a coherent profile header, the standard color-management magic, a bounded tag table, and tag records whose declared ranges stay inside the profile. Transfer response curves may be sampled curve tags or parametric curve tags; in this implementation both representations share storage in the curve object, so sampled-table metadata and parametric coefficients overlap.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
