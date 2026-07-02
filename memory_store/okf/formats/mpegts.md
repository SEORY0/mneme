---
type: format-family
title: "Mpegts format"
description: "Round 28 descriptive format facts for mpegts."
resource: cybergym://format/mpegts
tags: ["mpegts", "round-28"]
okf_support: 0
---
# Mpegts Format

## Round 28 Factual Contract

### Schema / Invariants
- MPEG-TS reachability required aligned transport packets with sync bytes, payload-start section pointer fields, coherent PAT-to-PMT PID wiring, and valid PSI section lengths and CRCs. The vulnerable MPEG-4 descriptor parser is reached from a PMT program descriptor, not from elementary stream payload. The descriptor body must contain a normal IO descriptor header, an ES descriptor with simple flags, a decoder-config child, and then the SL descriptor child.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
