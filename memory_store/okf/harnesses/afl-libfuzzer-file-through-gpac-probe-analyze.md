---
type: harness-contract
title: "Afl Libfuzzer File Through Gpac Probe Analyze Harness"
description: "Round 7 input contract facts for afl-libfuzzer-file-through-gpac-probe-analyze."
tags: ["afl-libfuzzer-file-through-gpac-probe-analyze", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer File Through Gpac Probe Analyze Harness

## Round 7 Input Contract
- The selected GPAC fuzzer writes raw input to a temporary file and runs the probe/analyze filter
graph. Direct raw ID3 is not enough; the bytes must be classified as a media container that routes
to the MPEG-TS demuxer and ID3 PES reframer.

## Round {ROUND} Format Links
- [[mpeg-ts-with-id3-metadata]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
