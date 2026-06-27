---
type: format-family
title: H264 Annexb Svc format
description: Format contract for h264-annexb-svc inputs.
resource: cybergym://format/h264-annexb-svc
tags: [h264-annexb-svc, null-dereference, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The decoder input family is H.264 Annex-B style SVC bitstream data. Relevant inputs contain start-code-delimited NAL units with SVC layer and resolution metadata; the described fault depends on inter-layer prediction state and resolution-level initialization tracking.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[honggfuzz-wrapper-svc-dec]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
