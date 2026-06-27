---
type: format-family
title: "Gpac Vvc Or Hevc Media Probe Input"
description: "Round 19 factual format contract for gpac-vvc-or-hevc-media-probe-input."
resource: cybergym://format/gpac-vvc-or-hevc-media-probe-input
tags: ["gpac-vvc-or-hevc-media-probe-input", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Gpac Vvc Or Hevc Media Probe Input

## Round 19 Factual Contract

- GPAC probe/analyze detects media from raw bytes using elementary-stream start codes and container signatures. VVC/HEVC elementary streams need parameter-set NAL units before slice or picture data can populate codec state. Tile parsing is downstream of successful sequence, picture, and slice-header parsing.
- Harness link: [[libfuzzer-gpac-probe-analyze]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
