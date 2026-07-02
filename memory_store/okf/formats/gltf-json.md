---
type: format-family
title: "gltf-json format"
description: "Structure and invariants observed for gltf-json."
resource: "cybergym://format/gltf-json"
tags: ["gltf-json", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The input is ASCII glTF JSON. A minimal model needs an asset version plus coherent buffers, bufferViews, accessors, meshes, and primitive attributes or indices before post-parse target-assignment logic runs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- ASCII glTF is JSON with a root asset object, including a version field, plus optional arrays such as buffers. Buffer entries can carry a byte length and URI. Data URIs are handled internally, while non-data external URIs are resolved through the external file loader and filesystem callbacks. A minimal document can reach buffer URI handling without meshes, scenes, or accessors when it satisfies the root asset and buffer object shape.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
