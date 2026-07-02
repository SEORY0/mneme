---
type: format-family
title: "FLAC CLI Fuzzer Input Format"
description: "Round 26 descriptive structure and invariant facts for flac-cli-fuzzer-input."
tags: ["flac-cli-fuzzer-input", "round-26"]
okf_support: 1
train_only: true
---
# FLAC CLI Fuzzer Input Format

## Round 26 Factual Contract

### Schema / Invariants
- FLAC files begin with the FLAC marker, followed by metadata blocks and then audio frames. Vorbis-comment metadata contains a vendor string and key/value comments such as ReplayGain reference, gain, and peak fields. Stream-info metadata later supplies sample geometry including bits per sample. Valid frames require internally consistent frame headers and frame checksums for the decoder to reach audio synthesis.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
