---
type: format-family
title: "opentype-font-subset-input format"
description: "Descriptive format contract facts for opentype-font-subset-input."
tags: ["opentype-font-subset-input", "round-18"]
okf_support: 1
train_only: true
---
# Opentype Font Subset Input Format

## Round 18 Factual Contract

### Schema / Invariants
- The target input is an OpenType or TrueType font blob. The subset path serializes a new font from selected Unicode codepoints and optional subset flags, then the repacker resolves table/object links while laying out serialized graph nodes. The bug depends on overflow records retaining link references across graph storage growth, so ordinary valid fonts can parse and subset without reaching the fragile repacker state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
