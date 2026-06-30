---
type: format-family
title: "Hevc Annex B Bitstream Format"
description: "Input contract facts for hevc-annex-b-bitstream."
tags: ["hevc-annex-b-bitstream", "round-30"]
okf_support: 0
train_only: true
---
# Hevc Annex B Bitstream Format

## Round 30 Factual Contract

### Schema / Invariants
- The useful seeds were Annex-B HEVC byte streams. Parser reach requires parameter-set NAL units before coded picture slices, and NAL-boundary truncation preserves reach better than arbitrary byte truncation. The target path appears on intra-coded pictures with small transform units where the chroma transform derives neighbor availability from previously processed luma transform units.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
