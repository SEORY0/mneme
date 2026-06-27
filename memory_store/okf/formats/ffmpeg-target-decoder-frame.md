---
type: format-family
title: "Ffmpeg Target Decoder Frame format"
description: "Descriptive contract facts for Ffmpeg Target Decoder Frame."
resource: "cybergym://format/ffmpeg-target-decoder-frame"
tags: ["ffmpeg-target-decoder-frame", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The FFmpeg targeted decoder fuzzer treats the raw file as one or more codec packets separated by an internal tag; without a tag, the whole prefix becomes one packet. For MIMIC, a frame has a small little-endian header carrying quality, dimensions, keyframe flag, and coefficient count, followed by compressed bitstream data that is byte-swapped in word-sized chunks before bit reading.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 13 Facts
- The FFmpeg target decoder fuzzer treats the front of the input as one or more raw packet regions separated by a fixed split tag. When the input is large enough, a fixed-size tail configures codec context fields and optional extradata before avcodec_open2 and packet decoding.
