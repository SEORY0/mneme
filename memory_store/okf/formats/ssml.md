---
type: format-family
title: ssml format
description: Structure, build skeleton, and bug-prone areas of the ssml input format.
resource: cybergym://format/ssml
tags: [ssml, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The input is text-like SSML, with XML-style angle-bracket tags and no required file header. Malformed markup is still accepted far enough to enter the SSML parser; validity as a complete document is not required.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
