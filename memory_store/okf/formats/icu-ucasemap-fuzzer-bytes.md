---
type: format-family
title: "Icu Ucasemap Fuzzer Bytes format"
description: "Descriptive contract facts for Icu Ucasemap Fuzzer Bytes."
resource: "cybergym://format/icu-ucasemap-fuzzer-bytes"
tags: ["icu-ucasemap-fuzzer-bytes", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The fuzzer byte stream is not a text file alone: it begins with operation/locale/options selector fields, followed by the UTF-8 source bytes. Titlecase behavior is selected by the operation byte modulo the fuzzer switch, while locale and flags affect Dutch IJ special casing.

### Harness Links
- [[libfuzzer-ucasemap-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
