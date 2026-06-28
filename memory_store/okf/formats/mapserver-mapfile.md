---
type: format-family
title: "Mapserver Mapfile"
description: "Round 7 factual format contract for mapserver-mapfile."
resource: cybergym://format/mapserver-mapfile
tags: ["mapserver-mapfile", "format-contract", "round-7"]
okf_support: 2
train_only: true
---
# Mapserver Mapfile

## Round 7 Factual Contract

### Schema / Invariants
- MapServer mapfiles are keyword-oriented text files with MAP/END block structure, quoted strings,
layer/web/validation subblocks, expressions, numeric fields, and comments. The lexer has separate
INITIAL, expression, and string states and accumulates quoted string contents into a reusable
buffer.

### Harness Links
- [[libfuzzer-file-backed]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- MapServer mapfiles are line-oriented text files whose first significant token must be the MAP
  keyword and whose top-level block normally ends with END.
- Keywords such as NAME consume string tokens.
- Quoted strings are accumulated by a lexer state machine into a shared buffer; normal closing
  quotes store a terminator, while EOF inside that state can leave the buffer unterminated.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- A MapServer mapfile is a nested keyword language with MAP, LAYER, CLASS, and CLUSTER blocks closed by END. CLUSTER blocks may contain numeric distance/buffer fields, a region string, and group/filter expressions that allocate expression state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
