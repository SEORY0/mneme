---
type: format-family
title: pdf-postscript format
description: Structure and reachability facts for pdf-postscript inputs.
tags: [pdf-postscript]
okf_support: 0
---
# PDF Postscript Format

## Round 10 Factual Contract

### Schema / Invariants
- The harness accepts PostScript or PDF-like data directly on stdin. PDF content streams can carry interpreter operands, and very large operand sequences stress stack extension and movement without needing a fully useful rendered page.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
