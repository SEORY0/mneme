---
type: format-family
title: isobmff format
description: Structure, build skeleton, and bug-prone areas of the isobmff input format.
resource: cybergym://format/isobmff
tags: [isobmff]
timestamp: 2026-06-24T00:00:00Z
okf_support: 3
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 3 train-set solves.
- Winning strategies (observed): {'fuzzer': 1, 'seed-sweep': 2}
- Format families (observed): {'isobmff': 3}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.

## Round 8 Factual Contract

### Schema / Invariants
- ISOBMFF boxes use a big-endian size followed by a four-character type. Container boxes such as moov contain child boxes whose declared sizes are counted against the parent remaining size. A valid MP4-family envelope normally starts with an ftyp box and a moov box; the moov box usually contains an mvhd movie header before track or metadata children.

### Harness Links
- [[libfuzzer-afl-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
