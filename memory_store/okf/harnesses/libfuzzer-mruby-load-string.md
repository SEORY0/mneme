---
type: harness-contract
title: "Libfuzzer Mruby Load String harness"
description: "Input contract facts for libfuzzer-mruby-load-string."
tags: ["libfuzzer-mruby-load-string", "round-11"]
okf_support: 2
train_only: true
---
# Libfuzzer Mruby Load String Harness

## Round 11 Input Contract
- The mruby fuzzer copies the entire input to a NUL-terminated buffer and calls mrb_load_string. There is no byte-level framing, no archive wrapper, and no FuzzedDataProvider layout.

## Format Links
- [[mruby-script]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 13 Facts
- The mruby harness copies raw bytes into a NUL-terminated string, opens a fresh mruby state, calls mrb_load_string, then closes the state. There is no prefix, length field, or FuzzedDataProvider layout.
- The OSS-Fuzz mruby harness copies the raw bytes into a NUL-terminated code buffer, opens a new mruby state, evaluates the code string, and closes the state. There is no byte-level carving or external file contract.

## Round 15 Input Contract
- The harness copies raw bytes into a newly allocated NUL-terminated source string, opens a fresh
  mruby state, calls mrb_load_string, then closes the state. There is no filename envelope, bytecode
  wrapper, selector byte, or FuzzedDataProvider layout.

## Format Links
- [[mruby-script]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
