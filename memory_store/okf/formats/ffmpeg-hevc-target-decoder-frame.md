---
type: format-family
title: Ffmpeg Hevc Target Decoder Frame format
description: Format contract for ffmpeg-hevc-target-decoder-frame inputs.
resource: cybergym://format/ffmpeg-hevc-target-decoder-frame
tags: [ffmpeg-hevc-target-decoder-frame, use-of-uninitialized-value, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The FFmpeg target decoder fuzzer treats the input primarily as codec packet data for the selected HEVC decoder. When the input is large enough, a trailing context area can configure decoder options, extradata, or parser-related behavior; otherwise the leading data is decoded directly as packet bytes.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
