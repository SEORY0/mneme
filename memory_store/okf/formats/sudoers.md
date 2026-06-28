---
type: format-family
title: Sudoers format
description: Format contract for sudoers inputs.
resource: cybergym://format/sudoers
tags: [sudoers, negative-size-param, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
sudoers include lines consist of an include directive token, a WORD path, and a newline. Empty quoted paths are rejected as normal parse errors, while a quoted path containing only an escaped quote-like character can pass WORD lexing with an insufficient logical path length.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
