---
type: format-family
title: "Libxml2 Xml Fuzzer Entity Envelope Format"
description: "Round 27 descriptive format facts for libxml2-xml-fuzzer-entity-envelope."
resource: cybergym://format/libxml2-xml-fuzzer-entity-envelope
tags: ["libxml2-xml-fuzzer-entity-envelope", "round-27"]
okf_support: 1
---
# Libxml2 Xml Fuzzer Entity Envelope Format

## Round 27 Factual Contract

- The fuzzer input is a libxml2-specific envelope, not plain XML alone.
- It carries parser options followed by URL/resource string pairs; the first pair supplies the main XML document and later pairs can supply external resources.
- Strings use the harness' escape-and-terminator convention, so valid XML bytes still need to be wrapped by that envelope.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
