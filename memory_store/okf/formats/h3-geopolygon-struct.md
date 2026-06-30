---
type: format-family
title: "H3 Geopolygon Struct Format"
description: "Round 26 descriptive structure and invariant facts for h3-geopolygon-struct."
tags: ["h3-geopolygon-struct", "round-26"]
okf_support: 1
train_only: true
---
# H3 Geopolygon Struct Format

## Round 26 Factual Contract

### Schema / Invariants
- The H3 input describes a polygon: a resolution field, a hole-count field, then loop records. Each loop record contains a vertex count followed by latitude/longitude coordinate pairs, and hole loops repeat that same record shape. The experimental max-size routine estimates using overlapping bounding boxes and compact cells, while the writer iterates cells using the requested containment mode.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
