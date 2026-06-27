---
type: format-family
title: "Fluent Bit Parser Fuzzer Control Plus Json"
description: "Round 12 factual format contract for fluent-bit-parser-fuzzer-control-plus-json."
resource: cybergym://format/fluent-bit-parser-fuzzer-control-plus-json
tags: ["fluent-bit-parser-fuzzer-control-plus-json", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Fluent Bit Parser Fuzzer Control Plus Json

## Round 12 Factual Contract

### Schema / Invariants
- The useful payload is not pure JSON from byte zero under this harness. A short control prefix selects parser family and optional parser settings, then the remaining bytes are parsed as the record. JSON records can contain objects, arrays, strings, booleans, numbers, and null values after the prefix.

### Harness Links
- [[honggfuzz-libfuzzer-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
