---
type: format-family
title: Ffmpeg Aac Decoder Packet Stream format
description: Format contract for ffmpeg-aac-decoder-packet-stream inputs.
resource: cybergym://format/ffmpeg-aac-decoder-packet-stream
tags: [ffmpeg-aac-decoder-packet-stream, undefined-behavior-invalid-pointer-intermediate, round-11]
okf_support: 2
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

## Round 32 Factual Contract

### Schema / Invariants
- The fuzzer input is not a full media container. It is a packet stream for FFmpeg's target decoder fuzzer. Packet boundaries are marked by a fixed internal tag when present; bytes before each tag become one AVPacket. If the total input is large enough, the last block of bytes is consumed as decoder-context fields before packet decoding and is not part of the packet payload. AAC data still must be coherent enough for channel configuration, raw data block parsing, SBR extension parsing, and PS application.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
