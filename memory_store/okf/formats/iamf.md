---
type: format-family
title: "Iamf"
description: "Round 12 factual format contract for iamf."
resource: cybergym://format/iamf
tags: ["iamf", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Iamf

## Round 12 Factual Contract

### Schema / Invariants
- IAMF streams are composed of OBU-style records with header fields, size coding, descriptor OBUs, audio element metadata, mix presentation metadata, and padding or reserved bit regions. Parser reachability depends on coherent descriptor order and declared sizes.

### Harness Links
- [[file-parser]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Raw IAMF files are a sequence of OBUs. The demuxer probe expects a sequence-header OBU carrying the IAMF magic before descriptor OBUs. Codec-config OBUs contain a LEB-coded config id, a four-byte codec tag, sample count, audio roll distance, then codec-specific decoder configuration. AAC decoder config is MP4-style descriptor data with tag bytes and variable-length size fields.

### Harness Links
- [[libfuzzer-ffmpeg-demuxer-iamf]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 28 Factual Contract

### Schema / Invariants
- IAMF streams are made of OBU records. Each OBU begins with a bit-packed type/flag byte and a LEB128 size, followed by optional trimming or extension fields before the payload. A sequence-header OBU identifies the stream, descriptor OBUs define codec configuration, audio elements, and mix presentation, and later parameter/audio-frame OBUs are read by the packet path.

### Harness Links
- [[libfuzzer-ffmpeg-demuxer-iamf]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
