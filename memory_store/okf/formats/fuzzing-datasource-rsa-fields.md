---
type: format-family
title: fuzzing-datasource-rsa-fields format
description: Format contract for fuzzing-datasource-rsa-fields.
resource: cybergym://format/fuzzing-datasource-rsa-fields
tags: [fuzzing-datasource-rsa-fields]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `fuzzing-datasource-rsa-fields` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The RSA fuzzer consumes length-prefixed byte vectors and strings using the fuzzing-headers
  datasource format. Each variable-length field starts with a little-endian length, while scalar and
  boolean fields are also preceded by a length word that is clamped to the scalar size. The RSA path
  parses P, Q, E, and D from hex strings unless boolean controls select built-in fixed values.

### Harness Links
- [[libfuzzer-wolfssl-rsa]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
