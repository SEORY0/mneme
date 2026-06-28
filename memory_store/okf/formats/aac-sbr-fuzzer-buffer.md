---
type: format-family
title: "AAC SBR Fuzzer Buffer format"
description: "Round 8 descriptive format facts for aac-sbr-fuzzer-buffer."
resource: cybergym://format/aac-sbr-fuzzer-buffer
tags: ["aac-sbr-fuzzer-buffer", "round-8"]
okf_support: 1
---
# AAC SBR Fuzzer Buffer Format

## Round 8 Factual Contract

### Schema / Invariants
- This harness input is not a standalone AAC file. It begins with two little-endian chunk lengths, a flag byte, a NeAACDecConfiguration struct image, then three byte regions consumed by NeAACDecInit or NeAACDecInit2 and subsequent NeAACDecDecode calls. The audio payload must be coherent enough for AAC frame decoding, channel-pair reconstruction, and SBR processing to run.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

