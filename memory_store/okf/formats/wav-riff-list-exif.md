---
type: format-family
title: "Wav Riff List Exif"
description: "Round 36 factual format contract for wav-riff-list-exif."
tags: ["wav-riff-list-exif", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Wav Riff List Exif

## Round 36 Factual Contract

### Schema / Invariants
- A WAV file accepted by this harness can be a minimal RIFF/WAVE container containing a PCM fmt chunk, optional metadata chunks, and a data chunk. A LIST chunk is parsed as nested four-character records. When the nested record marker is EXIF, libsndfile dispatches to the EXIF audio metadata parser. EXIF audio records use four-character markers; several string-valued markers are followed by a little-endian declared byte count and then that many bytes of string data, rounded to even length by the parser.

### Harness Links
- [[libfuzzer-sndfile-virtual-io]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
