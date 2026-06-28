---
type: format-family
title: "dds-xtypes-typemap-cdr format"
description: "Descriptive format contract facts for dds-xtypes-typemap-cdr."
tags: ["dds-xtypes-typemap-cdr", "round-18"]
okf_support: 1
train_only: true
---
# DDS Xtypes Typemap Cdr Format

## Round 18 Factual Contract

### Schema / Invariants
- The input is a CDR-serialized DDS XTypes typemap. It contains sequences of complete and minimal identifier-object pairs plus mappings between complete and minimal identifiers. Type objects may reference dependent types, and the harness derives dependent counts from the number of complete pairs before building proxy type information.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
