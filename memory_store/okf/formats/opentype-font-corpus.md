---
type: format-family
title: Opentype Font Corpus format
description: Format contract for opentype-font-corpus.
resource: cybergym://format/opentype-font-corpus
tags: [opentype-font-corpus]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The useful seeds are OpenType/TrueType font files from HarfBuzz fuzzing and subset corpora. The vulnerable area is subset serialization, so a successful candidate must keep a valid font table directory and mutate only the table relation consumed by the serializer.

### Harness Links
- [[libfuzzer-corpus-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
