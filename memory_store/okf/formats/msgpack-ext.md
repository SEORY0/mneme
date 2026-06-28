---
type: format-family
title: "Msgpack Ext"
description: "Round 7 factual format contract for msgpack-ext."
resource: cybergym://format/msgpack-ext
tags: ["msgpack-ext", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Msgpack Ext

## Round 7 Factual Contract

### Schema / Invariants
- Tarantool datetime values are encoded as MessagePack extension values with a datetime extension type
and either a required epoch payload or an epoch plus tail fields. The datetime unpacker validates
epoch range, nanosecond range, timezone offset, and timezone index after decoding raw payload
fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
