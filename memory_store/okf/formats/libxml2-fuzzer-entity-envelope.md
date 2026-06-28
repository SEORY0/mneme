---
type: format-family
title: libxml2-fuzzer-entity-envelope format
description: Structure, build skeleton, and bug-prone areas of the libxml2-fuzzer-entity-envelope input format.
resource: cybergym://format/libxml2-fuzzer-entity-envelope
tags: [libxml2-fuzzer-entity-envelope, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The fuzzer format starts with parser options, then a sequence of URL and entity-body strings. Strings are terminated by an escaped line ending and backslashes are escaped. The first URL/body pair is the main XML document; later pairs are available to the custom external entity loader. XInclude behavior is controlled by parser option bits inside the leading options field.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
