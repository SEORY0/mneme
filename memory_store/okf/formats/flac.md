---
type: format-family
title: "Flac format"
description: "Round 8 descriptive format facts for flac."
resource: cybergym://format/flac
tags: ["flac", "round-8"]
okf_support: 1
---
# Flac Format

## Round 8 Factual Contract

### Schema / Invariants
- FLAC inputs begin with the native stream marker followed by metadata blocks and audio frames. Metadata seeds are useful parser-reaching envelopes, but the bitreader target appears tied to compressed frame contents and bit-level residual/subframe boundaries.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

