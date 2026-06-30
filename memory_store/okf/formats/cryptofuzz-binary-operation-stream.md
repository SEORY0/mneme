---
type: format-family
title: "cryptofuzz-binary-operation-stream format"
description: "Structure and reachability facts for cryptofuzz-binary-operation-stream."
resource: cybergym://format/cryptofuzz-binary-operation-stream
tags: ["cryptofuzz-binary-operation-stream"]
okf_support: 2
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

## Round 31 Factual Contract

### Schema / Invariants
- Cryptofuzz inputs are a front-consumed binary operation stream, not a conventional file. The outer stream records an operation selector, a length-prefixed nested payload, a length-prefixed modifier blob, a module selector that is still consumed even when the binary forces wolfCrypt, and a continuation flag. BignumCalc payloads contain a calc-operation selector followed by decimal bignum buffers. The modifier blob is consumed later by wolfCrypt helpers for decimal-vs-hex parsing, optional pointer clamping, optional base-conversion round trips, and bignum rewiring.

### Harness Links
- [[libfuzzer-cryptofuzz-binary-operation-stream]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
