---
type: format-family
title: "Mpeg Ts With Id3 Metadata"
description: "Round 7 factual format contract for mpeg-ts-with-id3-metadata."
resource: cybergym://format/mpeg-ts-with-id3-metadata
tags: ["mpeg-ts-with-id3-metadata", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Mpeg Ts With Id3 Metadata

## Round 7 Factual Contract

### Schema / Invariants
- The successful reachability carrier is MPEG-TS with a PAT, PMT, metadata PES stream signaling, and
an ID3v2 tag in the PES payload. ID3v2 frames use a frame identifier, a synchsafe length, flags, and
a frame body; an oversized claimed frame length can affect parser copy bounds.

### Harness Links
- [[afl-libfuzzer-file-through-gpac-probe-analyze]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
