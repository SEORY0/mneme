---
type: format-family
title: "Svc H264 Annex B Stream"
description: "Round 12 factual format contract for svc-h264-annex-b-stream."
resource: cybergym://format/svc-h264-annex-b-stream
tags: ["svc-h264-annex-b-stream", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Svc H264 Annex B Stream

## Round 12 Factual Contract

### Schema / Invariants
- The input is a raw H.264/SVC byte stream, commonly Annex-B NAL units, with the same bytes also used by the fuzzer for color format, core count, architecture, and target-layer selectors at fixed early positions. Valid SPS/PPS and slice structure are needed for meaningful header and frame decode.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
