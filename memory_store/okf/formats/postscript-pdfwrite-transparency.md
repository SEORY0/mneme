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
