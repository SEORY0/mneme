---
type: format-family
title: audio-container-aiff-au format
description: "Round 23 descriptive structure and invariant facts for audio-container-aiff-au."
resource: cybergym://format/audio-container-aiff-au
tags: ["audio-container-aiff-au", "round-23"]
okf_support: 1
train_only: true
---
# Audio Container Aiff Au Format

## Round 23 Factual Contract

### Schema / Invariants
- The relevant formats are framed audio containers with a header declaring encoding, channel count, sample rate, and sample data length. AIFF-C uses chunked metadata and can select floating-point sample encodings; AU has a compact header with data offset, data size, encoding, sample rate, and channel count.

### Harness Links
- [[libfuzzer-libsndfile-virtual-io]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
