---
type: format-family
title: "Aac Loas Latm Format"
description: "Input contract facts for aac-loas-latm."
tags: ["aac-loas-latm", "round-30"]
okf_support: 1
train_only: true
---
# Aac Loas Latm Format

## Round 30 Factual Contract

### Schema / Invariants
- LOAS/LATM input starts with a sync and mux-length envelope, followed by AudioMuxElement data. StreamMuxConfig precedes the raw AAC payload when a new mux config is present. PayloadLengthInfo is followed immediately by AAC raw-data bits; there is no byte-alignment boundary before the payload. ER AAC LC configuration can select an HCR-capable single-channel element list with global gain, ICS info, section data, scalefactors, tool flags, HCR side information, and spectral data. HCR spectral data is bit-oriented, and non-priority codewords may be consumed from the right side of the spectral block.

### Harness Links
- [[afl-stdin-libfuzzer-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 33 Factual Contract

### Schema / Invariants
- LOAS frames contain a sync and mux-length envelope around LATM AudioMuxElement data. A StreamMuxConfig can precede each raw payload and carries AudioSpecificConfig fields such as object type, sampling-frequency index, channel configuration, and SBR signaling. PayloadLengthInfo is followed by raw AAC/SBR bits without a byte-alignment boundary. SBR headers carry start and stop frequency bands, crossover band, optional frequency-scale and noise-band fields, and optional limiter fields; AAC-ELD uses a low-delay SBR header path while HE-AAC uses hierarchical SBR signaling.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
