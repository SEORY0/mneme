---
type: format-family
title: "Fluent Bit Parser Fuzzer Control Plus Record"
description: "Round 7 factual format contract for fluent-bit-parser-fuzzer-control-plus-record."
resource: cybergym://format/fluent-bit-parser-fuzzer-control-plus-record
tags: ["fluent-bit-parser-fuzzer-control-plus-record", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Fluent Bit Parser Fuzzer Control Plus Record

## Round 7 Factual Contract

### Schema / Invariants
- The fuzzer can select JSON, regex, LTSV, or logfmt parsing. Optional parser settings include time
fields, type coercions for fixed key names, and decoder rules; only the bytes after those control
fields become the record text parsed by Fluent Bit.

### Harness Links
- [[honggfuzz-style-file-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- The payload format is selected by the first control byte: JSON, regex, LTSV, or logfmt.
- Logfmt records are key=value pairs with optional quoted values; LTSV records are key:value pairs
  separated by tabs.
- Parser typecasting only affects fixed keys named AAA, BBB, CCC, DDD, and EEE when the types
  control byte is enabled.
- Among those fixed types, DDD is boolean and invalid boolean text triggers the cast-error path.
- The fuzzer input begins with control fields selecting parser kind and optional time, type, and
  decoder configuration.
- For JSON mode, the remaining bytes are parsed as a log record; optional type fields name fixed
  keys and optional decoder rules apply to a fixed key before parsing the record.

### Harness Links
- [[honggfuzz-file]]
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
