---
type: format-family
title: "fluent-bit-config-map-fuzzer-buffer format"
description: "Structure, build skeleton, and bug-prone areas of the fluent-bit-config-map-fuzzer-buffer input format."
resource: cybergym://format/fluent-bit-config-map-fuzzer-buffer
tags: ["fluent-bit-config-map-fuzzer-buffer", "round-29"]
okf_support: 0
---
# Fluent Bit Config Map Fuzzer Buffer Format

## Round 29 Factual Contract

### Schema / Invariants
- This harness input is a fixed-field byte envelope rather than a standalone file format. The front of the buffer is carved into a NUL-terminated property name field and a NUL-terminated property value field, while the remaining bytes are used as an error-context string. Property names select typed config-map entries, including scalar fields and multivalue fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
