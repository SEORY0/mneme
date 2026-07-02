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

## Round 36 Factual Contract

### Schema / Invariants
- RIFF/WAVE inputs use a RIFF container header, WAVE form marker, a format chunk, optional fact data, and a data chunk. Ordinary MS ADPCM carries channel count, sample rate, byte rate, block alignment, bit width, extension size, samples-per-block, coefficient count, and coefficient pairs. WAVE extensible instead carries valid-bits, channel mask, and a subtype GUID; when that subtype is MS ADPCM, shared union fields feed the MS ADPCM initializer.

### Harness Links
- [[afl-libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
