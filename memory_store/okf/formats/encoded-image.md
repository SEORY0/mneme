---
type: format-family
title: "Encoded Image format"
description: "Round 8 descriptive format facts for encoded-image."
resource: cybergym://format/encoded-image
tags: ["encoded-image", "round-8"]
okf_support: 1
---
# Encoded Image Format

## Round 8 Factual Contract

### Schema / Invariants
- The imdecode harness auto-detects image formats from raw encoded bytes. Ordinary PNG and JPEG samples are accepted; truncated PNG inputs are rejected by the image library without crashing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

