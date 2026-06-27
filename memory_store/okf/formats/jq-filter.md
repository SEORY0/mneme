---
type: format-family
title: Jq Filter format
description: Format contract for jq-filter inputs.
resource: cybergym://format/jq-filter
tags: [jq-filter, integer-overflow, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The harness input is a jq program, not JSON data. Numeric literals with large positive and negative exponents can be parsed as jq constants, and comparison operators are valid filter syntax. Runtime filters such as sort require execution with data and are not necessarily evaluated by a compile-only target.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
