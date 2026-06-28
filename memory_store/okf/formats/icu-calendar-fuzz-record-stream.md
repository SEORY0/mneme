---
type: format-family
title: "icu-calendar-fuzz-record-stream format"
description: "Descriptive format contract facts for icu-calendar-fuzz-record-stream."
tags: ["icu-calendar-fuzz-record-stream", "round-18"]
okf_support: 1
train_only: true
---
# ICU Calendar Fuzz Record Stream Format

## Round 18 Factual Contract

### Schema / Invariants
- The input is not a serialized ICU file. It is a fuzzer-defined record stream: an initial selector prefix chooses calendar construction parameters, then each record supplies a date-field selector, a command selector, and numeric payload interpreted as both time and amount data.

### Harness Links
- [[libfuzzer-fuzzed-data-provider-style]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
