---
type: format-family
title: wav-ima-adpcm format
description: "Round 23 descriptive structure and invariant facts for wav-ima-adpcm."
resource: cybergym://format/wav-ima-adpcm
tags: ["wav-ima-adpcm", "round-23"]
okf_support: 1
train_only: true
---
# Wav Ima Adpcm Format

## Round 23 Factual Contract

### Schema / Invariants
- WAV IMA ADPCM uses a RIFF/WAVE envelope with a fmt chunk containing codec, channel count, sample rate, byte rate, block alignment, bit depth, extension length, and samples per block, followed by a data chunk of ADPCM blocks. The decoder expects a per-channel predictor header, then packed nibbles expanded in groups.

### Harness Links
- [[afl-libfuzzer-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
