---
type: format-family
title: "Ani Riff"
description: "Round 7 factual format contract for ani-riff."
resource: cybergym://format/ani-riff
tags: ["ani-riff", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Ani Riff

## Round 7 Factual Contract

### Schema / Invariants
- ANI is a RIFF-family format: an outer RIFF marker is followed by a little-endian RIFF size and then
an ACON form marker before chunk records. Chunk records use an identifier plus a little-endian size
and payload.

### Harness Links
- [[libfuzzer-raw-qbuffer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
