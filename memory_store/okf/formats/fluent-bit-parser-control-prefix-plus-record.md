---
type: format-family
title: "Fluent Bit Parser Control Prefix Plus Record"
description: "Round 19 factual format contract for fluent-bit-parser-control-prefix-plus-record."
resource: cybergym://format/fluent-bit-parser-control-prefix-plus-record
tags: ["fluent-bit-parser-control-prefix-plus-record", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Fluent Bit Parser Control Prefix Plus Record

## Round 19 Factual Contract

- The parser fuzzer uses a control prefix to choose parser type and optional parser settings, then parses the remaining bytes as the selected record format. Parser choices include JSON, regex, LTSV, and logfmt. Optional controls can enable time-format fields, time key, time offset, time-keep behavior, typecast tables for fixed keys, and decoders.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
