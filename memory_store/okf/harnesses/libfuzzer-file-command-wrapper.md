---
type: harness-contract
title: "Libfuzzer File Command Wrapper harness"
description: "Input contract facts for libfuzzer-file-command-wrapper."
tags: ["libfuzzer-file-command-wrapper", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer File Command Wrapper Harness

## Round 11 Input Contract
- The UPX fuzz harness writes raw bytes to a temporary file and invokes the real upx command path such as list or decompression mode. Therefore the PoC must be a complete file recognized by UPX rather than a carved libFuzzer buffer.

## Format Links
- [[elf-or-upx-packed-elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
