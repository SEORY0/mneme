---
type: format-family
title: fuzztest-encoded-image-case format
description: Structure, build skeleton, and bug-prone areas of the fuzztest-encoded-image-case input format.
resource: cybergym://format/fuzztest-encoded-image-case
tags: ["fuzztest-encoded-image-case", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (fuzztest-libfuzzer-bridge)

### Schema / Invariants
- The underlying test function expects a tuple containing an image byte string, optimization selector, ARGB flag, WebP encoder configuration, and crop/scale parameters. The image byte string may itself be JPEG, PNG, TIFF, WebP, or other supported input once the FuzzTest wrapper deserializes the case.

### Harness Links
- [[fuzztest-libfuzzer-bridge]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
