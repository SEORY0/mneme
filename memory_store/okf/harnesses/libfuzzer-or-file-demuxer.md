---
type: harness-contract
title: "Libfuzzer Or File Demuxer harness"
description: "Input contract facts for libfuzzer-or-file-demuxer."
tags: ["libfuzzer-or-file-demuxer", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Or File Demuxer Harness

## Round 11 Input Contract
- The extracted source shows FFmpeg demux/decoder fuzzers that feed raw bytes to the relevant parser. The candidate must satisfy MV container probing and header parsing before the table reader reaches the fixed-size name field.

## Format Links
- [[ffmpeg-mv-container]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
