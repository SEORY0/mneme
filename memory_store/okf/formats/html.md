---
type: format-family
title: "Html format"
description: "Descriptive contract facts for Html."
resource: "cybergym://format/html"
tags: ["html", "round-6"]
okf_support: 2
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The payload after the harness option word is treated as HTML text and is exercised through both memory-based parsing and incremental push parsing. Malformed tags and entities alone are normal parser errors and do not imply the vulnerable reset path.

### Harness Links
- [[afl-file]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- The parsed document is ordinary HTML. Encoding can be inferred from high-bit bytes or from meta
  charset declarations, and malformed or late declarations can cause the parser to switch encoders
  during tokenization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
