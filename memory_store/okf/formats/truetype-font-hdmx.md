---
type: format-family
title: truetype-font-hdmx format
description: Structure, build skeleton, and bug-prone areas of the truetype-font-hdmx input format.
resource: cybergym://format/truetype-font-hdmx
tags: ["truetype-font-hdmx", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- A TrueType sfnt has a table directory with checksums, offsets, and lengths for each table. The hdmx table contains a version, record count, device-record size, then per-pixel-size records with width bytes indexed by glyph id. The hdmx table is normally a hinting-related table and is subset when no no-hinting flag is set.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
