---
type: format-family
title: Ntfs Filesystem Image format
description: Format contract for ntfs-filesystem-image.
resource: cybergym://format/ntfs-filesystem-image
tags: [ntfs-filesystem-image]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The target format is an NTFS filesystem image. Reaching the data-run parser requires a coherent filesystem boot sector, MFT metadata, attributes, and a resident or non-resident runlist structure for file data.

### Harness Links
- [[libfuzzer-memory-image]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
