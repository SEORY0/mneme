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
