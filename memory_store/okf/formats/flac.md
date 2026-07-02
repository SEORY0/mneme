---
type: format-family
title: "Flac format"
description: "Round 8 descriptive format facts for flac."
resource: cybergym://format/flac
tags: ["flac", "round-8"]
okf_support: 12
---
# Flac Format

## Round 8 Factual Contract

### Schema / Invariants
- FLAC inputs begin with the native stream marker followed by metadata blocks and audio frames. Metadata seeds are useful parser-reaching envelopes, but the bitreader target appears tied to compressed frame contents and bit-level residual/subframe boundaries.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- A FLAC stream starts with the stream marker, a required STREAMINFO metadata block, optional metadata blocks, then audio frames. Audio frames contain sync and stream parameters, subframe headers, optional wasted-bit flags, predictor warmup samples, and partitioned Rice residuals. The residual path depends on the entropy coding method, partition order, predictor order, and the number of residual samples implied by block size.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 27 Factual Contract

- A native FLAC stream starts with the FLAC marker, then STREAMINFO must appear first and provide valid stream parameters.
- Metadata block headers carry a last-block flag, a block type, and a body length; responded metadata block types are parsed rather than skipped.
- For this bug, audio frames are not required: the important invariant is that a parsed metadata block advertises more body than the datasource will provide.

### Harness Links
- [[libfuzzer-flac-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
