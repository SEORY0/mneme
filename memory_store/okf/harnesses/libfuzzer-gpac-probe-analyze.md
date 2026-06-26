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
