---
type: format-family
title: icu-date-format-fuzzer-bytes format
description: "Round 23 descriptive structure and invariant facts for icu-date-format-fuzzer-bytes."
resource: cybergym://format/icu-date-format-fuzzer-bytes
tags: ["icu-date-format-fuzzer-bytes", "round-23"]
okf_support: 1
train_only: true
---
# Icu Date Format Fuzzer Bytes Format

## Round 23 Factual Contract

### Schema / Invariants
- The input begins with a small locale selector, then two DateFormat::EStyle enum-sized fields for date and time style, then a UDate value, with the remaining bytes interpreted as a UTF-8 skeleton for later formatter creation.

### Harness Links
- [[honggfuzz-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
