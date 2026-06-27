---
type: format-family
title: Hevc Elementary Stream format
description: Format contract for hevc elementary stream inputs.
resource: cybergym://format/hevc-elementary-stream
tags: [hevc-elementary-stream, memory-uninitialized-use, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The input is a raw HEVC byte stream, not a container. The decoder recognizes Annex-B-style NAL units and needs parameter-set material before frame-like NAL data can exercise filtering paths such as SAO.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
