---
type: format-family
title: "Postscript Or Pdf"
description: "Round 7 factual format contract for postscript-or-pdf."
resource: cybergym://format/postscript-or-pdf
tags: ["postscript-or-pdf", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Postscript Or Pdf

## Round 7 Factual Contract

### Schema / Invariants
- Ghostscript accepts PostScript programs and PDF files from the same raw stdin harness. ICC/color-
management paths can be requested with device color spaces, calibrated color spaces, patterns, or
PDF ICCBased color spaces, but the target bug depends on an internal allocation-failure
interleaving.

### Harness Links
- [[libfuzzer-raw-ghostscript-stdin]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
