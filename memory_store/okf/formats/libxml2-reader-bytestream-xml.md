---
type: format-family
title: "libxml2-reader-bytestream-xml format"
description: "Structure and invariants observed for libxml2-reader-bytestream-xml."
resource: "cybergym://format/libxml2-reader-bytestream-xml"
tags: ["libxml2-reader-bytestream-xml", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- The harness input is not raw XML. It starts with a native little-endian parser-options integer, then a native-size encoding-string length, then that many encoding bytes, and only the remaining bytes are written to the temporary XML file. For this bug, the XML body can be a compact document with an internal DTD subset declaring an ID-typed attribute on a repeated element. DTD loading/validation options are needed for the ID table path; dictionary ownership control is relevant because dictionary-owned names do not expose the same double-free.

### Harness Links
- [[libfuzzer-afl-file-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
