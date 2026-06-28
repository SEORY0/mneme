---
type: format-family
title: "postscript-raster-document format"
description: "Descriptive format contract facts for postscript-raster-document."
tags: ["postscript-raster-document", "round-18"]
okf_support: 1
train_only: true
---
# Postscript Raster Document Format

## Round 18 Factual Contract

### Schema / Invariants
- The input is a PostScript program interpreted by Ghostscript. Reaching this bug requires a rendering operation that creates an internal bitmap or halftone/tile buffer where vertical replication copies within the same allocation and source and destination ranges overlap.

### Harness Links
- [[libfuzzer-ghostscript-gstoraster]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
