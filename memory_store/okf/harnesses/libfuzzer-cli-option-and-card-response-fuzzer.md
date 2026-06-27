---
type: harness-contract
title: "Libfuzzer Cli Option And Card Response Fuzzer harness"
description: "Input contract facts for libfuzzer-cli-option-and-card-response-fuzzer."
tags: ["libfuzzer-cli-option-and-card-response-fuzzer"]
okf_support: 0
---
# Libfuzzer Cli Option And Card Response Fuzzer Harness

## Round 10 Input Contract
- Before the reader transcript, the fuzz bytes select the pkcs15-crypt operation, PIN string, option flags, optional AID/key strings, and an input-file slice. Only the remaining bytes are passed to the virtual card reader.

## Round 10 Format Links
- [[opensc-pkcs15-crypt-cli-bytes-plus-virtual-card-transcript]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
