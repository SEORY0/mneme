---
type: format-family
title: "Net Snmp Api Fuzzer Stream"
description: "Round 12 factual format contract for net-snmp-api-fuzzer-stream."
resource: cybergym://format/net-snmp-api-fuzzer-stream
tags: ["net-snmp-api-fuzzer-stream", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Net Snmp Api Fuzzer Stream

## Round 12 Factual Contract

### Schema / Invariants
- The active input is a structured byte stream for snmp_api_fuzzer, not a standalone MIB file. It is consumed front-to-back into a short value buffer and type selector, data-store flags, a bounded output buffer, a parse-data region, context/security strings, and session fields. Object identifiers can be introduced through text value parsing or BER-encoded SNMP parse data.

### Harness Links
- [[honggfuzz-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
