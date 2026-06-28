---
type: format-family
title: "datasource-wrapped-flac format"
description: "Structure and invariants observed for datasource-wrapped-flac."
resource: "cybergym://format/datasource-wrapped-flac"
tags: ["datasource-wrapped-flac", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The vulnerable parser state is a FLAC stream containing metadata followed by an audio frame whose subframe type encodes a fixed or LPC predictor order larger than the frame blocksize. Residual coding and warmup samples must remain coherent enough for the decoder to call the subframe restore path.

### Harness Links
- [[libfuzzer-flac-decoder-datasource]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
