---
type: format-family
title: "Libxml2 Html Fuzzer Input format"
description: "Structure and invariants for the libxml2-html-fuzzer-input input format."
tags: ["libxml2-html-fuzzer-input", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The HTML fuzzer input starts with parser option bits and an allocator limit, followed by the HTML document bytes. Attribute-heavy tags and long quoted or unquoted attribute values reach htmlParseHTMLAttribute, but allocator limit placement controls which allocation fails.

### Harness Links
- [[libfuzzer-libxml2-html-with-carved-options-and-allocation-limit]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
