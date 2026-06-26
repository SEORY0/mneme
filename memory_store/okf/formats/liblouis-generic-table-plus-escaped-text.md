---
type: format-family
title: "Liblouis Generic Table Plus Escaped Text"
description: "Round 7 factual format contract for liblouis-generic-table-plus-escaped-text."
resource: cybergym://format/liblouis-generic-table-plus-escaped-text
tags: ["liblouis-generic-table-plus-escaped-text", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Liblouis Generic Table Plus Escaped Text

## Round 7 Factual Contract

### Schema / Invariants
- The generic liblouis fuzzer file is split into a table-definition region and an escaped character
stream. The escaped stream is parsed by liblouis into wide characters before translation, so
arbitrary binary bytes are not the direct translated text.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
