---
type: format-family
title: "libxml2-api-vm-bytecode format"
description: "Structure and invariants observed for libxml2-api-vm-bytecode."
resource: "cybergym://format/libxml2-api-vm-bytecode"
tags: ["libxml2-api-vm-bytecode", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The API fuzzer is a bytecode VM. After an allocation-limit word, each opcode byte selects a libxml2 API call. Strings are backslash-newline terminated, integers are big-endian byte reads, and node/string/integer registers are newest-first rings. DTD nodes can be created from documents and then used by tree-manipulation opcodes.

### Harness Links
- [[libfuzzer-libxml2-api-fuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
