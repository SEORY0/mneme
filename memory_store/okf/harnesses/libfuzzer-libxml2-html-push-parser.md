---
type: harness-contract
title: "libfuzzer-libxml2-html-push-parser harness"
description: "Input contract facts for libfuzzer-libxml2-html-push-parser."
tags: ["libfuzzer-libxml2-html-push-parser", "round-35"]
okf_support: 1
train_only: true
---
# libfuzzer-libxml2-html-push-parser Harness

## Round 35 Input Contract
### Input Contract
- The libFuzzer target consumes a fixed-width parser-options integer from the front of the input, then treats the remaining bytes as one HTML document. It first parses the whole document with the pull parser and serializes it, then creates an HTML push-parser context with the same options and feeds the document in bounded chunks before a final terminating chunk. There is no magic header, integrity gate, filename, mode selector, or FuzzedDataProvider tail layout.

### Format Links
- [[libxml2-html-fuzzer-input]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
