---
type: format-family
title: "Libxslt Fuzz Entities"
description: "Round 12 factual format contract for libxslt-fuzz-entities."
resource: cybergym://format/libxslt-fuzz-entities
tags: ["libxslt-fuzz-entities", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Libxslt Fuzz Entities

## Round 12 Factual Contract

### Schema / Invariants
- The XSLT fuzzer input starts with a big-endian allocation-limit word followed by escaped string pairs representing URL and entity contents. The first entity is the stylesheet and the second entity is the source document. Strings terminate with the harness escape-newline convention, and backslashes are escaped.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
