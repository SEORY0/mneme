---
type: format-family
title: "Aac Loas Latm Format"
description: "Input contract facts for aac-loas-latm."
tags: ["aac-loas-latm", "round-30"]
okf_support: 0
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
