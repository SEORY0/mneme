---
type: format-family
title: opensc-virtual-card-transcript format
description: Structure and reachability facts for opensc-virtual-card-transcript inputs.
tags: [opensc-virtual-card-transcript]
okf_support: 0
---
# Opensc Virtual Card Transcript Format

## Round 10 Factual Contract

### Schema / Invariants
- The input is a sequence of little-endian length-prefixed chunks. The first chunk becomes the virtual card ATR. Each later chunk is one APDU response where the final two bytes are status words and preceding bytes are response data.

### Harness Links
- [[libfuzzer-raw-transcript-chunks]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
