---
type: format-family
title: "Gml"
description: "Round 7 factual format contract for gml."
resource: cybergym://format/gml
tags: ["gml", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Gml

## Round 7 Factual Contract

### Schema / Invariants
- GML is a bracketed text graph format with top-level graph lists containing node and edge lists.
Nodes require integer identifiers; edges refer to source and target node identifiers. The igraph
reader builds an intermediate tree and then translates node ids, edges, and simple attributes into
graph structures.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
