---
type: format-family
title: "thin-ar-archive format"
description: "Descriptive format contract facts for thin-ar-archive."
tags: ["thin-ar-archive", "round-18"]
okf_support: 1
train_only: true
---
# Thin Ar Archive Format

## Round 18 Factual Contract

### Schema / Invariants
- GNU thin archives start with a thin-archive magic and member headers. Long-name table entries can be referenced by archive member names, and thin archives can encode a nested-member origin after the long-name reference so the parser opens an external or nested archive while resolving a member name.

### Harness Links
- [[libfuzzer-tempfile-readelf]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
