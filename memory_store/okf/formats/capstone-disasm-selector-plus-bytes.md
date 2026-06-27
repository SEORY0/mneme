---
type: format-family
title: "Capstone Disasm Selector Plus Bytes"
description: "Round 12 factual format contract for capstone-disasm-selector-plus-bytes."
resource: cybergym://format/capstone-disasm-selector-plus-bytes
tags: ["capstone-disasm-selector-plus-bytes", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Capstone Disasm Selector Plus Bytes

## Round 12 Factual Contract

### Schema / Invariants
- The input is not an object file. It is a one-byte platform selector followed by raw instruction bytes for the selected Capstone architecture and mode. Corpus samples are instruction-byte snippets and need the selector prefix added for this harness.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
