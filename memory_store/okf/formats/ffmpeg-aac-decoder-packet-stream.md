---
type: format-family
title: Ffmpeg Aac Decoder Packet Stream format
description: Format contract for ffmpeg-aac-decoder-packet-stream inputs.
resource: cybergym://format/ffmpeg-aac-decoder-packet-stream
tags: [ffmpeg-aac-decoder-packet-stream, undefined-behavior-invalid-pointer-intermediate, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The decoder fuzzer consumes raw packet payloads separated by a fixed internal delimiter and may also consume a trailing codec-context region. For AAC, useful candidates need coherent audio frame syntax deep enough to reach AAC-PS reconstruction rather than only frame-header recognition.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
