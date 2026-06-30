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

## Round 30 Factual Contract

### Schema / Invariants
- OpenType CFF2 inputs need a valid OTTO SFNT table directory plus coherent CFF2, cmap, metrics, name, post, and fvar-related tables for FreeType face creation. The CFF2 table contains a header and Top DICT, a VarStore, CharStrings, and an FDArray whose Font DICT points to a Private DICT. Private DICT blend requires a VarStore/region relationship so the blend vector has default plus delta components. CFF2 Top DICT maxstack controls the private parser operand-stack capacity; leaving the default can reject large blend programs before the target invariant is reached. The CFF parser does not clear operand stack entries after a blend operator, so adjacent blends can reuse earlier blend results.

### Harness Links
- [[libfuzzer-freetype-ftfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
