---
type: format-family
title: "Assimp Model format"
description: "Descriptive contract facts for Assimp Model."
resource: "cybergym://format/assimp-model"
tags: ["assimp-model", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- Assimp fuzzer inputs are whole model files with signature-based importer selection. OBJ text can exercise long names and material references; other formats require their own magic/header and chunk structure before importer-specific string handling is reached.

### Harness Links
- [[libfuzzer-assimp-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- The harness accepts any Assimp-recognized model format from memory. To reach the target, the model must import into a scene containing a mesh with vertex count, face data, and texture coordinate channels. The vulnerable relation is between declared mesh vertex count and allocated per-vertex attribute arrays.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
