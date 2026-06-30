---
type: format-family
title: "MXF"
description: "Round 19 factual format contract for mxf."
resource: cybergym://format/mxf
tags: ["mxf", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# MXF

## Round 19 Factual Contract

- MXF is a KLV-based container with partition packs, metadata sets, essence containers, and index table segments. The described hot path computes absolute edit-unit offsets from index table segment data; complexity depends on how many segments and edit-unit ranges are present and how lookups are distributed across them.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 30 Factual Contract

### Schema / Invariants
- MXF is parsed as KLV records: a universal key, a BER-encoded payload length, then the payload. The demuxer first syncs on a header partition pack before parsing metadata KLVs. Some metadata KLVs are local sets made of tag-and-size entries; a TaggedValue local set can contain an indirect value whose payload begins with a fixed-width type key.

### Harness Links
- [[libfuzzer-ffmpeg-dem-mxf]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
