---
type: harness-contract
title: "Libfuzzer Raw Rules File harness"
description: "Input contract facts for libfuzzer-raw-rules-file."
tags: ["libfuzzer-raw-rules-file", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Rules File Harness

## Round 17 Input Contract
- The harness passes the raw input as the custom protocol configuration file.
- There is no container or selector byte; each line is parsed as a rule by ndpi_load_protocols_file-style code.

## Round 17 Format Links
- [[ndpi-custom-protocol-rules]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[ndpi-custom-protocol-rules]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
