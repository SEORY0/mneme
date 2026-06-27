---
type: format-family
title: "Mng"
description: "Round 12 factual format contract for mng."
resource: cybergym://format/mng
tags: ["mng", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Mng

## Round 12 Factual Contract

### Schema / Invariants
- MNG uses a PNG-like byte stream: file signature followed by big-endian length, four-character chunk type, chunk data, and CRC for each chunk. The basic image header chunk must appear before control chunks, and a terminal chunk can close the stream. LOOP chunk data is interpreted as a level byte followed by a loop-count integer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
