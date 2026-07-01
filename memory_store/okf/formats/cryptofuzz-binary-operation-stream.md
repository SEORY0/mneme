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
## Round 37 Factual Contract

### Schema / Invariants
- The relevant format is a Cryptofuzz binary datasource rather than JSON or a normal wolfSSL input file.
- The useful high-level envelope is an operation selector, nested operation payload, modifier data, module selector, and continuation control.
- BignumCalc payloads carry an arithmetic selector plus multiple bignum buffers; modifier data can steer decimal versus hexadecimal parsing, base-conversion round trips, pointer clamping, and bignum rewiring.
- Cryptofuzz binary inputs are a front-consumed operation stream.
- Scalar values and byte blobs are encoded as little-endian length-prefixed datasource items.
- The outer stream begins with an operation selector, then a length-prefixed operation payload, a length-prefixed modifier stream, a module selector consumed by the harness, and a continuation boolean.
- HMAC payload fields are read in order as cleartext, digest type, symmetric IV, symmetric key, and cipher type.
- Cryptofuzz inputs are a front-consumed binary datasource.
- Each scalar or blob is length-prefixed before its value.
- The outer stream selects an operation, then contains a nested operation payload, a modifier blob consumed by module helpers, a module selector field that is still structurally present even when the binary forces a module, and a continuation flag.
- BignumCalc payloads contain a calculation selector followed by four length-prefixed decimal digit buffers; non-digit bytes are normalized to decimal digits before module execution.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-cryptofuzz-binary-operation-stream]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- Cryptofuzz inputs are front-consumed datasource records, not DER, TLS, JSON, or a normal wolfSSL file. Each scalar or byte buffer is stored as a length-prefixed datasource item. The outer stream carries an operation selector, a nested operation payload buffer, a modifier buffer, a module selector consumed even when the binary forces a module, and a continuation boolean. DH_Derive payloads contain four bignum buffers: group modulus, generator, peer public value, and private value. Bignum buffers are normalized as decimal-like strings before wolfCrypt converts them to binary integers.

### Harness Links
- [[libfuzzer-cryptofuzz-sp-math]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
