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

## Round 26 Factual Contract


### Schema / Invariants
- Cryptofuzz inputs use a binary datasource rather than JSON. Each consumed scalar or blob is length-prefixed in stream order. The top-level stream selects an operation, then carries an operation payload, a modifier blob, a module selector, and a continuation flag. BignumCalc payloads contain a calc operation followed by four length-prefixed decimal digit buffers; non-digit bytes are normalized to digits before module execution.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
