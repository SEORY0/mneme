---
type: format-family
title: "Wav Riff Exif"
description: "Round 12 factual format contract for wav-riff-exif."
resource: cybergym://format/wav-riff-exif
tags: ["wav-riff-exif", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Wav Riff Exif

## Round 12 Factual Contract

### Schema / Invariants
- A RIFF/WAV file needs a RIFF container, WAVE form marker, a valid audio format chunk, and then metadata chunks. LIST/INFO-style metadata contains nested four-character markers; an EXIF nested marker dispatches to EXIF subrecords, several of which carry a length followed by string-like data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
