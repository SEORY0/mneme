---
type: harness-contract
title: "Libfuzzer Ffmpeg Vp9 Metadata Bsf harness"
description: "Round 23 input contract facts for libfuzzer-ffmpeg-vp9-metadata-bsf."
tags: ["libfuzzer-ffmpeg-vp9-metadata-bsf", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Ffmpeg Vp9 Metadata Bsf Harness

## Round 23 Input Contract
- If the input is large enough, the trailing configuration block initializes codec parameters; otherwise the packet data is sent directly through the bitstream-filter fuzzer. Packet boundaries are determined by a fixed delimiter, but a single packet without the delimiter is accepted as one packet.

## Round 23 Format Links
- [[vp9-raw-superframe]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
