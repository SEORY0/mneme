---
type: format-family
title: Fluent Bit Strptime Format Plus Buffer format
description: Format contract for fluent-bit-strptime-format-plus-buffer inputs.
resource: cybergym://format/fluent-bit-strptime-format-plus-buffer
tags: [fluent-bit-strptime-format-plus-buffer, bounds-check, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The input is split into two NUL-terminated strings: a format string followed by the candidate time buffer. Embedded NULs in the format region can intentionally stop format parsing while preserving the harness split.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
