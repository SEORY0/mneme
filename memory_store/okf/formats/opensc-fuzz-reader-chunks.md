---
type: format-family
title: "Opensc Fuzz Reader Chunks"
description: "Round 7 factual format contract for opensc-fuzz-reader-chunks."
resource: cybergym://format/opensc-fuzz-reader-chunks
tags: ["opensc-fuzz-reader-chunks", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Opensc Fuzz Reader Chunks

## Round 7 Factual Contract

### Schema / Invariants
- The OpenSC reader harness is a sequence of little-endian length-prefixed chunks. The first chunk is
used as ATR data; later chunks are consumed as card transmit responses where the last two bytes are
status words and the preceding bytes are copied as APDU response data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
