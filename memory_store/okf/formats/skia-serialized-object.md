---
type: format-family
title: "skia-serialized-object format"
description: "Structure and reachability facts for skia-serialized-object."
resource: cybergym://format/skia-serialized-object
tags: ["skia-serialized-object"]
okf_support: 1
---
# Skia Serialized Object Format

## Round 9 Factual Contract

### Schema / Invariants
- The reachable targets deserialize Skia binary object streams for image filters or regions.
- These are not ordinary image files; small integer fields can be parsed as serialized object
  headers and region bounds.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
