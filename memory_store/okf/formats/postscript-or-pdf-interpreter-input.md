---
type: format-family
title: "Postscript Or PDF Interpreter Input format"
description: "Structure and invariants for the postscript-or-pdf-interpreter-input input format."
tags: ["postscript-or-pdf-interpreter-input", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Ghostscript can process both PostScript and PDF-like content through the rasterizer front end. PDFI state is interpreter-owned: a context may exist separately from the stream object it should reference. The bug requires a mismatch between context lifetime and input-stream setup, not merely malformed PDF syntax.

### Harness Links
- [[libfuzzer-ghostscript-gstoraster]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
