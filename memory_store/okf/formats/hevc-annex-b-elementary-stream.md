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

## Round 30 Factual Contract

### Schema / Invariants
- HEVC Annex-B inputs are start-code-delimited NAL units. For this path, VPS, SPS, PPS, and a VCL slice must remain coherent; the PPS must be from an RExt-compatible stream so range-extension PPS fields are parsed. PPS RBSP edits must be converted back to escaped NAL payload bytes. The relevant PPS relation is the chroma-QP offset-list enable flag, list length, and per-CU slice/CABAC signalling; corrupting parameter-set recognition or shifting CABAC too early produces clean exits.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 34 Factual Contract

### Schema / Invariants
- The input is a raw HEVC elementary stream, not a container. Start-code-delimited parameter-set NAL units must precede the VCL slice. Streams with coherent intra prediction, chroma enabled, and small transform-unit structure reach the target CTB reconstruction path; arbitrary parameter-set stubs, late truncation, or unrelated multi-frame carriers either decode cleanly or crash in unrelated prediction/filtering code.

### Harness Links
- [[libfuzzer-raw-libhevc-decoder]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
