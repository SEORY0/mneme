---
type: harness-contract
title: "Afl Libfuzzer Raw Request Parser harness"
description: "Input contract facts for afl/libfuzzer raw request parser."
tags: ["afl-libfuzzer-raw-request-parser", "round-17"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer Raw Request Parser Harness

## Round 17 Input Contract
- The fuzz target passes the raw input bytes to the request parser.
- The harness copies the input into a fixed internal request buffer, requires a complete header terminator before parsing, and then parses headers across the copied request length.

## Round 17 Format Links
- [[http-request]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[http-request]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
