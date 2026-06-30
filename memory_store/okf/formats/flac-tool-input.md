---
type: format-family
title: flac-tool-input format
description: "Round 23 descriptive structure and invariant facts for flac-tool-input."
resource: cybergym://format/flac-tool-input
tags: ["flac-tool-input", "round-23"]
okf_support: 1
train_only: true
---
# Flac Tool Input Format

## Round 23 Factual Contract

### Schema / Invariants
- The fuzzer_tool_flac input starts with a control byte that limits how many NUL-delimited command-line arguments are read. Remaining bytes become a temporary file. FLAC foreign metadata is represented by application metadata blocks identifying RIFF, AIFF, or Wave64 chunks, and decode options can force output container and AIFF-C subformat.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- The useful carrier is a valid native FLAC stream: stream marker, STREAMINFO, optional SEEKTABLE and other metadata, then decodable audio frames. The trigger depends on a fixed or LPC-coded frame where predictor order and residual metadata remain coherent for the original frame but become inconsistent after the post-seek blocksize adjustment.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
