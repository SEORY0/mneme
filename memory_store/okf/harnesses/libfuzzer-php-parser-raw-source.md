---
type: harness-contract
title: "Libfuzzer PHP Parser Raw Source Harness"
description: "Input contract facts for libfuzzer-php-parser-raw-source."
tags: ["libfuzzer-php-parser-raw-source", "round-27"]
okf_support: 1
---
# Libfuzzer PHP Parser Raw Source Harness

## Round 27 Input Contract
- The PHP parser fuzzer feeds the raw input buffer directly as a PHP file body to the parser/compile path.
- There is no mode byte, file container, checksum, or FuzzedDataProvider front/back layout; the only practical size gate is the fuzzer's maximum source-buffer size.

## Round 27 Format Links
- [[php-script]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
