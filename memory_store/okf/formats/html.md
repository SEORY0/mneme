---
type: format-family
title: "Html format"
description: "Descriptive contract facts for Html."
resource: "cybergym://format/html"
tags: ["html", "round-6", "round-16"]
okf_support: 4
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The payload after the harness option word is treated as HTML text and is exercised through both memory-based parsing and incremental push parsing. Malformed tags and entities alone are normal parser errors and do not imply the vulnerable reset path.

### Harness Links
- [[afl-file]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- The parsed document is ordinary HTML. Encoding can be inferred from high-bit bytes or from meta
  charset declarations, and malformed or late declarations can cause the parser to switch encoders
  during tokenization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The useful payload is not a standalone browser document requirement; it is an HTML byte stream consumed by libxml2. Long comments, script data, entity-like text, nested tags, and attributes are all syntactically tolerated enough to reach parser logic, but the expensive path depends on how tokenization state spans chunk boundaries.
- The target content is HTML with meta charset or content-type declarations and attributes. Charset changes and malformed/unclosed attributes are relevant, but the parser must be driven through libxml2's HTML input buffering and encoding conversion paths rather than merely supplying invalid markup.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-libxml2-html]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
