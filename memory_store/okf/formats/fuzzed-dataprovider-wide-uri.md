---
type: format-family
title: "fuzzed-dataprovider-wide-uri format"
description: "Structure, build skeleton, and bug-prone areas of the fuzzed-dataprovider-wide-uri input format."
resource: cybergym://format/fuzzed-dataprovider-wide-uri
tags: ["fuzzed-dataprovider-wide-uri", "round-29"]
okf_support: 0
---
# Fuzzed Dataprovider Wide Uri Format

## Round 29 Factual Contract

### Schema / Invariants
- The fuzzer input is not a serialized URI file; it is a FuzzedDataProvider stream split into a first URI string of selected length and a second URI string from the remaining front bytes. In the wide build, each URI character occupies the platform wide-character width. Ordinary absolute or relative URI text with a long query or path parses and is later recomposed by uriToStringW.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
