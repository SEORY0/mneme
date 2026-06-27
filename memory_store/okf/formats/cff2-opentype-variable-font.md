---
type: format-family
title: Cff2 Opentype Variable Font format
description: Format contract for cff2-opentype-variable-font inputs.
resource: cybergym://format/cff2-opentype-variable-font
tags: [cff2-opentype-variable-font, null-dereference, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The relevant format is an OpenType variable font with CFF2 outlines and variation tables. Reaching the bug requires a valid sfnt directory and compatible CFF2, variation-axis, and metrics-variation tables so the face is treated as a CFF2 variable font and MVAR application can request size reset actions.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-freetype-ftfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
