---
type: format-family
title: zstd-sequence-compression-api-bytes format
description: Structure, build skeleton, and bug-prone areas of the zstd-sequence-compression-api-bytes input format.
resource: cybergym://format/zstd-sequence-compression-api-bytes
tags: ["zstd-sequence-compression-api-bytes", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The format is harness-specific raw bytes, not a zstd frame. A FuzzedDataProvider consumes control fields from the back of the input and uses the remaining front bytes as data for generated sequences and optional dictionary material.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
