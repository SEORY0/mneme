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

## Round 26 Factual Contract


### Schema / Invariants
- The input is not a raw AAC stream. It is a FuzzedDataProvider-driven encoder input: scalar configuration chooses bitrate, MPS/ADTS/ES switches, TNS/noise flags, PCM word size, channel count, sample rate, frame length, AOT, USAC/SBR-related flags, DRC enablement, codec mode, loudness fields, and stream id. The remaining front bytes are then consumed as encoder input buffers or as fill values for process iterations.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
