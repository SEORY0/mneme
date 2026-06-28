---
type: format-family
title: jpeg-r-ultrahdr format
description: "Round 23 descriptive structure and invariant facts for jpeg-r-ultrahdr."
resource: cybergym://format/jpeg-r-ultrahdr
tags: ["jpeg-r-ultrahdr", "round-23"]
okf_support: 1
train_only: true
---
# Jpeg R Ultrahdr Format

## Round 23 Factual Contract

### Schema / Invariants
- Ultra HDR JPEG-R decoding expects a primary JPEG plus gainmap image and gainmap metadata. ISO gainmap metadata begins after an ISO namespace marker and encodes version, flags, optional common denominator, and one or three channels of numerator/denominator fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
