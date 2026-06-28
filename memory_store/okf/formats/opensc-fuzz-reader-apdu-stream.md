---
type: format-family
title: "Opensc Fuzz Reader Apdu Stream format"
description: "Round 8 descriptive format facts for opensc-fuzz-reader-apdu-stream."
resource: cybergym://format/opensc-fuzz-reader-apdu-stream
tags: ["opensc-fuzz-reader-apdu-stream", "round-8"]
okf_support: 1
---
# Opensc Fuzz Reader Apdu Stream Format

## Round 8 Factual Contract

### Schema / Invariants
- This fuzzer input is a sequence of length-prefixed chunks. The first chunk is consumed as the card ATR. Later chunks are APDU responses, where the trailing status bytes are separated from response data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

