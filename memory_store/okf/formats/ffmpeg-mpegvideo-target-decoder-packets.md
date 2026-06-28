---
type: format-family
title: "Ffmpeg Mpegvideo Target Decoder Packets"
description: "Round 19 factual format contract for ffmpeg-mpegvideo-target-decoder-packets."
resource: cybergym://format/ffmpeg-mpegvideo-target-decoder-packets
tags: ["ffmpeg-mpegvideo-target-decoder-packets", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Ffmpeg Mpegvideo Target Decoder Packets

## Round 19 Factual Contract

- The useful input is raw decoder packet data rather than an MP4 or pcap-style container. MPEG video candidates use start-code-delimited sequence, picture, and slice data; missing-slice bugs require enough valid header state for frame allocation and decoding before omitting or corrupting a slice relation.
- Harness link: [[oss-fuzz-run-poc-ffmpeg-target-decoder]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
