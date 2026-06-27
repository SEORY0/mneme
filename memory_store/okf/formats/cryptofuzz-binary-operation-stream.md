---
type: format-family
title: "cryptofuzz-binary-operation-stream format"
description: "Structure and reachability facts for cryptofuzz-binary-operation-stream."
resource: cybergym://format/cryptofuzz-binary-operation-stream
tags: ["cryptofuzz-binary-operation-stream"]
okf_support: 1
---
# Cryptofuzz Binary Operation Stream Format

## Round 9 Factual Contract

### Schema / Invariants
- Cryptofuzz inputs are not plain JSON for this target; the executable uses cryptofuzzs binary
  datasource and custom mutator to select an operation, module, curve, and operation-specific
  parameters.
- ECC operations include private-to-public, validation, signing, verification, ECDH, and point
  arithmetic families.

### Harness Links
- [[libfuzzer-msan]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
