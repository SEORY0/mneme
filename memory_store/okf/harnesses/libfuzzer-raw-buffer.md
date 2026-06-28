---
type: harness-contract
title: "Libfuzzer Raw Buffer harness"
description: "Input contract facts for libfuzzer-raw-buffer."
tags: ["libfuzzer-raw-buffer", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Buffer Harness

## Round 17 Input Contract
- The harness rejects inputs below its minimum size, then copies the entire raw buffer to a heap allocation and appends a terminator.
- An early terminator in the raw bytes controls the C-string length seen by the target parser.

## Round 17 Format Links
- [[fluent-bit-time-string-buffer]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[fluent-bit-time-string-buffer]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
