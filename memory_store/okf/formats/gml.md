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
## Round 37 Factual Contract

### Schema / Invariants
- GML is a text graph format made of keyword/value pairs and bracketed lists.
- A top-level graph list contains node and edge lists; nodes need integer ids, and edges refer to source and target ids.
- Attribute values may be numbers, quoted strings, or nested lists.
- The igraph reader first builds a GML tree, then scans nodes and edges to infer attribute names and types before a second pass populates graph attribute arrays.
- GML is a bracketed text graph format with top-level key/value pairs.
- The reader recognizes a top-level Version field and the first graph object.
- A graph object contains node and edge lists; nodes require integer ids, and edges use integer source and target ids referring to those nodes.
- Node and edge attributes are inferred as numeric or string across a first pass, with value vectors allocated before edge translation and vertex attribute population.

### Harness Links
- [[honggfuzz-wrapper]]
- [[honggfuzz-wrapper-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
