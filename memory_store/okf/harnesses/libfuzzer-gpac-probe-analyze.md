---
type: harness-contract
title: "Libfuzzer Gpac Probe Analyze Harness"
description: "Round 7 input contract facts for libfuzzer-gpac-probe-analyze."
tags: ["libfuzzer-gpac-probe-analyze", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Gpac Probe Analyze Harness

## Round 7 Input Contract
- The harness writes the raw input to a temporary file and runs GPAC probe/analyze parsing. There is
no mode byte; format detection is by container signatures, file-extension-like probing, and
elementary-stream start codes.

## Round {ROUND} Format Links
- [[mpeg-video-elementary-or-program-stream]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 19 Input Contract

- The active binary is GPAC fuzz_probe_analyze. It treats the raw input as a media asset in a temporary file and runs GPAC probing and inspection. There is no mode byte or FuzzedDataProvider layout; successful reachability appears in the inspection output and codec-specific parser diagnostics.
- Format link: [[gpac-vvc-or-hevc-media-probe-input]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 20 Input Contract
- The GPAC probe/analyze harness writes the raw input bytes as a temporary media asset and runs format probing and analysis. The fuzzer input is the media file itself; there is no leading mode selector or FuzzedDataProvider carving.

## Round 20 Format Links
- [[mp3-id3v2]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
