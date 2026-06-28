---
type: format-family
title: "libxml2-html-fuzzer-envelope format"
description: "Structure and invariants observed for libxml2-html-fuzzer-envelope."
resource: "cybergym://format/libxml2-html-fuzzer-envelope"
tags: ["libxml2-html-fuzzer-envelope", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The selected HTML fuzzer consumes parser options and an allocation limit from the front, then treats all remaining bytes as the HTML document. It exercises pull parsing, serialization, push parsing in fixed-size chunks, and reader-like paths for the same document.

### Harness Links
- [[libfuzzer-libxml2-html-parser]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
