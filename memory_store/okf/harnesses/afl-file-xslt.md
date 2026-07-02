---
type: harness-contract
title: "Afl File Xslt Harness"
description: "Input contract facts for afl-file-xslt."
tags: ["afl-file-xslt", "round-37", "harness-contract"]
okf_support: 1
train_only: true
---
# Afl File Xslt Harness
## Round 37 Input Contract

### Input Contract
- The AFL-style wrapper passes the whole file as a single stylesheet document.
- The fuzzer calls xmlReadMemory with parser options set to zero, then adds extension namespaces, parses the document as a user-provided stylesheet, applies it to a fixed XML source document, serializes any result, and frees the transform context and stylesheet.

### Format Links
- [[xslt-stylesheet]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
