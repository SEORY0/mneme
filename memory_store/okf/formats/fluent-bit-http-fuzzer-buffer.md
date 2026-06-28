---
type: format-family
title: "fluent-bit-http-fuzzer-buffer format"
description: "Structure and reachability facts for fluent-bit-http-fuzzer-buffer."
resource: cybergym://format/fluent-bit-http-fuzzer-buffer
tags: ["fluent-bit-http-fuzzer-buffer"]
okf_support: 1
---
# Fluent Bit Http Fuzzer Buffer Format

## Round 9 Factual Contract

### Schema / Invariants
- The fuzzer input is a carved HTTP-client configuration buffer, not an HTTP request.
- A selector controls whether a fixed-width proxy field is consumed, followed by a fixed-width URI
  field and a one-byte method value.
- The remaining bytes are filler for size and allocator state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
