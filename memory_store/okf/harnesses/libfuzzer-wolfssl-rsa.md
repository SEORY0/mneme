---
type: harness-contract
title: "Libfuzzer Wolfssl RSA harness"
description: "Input contract facts for libfuzzer-wolfssl-rsa."
tags: ["libfuzzer-wolfssl-rsa", "round-15"]
okf_support: 1
---
# Libfuzzer Wolfssl RSA Harness

## Round 15 Input Contract
- The selected target is the wolfSSL RSA libFuzzer harness. It first reads an input blob, output size
  and operation controls, then booleans deciding whether P, Q, and E are fixed. It parses the
  remaining RSA integer strings with mp_read_radix before running the selected RSA operation; choosing
  an operation outside the handled cases avoids needing additional operation-specific blobs.

## Format Links
- [[fuzzing-datasource-rsa-fields]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
