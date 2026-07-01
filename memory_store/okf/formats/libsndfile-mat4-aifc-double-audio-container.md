---
type: format-family
title: "Libsndfile Mat4 Aifc Double Audio Container"
description: "Round 36 factual format contract for libsndfile-mat4-aifc-double-audio-container."
tags: ["libsndfile-mat4-aifc-double-audio-container", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Libsndfile Mat4 Aifc Double Audio Container

## Round 36 Factual Contract

### Schema / Invariants
- AIFC uses a FORM/AIFC chunk envelope with COMM selecting channel count, sample count, sample size, and FL64-style double samples, then SSND carrying offset/blocksize and sample data. MAT4 begins with a scalar samplerate matrix and then a wavedata matrix whose row count is the channel count and column count is the frame count; a big-endian double marker selects the endian-swapping double reader. In these libsndfile paths, double initialization derives effective frames from actual data length and channel width before sf_readf_float consumes frames.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
