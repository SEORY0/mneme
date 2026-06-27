---
type: harness-contract
title: "Libfuzzer Mruby Load String harness"
description: "Input contract facts for libfuzzer-mruby-load-string."
tags: ["libfuzzer-mruby-load-string", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Mruby Load String Harness

## Round 11 Input Contract
- The mruby fuzzer copies the entire input to a NUL-terminated buffer and calls mrb_load_string. There is no byte-level framing, no archive wrapper, and no FuzzedDataProvider layout.

## Format Links
- [[mruby-script]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
