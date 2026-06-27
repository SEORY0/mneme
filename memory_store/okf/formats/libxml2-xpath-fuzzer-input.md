---
type: format-family
title: "libxml2-xpath-fuzzer-input format"
description: "Structure and reachability facts for libxml2-xpath-fuzzer-input."
resource: cybergym://format/libxml2-xpath-fuzzer-input
tags: ["libxml2-xpath-fuzzer-input"]
okf_support: 1
---
# Libxml2 Xpath Fuzzer Input Format

## Round 9 Factual Contract

### Schema / Invariants
- The input begins with a big-endian allocation-limit field, followed by two escaped strings.
- The first string is the XPath or XPointer expression, and the second string is the XML document
  parsed in recovery mode.
- A backslash-newline terminates each string and doubled backslashes encode literal backslashes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
