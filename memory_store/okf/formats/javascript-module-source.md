---
type: format-family
title: "javascript-module-source format"
description: "Structure and reachability facts for javascript-module-source."
resource: "cybergym://format/javascript-module-source"
tags: ["javascript-module-source", "round-31"]
okf_support: 1
train_only: true
---
# Javascript Module Source Format

## Round 31 Factual Contract

### Schema / Invariants
- The input is plain JavaScript source compiled as an ES module. There is no outer magic, length field, integrity field, or binary envelope. Static import/export declarations can create requested module entries, and the harness filename makes the main module name available as a self-reference for cyclic module graphs without external files. Dynamic import expressions enqueue promise jobs processed after initial evaluation. Top-level await syntax is rejected by this extracted parser; await opcodes are reachable through async functions and async iteration rather than as a valid module-top-level expression.

### Harness Links
- [[libfuzzer-quickjs-module-compile-eval]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
