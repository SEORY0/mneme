---
type: format-family
title: "Assimp Model format"
description: "Descriptive contract facts for Assimp Model."
resource: "cybergym://format/assimp-model"
tags: ["assimp-model", "round-6"]
okf_support: 2
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

## Round 18 Factual Contract

### Schema / Invariants
- Assimp accepts whole model files selected by importer signatures. To reach SortByPTypeProcess, the imported scene must contain at least one mesh with face and primitive-type metadata that survives earlier post-processing stages.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- The harness accepts raw model bytes without an extension and relies on signature or content-based importer detection. Collada XML and Wavefront OBJ both reach import code; external resource references are the relevant path because the cleanup filter only runs when importers try to open secondary files.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 38 Factual Contract

### Schema / Invariants
- Assimp import selection in this harness has no useful extension hint, so formats must be selected by content signatures. OBJ can be selected by recognizable Wavefront syntax and uses material-library directives for secondary file loading. LWS is line-oriented text with a magic scene token, a version line, and object-loading records that reference external object files. LWS resolves those object paths through Exists and then queues external loads. glTF/glb importers in this build require a filename extension and therefore lose selection under the extensionless memory filename; X3D can catch extensionless inputs broadly but behaves as a minimal importer here.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
