---
type: format-family
title: "CAF"
description: "Round 36 factual format contract for caf."
tags: ["caf", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# CAF

## Round 36 Factual Contract

### Schema / Invariants
- CAF recognition in this libsndfile path depends on the top-level CAF marker, version/flags header, and a descriptor chunk marker as the mandatory first chunk. Descriptor parsing then reads a fixed-width chunk size followed by descriptor payload fields, so EOF inside that size field reaches the binary-header reader before audio data is needed.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
