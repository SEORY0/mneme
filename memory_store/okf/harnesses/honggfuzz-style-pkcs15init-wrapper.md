---
type: harness-contract
title: "Honggfuzz Style Pkcs15Init Wrapper harness"
description: "Input contract facts for honggfuzz-style-pkcs15init-wrapper."
tags: ["honggfuzz-style-pkcs15init-wrapper", "round-17"]
okf_support: 1
train_only: true
---
# Honggfuzz Style Pkcs15Init Wrapper Harness

## Round 17 Input Contract
- The wrapper runs fuzz_pkcs15init, connects a virtual card from the chunk stream, loads the profile text, initializes PKCS#15 state, stores PIN/data objects, then tries RSA and EC key generation.
- APDU status words are taken from the last two bytes of each response chunk.

## Round 17 Format Links
- [[opensc-pkcs15init-profile-plus-virtual-reader-chunks]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[opensc-pkcs15init-profile-plus-virtual-reader-chunks]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
