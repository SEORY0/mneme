---
type: harness-contract
title: "Honggfuzz Libfuzzer Entry Harness"
description: "Input contract facts for honggfuzz/libfuzzer-entry."
tags: ["honggfuzz-libfuzzer-entry", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Honggfuzz Libfuzzer Entry Harness

## Round 19 Input Contract

- The fuzzer copies raw input bytes into a buffer and calls the RSA key parser once. The local binary advertises a honggfuzz-style invocation wrapper, and no separate length prefix or mode selector is present in the source harness.
- Format link: [[asn1-der-rsa-key]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
