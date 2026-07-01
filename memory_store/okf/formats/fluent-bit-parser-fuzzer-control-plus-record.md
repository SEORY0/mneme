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

## Round 12 Factual Contract

### Schema / Invariants
- The general parser fuzzer consumes control bytes before the record: parser format selection, optional time fields, time retention, optional typecast table, optional decoder list, and then the remaining bytes as the log record parsed by the selected parser.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The general Fluent Bit parser fuzzer input is a front control block followed by a parser record. The control block selects JSON, regex, LTSV, or logfmt parsing and can enable optional time fields, fixed-key type casts, and decoder rules. Logfmt records are key/value text pairs; typecasting applies only to the harness-installed fixed keys.
- The useful input is not a standalone log file but a Fluent Bit parser-fuzzer envelope followed by a parser record. For the logfmt branch, records are key/value text using ident-byte runs around an equals sign. The harness' typecast table maps a small fixed key set to integer, float, boolean, string, and hex conversions; the boolean conversion error path is reached by a matching key with a non-boolean value.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
