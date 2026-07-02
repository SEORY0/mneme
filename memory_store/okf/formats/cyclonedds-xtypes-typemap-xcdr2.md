---
type: format-family
title: "cyclonedds-xtypes-typemap-xcdr2 format"
description: "Structure, build skeleton, and bug-prone areas of the cyclonedds-xtypes-typemap-xcdr2 input format."
resource: cybergym://format/cyclonedds-xtypes-typemap-xcdr2
tags: ["cyclonedds-xtypes-typemap-xcdr2", "round-29"]
okf_support: 0
---
# Cyclonedds Xtypes Typemap Xcdr2 Format

## Round 29 Factual Contract

### Schema / Invariants
- CycloneDDS TypeMapping fuzz inputs are XCDR2-serialized maps with three top-level length-delimited sequences: minimal type-object pairs, complete type-object pairs, and complete-to-minimal identifier pairs. Hash-style type identifiers are stored separately from the length-delimited TypeObject payloads, and the hash for a TypeObject is computed over its serialized TypeObject envelope including its own length delimiter. Complete enumerated type objects contain enum flags, an enumerated header with bit-bound and type detail, then a length-delimited literal sequence whose count may be made zero if enclosing lengths and identifiers are kept consistent.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
