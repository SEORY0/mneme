---
type: format-family
title: Elf Or Upx Packed Elf format
description: Format contract for elf-or-upx-packed-elf inputs.
resource: cybergym://format/elf-or-upx-packed-elf
tags: [elf-or-upx-packed-elf, bad-elf-hash-chain, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The relevant relation is in ELF dynamic symbol lookup: DT_HASH or DT_GNU_HASH bucket and chain arrays must be structurally accepted, then contain a chain relation that is cyclic or out of valid bounds during lookup for a named symbol.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-file-command-wrapper]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
