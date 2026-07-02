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

## Round 35 Input Contract

### Input Contract
- The parser fuzzer receives the submitted bytes as one raw PHP file body, copies them into a NUL-terminated buffer, compiles the source, and destroys any resulting op_array during request shutdown. It does not execute user script code, has no leading mode byte, no checksum, no archive wrapper, and no FuzzedDataProvider front/back carving.
- The target is the PHP parser fuzzer over raw source bytes. The fuzzer copies the submitted buffer, NUL-terminates it, compiles it through zend_compile_file, destroys any produced op_array, and does not need to execute userland PHP. There is no leading selector byte, checksum, length wrapper, archive, or FuzzedDataProvider split. The container wrapper always runs the file mounted at the fixed PoC path, so manual checks must place the candidate at that path rather than pass it as an argv filename.

### Format Links
- [[php-script]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
