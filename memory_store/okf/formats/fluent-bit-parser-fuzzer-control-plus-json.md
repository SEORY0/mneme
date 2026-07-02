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
## Round 37 Factual Contract

### Schema / Invariants
- The useful input is not raw JSON from byte zero.
- The parser fuzzer consumes leading selector bytes for parser family and optional parser configuration, may consume fixed-width strings for time format and time key, and then passes the remaining bytes to flb_parser_do.
- In JSON mode, the remaining record is converted to MsgPack before time lookup.
- The JSON parser accepts object records and later walks MsgPack map entries, assuming the configured time field is represented as a string.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- This harness input is a control prefix followed by a JSON record, not raw JSON from byte zero. In JSON mode the record is converted to MsgPack and must unpack as a map before time lookup. Strict JSON syntax means object keys that survive JSON conversion are string keys; primitive values can be booleans, numbers, null, arrays, or objects. The decoder machinery can target a fixed string key and, with the JSON backend, decode a string value into an additional MsgPack object that is merged back into the record before time lookup.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
