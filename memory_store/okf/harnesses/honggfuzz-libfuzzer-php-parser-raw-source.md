---
type: harness-contract
title: "Honggfuzz Libfuzzer PHP Parser Raw Source harness"
description: "Input contract facts for honggfuzz-libfuzzer-php-parser-raw-source."
tags: ["honggfuzz-libfuzzer-php-parser-raw-source", "round-29"]
okf_support: 0
---
# Honggfuzz Libfuzzer PHP Parser Raw Source Harness

## Round 29 Input Contract

- The wrapper runs the PHP parser fuzzer on the raw file contents as a PHP file body. There is no leading mode byte, checksum, archive wrapper, or FuzzedDataProvider split. The fuzzer copies the raw bytes into a NUL-terminated buffer, compiles them, destroys any resulting op_array, and does not execute script code.

## Round 29 Format Links
- [[php-script]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
