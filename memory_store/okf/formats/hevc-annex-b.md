---
type: format-family
title: hevc-annex-b format
description: Structure, build skeleton, and bug-prone areas of the hevc-annex-b input format.
resource: cybergym://format/hevc-annex-b
tags: ["hevc-annex-b", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-raw-libhevc-decoder)

### Schema / Invariants
- The input is an Annex-B style HEVC byte stream with start-code-delimited NAL units. Deeper decode paths generally require coherent parameter-set and slice NAL ordering; malformed or tail-truncated delimiters alone can be parsed as invalid NAL boundaries without triggering the target condition.

### Harness Links
- [[libfuzzer-raw-libhevc-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
