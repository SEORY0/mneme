---
type: format-family
title: wav-ms-adpcm format
description: "Round 23 descriptive structure and invariant facts for wav-ms-adpcm."
resource: cybergym://format/wav-ms-adpcm
tags: ["wav-ms-adpcm", "round-23"]
okf_support: 1
train_only: true
---
# Wav Ms Adpcm Format

## Round 23 Factual Contract

### Schema / Invariants
- WAV MS-ADPCM requires RIFF/WAVE chunks, a fmt chunk with the MS-ADPCM format tag, channel count, sample rate, byte rate, block alignment, sample size, extension size, samples-per-block, coefficient count, and coefficient pairs, followed by a data chunk containing ADPCM blocks.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
