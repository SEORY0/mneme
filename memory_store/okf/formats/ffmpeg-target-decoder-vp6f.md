---
type: format-family
title: "ffmpeg-target-decoder-vp6f format"
description: "Structure and invariants observed for ffmpeg-target-decoder-vp6f."
resource: "cybergym://format/ffmpeg-target-decoder-vp6f"
tags: ["ffmpeg-target-decoder-vp6f", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The target decoder input is a simple packet stream for a fixed codec. Packet boundaries are found by a fixed marker tag; data before each marker becomes one packet. For VP6F, valid compressed frame payloads can decode even without a file container.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
