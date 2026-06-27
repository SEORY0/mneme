---
type: format-family
title: "Ffmpeg Dvbsub Packet Stream format"
description: "Structure and invariants for the ffmpeg-dvbsub-packet-stream input format."
tags: ["ffmpeg-dvbsub-packet-stream", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The decoder consumes elementary DVB subtitle packets, not a container. A subtitle segment starts with a sync marker, followed by a segment type, page identifier, segment length, and segment-specific body. CLUT bodies contain a CLUT id/version byte and a sequence of CLUT entries whose flags determine whether full color components are present.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
