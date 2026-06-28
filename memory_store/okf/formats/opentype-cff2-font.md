---
type: format-family
title: opentype-cff2-font format
description: Structure, build skeleton, and bug-prone areas of the opentype-cff2-font input format.
resource: cybergym://format/opentype-cff2-font
tags: ["opentype-cff2-font", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The relevant input is an sfnt/OpenType font where the table directory, CFF/CFF2 outline table, and variation tables must be coherent enough for FreeType to initialize a CFF2 variable face. CFF and CFF2 table priority affects how named instances and variation support are derived.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
