---
type: format-family
title: apfs-disk-image format
description: Structure, build skeleton, and bug-prone areas of the apfs-disk-image input format.
resource: cybergym://format/apfs-disk-image
tags: ["apfs-disk-image", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The APFS harness expects a disk image that can be opened as an APFS pool, then uses a pool-derived image to open an APFS filesystem and walk the root directory recursively.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
