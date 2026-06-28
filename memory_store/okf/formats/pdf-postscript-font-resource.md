---
type: format-family
title: Pdf Postscript Font Resource format
description: Format contract for pdf/postscript font resource inputs.
resource: cybergym://format/pdf-postscript-font-resource
tags: [pdf-postscript-font-resource, invalid-font-type-use, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The fuzzer accepts raw PDF or PostScript. A Type 0 font uses an encoding/CMap plus a DescendantFonts array that should contain CIDFont dictionaries or resources; invalid descendants can be represented as ordinary Type 1, TrueType, nested Type 0, or PostScript resources, but many malformed forms are rejected without rendering.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-gstoraster]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
