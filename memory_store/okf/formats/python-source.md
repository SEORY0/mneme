---
type: format-family
title: Python Source format
description: Format contract for python-source inputs.
resource: cybergym://format/python-source
tags: [python-source, tokenizer-f-string-state, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The relevant format is normal Python source with f-string literals. F-strings can contain replacement fields, nested format specifiers, doubled literal braces, and debug-expression equal signs. Syntax errors are not sanitizer failures under this harness.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
