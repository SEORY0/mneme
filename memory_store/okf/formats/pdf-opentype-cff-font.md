---
type: format-family
title: "PDF Opentype CFF Font Format"
description: "Round 26 descriptive structure and invariant facts for pdf-opentype-cff-font."
tags: ["pdf-opentype-cff-font", "round-26"]
okf_support: 1
train_only: true
---
# PDF Opentype CFF Font Format

## Round 26 Factual Contract

### Schema / Invariants
- A CFF font starts with a header followed by Name INDEX, Top DICT INDEX, String INDEX, Global Subr INDEX, and offset-referenced structures such as charset, encoding, Private DICT, local subrs, and CharStrings. In this harness the reliable carrier was not a bare CFF stream: the CFF table needed to sit inside an OpenType sfnt wrapper embedded as a PDF FontFile stream, and the PDF page needed to select the font in content so Ghostscript loaded it.

### Harness Links
- [[libfuzzer-gstoraster-stdin]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
