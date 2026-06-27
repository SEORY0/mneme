---
type: format-family
title: postscript-pdf-for-ghostscript-pdfwrite format
description: Structure and reachability facts for postscript-pdf-for-ghostscript-pdfwrite inputs.
tags: [postscript-pdf-for-ghostscript-pdfwrite]
okf_support: 0
---
# Postscript PDF For Ghostscript Pdfwrite Format

## Round 10 Factual Contract

### Schema / Invariants
- The fuzzer input is interpreter content for Ghostscript. PostScript can set device parameters, draw pages, and use pdfmark/pdfwrite features; malformed PDF input may be accepted by the same wrapper but needs enough structure to reach pdfwrite device internals.

### Harness Links
- [[libfuzzer-ghostscript-device-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
