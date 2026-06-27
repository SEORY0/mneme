---
type: format-family
title: "MXF"
description: "Round 19 factual format contract for mxf."
resource: cybergym://format/mxf
tags: ["mxf", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# MXF

## Round 19 Factual Contract

- MXF is a KLV-based container with partition packs, metadata sets, essence containers, and index table segments. The described hot path computes absolute edit-unit offsets from index table segment data; complexity depends on how many segments and edit-unit ranges are present and how lookups are distributed across them.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
