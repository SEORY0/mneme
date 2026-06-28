---
type: harness-contract
title: "Libfuzzer Libxml2 Html Parser harness"
description: "Input contract facts for libfuzzer-libxml2-html-parser."
tags: ["libfuzzer-libxml2-html-parser", "round-24"]
okf_support: 1
---
# Libfuzzer Libxml2 Html Parser Harness

## Round 24 Factual Contract

### Input Contract
- There is no magic file header. The important contract is the front control words followed by raw HTML bytes; push parsing splits the document into bounded chunks internally.

### Format Links
- [[libxml2-html-fuzzer-envelope]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
