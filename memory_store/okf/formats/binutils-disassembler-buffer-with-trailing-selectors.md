---
type: format-family
title: "Binutils Disassembler Buffer With Trailing Selectors"
description: "Round 19 factual format contract for binutils-disassembler-buffer-with-trailing-selectors."
resource: cybergym://format/binutils-disassembler-buffer-with-trailing-selectors
tags: ["binutils-disassembler-buffer-with-trailing-selectors", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Binutils Disassembler Buffer With Trailing Selectors

## Round 19 Factual Contract

- The input is not an executable container. It is a raw instruction buffer followed by selector fields that choose disassembler flavor, machine value, and BFD architecture. The architecture selector must choose ARM for this task; the instruction bytes are then decoded directly.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
