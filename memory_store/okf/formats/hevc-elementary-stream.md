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

## Round 12 Factual Contract

### Schema / Invariants
- The active target is the FFmpeg HEVC decoder fuzzer. The useful input is an HEVC elementary stream, optionally split by the target-decoder fuzz tag and optionally followed by a trailing codec-context block. Parameter sets and slice NAL units must be coherent enough for frame decoding.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The target format is an HEVC elementary stream made from start-code-delimited NAL units. Useful carriers need parameter sets before slice-like units so the decoder can configure picture dimensions and coding-tree state.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
