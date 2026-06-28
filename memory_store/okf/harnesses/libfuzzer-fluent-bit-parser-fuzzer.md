---
type: harness-contract
title: "Libfuzzer Fluent Bit Parser Fuzzer harness"
description: "Input contract facts for libfuzzer-fluent-bit-parser-fuzzer."
tags: ["libfuzzer-fluent-bit-parser-fuzzer", "round-24"]
okf_support: 1
---
# Libfuzzer Fluent Bit Parser Fuzzer Harness

## Round 24 Factual Contract

### Input Contract
- The fuzzer ignores inputs below a minimum size, consumes control bytes from the front, creates a Fluent Bit parser from those options, then passes the remaining bytes and explicit length to flb_parser_do.

### Format Links
- [[fluent-bit-parser-fuzzer-control-block-plus-record-payload]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
