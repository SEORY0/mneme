---
type: format-family
title: libxml2-valid-fuzz-entities format
description: Structure, build skeleton, and bug-prone areas of the libxml2-valid-fuzz-entities input format.
resource: cybergym://format/libxml2-valid-fuzz-entities
tags: [libxml2-valid-fuzz-entities, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The active fuzzer format begins with parser option bits and an allocation-limit integer, followed by URL/content virtual-entity pairs terminated by backslash-newline markers. The first entity is the main XML document; later entities can satisfy external DTD references through the fuzz entity loader. Conditional sections are parsed in the external subset, not ordinary document content.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
