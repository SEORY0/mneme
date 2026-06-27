---
type: format-family
title: "Ffmpeg Rv60 Elementary Packet Stream format"
description: "Structure and invariants for the ffmpeg-rv60-elementary-packet-stream input format."
tags: ["ffmpeg-rv60-elementary-packet-stream", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- RV60 decoding operates on codec packets containing frame headers, slice descriptors, and slice payload data. The described bug concerns initializing a per-slice bitreader with a size inconsistent with the actual allocated slice buffer, so the input must pass frame-header parsing and create at least one slice whose declared boundaries differ from the accessible payload.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
