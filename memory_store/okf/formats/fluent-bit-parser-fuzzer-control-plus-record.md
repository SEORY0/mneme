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
