---
type: format-family
title: "Libxaac Encoder Fuzzed Provider format"
description: "Descriptive contract facts for libxaac-encoder-fuzzed-provider."
resource: "cybergym://format/libxaac-encoder-fuzzed-provider"
tags: ["libxaac-encoder-fuzzed-provider", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The relevant target is the encoder fuzzer, not a raw AAC decoder stream.
- FuzzedDataProvider consumes scalar configuration values from the end of the input, while frame payload bytes are consumed from the front or used as fill values during processing iterations.

### Harness Links
- [[libfuzzer-fuzzed-data-provider]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
