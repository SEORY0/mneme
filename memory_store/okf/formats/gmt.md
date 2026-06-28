---
type: format-family
title: "GMT format"
description: "Round 8 descriptive format facts for gmt."
resource: cybergym://format/gmt
tags: ["gmt", "round-8"]
okf_support: 1
---
# GMT Format

## Round 8 Factual Contract

### Schema / Invariants
- OGR GMT vector files are line-oriented text. Driver selection depends on an early GMT version marker in a comment/header line. Header metadata uses at-sign keyed tokens; geometry type, region, field names/types, and projection metadata are parsed before feature rows. A full feature section is not required to reach header metadata parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

