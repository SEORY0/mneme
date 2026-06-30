---
type: format-family
title: "hevc-annex-b-elementary-stream format"
description: "Structure, build skeleton, and bug-prone areas of the hevc-annex-b-elementary-stream input format."
resource: cybergym://format/hevc-annex-b-elementary-stream
tags: ["hevc-annex-b-elementary-stream", "round-29"]
okf_support: 0
---
# HEVC Annex B Elementary Stream Format

## Round 29 Factual Contract

### Schema / Invariants
- The useful carrier is a raw HEVC elementary stream made of start-code-delimited NAL units, not a container. Parameter sets must precede slices, and the target slice syntax depends on SPS and PPS gates such as long-term-reference presence, picture-order-count width, short-term reference sets, and slice-header flags. RBSP edits must be converted back to escaped NAL payload bytes so emulation-prevention rules remain valid.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
