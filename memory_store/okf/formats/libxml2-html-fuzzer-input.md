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

## Round 35 Factual Contract

### Schema / Invariants
- The payload after the harness control word is ordinary HTML text. The relevant parser structures are start tags, end tags, comments, processing instructions, script/style raw-text content, character data, and entity references. In push parsing, lookahead searches for terminating characters or sequences before invoking the real parser for the current state; malformed text can make the lookahead consume more future input than the parser later consumes.

### Harness Links
- [[libfuzzer-libxml2-html-push-parser]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
