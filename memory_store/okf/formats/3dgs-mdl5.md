---
type: format-family
title: "3dgs Mdl5"
description: "Round 36 factual format contract for 3dgs-mdl5."
tags: ["3dgs-mdl5", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# 3dgs Mdl5

## Round 36 Factual Contract

### Schema / Invariants
- 3D GameStudio MDL5 is a whole-file binary model selected by its MDL signature. Its common header carries model counts and a skin count; for MDL5 skin records, the skin type is followed by per-skin texture dimensions and then texture data. Material setup can inspect embedded textures after the importer parses skins and before post-processing.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
