---
type: format-family
title: Hevc Elementary Stream format
description: Format contract for hevc elementary stream inputs.
resource: cybergym://format/hevc-elementary-stream
tags: [hevc-elementary-stream, memory-uninitialized-use, round-11]
okf_support: 2
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

## Round 24 Factual Contract

### Schema / Invariants
- The input is a raw HEVC elementary stream with decoder-recognized NAL units. Parameter sets must precede slice-like data for reconstruction and filtering paths such as SAO to become reachable.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- The useful input is a raw HEVC elementary stream, not a container. Start-code-delimited VPS, SPS, PPS, and VCL NAL units must remain coherent enough to open the HEVC decoder and reach frame reconstruction. Streams that exercise SAO edge filtering and picture-size relationships are stronger carriers than generic valid samples or arbitrary truncation.

### Harness Links
- [[libfuzzer-ffmpeg-target-dec-fuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- HEVC elementary streams are start-code/NAL-unit streams with VPS/SPS/PPS parameter sets followed by VCL slices. Valid seeds are much better carriers than minimal construction because the decoder needs coherent profile information, picture dimensions, reference state, slice headers, and in-loop reconstruction metadata before SAO and neighboring prediction paths are exercised.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
