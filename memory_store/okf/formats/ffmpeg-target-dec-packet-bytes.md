---
type: format-family
title: "Ffmpeg Target Dec Packet Bytes format"
description: "Structure and invariants for the ffmpeg-target-dec-packet-bytes input format."
tags: ["ffmpeg-target-dec-packet-bytes", "round-20"]
okf_support: 2
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The decoder consumes compressed packet bytes for the selected codec, not a container file unless the target wrapper adds one. RV60 reachability requires enough frame and slice syntax for the decoder to initialize dimensions, slices, QP state, and CU recursion.
- MSMPEG4 decoder reachability requires compressed video packet syntax sufficient for picture header, macroblock mode, coded-block pattern, and intra block coefficient decoding. The relevant state is internal bitstream syntax rather than an outer AVI/ASF container.

### Harness Links
- [[oss-fuzz-ffmpeg-target-dec-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
