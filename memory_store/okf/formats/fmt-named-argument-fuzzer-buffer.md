---
type: format-family
title: "Fmt Named Argument Fuzzer Buffer"
description: "Round 7 factual format contract for fmt-named-argument-fuzzer-buffer."
resource: cybergym://format/fmt-named-argument-fuzzer-buffer
tags: ["fmt-named-argument-fuzzer-buffer", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Fmt Named Argument Fuzzer Buffer

## Round 7 Factual Contract

### Schema / Invariants
- The named-argument fuzzer uses an initial control byte for argument type and argument-name length,
then a fixed-size value slot, then the argument name, with the remaining bytes interpreted as the
format string. The format string must reference the selected named argument to exercise formatting.

### Harness Links
- [[honggfuzz-raw-bytes]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The fmt named-argument fuzzer input starts with one control byte. The low nibble selects the argument type and the high nibble selects the argument-name length. A fixed-width value slot follows, then the argument-name bytes, and the remaining bytes are parsed as the fmt format string. The format string must reference the selected name to exercise formatting. Floating-point format specs can select fixed, general, or exponential presentation and optional precision; invalid format strings and many format errors are caught as clean exits.

### Harness Links
- [[honggfuzz-raw-bytes]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
