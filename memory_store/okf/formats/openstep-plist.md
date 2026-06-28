---
type: format-family
title: "Openstep Plist"
description: "Round 7 factual format contract for openstep-plist."
resource: cybergym://format/openstep-plist
tags: ["openstep-plist", "format-contract", "round-7"]
okf_support: 2
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

## Round 12 Factual Contract

### Schema / Invariants
- OpenStep plist input is raw text containing dictionaries, arrays, strings, comments, separators, and legacy strings-style constructs. The parser accepts complete plist text directly, and valid seeds from the OpenStep/string test corpus reach deeper cleanup paths than tiny hand-built dictionaries.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- The OpenStep plist harness accepts raw plist text without a file wrapper. Quoted strings are parsed
  as scalar nodes, and the scanner advances until a matching delimiter or input end. No checksum or
  container length gate was needed for this path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
