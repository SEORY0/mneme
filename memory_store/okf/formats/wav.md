---
type: format-family
title: "Wav"
description: "Round 7 factual format contract for wav."
resource: cybergym://format/wav
tags: ["wav", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Wav

## Round 7 Factual Contract

### Schema / Invariants
- WAV files use RIFF/WAVE framing with chunk ids and little-endian chunk lengths. A fmt chunk
describes audio layout, LIST chunks can carry INFO metadata subchunks, and chunk payloads are padded
to even length before the data chunk.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
