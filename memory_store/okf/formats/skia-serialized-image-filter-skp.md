---
type: format-family
title: "Skia Serialized Image Filter Skp Format"
description: "Input contract facts for skia-serialized-image-filter-skp."
tags: ["skia-serialized-image-filter-skp", "round-30"]
okf_support: 0
train_only: true
---
# Skia Serialized Image Filter Skp Format

## Round 30 Factual Contract

### Schema / Invariants
- The harness input is a raw Skia flattened object stream for an image filter. A reachable picture-image-filter object carries a has-picture gate, an embedded SKP-style picture header, picture-data tags, a reader-op data chunk, and a paint table. Text-RSXform picture ops carry a paint reference, glyph count, flags, counted text data, a transform array, and optionally a cull rectangle. Paint entries can carry effect flattenables; a simple color shader is sufficient to make the shader path non-null.

### Harness Links
- [[libfuzzer-skia-image-filter-deserialize]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
