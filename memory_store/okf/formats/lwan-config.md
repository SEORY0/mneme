---
type: format-family
title: Lwan Config format
description: Format contract for lwan-config inputs.
resource: cybergym://format/lwan-config
tags: [lwan-config, out-of-bounds-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The config format uses braces for sections, equals for key-value pairs, comments beginning with a hash character, normal strings, variable expansions, and multiline strings opened by triple single or double quotes. Multiline lexing scans for the matching three-character terminator and otherwise emits an EOF lexer error.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
