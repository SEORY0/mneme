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
