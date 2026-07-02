---
type: format-family
title: "Postscript Pdfwrite Transparency Format"
description: "Round 27 descriptive format facts for postscript-pdfwrite-transparency."
resource: cybergym://format/postscript-pdfwrite-transparency
tags: ["postscript-pdfwrite-transparency", "round-27"]
okf_support: 1
---
# Postscript Pdfwrite Transparency Format

## Round 27 Factual Contract

- Ghostscript accepts PostScript programs directly in this harness.
- For pdfwrite, transparency setup can be expressed with a page-device dictionary enabling transparency and compatibility level, followed by transparency-group begin/end operators around drawing or text operations.
- Direct transparency groups are handled as pdfwrite XObject substreams; using an explicit pdf14 device filter can route drawing through the compositor and avoid the high-level pdfwrite text transition.

### Harness Links
- [[libfuzzer-raw-bytes-to-ghostscript-pdfwrite]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- Ghostscript accepts complete PostScript programs and PDF files as raw stdin for this harness. Pdfwrite transparency setup in PostScript uses a page-device dictionary with transparency-related compatibility settings and transparency group begin/end operations; when the privileged transparency operators are not enabled by startup flags, the shipped example can replace them with no-op fallbacks. PDF transparency can also be expressed with Form XObjects that carry transparency group dictionaries and nested drawing resources. Text clipping can be represented through text rendering modes in PDF or charpath/clip operations in PostScript.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
