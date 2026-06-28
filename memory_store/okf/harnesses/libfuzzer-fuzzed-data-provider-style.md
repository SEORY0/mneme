---
type: harness-contract
title: "libfuzzer-fuzzed-data-provider-style harness"
description: "Descriptive harness contract facts for libfuzzer-fuzzed-data-provider-style."
tags: ["libfuzzer-fuzzed-data-provider-style", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Fuzzed Data Provider Style Harness

## Round 18 Input Contract

### Schema / Invariants
- The harness consumes bytes front-to-back in a FuzzedDataProvider-like layout. Early bytes choose timezone, locale, and calendar type; subsequent records repeatedly select a calendar operation, and one command value dispatches to Calendar::set.

### Format Links
- [[icu-calendar-fuzz-record-stream]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
