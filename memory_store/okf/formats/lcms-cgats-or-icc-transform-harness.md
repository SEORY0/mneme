---
type: format-family
title: "lcms-cgats-or-icc-transform-harness format"
description: "Descriptive format contract facts for lcms-cgats-or-icc-transform-harness."
tags: ["lcms-cgats-or-icc-transform-harness", "round-18"]
okf_support: 1
train_only: true
---
# Lcms Cgats Or Icc Transform Harness Format

## Round 18 Factual Contract

### Schema / Invariants
- CGATS text uses a printable sheet-type line followed by property records, declared field names, a data-format section, a declared set count, and a data section. The scanner distinguishes keywords, quoted strings, numbers, and syntax errors; invalid control or punctuation characters in sensitive positions should be rejected by a strict CGATS loader.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
