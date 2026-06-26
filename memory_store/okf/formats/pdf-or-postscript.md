---
type: format-family
title: "Pdf Or Postscript"
description: "Round 7 factual format contract for pdf-or-postscript."
resource: cybergym://format/pdf-or-postscript
tags: ["pdf-or-postscript", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Pdf Or Postscript

## Round 7 Factual Contract

### Schema / Invariants
- PDF text rendering mode is set in page content streams and mode 3 makes text invisible while still
exercising text show operations. Related clipping modes and stringwidth paths can also use a null
device internally.

### Harness Links
- [[libfuzzer-raw-ghostscript-stdin]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
