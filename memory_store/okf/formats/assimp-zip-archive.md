---
type: format-family
title: "Assimp Zip Archive"
description: "Round 7 factual format contract for assimp-zip-archive."
resource: cybergym://format/assimp-zip-archive
tags: ["assimp-zip-archive", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Assimp Zip Archive

## Round 7 Factual Contract

### Schema / Invariants
- Assimp can treat ZIP archives as container inputs for model formats. The vulnerable path is in the
ZIP disk-open callback, which derives a sibling disk filename by scanning backward for a dot in the
current archive filename.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
