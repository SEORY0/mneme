---
type: format-family
title: "assimp-mdl7-model format"
description: "Structure and reachability facts for assimp-mdl7-model."
resource: cybergym://format/assimp-mdl7-model
tags: ["assimp-mdl7-model"]
okf_support: 1
---
# Assimp Mdl7 Model Format

## Round 9 Factual Contract

### Schema / Invariants
- MDL7 inputs begin with an MDL7 header carrying structure sizes and counts, followed by group
  records.
- Each group can contain skin records with a type, width, height, fixed-size texture name, and type-
  dependent payload such as embedded pixels or an external texture string.
- Header structure-size fields must match the importer constants or the loader rejects the file
  before skin parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
