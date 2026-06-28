---
type: format-family
title: Mlv format
description: Format contract for mlv.
resource: cybergym://format/mlv
tags: [mlv]
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
- MLV files are block streams. Each block has a tag, declared size, timestamp area, and payload. Several metadata tags contain fixed-width strings read into freshly allocated buffers; if the declared block payload is large enough for the parser branch but the actual file ends early, unchecked reads can leave string bytes uninitialized.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
