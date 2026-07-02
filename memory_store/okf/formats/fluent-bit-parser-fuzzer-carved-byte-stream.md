---
type: format-family
title: "Fluent Bit Parser Fuzzer Carved Byte Stream"
description: "Round 36 factual format contract for fluent-bit-parser-fuzzer-carved-byte-stream."
tags: ["fluent-bit-parser-fuzzer-carved-byte-stream", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Fluent Bit Parser Fuzzer Carved Byte Stream

## Round 36 Factual Contract

### Schema / Invariants
- The fuzzer input is a carved control stream followed by parser payload. Early control fields choose one of the built-in parser formats, optionally provide fixed-size strings for time format, time key, and timezone offset, choose time retention, optionally create type-cast entries, and optionally build a decoder-list object with one or more decoder rules. The remaining bytes are passed to the created parser only if parser creation succeeds.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
