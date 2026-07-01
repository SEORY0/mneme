---
type: format-family
title: "postscript/dos-eps format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/postscript-dos-eps"
tags: ["postscript-dos-eps", "round-35"]
okf_support: 1
train_only: true
---
# postscript/dos-eps Format

## Round 35 Factual Contract
### Schema / Invariants
- The libspectre reader accepts raw PostScript streams, DSC-structured PostScript with header/page/trailer comments, EPS-style documents, and DOS EPS wrappers. DSC parsing recognizes document/page counts, bounding boxes, page order, orientation, document media, page media, embedded document/resource blocks, and binary/data sections. DOS EPS adds a binary wrapper header containing a marker plus fixed-width section offsets and lengths before the PostScript section.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
