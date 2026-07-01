---
type: format-family
title: "XML Fuzzer Entity Envelope"
description: "Round 36 factual format contract for xml-fuzzer-entity-envelope."
tags: ["xml-fuzzer-entity-envelope", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# XML Fuzzer Entity Envelope

## Round 36 Factual Contract

### Schema / Invariants
- The fuzzer input begins with a native parser-options word, then a sequence of escaped URL/content string pairs. The first pair is the main XML document; later pairs are external resource mappings for the entity loader. XInclude reachability requires a well-formed XML document with the XInclude parse option enabled and an include element in an accepted XInclude namespace whose target fails or resolves through the resource map.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
