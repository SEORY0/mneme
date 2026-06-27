---
type: format-family
title: "MP3 ID3V2 format"
description: "Structure and invariants for the mp3-id3v2 input format."
tags: ["mp3-id3v2", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- An MP3 stream may start with an ID3v2 tag whose header declares the total tag payload size. Frames inside the tag have an identifier, a frame payload length, flags, and frame-specific payload. APIC payloads contain an encoding byte followed by string fields separated by NUL delimiters before picture data.

### Harness Links
- [[libfuzzer-gpac-probe-analyze]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
