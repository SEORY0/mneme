---
type: format-family
title: audio-container format
description: Format contract for audio-container.
resource: cybergym://format/audio-container
tags: [audio-container]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `audio-container` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The libsndfile front end autodetects several audio containers from raw file magic. Common PCM
  containers carry channel count, samplerate, frame sizing, and data chunks in their own endian/layout
  conventions. WAV-style channel count is limited by its field width, so formats with wider channel
  metadata may be more promising for this class.

### Harness Links
- [[libfuzzer-virtual-io]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
