---
type: format-family
title: Vc1 Vc1Image Elementary Stream format
description: Format contract for vc1/vc1image elementary stream inputs.
resource: cybergym://format/vc1-vc1image-elementary-stream
tags: [vc1-vc1image-elementary-stream, uninitialized-value-use, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The decoder fuzzer consumes raw codec payloads, not media containers. VC1 samples may be raw elementary streams or RCV-like streams; the selected target here is the VC1IMAGE decoder, so ordinary VC1 video seeds may not exercise the exact block path unless their picture headers match that decoder mode.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-decoder-target]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
