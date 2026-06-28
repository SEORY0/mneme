---
type: format-family
title: "xml-entity-envelope format"
description: "Structure and invariants observed for xml-entity-envelope."
resource: "cybergym://format/xml-entity-envelope"
tags: ["xml-entity-envelope", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The fuzzer input starts with parser option bits, then a sequence of URL/body string pairs terminated by the custom backslash-newline string delimiter. The first pair is the main XML document; later pairs are resolved by the custom external entity loader. XInclude processing is controlled by a parser option bit.

### Harness Links
- [[afl-libxml2-xml]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
