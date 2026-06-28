---
type: format-family
title: "Mng"
description: "Round 12 factual format contract for mng."
resource: cybergym://format/mng
tags: ["mng", "format-contract", "round-12", "round-16"]
okf_support: 2
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

## Round 16 Factual Contract

### Schema / Invariants
- MNG uses a distinct stream signature followed by PNG-style chunks with lengths and CRCs. MHDR establishes the animation canvas, control chunks such as MAGN can precede image chunks, and a tiny embedded PNG-like image can be closed before the final MNG terminator.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- MNG uses a distinct signature followed by PNG-style chunks: big-endian length, four-character chunk type, chunk data, and CRC. The image header establishes the stream before control chunks such as DISC are interpreted.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
