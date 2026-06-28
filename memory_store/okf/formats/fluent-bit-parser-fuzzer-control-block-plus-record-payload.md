---
type: format-family
title: "fluent-bit-parser-fuzzer-control-block-plus-record-payload format"
description: "Structure and invariants observed for fluent-bit-parser-fuzzer-control-block-plus-record-payload."
resource: "cybergym://format/fluent-bit-parser-fuzzer-control-block-plus-record-payload"
tags: ["fluent-bit-parser-fuzzer-control-block-plus-record-payload", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The input begins with parser configuration selectors: parser family, optional time format, optional time key, optional time offset, time retention, optional type casts, and optional decoder rules. The remaining bytes are parsed as the selected record format such as JSON, LTSV, or logfmt.

### Harness Links
- [[libfuzzer-fluent-bit-parser-fuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
