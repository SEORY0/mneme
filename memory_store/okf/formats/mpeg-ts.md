---
type: format-family
title: "Mpeg Ts format"
description: "Round 28 descriptive format facts for mpeg-ts."
resource: cybergym://format/mpeg-ts
tags: ["mpeg-ts", "round-28"]
okf_support: 0
---
# Mpeg Ts Format

## Round 28 Factual Contract

### Schema / Invariants
- MPEG-TS input is packetized with sync-marked fixed-size packets. PAT sections map programs to PMT packet IDs, and PMT sections declare a PCR carrier plus elementary streams with stream type, elementary PID, and descriptor length. PMT version changes are needed for the demuxer to treat a later table as an update rather than a repeat.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
