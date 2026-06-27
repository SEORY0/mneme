---
type: format-family
title: Macho format
description: Format contract for macho inputs.
resource: cybergym://format/macho
tags: [macho, heap-buffer-overflow-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
Mach-O begins with a fixed header containing CPU/file type fields, a load-command count, and the total load-command byte count. Variable-size load commands immediately follow the header and each command has its own type and size.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-yara-macho-module]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
