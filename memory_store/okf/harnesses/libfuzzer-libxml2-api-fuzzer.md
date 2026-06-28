---
type: harness-contract
title: "Libfuzzer Libxml2 Api Fuzzer harness"
description: "Input contract facts for libfuzzer-libxml2-api-fuzzer."
tags: ["libfuzzer-libxml2-api-fuzzer", "round-24"]
okf_support: 1
---
# Libfuzzer Libxml2 Api Fuzzer Harness

## Round 24 Factual Contract

### Input Contract
- The fuzzer interprets the full byte stream as VM operations and calls libxml2 APIs directly; it is not parsing an XML file unless the bytecode explicitly invokes the parse-document opcode.

### Format Links
- [[libxml2-api-vm-bytecode]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
