---
type: harness-contract
title: "Honggfuzz File Wrapper harness"
description: "Input contract facts for honggfuzz-file-wrapper."
tags: ["honggfuzz-file-wrapper", "round-28"]
okf_support: 0
---
# Honggfuzz File Wrapper Harness

## Round 28 Input Contract

- The source harness copies the whole input file into a null-terminated buffer and calls mrb_load_string, with no mode selector or FuzzedDataProvider layout. In this generated arvo image, the command wrapper invokes a Honggfuzz-built binary with the file path, and that binary exits after printing its fuzzing usage instead of evaluating the file.

## Round 28 Format Links
- [[mruby-script]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
