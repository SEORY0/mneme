---
type: format-family
title: "Rar5 format"
description: "Round 8 descriptive format facts for rar5."
resource: cybergym://format/rar5
tags: ["rar5", "round-8"]
okf_support: 2
---
# Rar5 Format

## Round 8 Factual Contract

### Schema / Invariants
- RAR5 archives begin with a versioned RAR marker followed by variable-length block headers. File service blocks carry compression metadata, including dictionary/window parameters, and header corruption often causes the libarchive reader to reject or skip an entry before dictionary reads occur.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


## Round 13 Facts
- RAR5 inputs start with the RAR5 marker, then CRC-protected variable-length base block headers. FILE base blocks carry split-before/split-after flags, data size, unpacked size, compression metadata, and a dictionary/window-size selector; header CRC validity is a hard parser gate.

## Round 24 Factual Contract

### Schema / Invariants
- RAR5 archives start with a fixed signature and then variable-length records. File-service records carry flags and attributes that distinguish directories from files, while compressed data is referenced by block sizes. Mutating a real RAR5 seed preserves the signature and record framing better than constructing from scratch.

### Harness Links
- [[afl-libfuzzer-libarchive-archive-reader]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
