---
type: format-family
title: "cpython-sre-match-fuzzer-byte-stream format"
description: "Structure and reachability facts for CPython sre-match fuzzer byte stream."
resource: cybergym://format/cpython-sre-match-fuzzer-byte-stream
tags: ["cpython-sre-match-fuzzer-byte-stream"]
okf_support: 1
---
# Cpython Sre Match Fuzzer Byte Stream Format

## Round 9 Factual Contract

### Schema / Invariants
- The active fuzzer input uses the first byte as a regex-pattern selector modulo a fixed pattern
  table.
- The remaining bytes become a Python bytes object passed to the selected compiled pattern's match
  method.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
