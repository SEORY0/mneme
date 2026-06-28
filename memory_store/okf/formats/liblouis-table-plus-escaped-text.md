---
type: format-family
title: liblouis-table-plus-escaped-text format
description: Structure, build skeleton, and bug-prone areas of the liblouis-table-plus-escaped-text input format.
resource: cybergym://format/liblouis-table-plus-escaped-text
tags: ["liblouis-table-plus-escaped-text", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The input is split into a fixed-size table-file prefix and an escaped text suffix. The table prefix must be a self-contained liblouis table with valid opcodes such as display, space, letter, or punctuation. The suffix accepts backslash escapes that are expanded by the same character parsing family used during table compilation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
