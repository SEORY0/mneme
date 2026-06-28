---
type: format-family
title: "Mapfile"
description: "Round 7 factual format contract for mapfile."
resource: cybergym://format/mapfile
tags: ["mapfile", "format-contract", "round-7"]
okf_support: 2
train_only: true
---
# Mapfile

## Round 7 Factual Contract

### Schema / Invariants
- MapServer mapfiles are keyword-oriented text. A MAP can contain SYMBOL definitions; vector symbols
have a POINTS block containing coordinate pairs terminated by END markers.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer-tempfile-mapserver-mapfuzzer)

### Schema / Invariants
- MapServer mapfiles are text block documents. A MAP block can contain metadata, a PROJECTION block terminated by END, and at least one LAYER block. Projection parameters are represented as individual quoted strings, not a single combined token.

### Harness Links
- [[libfuzzer-tempfile-mapserver-mapfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
