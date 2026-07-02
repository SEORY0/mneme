---
type: format-family
title: "HMP"
description: "Round 36 factual format contract for hmp."
tags: ["hmp", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# HMP

## Round 36 Factual Contract

### Schema / Invariants
- HMP is selected by its magic at the start of the whole model file. The packed terrain header carries version, scale fields, triangle sizes, a vertex-grid width/count relation, skin count, skin dimensions, total vertices, triangle count, frame count, and flags. The HMP loader validates a minimum file/header size, nonzero triangle sizes, a positive grid, and a nonzero frame count before material parsing. Skin metadata is consumed before the later vertex-size check, so declared skin count and available skin records are the important relation.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
