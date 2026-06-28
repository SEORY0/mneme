---
type: format-family
title: "font format"
description: "Structure and invariants observed for font."
resource: "cybergym://format/font"
tags: ["font", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The input is a raw font blob, not an archive or command file. Valid corpus seeds contain enough table structure for HarfBuzz subset parsing to proceed into face construction instead of failing immediately at the font loader.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
