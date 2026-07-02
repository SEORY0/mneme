---
type: format-family
title: "Quicktime Mp4 Format"
description: "Input contract facts for quicktime-mp4."
tags: ["quicktime-mp4", "round-30"]
okf_support: 0
train_only: true
---
# Quicktime Mp4 Format

## Round 30 Factual Contract

### Schema / Invariants
- QuickTime/MP4 recognition accepts a big-endian atom stream whose first recognized atom carries a known video brand. Atoms use a big-endian size followed by a four-character type. The parser handles top-level movie, track, media, sample-table, user-data, and file-type atoms, and nested user-data records use the same size-plus-four-character-type record convention. User-data records can dispatch into plain reference strings, Nikon tag records, and camera tag records; sample descriptions are reached through a track/media/sample-table hierarchy or equivalent parser state.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
