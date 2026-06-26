---
type: format-family
title: "Wkb format"
description: "Descriptive contract facts for Wkb."
resource: "cybergym://format/wkb"
tags: ["wkb", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- WKB inputs are endian-tagged records with a geometry type followed by type-specific counts and nested geometry records. CurvePolygon records carry a ring count and then delegate each contained ring to the generic WKB geometry reader.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
