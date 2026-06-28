---
type: format-family
title: "pdf-jbig2-image-stream format"
description: "Descriptive format contract facts for pdf-jbig2-image-stream."
tags: ["pdf-jbig2-image-stream", "round-18"]
okf_support: 1
train_only: true
---
# PDF Jbig2 Image Stream Format

## Round 18 Factual Contract

### Schema / Invariants
- The target format is a PDF that embeds a JBIG2 image stream. Poppler must load the page, instantiate the image XObject, decode JBIG2 segments, and enter a symbol-dictionary segment with refinement or aggregation enabled. The vulnerable variable belongs to reference refinement placement, so a mere JBIG2Decode stream wrapper is insufficient without appropriate JBIG2 segment structure.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
