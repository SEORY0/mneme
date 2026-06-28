---
type: format-family
title: "Sql format"
description: "Descriptive contract facts for Sql."
resource: "cybergym://format/sql"
tags: ["sql", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The input is a SQL statement string. bitstring_agg accepts an expression and optional bounds; dangerous cases are tied to the span between aggregate bounds and how the aggregate allocates or indexes the resulting bitstring.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
