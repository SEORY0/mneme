---
type: format-family
title: Openexr Dwa format
description: Format contract for openexr-dwa inputs.
resource: cybergym://format/openexr-dwa
tags: [openexr-dwa, out-of-bounds-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
OpenEXR inputs contain a file header with attributes, chunk metadata, and compressed image chunks. DWA-compressed chunks include a DWA subheader with component counts followed by compressed component streams; the vulnerable relation concerns declared DC component counts versus the component data actually read.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-openexr-check]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
