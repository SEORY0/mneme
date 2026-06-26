---
type: format-family
title: "Openstep Plist"
description: "Round 7 factual format contract for openstep-plist."
resource: cybergym://format/openstep-plist
tags: ["openstep-plist", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Openstep Plist

## Round 7 Factual Contract

### Schema / Invariants
- OpenStep plist accepts dictionaries, arrays, data groups, quoted strings, and unquoted atoms. Quoted
strings use either quote delimiter and support backslash escapes; the parser scans until an
unescaped matching delimiter before constructing a string node.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
