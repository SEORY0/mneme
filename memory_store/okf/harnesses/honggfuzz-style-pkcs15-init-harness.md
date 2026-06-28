---
type: harness-contract
title: "Honggfuzz Style Pkcs15 Init Harness harness"
description: "Input contract facts for honggfuzz-style pkcs15-init harness."
tags: ["honggfuzz-style-pkcs15-init-harness", "round-16"]
okf_support: 1
---
# Honggfuzz Style Pkcs15 Init Harness Harness

## Round 16 Input Contract
- The selected wrapper runs fuzz_pkcs15init. It splits raw input at the first NUL into profile text and reader data, connects a virtual card from chunked responses, binds a profile, and then attempts PKCS#15 initialization, object storage, key generation, finalization, sanity checks, and erase.

## Round 16 Format Links
- [[opensc-pkcs15-init-profile-plus-virtual-reader-chunks]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
