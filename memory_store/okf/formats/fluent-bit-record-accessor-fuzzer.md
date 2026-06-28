---
type: format-family
title: "fluent-bit-record-accessor-fuzzer format"
description: "Structure and invariants observed for fluent-bit-record-accessor-fuzzer."
resource: "cybergym://format/fluent-bit-record-accessor-fuzzer"
tags: ["fluent-bit-record-accessor-fuzzer", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- This fuzzer consumes a fixed-size JSON record prefix, packs it to msgpack, then treats the remaining bytes as a Fluent Bit record accessor expression. Accessors can name top-level keys and nested map or array subkeys.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
